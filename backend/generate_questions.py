"""
OPSC Question Generator
Generates 2600+ unique, OPSC-level questions across 11 subjects
Using AI to create multi-statement, tricky, analytical questions
"""

import os
import json
import random
from openai import OpenAI

# Initialize OpenAI client with Emergent LLM key
client = OpenAI(
    api_key="sk-emergent-4C1A73aEe3bEe59Ca9",
    base_url="https://llm.api.emergentagi.com/v1"
)

# Subject definitions with detailed topics to cover
SUBJECTS = {
    "Polity": {
        "topics": [
            "Indian Constitution - Preamble, Parts, Schedules, Articles",
            "Fundamental Rights (Art 12-35), Directive Principles (Art 36-51), Fundamental Duties",
            "Union Executive - President, Vice President, Prime Minister, Council of Ministers",
            "Parliament - Lok Sabha, Rajya Sabha, Joint Sessions, Parliamentary Committees",
            "State Executive - Governor, Chief Minister, State Legislature",
            "Judiciary - Supreme Court, High Courts, Subordinate Courts, Judicial Review",
            "Constitutional Bodies - Election Commission, UPSC, Finance Commission, CAG",
            "Federalism, Centre-State Relations, Emergency Provisions",
            "Constitutional Amendments, Landmark Judgments",
            "Local Self Government - Panchayati Raj, Municipalities, 73rd & 74th Amendments",
            "Recent Constitutional Developments, New Laws enacted by Parliament",
            "Comparison with other countries' constitutions"
        ]
    },
    "Geography": {
        "topics": [
            "Physical Geography - Landforms, Mountains, Plateaus, Plains",
            "Indian Geography - Rivers, Drainage Systems, Lakes",
            "Climate and Monsoons - Indian Monsoon Mechanism, Climate Zones",
            "Soils and Natural Vegetation - Types, Distribution, Conservation",
            "World Geography - Continents, Oceans, Important Straits, Passes",
            "Map-based Questions - Locations, Boundaries, Neighboring Countries",
            "Economic Geography - Agriculture, Industries, Resources",
            "Human Geography - Population, Migration, Urbanization",
            "Environmental Geography - Biodiversity Hotspots, Protected Areas",
            "Odisha Geography - Districts, Rivers, Minerals, Climate",
            "Oceanography - Currents, Tides, Marine Resources",
            "Recent Geographical Events - Earthquakes, Cyclones, Climate Change"
        ]
    },
    "History of Modern India": {
        "topics": [
            "British Expansion - Battles, Treaties, Doctrines",
            "Economic Impact of British Rule - Drain Theory, Famines",
            "Social Reform Movements - Brahmo Samaj, Arya Samaj, Reform Leaders",
            "1857 Revolt - Causes, Leaders, Centers, Consequences",
            "Indian National Congress - Formation, Moderate & Extremist Phase",
            "Revolutionary Movements - Anushilan Samiti, Ghadar Movement",
            "Gandhian Era - NCM, CDM, Quit India, Salt March",
            "Subhas Chandra Bose and INA",
            "Constitutional Development - Acts of 1909, 1919, 1935",
            "Independence and Partition",
            "Post-Independence Developments",
            "Freedom Fighters from Odisha"
        ]
    },
    "Ethics": {
        "topics": [
            "Ethics - Definitions, Theories, Concepts",
            "Attitude - Formation, Components, Change",
            "Aptitude and Foundational Values for Civil Services",
            "Emotional Intelligence - Concepts, Components, Application",
            "Public Administration Ethics - Code of Conduct, Accountability",
            "Corruption - Types, Causes, Remedies, Anti-corruption Bodies",
            "Case Studies in Ethics - Moral Dilemmas",
            "Work Culture and Values",
            "Corporate Governance and CSR",
            "Environmental Ethics",
            "Ethics in International Relations",
            "Contributions of Moral Thinkers - Gandhi, Ambedkar, etc."
        ]
    },
    "Science and Technology": {
        "topics": [
            "Physics - Mechanics, Heat, Light, Sound, Electricity",
            "Chemistry - Elements, Compounds, Reactions, Everyday Chemistry",
            "Biology - Cell Biology, Genetics, Human Physiology",
            "Space Technology - ISRO Missions, Satellites, Rockets",
            "Nuclear Technology - Power Plants, Applications",
            "Information Technology - AI, Blockchain, Cybersecurity",
            "Biotechnology - Applications, Concerns, Regulations",
            "Nanotechnology - Applications and Implications",
            "Defence Technology - Missiles, Weapons Systems",
            "Recent Scientific Discoveries and Inventions",
            "Science in Daily Life",
            "Health and Medicine - Diseases, Vaccines, Treatments"
        ]
    },
    "Economics": {
        "topics": [
            "Basic Economic Concepts - GDP, GNP, NDP, Inflation",
            "Indian Economy - Structure, Sectors, Growth",
            "Economic Planning - Five Year Plans, NITI Aayog",
            "Fiscal Policy - Budget, Taxation, Deficit",
            "Monetary Policy - RBI, Interest Rates, Money Supply",
            "Banking - Types, RBI Functions, NPAs",
            "Agriculture - Green Revolution, MSP, Subsidies",
            "Industry - Industrial Policy, Make in India",
            "International Trade - WTO, FTAs, Balance of Payments",
            "Economic Reforms - LPG, Recent Reforms",
            "Social Sector - Poverty, Employment, Schemes",
            "Odisha Economy - Resources, Industries, Development"
        ]
    },
    "Environment and Ecology": {
        "topics": [
            "Ecology Basics - Ecosystems, Food Chains, Biogeochemical Cycles",
            "Biodiversity - Hotspots, Endangered Species, Conservation",
            "Climate Change - Global Warming, Greenhouse Effect, Mitigation",
            "Environmental Pollution - Air, Water, Soil, Noise",
            "Environmental Laws and Policies - EPA, Wildlife Protection Act",
            "International Environmental Agreements - Paris Agreement, COP",
            "Sustainable Development - SDGs, Green Economy",
            "Renewable Energy - Solar, Wind, Biomass",
            "Forest and Wildlife - National Parks, Sanctuaries, Biosphere Reserves",
            "Environmental Impact Assessment",
            "Waste Management - Solid, E-waste, Biomedical",
            "Environmental Issues in Odisha"
        ]
    },
    "Ancient & Medieval History": {
        "topics": [
            "Indus Valley Civilization - Sites, Features, Decline",
            "Vedic Period - Early and Later Vedic",
            "Buddhism and Jainism - Founders, Teachings, Councils",
            "Mauryan Empire - Chandragupta, Ashoka, Administration",
            "Post-Mauryan Period - Sungas, Kushanas, Satavahanas",
            "Gupta Empire - Golden Age, Art, Literature",
            "Regional Kingdoms - Cholas, Pallavas, Chalukyas",
            "Delhi Sultanate - Slave, Khilji, Tughlaq, Lodhi",
            "Mughal Empire - Babur to Aurangzeb",
            "Bhakti and Sufi Movements",
            "Art and Architecture - Temples, Mosques, Paintings",
            "History of Odisha - Kalinga, Bhauma-Karas, Gangas"
        ]
    },
    "Indian Society": {
        "topics": [
            "Indian Social Structure - Caste, Class, Tribe",
            "Religious and Linguistic Diversity",
            "Women and Society - Status, Issues, Empowerment",
            "Population - Trends, Policy, Demographic Dividend",
            "Urbanization - Patterns, Problems, Smart Cities",
            "Globalization and its Impact on Society",
            "Social Issues - Poverty, Inequality, Communalism",
            "Social Movements in India",
            "Role of Civil Society and NGOs",
            "Social Security and Welfare Schemes",
            "Youth and Education",
            "Regional and Cultural Identity"
        ]
    },
    "Odisha Studies": {
        "topics": [
            "History of Odisha - Ancient, Medieval, Modern",
            "Freedom Movement in Odisha - Leaders, Events",
            "Geography of Odisha - Rivers, Climate, Minerals",
            "Economy of Odisha - Agriculture, Industries, Development",
            "Art and Culture - Odissi, Pattachitra, Tribal Art",
            "Temples and Architecture - Konark, Puri, Bhubaneswar",
            "Festivals and Fairs - Rath Yatra, Durga Puja",
            "Literature - Writers, Poets, Odia Literature",
            "Tribal Communities and Development",
            "Administration and Governance",
            "Current Affairs of Odisha",
            "Tourism and Heritage"
        ]
    },
    "Current Affairs": {
        "topics": [
            "National Events - Politics, Economy, Society",
            "International Affairs - UN, G20, BRICS, Bilateral Relations",
            "Government Schemes and Policies",
            "Awards and Honours - National, International",
            "Sports - Achievements, Events, Awards",
            "Science and Technology Updates",
            "Environment and Climate Updates",
            "Defence and Security",
            "Economy and Business",
            "Books, Authors, Personalities",
            "Important Days and Themes",
            "Summits and Conferences"
        ]
    }
}

