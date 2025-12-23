from fastapi import FastAPI, APIRouter, HTTPException, Query, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime, timedelta
import random
import hashlib
import jwt
import secrets

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# JWT Configuration
JWT_SECRET = os.environ.get('JWT_SECRET', secrets.token_hex(32))
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 72

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Security
security = HTTPBearer(auto_error=False)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============ AUTH HELPERS ============

def hash_password(password: str) -> str:
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash"""
    return hash_password(password) == hashed

def create_token(user_id: str, email: str) -> str:
    """Create JWT token"""
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_token(token: str) -> Optional[Dict]:
    """Decode JWT token"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Optional[Dict]:
    """Get current user from token, returns None for guest users"""
    if not credentials:
        return None
    
    payload = decode_token(credentials.credentials)
    if not payload:
        return None
    
    user = await db.users.find_one({"id": payload["user_id"]})
    if user:
        user.pop('_id', None)
        user.pop('password', None)
    return user

async def get_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Get user ID from token or return guest ID"""
    if not credentials:
        return "guest_user"
    
    payload = decode_token(credentials.credentials)
    if not payload:
        return "guest_user"
    
    return payload.get("user_id", "guest_user")

# ============ AUTH MODELS ============

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class ForgotPassword(BaseModel):
    email: str

class ResetPassword(BaseModel):
    email: str
    reset_code: str
    new_password: str

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    total_attempts: int = 0
    total_correct: int = 0
    total_questions_attempted: int = 0
    reset_code: Optional[str] = None
    reset_code_expires: Optional[datetime] = None

class UserProfile(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime
    total_attempts: int
    total_correct: int
    total_questions_attempted: int
    overall_accuracy: float
    subject_progress: List[Dict]

# ============ MODELS ============

class Subject(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    icon: str
    color: str
    total_papers: int = 26  # 20 regular + 5 extreme + 1 master
    total_questions: int = 2600  # 26 papers x 100 questions

class Paper(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    subject_id: str
    paper_number: int
    is_master: bool = False
    title: str
    total_questions: int = 100
    duration_minutes: int = 90

class Question(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    paper_id: str
    subject_id: str
    question_number: int
    question_text: str
    options: List[str]
    correct_option: int  # 0-3 index
    explanation: Optional[str] = None
    difficulty: str = "medium"  # easy, medium, hard
    topic: str = ""

class AttemptCreate(BaseModel):
    paper_id: str
    subject_id: str
    answers: Dict[str, int]  # question_id -> selected_option
    time_taken_seconds: int
    timer_mode: str = "total"  # total or per_question

class Attempt(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = "default_user"
    paper_id: str
    subject_id: str
    answers: Dict[str, int]
    correct_count: int
    wrong_count: int
    skipped_count: int
    total_questions: int
    score_percentage: float
    time_taken_seconds: int
    timer_mode: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserSettings(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = "default_user"
    timer_mode: str = "total"  # total or per_question
    total_time_minutes: int = 90
    per_question_seconds: int = 60
    show_timer: bool = True

# ============ SUBJECT DATA ============

SUBJECTS_DATA = [
    {
        "name": "Polity",
        "description": "Constitution of India, governance, rights, duties, institutions",
        "icon": "bank",
        "color": "#3B82F6"
    },
    {
        "name": "Geography",
        "description": "Physical Geography, Indian Geography, Odisha Geography",
        "icon": "earth",
        "color": "#10B981"
    },
    {
        "name": "History of Modern India",
        "description": "Freedom struggle, reforms, movements (1757-1947)",
        "icon": "book-open-variant",
        "color": "#F59E0B"
    },
    {
        "name": "Ethics",
        "description": "Ethics & Human Values, integrity, aptitude, moral thinkers, case studies",
        "icon": "scale-balance",
        "color": "#8B5CF6"
    },
    {
        "name": "Science and Technology",
        "description": "General science, emerging technologies, space, defence, health, IT",
        "icon": "atom",
        "color": "#EC4899"
    },
    {
        "name": "Economics",
        "description": "Indian economy basics, growth, inflation, budgeting, development & planning",
        "icon": "chart-line",
        "color": "#06B6D4"
    },
    {
        "name": "Environment and Ecology",
        "description": "Ecology basics, climate change, environmental laws & conventions",
        "icon": "leaf",
        "color": "#22C55E"
    },
    {
        "name": "Ancient & Medieval Indian History",
        "description": "Pre-independence Indian history, dynasties, culture, architecture",
        "icon": "castle",
        "color": "#D97706"
    },
    {
        "name": "Indian Society & Social Issues",
        "description": "Social structure, issues, diversity, communalism, regionalism",
        "icon": "account-group",
        "color": "#EF4444"
    },
    {
        "name": "Odisha-Specific Studies",
        "description": "History & culture of Odisha, Odisha economy, state schemes & governance",
        "icon": "map-marker",
        "color": "#7C3AED"
    },
    {
        "name": "Current Affairs",
        "description": "National, International current events and developments",
        "icon": "newspaper",
        "color": "#0EA5E9"
    }
]

# ============ QUESTION TEMPLATES ============

QUESTION_TEMPLATES = {
    "Polity": {
        "topics": ["Constitution", "Fundamental Rights", "Directive Principles", "Parliament", "Judiciary", "President", "Governor", "Panchayati Raj", "Elections", "Constitutional Amendments"],
        "questions": [
            ("Which Article of the Indian Constitution deals with {topic}?", ["Article 14", "Article 21", "Article 32", "Article 19"], 0),
            ("The {topic} was added to the Constitution by which Amendment?", ["42nd Amendment", "44th Amendment", "73rd Amendment", "86th Amendment"], 0),
            ("Which of the following is NOT a feature of {topic}?", ["Option A related to topic", "Option B related to topic", "Option C unrelated", "Option D related to topic"], 2),
            ("The concept of {topic} in Indian Constitution is borrowed from which country?", ["USA", "UK", "Ireland", "Germany"], 0),
            ("Who has the power to decide disputes regarding {topic}?", ["Supreme Court", "High Court", "President", "Parliament"], 0),
        ]
    },
    "Geography": {
        "topics": ["Rivers", "Mountains", "Climate", "Soil Types", "Agriculture", "Minerals", "Industries", "Population", "Odisha Geography", "Natural Vegetation"],
        "questions": [
            ("Which of the following rivers originates in {topic} region?", ["Mahanadi", "Godavari", "Krishna", "Brahmani"], 0),
            ("The {topic} is characterized by which type of climate?", ["Tropical Monsoon", "Semi-arid", "Humid Subtropical", "Temperate"], 0),
            ("Which district of Odisha is known for {topic}?", ["Mayurbhanj", "Koraput", "Sundargarh", "Cuttack"], 0),
            ("The largest {topic} in India is located in which state?", ["Odisha", "Jharkhand", "Chhattisgarh", "West Bengal"], 0),
            ("What percentage of Odisha is covered by {topic}?", ["33%", "25%", "40%", "20%"], 0),
        ]
    },
    "History of Modern India": {
        "topics": ["Revolt of 1857", "Indian National Congress", "Non-Cooperation Movement", "Civil Disobedience", "Quit India Movement", "Partition", "British Reforms", "Social Reformers", "Revolutionary Movements", "Provincial Elections"],
        "questions": [
            ("The {topic} was started in which year?", ["1857", "1919", "1930", "1942"], 0),
            ("Who was the main leader associated with {topic}?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Bal Gangadhar Tilak"], 0),
            ("Which event triggered the {topic}?", ["Jallianwala Bagh Massacre", "Partition of Bengal", "Salt Tax", "Rowlatt Act"], 0),
            ("The {topic} had its major impact in which region?", ["Bengal", "Punjab", "Maharashtra", "Odisha"], 0),
            ("Which British policy was opposed during {topic}?", ["Divide and Rule", "Doctrine of Lapse", "Subsidiary Alliance", "Permanent Settlement"], 0),
        ]
    },
    "Ethics": {
        "topics": ["Integrity", "Impartiality", "Objectivity", "Dedication to Public Service", "Empathy", "Tolerance", "Compassion", "Emotional Intelligence", "Moral Thinkers", "Ethical Dilemmas"],
        "questions": [
            ("Which value is most important for a civil servant in context of {topic}?", ["Integrity", "Efficiency", "Obedience", "Loyalty"], 0),
            ("According to {topic}, what should be the primary concern of administration?", ["Public Welfare", "Economic Growth", "Political Stability", "Personal Achievement"], 0),
            ("The concept of {topic} was propounded by which philosopher?", ["Mahatma Gandhi", "Aristotle", "Kant", "John Rawls"], 0),
            ("In case of ethical dilemma regarding {topic}, what is the best approach?", ["Follow conscience", "Follow rules strictly", "Seek guidance", "Avoid decision"], 0),
            ("Which of the following best describes {topic}?", ["Acting without bias", "Following orders", "Maximizing efficiency", "Minimizing conflicts"], 0),
        ]
    },
    "Science and Technology": {
        "topics": ["Space Technology", "Nuclear Energy", "Biotechnology", "Information Technology", "Defence Technology", "Nanotechnology", "Artificial Intelligence", "Renewable Energy", "Medical Science", "Agriculture Technology"],
        "questions": [
            ("Which organization is primarily responsible for {topic} in India?", ["ISRO", "DRDO", "BARC", "CSIR"], 0),
            ("The latest development in {topic} includes which of the following?", ["Chandrayaan-3", "Agni-V", "Tejas", "INS Vikrant"], 0),
            ("What is the primary application of {topic}?", ["Research", "Defence", "Agriculture", "Healthcare"], 0),
            ("Which mission of India is related to {topic}?", ["Gaganyaan", "Make in India", "Digital India", "Startup India"], 0),
            ("The {topic} sector in India is regulated by which body?", ["ISRO", "DAE", "DST", "DRDO"], 0),
        ]
    },
    "Economics": {
        "topics": ["GDP", "Inflation", "Budget", "Fiscal Policy", "Monetary Policy", "Banking", "Taxation", "Foreign Trade", "Public Debt", "Economic Planning"],
        "questions": [
            ("Which factor directly affects {topic} in India?", ["Government spending", "Private investment", "Exports", "Imports"], 0),
            ("The {topic} of India is managed by which institution?", ["RBI", "SEBI", "Finance Ministry", "NITI Aayog"], 0),
            ("What is the current target for {topic} in India?", ["4%", "6%", "8%", "10%"], 0),
            ("Which scheme is related to improving {topic}?", ["Make in India", "Digital India", "Skill India", "Startup India"], 0),
            ("The {topic} has shown what trend in the last decade?", ["Increasing", "Decreasing", "Stable", "Fluctuating"], 0),
        ]
    },
    "Environment and Ecology": {
        "topics": ["Climate Change", "Biodiversity", "Pollution", "Forest Conservation", "Wildlife Protection", "Wetlands", "Sustainable Development", "Environmental Laws", "International Conventions", "Renewable Resources"],
        "questions": [
            ("Which international convention deals with {topic}?", ["Paris Agreement", "Kyoto Protocol", "Montreal Protocol", "Ramsar Convention"], 0),
            ("The {topic} in India is governed by which act?", ["Environment Protection Act", "Wildlife Protection Act", "Forest Conservation Act", "Water Act"], 0),
            ("Which state has the highest {topic} index?", ["Kerala", "Odisha", "Madhya Pradesh", "Maharashtra"], 0),
            ("The National Action Plan on {topic} was launched in which year?", ["2008", "2010", "2015", "2020"], 0),
            ("Which of the following is a consequence of {topic}?", ["Sea level rise", "Desertification", "Loss of biodiversity", "All of these"], 3),
        ]
    },
    "Ancient & Medieval Indian History": {
        "topics": ["Indus Valley Civilization", "Vedic Period", "Mauryan Empire", "Gupta Empire", "Delhi Sultanate", "Mughal Empire", "Vijayanagara Empire", "Chola Dynasty", "Buddhist Period", "Temple Architecture"],
        "questions": [
            ("The {topic} was established during which century?", ["3rd century BCE", "4th century CE", "12th century CE", "16th century CE"], 0),
            ("Which ruler is associated with the golden age of {topic}?", ["Ashoka", "Chandragupta II", "Akbar", "Krishnadevaraya"], 0),
            ("The administrative system of {topic} included which feature?", ["Decentralized governance", "Centralized bureaucracy", "Feudal system", "Democratic assemblies"], 0),
            ("Which architectural style is characteristic of {topic}?", ["Indo-Islamic", "Dravidian", "Nagara", "Vesara"], 0),
            ("The decline of {topic} was caused by which factor?", ["Foreign invasions", "Internal conflicts", "Economic decline", "All of these"], 3),
        ]
    },
    "Indian Society & Social Issues": {
        "topics": ["Caste System", "Gender Issues", "Poverty", "Urbanization", "Migration", "Communalism", "Regionalism", "Globalization Effects", "Education", "Healthcare"],
        "questions": [
            ("Which government scheme addresses {topic} in India?", ["MGNREGA", "PMJDY", "Beti Bachao", "Swachh Bharat"], 0),
            ("The {topic} in India has shown what trend recently?", ["Improvement", "Deterioration", "No change", "Regional variation"], 0),
            ("Which constitutional provision deals with {topic}?", ["Article 15", "Article 17", "Article 21", "Article 46"], 0),
            ("The main cause of {topic} in India is?", ["Economic inequality", "Social discrimination", "Political factors", "All of these"], 3),
            ("Which commission was formed to study {topic}?", ["Mandal Commission", "Sachar Committee", "Justice Verma Committee", "Ranganath Misra Commission"], 0),
        ]
    },
    "Odisha-Specific Studies": {
        "topics": ["Kalinga History", "Jagannath Culture", "Odissi Dance", "Tribal Communities", "Odisha Economy", "State Schemes", "Panchayati Raj in Odisha", "Industrial Development", "Natural Resources", "Coastal Geography"],
        "questions": [
            ("The {topic} of Odisha is famous for which aspect?", ["Cultural heritage", "Economic significance", "Historical importance", "All of these"], 3),
            ("Which district of Odisha is known for {topic}?", ["Puri", "Koraput", "Sundargarh", "Khordha"], 0),
            ("The state government's initiative for {topic} was launched in which year?", ["2015", "2018", "2020", "2022"], 0),
            ("What percentage of Odisha's economy depends on {topic}?", ["30%", "40%", "50%", "20%"], 0),
            ("Which temple or monument is associated with {topic}?", ["Konark Sun Temple", "Jagannath Temple", "Lingaraj Temple", "Udayagiri Caves"], 0),
        ]
    },
    "Current Affairs": {
        "topics": ["National Politics", "International Relations", "Economic Developments", "Science Achievements", "Sports Events", "Environmental Issues", "Social Schemes", "Defence Updates", "Technology News", "Awards and Honors"],
        "questions": [
            ("Which recent development is related to {topic}?", ["G20 Summit 2023", "Chandrayaan-3", "Women's Reservation Bill", "Digital India 2.0"], 0),
            ("The {topic} of 2024 was significant because of?", ["Policy changes", "International cooperation", "Technological advancement", "All of these"], 3),
            ("Which country hosted the recent summit on {topic}?", ["India", "USA", "China", "UAE"], 0),
            ("The government's latest initiative on {topic} aims to?", ["Improve efficiency", "Increase coverage", "Reduce costs", "All of these"], 3),
            ("Which organization released the report on {topic}?", ["UN", "World Bank", "IMF", "WTO"], 0),
        ]
    }
}

# ============ HELPER FUNCTIONS ============

# Import all high-quality question databases
from questions_polity import POLITY_QUESTIONS
from questions_geography import GEOGRAPHY_QUESTIONS
from questions_history_modern import HISTORY_MODERN_INDIA_QUESTIONS
from questions_ethics import ETHICS_QUESTIONS
from questions_science import SCIENCE_TECHNOLOGY_QUESTIONS
from questions_economics import ECONOMICS_QUESTIONS
from questions_environment import ENVIRONMENT_ECOLOGY_QUESTIONS
from questions_ancient_history import ANCIENT_MEDIEVAL_HISTORY_QUESTIONS
from questions_indian_society import INDIAN_SOCIETY_QUESTIONS
from questions_odisha import ODISHA_QUESTIONS
from questions_current_affairs import CURRENT_AFFAIRS_QUESTIONS

# Map subject names to question databases
QUESTIONS_DATABASE = {
    "Polity": POLITY_QUESTIONS,
    "Geography": GEOGRAPHY_QUESTIONS,
    "History of Modern India": HISTORY_MODERN_INDIA_QUESTIONS,
    "Ethics": ETHICS_QUESTIONS,
    "Science and Technology": SCIENCE_TECHNOLOGY_QUESTIONS,
    "Economics": ECONOMICS_QUESTIONS,
    "Environment and Ecology": ENVIRONMENT_ECOLOGY_QUESTIONS,
    "Ancient & Medieval Indian History": ANCIENT_MEDIEVAL_HISTORY_QUESTIONS,
    "Indian Society & Social Issues": INDIAN_SOCIETY_QUESTIONS,
    "Odisha-Specific Studies": ODISHA_QUESTIONS,
    "Current Affairs": CURRENT_AFFAIRS_QUESTIONS,
}

def generate_questions_for_subject(subject_name: str, paper_id: str, subject_id: str, count: int = 100, is_master: bool = False, paper_seed: int = 0) -> List[dict]:
    """Generate OPSC questions using high-quality question database for the subject"""
    questions = []
    
    # Get questions for this subject
    subject_questions = QUESTIONS_DATABASE.get(subject_name, [])
    
    if not subject_questions:
        # Fallback to Polity if no questions available
        subject_questions = QUESTIONS_DATABASE.get("Polity", [])
    
    # Create a deterministic shuffle based on paper_seed for variety
    shuffled_questions = subject_questions.copy()
    random.seed(paper_seed)
    random.shuffle(shuffled_questions)
    
    # For master papers, prioritize harder questions
    if is_master:
        hard_questions = [q for q in shuffled_questions if q.get("difficulty") in ["hard", "extreme"]]
        medium_questions = [q for q in shuffled_questions if q.get("difficulty") == "medium"]
        easy_questions = [q for q in shuffled_questions if q.get("difficulty") == "easy"]
        shuffled_questions = hard_questions + medium_questions + easy_questions
    
    # Create questions for this paper
    for i in range(count):
        # Cycle through questions if we need more than available
        source_q = shuffled_questions[i % len(shuffled_questions)]
        
        question = {
            "id": str(uuid.uuid4()),
            "paper_id": paper_id,
            "subject_id": subject_id,
            "question_number": i + 1,
            "question_text": source_q["question_text"],
            "options": source_q["options"].copy(),
            "correct_option": source_q["correct_option"],
            "explanation": source_q.get("explanation", f"This question tests knowledge of {source_q.get('topic', subject_name)}."),
            "difficulty": source_q.get("difficulty", "medium"),
            "topic": source_q.get("topic", subject_name)
        }
        questions.append(question)
    
    # Reset random seed
    random.seed()
    
    return questions


def generate_extreme_questions_for_subject(subject_name: str, paper_id: str, subject_id: str, count: int = 100, paper_seed: int = 0) -> List[dict]:
    """Generate extreme difficulty questions - pick only hard questions from the database"""
    questions = []
    
    # Get questions for this subject
    subject_questions = QUESTIONS_DATABASE.get(subject_name, [])
    
    if not subject_questions:
        subject_questions = QUESTIONS_DATABASE.get("Polity", [])
    
    # Filter to only hard/extreme questions first
    hard_questions = [q for q in subject_questions if q.get("difficulty") in ["hard", "extreme"]]
    if len(hard_questions) < 20:
        # If not enough hard questions, include medium as well
        hard_questions = [q for q in subject_questions if q.get("difficulty") in ["hard", "extreme", "medium"]]
    
    # Create a deterministic shuffle based on paper_seed
    random.seed(paper_seed + 1000)  # Different seed from regular papers
    random.shuffle(hard_questions)
    
    # Create questions for this paper
    for i in range(count):
        source_q = hard_questions[i % len(hard_questions)]
        
        question = {
            "id": str(uuid.uuid4()),
            "paper_id": paper_id,
            "subject_id": subject_id,
            "question_number": i + 1,
            "question_text": source_q["question_text"],
            "options": source_q["options"].copy(),
            "correct_option": source_q["correct_option"],
            "explanation": source_q.get("explanation", f"This is an extreme difficulty question testing deep knowledge of {source_q.get('topic', subject_name)}."),
            "difficulty": "extreme",  # Mark as extreme
            "topic": source_q.get("topic", subject_name)
        }
        questions.append(question)
    
    # Reset random seed
    random.seed()
    
    return questions

# ============ API ENDPOINTS ============

@api_router.get("/")
async def root():
    return {"message": "OPSC Exam Prep API", "version": "1.0"}

# ============ AUTH ENDPOINTS ============

@api_router.post("/auth/register")
async def register(user_data: UserRegister):
    """Register a new user"""
    # Check if email already exists
    existing_user = await db.users.find_one({"email": user_data.email.lower()})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    user = User(
        name=user_data.name,
        email=user_data.email.lower(),
        password=hash_password(user_data.password)
    )
    
    await db.users.insert_one(user.dict())
    
    # Create token
    token = create_token(user.id, user.email)
    
    return {
        "message": "Registration successful",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }

@api_router.post("/auth/login")
async def login(credentials: UserLogin):
    """Login user"""
    user = await db.users.find_one({"email": credentials.email.lower()})
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Create token
    token = create_token(user["id"], user["email"])
    
    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    }

@api_router.get("/auth/me")
async def get_current_user_profile(current_user: Optional[Dict] = Depends(get_current_user)):
    """Get current user profile"""
    if not current_user:
        return {"is_guest": True, "message": "Guest mode - login to save progress"}
    
    # Get user's attempts for statistics
    attempts = await db.attempts.find({"user_id": current_user["id"]}).to_list(1000)
    
    total_attempts = len(attempts)
    total_correct = sum(a.get("correct_count", 0) for a in attempts)
    total_questions = sum(a.get("total_questions", 0) for a in attempts)
    overall_accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0
    
    # Get subject-wise progress
    subject_stats = {}
    for attempt in attempts:
        sid = attempt["subject_id"]
        if sid not in subject_stats:
            subject_stats[sid] = {"attempts": 0, "correct": 0, "total": 0, "scores": []}
        subject_stats[sid]["attempts"] += 1
        subject_stats[sid]["correct"] += attempt.get("correct_count", 0)
        subject_stats[sid]["total"] += attempt.get("total_questions", 0)
        subject_stats[sid]["scores"].append(attempt.get("score_percentage", 0))
    
    # Get subject names
    subjects = await db.subjects.find({}).to_list(100)
    subject_map = {s["id"]: s["name"] for s in subjects}
    
    subject_progress = []
    for sid, stats in subject_stats.items():
        accuracy = (stats["correct"] / stats["total"] * 100) if stats["total"] > 0 else 0
        avg_score = sum(stats["scores"]) / len(stats["scores"]) if stats["scores"] else 0
        subject_progress.append({
            "subject_id": sid,
            "subject_name": subject_map.get(sid, "Unknown"),
            "attempts": stats["attempts"],
            "accuracy": round(accuracy, 1),
            "average_score": round(avg_score, 1),
            "total_questions_attempted": stats["total"]
        })
    
    return {
        "is_guest": False,
        "id": current_user["id"],
        "name": current_user["name"],
        "email": current_user["email"],
        "created_at": current_user.get("created_at"),
        "total_attempts": total_attempts,
        "total_correct": total_correct,
        "total_questions_attempted": total_questions,
        "overall_accuracy": round(overall_accuracy, 1),
        "subject_progress": sorted(subject_progress, key=lambda x: x["attempts"], reverse=True)
    }

@api_router.put("/auth/profile")
async def update_profile(
    name: str = None,
    current_user: Optional[Dict] = Depends(get_current_user)
):
    """Update user profile"""
    if not current_user:
        raise HTTPException(status_code=401, detail="Login required")
    
    update_data = {}
    if name:
        update_data["name"] = name
    
    if update_data:
        await db.users.update_one(
            {"id": current_user["id"]},
            {"$set": update_data}
        )
    
    return {"message": "Profile updated successfully"}

@api_router.post("/auth/forgot-password")
async def forgot_password(data: ForgotPassword):
    """Request password reset - generates a 6-digit code"""
    user = await db.users.find_one({"email": data.email.lower()})
    
    if not user:
        # Don't reveal if email exists for security
        return {
            "message": "If this email exists, a reset code has been generated",
            "reset_code": None
        }
    
    # Generate 6-digit reset code
    reset_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    reset_expires = datetime.utcnow() + timedelta(minutes=15)
    
    # Save reset code to user
    await db.users.update_one(
        {"email": data.email.lower()},
        {"$set": {
            "reset_code": reset_code,
            "reset_code_expires": reset_expires
        }}
    )
    
    # In production, this would be sent via email
    # For now, we return it in the response for testing
    logger.info(f"Password reset code for {data.email}: {reset_code}")
    
    return {
        "message": "Reset code generated successfully",
        "reset_code": reset_code,  # Remove this line in production
        "expires_in_minutes": 15
    }

@api_router.post("/auth/reset-password")
async def reset_password(data: ResetPassword):
    """Reset password using the reset code"""
    user = await db.users.find_one({"email": data.email.lower()})
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or reset code")
    
    # Check if reset code matches and hasn't expired
    if not user.get("reset_code") or user.get("reset_code") != data.reset_code:
        raise HTTPException(status_code=400, detail="Invalid reset code")
    
    if user.get("reset_code_expires") and user["reset_code_expires"] < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Reset code has expired")
    
    # Validate new password
    if len(data.new_password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
    
    # Update password and clear reset code
    await db.users.update_one(
        {"email": data.email.lower()},
        {"$set": {
            "password": hash_password(data.new_password),
            "reset_code": None,
            "reset_code_expires": None
        }}
    )
    
    return {"message": "Password reset successfully"}

@api_router.post("/auth/guest/convert")
async def convert_guest_to_user(
    user_data: UserRegister,
    guest_attempts: List[str] = []
):
    """Convert guest progress to a new user account"""
    # Check if email already exists
    existing_user = await db.users.find_one({"email": user_data.email.lower()})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    user = User(
        name=user_data.name,
        email=user_data.email.lower(),
        password=hash_password(user_data.password)
    )
    
    await db.users.insert_one(user.dict())
    
    # Transfer guest attempts to new user
    if guest_attempts:
        await db.attempts.update_many(
            {"id": {"$in": guest_attempts}, "user_id": "guest_user"},
            {"$set": {"user_id": user.id}}
        )
    
    # Create token
    token = create_token(user.id, user.email)
    
    return {
        "message": "Account created and progress saved",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }

@api_router.get("/subjects")
async def get_subjects():
    """Get all subjects"""
    subjects = await db.subjects.find().to_list(100)
    if not subjects:
        # Return empty list if no subjects seeded yet
        return []
    # Remove MongoDB _id field
    for s in subjects:
        s.pop('_id', None)
    return subjects

@api_router.get("/subjects/{subject_id}")
async def get_subject(subject_id: str):
    """Get a specific subject"""
    subject = await db.subjects.find_one({"id": subject_id})
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    subject.pop('_id', None)
    return subject

@api_router.get("/subjects/{subject_id}/papers")
async def get_papers(subject_id: str):
    """Get all papers for a subject"""
    papers = await db.papers.find({"subject_id": subject_id}).sort("paper_number", 1).to_list(100)
    for p in papers:
        p.pop('_id', None)
    return papers

@api_router.get("/papers/{paper_id}")
async def get_paper(paper_id: str):
    """Get a specific paper"""
    paper = await db.papers.find_one({"id": paper_id})
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    paper.pop('_id', None)
    return paper

@api_router.get("/papers/{paper_id}/questions")
async def get_questions(paper_id: str):
    """Get all questions for a paper"""
    questions = await db.questions.find({"paper_id": paper_id}).sort("question_number", 1).to_list(200)
    for q in questions:
        q.pop('_id', None)
    return questions

@api_router.post("/attempts")
async def create_attempt(
    attempt_data: AttemptCreate,
    user_id: str = Depends(get_user_id)
):
    """Submit an exam attempt"""
    # Get questions for the paper
    questions = await db.questions.find({"paper_id": attempt_data.paper_id}).to_list(200)
    
    if not questions:
        raise HTTPException(status_code=404, detail="Paper not found")
    
    # Calculate score
    correct_count = 0
    wrong_count = 0
    skipped_count = 0
    
    for q in questions:
        q_id = q["id"]
        if q_id in attempt_data.answers:
            if attempt_data.answers[q_id] == q["correct_option"]:
                correct_count += 1
            else:
                wrong_count += 1
        else:
            skipped_count += 1
    
    total_questions = len(questions)
    score_percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    
    attempt = Attempt(
        user_id=user_id,
        paper_id=attempt_data.paper_id,
        subject_id=attempt_data.subject_id,
        answers=attempt_data.answers,
        correct_count=correct_count,
        wrong_count=wrong_count,
        skipped_count=skipped_count,
        total_questions=total_questions,
        score_percentage=round(score_percentage, 2),
        time_taken_seconds=attempt_data.time_taken_seconds,
        timer_mode=attempt_data.timer_mode
    )
    
    await db.attempts.insert_one(attempt.dict())
    
    # Update user stats if not guest
    if user_id != "guest_user":
        await db.users.update_one(
            {"id": user_id},
            {
                "$inc": {
                    "total_attempts": 1,
                    "total_correct": correct_count,
                    "total_questions_attempted": total_questions
                }
            }
        )
    
    return attempt

@api_router.get("/attempts")
async def get_attempts(
    subject_id: Optional[str] = None,
    paper_id: Optional[str] = None,
    limit: int = Query(default=50, le=100),
    user_id: str = Depends(get_user_id)
):
    """Get user's attempt history"""
    query = {"user_id": user_id}
    if subject_id:
        query["subject_id"] = subject_id
    if paper_id:
        query["paper_id"] = paper_id
    
    attempts = await db.attempts.find(query).sort("created_at", -1).to_list(limit)
    for a in attempts:
        a.pop('_id', None)
    return attempts

@api_router.get("/analytics")
async def get_analytics():
    """Get performance analytics"""
    attempts = await db.attempts.find({"user_id": "default_user"}).to_list(1000)
    
    if not attempts:
        return {
            "total_attempts": 0,
            "total_questions_attempted": 0,
            "overall_accuracy": 0,
            "subject_performance": [],
            "recent_scores": [],
            "best_score": 0,
            "average_score": 0
        }
    
    # Calculate overall stats
    total_correct = sum(a["correct_count"] for a in attempts)
    total_questions = sum(a["total_questions"] for a in attempts)
    overall_accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0
    
    # Subject-wise performance
    subject_stats = {}
    for attempt in attempts:
        sid = attempt["subject_id"]
        if sid not in subject_stats:
            subject_stats[sid] = {"correct": 0, "total": 0, "attempts": 0, "scores": []}
        subject_stats[sid]["correct"] += attempt["correct_count"]
        subject_stats[sid]["total"] += attempt["total_questions"]
        subject_stats[sid]["attempts"] += 1
        subject_stats[sid]["scores"].append(attempt["score_percentage"])
    
    # Get subject names
    subjects = await db.subjects.find().to_list(100)
    subject_names = {s["id"]: s["name"] for s in subjects}
    
    subject_performance = []
    for sid, stats in subject_stats.items():
        accuracy = (stats["correct"] / stats["total"] * 100) if stats["total"] > 0 else 0
        subject_performance.append({
            "subject_id": sid,
            "subject_name": subject_names.get(sid, "Unknown"),
            "attempts": stats["attempts"],
            "accuracy": round(accuracy, 2),
            "best_score": max(stats["scores"]) if stats["scores"] else 0,
            "average_score": round(sum(stats["scores"]) / len(stats["scores"]), 2) if stats["scores"] else 0
        })
    
    # Recent scores (last 10)
    recent_attempts = sorted(attempts, key=lambda x: x["created_at"], reverse=True)[:10]
    recent_scores = [{"date": a["created_at"].isoformat(), "score": a["score_percentage"]} for a in recent_attempts]
    
    # Best and average score
    all_scores = [a["score_percentage"] for a in attempts]
    
    return {
        "total_attempts": len(attempts),
        "total_questions_attempted": total_questions,
        "overall_accuracy": round(overall_accuracy, 2),
        "subject_performance": subject_performance,
        "recent_scores": recent_scores,
        "best_score": max(all_scores) if all_scores else 0,
        "average_score": round(sum(all_scores) / len(all_scores), 2) if all_scores else 0
    }