def generate_questions_for_topic(subject: str, topic: str, count: int = 25) -> list:
    """Generate OPSC-level questions for a specific topic using AI"""
    
    prompt = f"""Generate {count} unique, challenging OPSC (Odisha Public Service Commission) exam-level MCQ questions for the topic: "{topic}" under the subject "{subject}".

IMPORTANT REQUIREMENTS:
1. Questions must be CHALLENGING and ANALYTICAL - this is one of India's toughest state-level exams
2. Use MULTI-STATEMENT format wherever applicable:
   Example: "Which of the following statements are correct regarding X?
   (1) Statement 1
   (2) Statement 2
   (3) Statement 3
   (4) Statement 4"
   With options like: (A) 1 and 3 only, (B) 2 and 4 only, (C) 1, 2 and 3, (D) All of the above

3. Include various question types:
   - "Which of the following is NOT correct?"
   - "Match the following pairs"
   - "Arrange in chronological order"
   - "Consider the following statements... Which is/are correct?"
   - Assertion-Reason questions
   - Map-based location questions (for Geography)
   - Date/Year specific questions

4. Each question must have exactly 4 options (A, B, C, D)
5. Mark the correct answer clearly
6. Include a brief explanation for each answer
7. Questions should test deep understanding, not just memorization
8. Include recent developments and current affairs where relevant

Return the questions in this exact JSON format:
[
  {{
    "question_text": "Full question text with all statements if applicable",
    "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
    "correct_option": 0,  // 0 for A, 1 for B, 2 for C, 3 for D
    "explanation": "Detailed explanation of why this is correct",
    "difficulty": "hard",  // or "medium" or "extreme"
    "topic": "{topic}"
  }}
]

Generate exactly {count} questions. Make them diverse and cover different aspects of the topic."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert question paper setter for OPSC (Odisha Public Service Commission) exams. Generate challenging, analytical MCQ questions that test deep understanding."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=8000
        )
        
        content = response.choices[0].message.content
        
        # Extract JSON from response
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        
        questions = json.loads(content)
        return questions
        
    except Exception as e:
        print(f"Error generating questions for {topic}: {e}")
        return []

def generate_all_questions():
    """Generate all questions for all subjects"""
    
    all_questions = {}
    
    for subject, data in SUBJECTS.items():
        print(f"\n{'='*60}")
        print(f"Generating questions for: {subject}")
        print(f"{'='*60}")
        
        subject_questions = []
        
        for topic in data["topics"]:
            print(f"  Processing: {topic}")
            questions = generate_questions_for_topic(subject, topic, count=25)
            
            if questions:
                subject_questions.extend(questions)
                print(f"    Generated {len(questions)} questions")
            else:
                print(f"    Failed to generate questions")
        
        all_questions[subject] = subject_questions
        print(f"\nTotal for {subject}: {len(subject_questions)} questions")
    
    return all_questions

def save_questions(questions: dict, filename: str = "opsc_questions_database.py"):
    """Save generated questions to a Python file"""
    
    output = '''"""
OPSC Questions Database
Auto-generated comprehensive question bank with 2600+ unique questions
Format follows actual OPSC exam patterns
"""

OPSC_QUESTIONS_DATABASE = '''
    
    output += json.dumps(questions, indent=2, ensure_ascii=False)
    
    with open(f"/app/backend/{filename}", "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"\nQuestions saved to {filename}")

if __name__ == "__main__":
    print("Starting OPSC Question Generation...")
    print("This will generate 2600+ unique questions across 11 subjects")
    
    questions = generate_all_questions()
    
    # Count total
    total = sum(len(q) for q in questions.values())
    print(f"\n{'='*60}")
    print(f"TOTAL QUESTIONS GENERATED: {total}")
    print(f"{'='*60}")
    
    save_questions(questions)