@api_router.get("/settings")
async def get_settings():
    """Get user settings"""
    settings = await db.settings.find_one({"user_id": "default_user"})
    if not settings:
        # Return default settings
        default_settings = UserSettings()
        await db.settings.insert_one(default_settings.dict())
        return default_settings.dict()
    settings.pop('_id', None)
    return settings

@api_router.put("/settings")
async def update_settings(settings: UserSettings):
    """Update user settings"""
    settings.user_id = "default_user"
    await db.settings.update_one(
        {"user_id": "default_user"},
        {"$set": settings.dict()},
        upsert=True
    )
    return settings

@api_router.post("/seed")
async def seed_database():
    """Seed the database with subjects, papers, and questions"""
    try:
        # Check if already seeded
        existing_subjects = await db.subjects.count_documents({})
        if existing_subjects > 0:
            return {"message": "Database already seeded", "subjects": existing_subjects}
        
        logger.info("Starting database seeding...")
        
        # Seed subjects
        subjects_created = []
        for subject_data in SUBJECTS_DATA:
            subject = Subject(**subject_data)
            await db.subjects.insert_one(subject.dict())
            subjects_created.append(subject)
            logger.info(f"Created subject: {subject.name}")
        
        # Seed papers and questions for each subject
        total_papers = 0
        total_questions = 0
        
        for subject_idx, subject in enumerate(subjects_created):
            # Create 20 practice papers
            for paper_num in range(1, 21):
                paper = Paper(
                    subject_id=subject.id,
                    paper_number=paper_num,
                    is_master=False,
                    title=f"{subject.name} Practice Paper {paper_num}",
                    total_questions=100,
                    duration_minutes=90
                )
                await db.papers.insert_one(paper.dict())
                total_papers += 1
                
                # Generate questions for this paper with unique seed for variety
                questions = generate_questions_for_subject(
                    subject.name, paper.id, subject.id, 100, False, paper_seed=subject_idx * 100 + paper_num
                )
                if questions:
                    await db.questions.insert_many(questions)
                    total_questions += len(questions)
            
            # Create 1 master sample paper
            master_paper = Paper(
                subject_id=subject.id,
                paper_number=0,
                is_master=True,
                title=f"{subject.name} Master Prediction Paper",
                total_questions=100,
                duration_minutes=90
            )
            await db.papers.insert_one(master_paper.dict())
            total_papers += 1
            
            # Generate master questions (higher difficulty)
            master_questions = generate_questions_for_subject(
                subject.name, master_paper.id, subject.id, 100, True, paper_seed=subject_idx * 100 + 99
            )
            if master_questions:
                await db.questions.insert_many(master_questions)
                total_questions += len(master_questions)
            
            logger.info(f"Seeded papers and questions for: {subject.name}")
        
        # Create default settings
        default_settings = UserSettings()
        await db.settings.insert_one(default_settings.dict())
        
        return {
            "message": "Database seeded successfully",
            "subjects": len(subjects_created),
            "papers": total_papers,
            "questions": total_questions
        }
        
    except Exception as e:
        logger.error(f"Error seeding database: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/reseed")
async def reseed_database():
    """Clear and reseed the database with fresh questions from real PYQ database including extreme papers"""
    try:
        logger.info("Clearing existing data...")
        
        # Clear all collections
        await db.subjects.delete_many({})
        await db.papers.delete_many({})
        await db.questions.delete_many({})
        await db.attempts.delete_many({})
        await db.settings.delete_many({})
        
        logger.info("Starting fresh database seeding with real PYQs and extreme papers...")
        
        # Seed subjects
        subjects_created = []
        for subject_data in SUBJECTS_DATA:
            subject = Subject(**subject_data)
            await db.subjects.insert_one(subject.dict())
            subjects_created.append(subject)
            logger.info(f"Created subject: {subject.name}")
        
        # Seed papers and questions for each subject
        total_papers = 0
        total_questions = 0
        
        for subject_idx, subject in enumerate(subjects_created):
            # Create 20 practice papers
            for paper_num in range(1, 21):
                paper = Paper(
                    subject_id=subject.id,
                    paper_number=paper_num,
                    is_master=False,
                    title=f"{subject.name} Practice Paper {paper_num}",
                    total_questions=100,
                    duration_minutes=90
                )
                await db.papers.insert_one(paper.dict())
                total_papers += 1
                
                # Generate questions for this paper using high-quality database
                questions = generate_questions_for_subject(
                    subject.name, paper.id, subject.id, 100, False, paper_seed=subject_idx * 100 + paper_num
                )
                if questions:
                    await db.questions.insert_many(questions)
                    total_questions += len(questions)
            
            # Create 5 EXTREME difficulty papers (numbered 21-25)
            for extreme_num in range(1, 6):
                extreme_paper = Paper(
                    subject_id=subject.id,
                    paper_number=20 + extreme_num,  # Papers 21-25
                    is_master=False,
                    title=f"Practice Paper {20 + extreme_num} (Extreme)",
                    total_questions=100,
                    duration_minutes=90
                )
                await db.papers.insert_one(extreme_paper.dict())
                total_papers += 1
                
                # Generate extreme difficulty questions with unique seed
                extreme_questions = generate_extreme_questions_for_subject(
                    subject.name, extreme_paper.id, subject.id, 100, paper_seed=subject_idx * 100 + 20 + extreme_num
                )
                if extreme_questions:
                    await db.questions.insert_many(extreme_questions)
                    total_questions += len(extreme_questions)
                
                logger.info(f"Created extreme paper {extreme_num} for: {subject.name}")
            
            # Create 1 master sample paper
            master_paper = Paper(
                subject_id=subject.id,
                paper_number=0,
                is_master=True,
                title=f"{subject.name} Master Prediction Paper",
                total_questions=100,
                duration_minutes=90
            )
            await db.papers.insert_one(master_paper.dict())
            total_papers += 1
            
            # Generate master questions (higher difficulty) with unique seed
            master_questions = generate_questions_for_subject(
                subject.name, master_paper.id, subject.id, 100, True, paper_seed=subject_idx * 100 + 99
            )
            if master_questions:
                await db.questions.insert_many(master_questions)
                total_questions += len(master_questions)
            
            logger.info(f"Seeded all papers for: {subject.name}")
        
        # Create default settings
        default_settings = UserSettings()
        await db.settings.insert_one(default_settings.dict())
        
        return {
            "message": "Database reseeded successfully with real PYQs and extreme papers",
            "subjects": len(subjects_created),
            "papers": total_papers,
            "questions": total_questions,
            "extreme_papers_per_subject": 5
        }
        
    except Exception as e:
        logger.error(f"Error reseeding database: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/attempt/{attempt_id}/review")
async def get_attempt_review(attempt_id: str):
    """Get detailed review of an attempt with correct answers"""
    attempt = await db.attempts.find_one({"id": attempt_id})
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    
    attempt.pop('_id', None)
    questions = await db.questions.find({"paper_id": attempt["paper_id"]}).sort("question_number", 1).to_list(200)
    
    review_data = []
    for q in questions:
        q.pop('_id', None)
        user_answer = attempt["answers"].get(q["id"], -1)
        review_data.append({
            "question": q,
            "user_answer": user_answer,
            "is_correct": user_answer == q["correct_option"],
            "is_skipped": user_answer == -1
        })
    
    return {
        "attempt": attempt,
        "review": review_data
    }

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
