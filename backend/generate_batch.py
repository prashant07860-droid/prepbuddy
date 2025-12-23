"""
OPSC Question Generator - Batch Mode
Generates questions subject by subject to handle the large volume
"""

import os
import json
import sys
from openai import OpenAI

# Initialize OpenAI client with Emergent LLM key
client = OpenAI(
    api_key="sk-emergent-4C1A73aEe3bEe59Ca9",
    base_url="https://llm.api.emergentagi.com/v1"
)

def generate_subject_questions(subject: str, topics: list, questions_per_topic: int = 25):
    """Generate questions for a single subject"""
    
    all_questions = []
    
    for topic in topics:
        print(f"  Generating for: {topic[:50]}...")
        
        prompt = f"""Generate {questions_per_topic} unique, challenging OPSC exam MCQ questions for:
Subject: {subject}
Topic: {topic}

REQUIREMENTS:
1. Use MULTI-STATEMENT format: "Which statements are correct? (1)... (2)... (3)... (4)..." with options like "(A) 1 and 3", "(B) 2 and 4"
2. Include "NOT correct" questions
3. Include matching pairs
4. Include chronological ordering
5. Include assertion-reason type
6. Questions must be CHALLENGING - test analytical thinking
7. Include specific dates, years, names where relevant
8. Each question has exactly 4 options (A, B, C, D)

Return ONLY valid JSON array:
[{{"question_text": "...", "options": ["A", "B", "C", "D"], "correct_option": 0, "explanation": "...", "difficulty": "hard", "topic": "{topic}"}}]

Generate exactly {questions_per_topic} diverse questions."""

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are an expert OPSC question setter. Generate challenging MCQs in valid JSON format only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=8000
            )
            
            content = response.choices[0].message.content.strip()
            
            # Extract JSON
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            questions = json.loads(content)
            all_questions.extend(questions)
            print(f"    ✓ Generated {len(questions)} questions")
            
        except Exception as e:
            print(f"    ✗ Error: {str(e)[:50]}")
    
    return all_questions

# Subject topics
SUBJECTS = {
    "Polity": [
        "Indian Constitution - Preamble, Parts, Schedules, Articles 1-395",
        "Fundamental Rights Articles 12-35 and their restrictions",
        "Directive Principles of State Policy Articles 36-51",
        "Fundamental Duties Article 51A",
        "Union Executive - President, Vice President, PM, Council of Ministers",
        "Parliament - Lok Sabha, Rajya Sabha, Joint Sessions, Parliamentary Committees",
        "State Legislature and Executive - Governor, CM, State Legislature",
        "Judiciary - Supreme Court, High Courts, Judicial Review, PIL",
        "Constitutional Bodies - EC, UPSC, Finance Commission, CAG, NCSC, NCST",
        "Emergency Provisions - National, State, Financial Emergency",
        "Amendment Procedure and Important Amendments",
        "Centre-State Relations - Legislative, Administrative, Financial"
    ],
    "Geography": [
        "Physical Geography - Plate Tectonics, Landforms, Weathering, Erosion",
        "Indian Rivers and Drainage Systems - Himalayan and Peninsular Rivers",
        "Indian Monsoon Mechanism and Climate Zones",
        "Soils of India - Types, Distribution, Conservation",
        "Natural Vegetation and Wildlife - Forests, National Parks, Sanctuaries",
        "World Physical Geography - Mountains, Deserts, Islands, Straits",
        "World Map Questions - Countries, Capitals, Boundaries, Strategic Locations",
        "Agriculture in India - Crops, Irrigation, Green Revolution",
        "Minerals and Energy Resources - Distribution, Mining, Power",
        "Oceanography - Currents, Tides, Marine Resources, Sea Routes",
        "Population Geography - Distribution, Migration, Census Data",
        "Odisha Geography - Rivers, Districts, Minerals, Ports, Climate"
    ],
    "History of Modern India": [
        "British Expansion - Battles of Plassey, Buxar, Anglo-Mysore, Anglo-Maratha Wars",
        "Administrative and Economic Policies of British",
        "Social and Religious Reform Movements of 19th Century",
        "1857 Revolt - Causes, Leaders, Centers, Consequences",
        "Indian National Congress - Moderate, Extremist, Revolutionary Phases",
        "Revolutionary Nationalism - Secret Societies, Individual Acts",
        "Gandhian Movements - NCM, CDM, Quit India, Salt March",
        "Subhas Chandra Bose, INA, and Revolutionary Activities Abroad",
        "Constitutional Development - Acts of 1773, 1784, 1833, 1858, 1909, 1919, 1935",
        "Communal Politics and Partition",
        "Tribal and Peasant Movements",
        "Freedom Movement in Odisha - Paika Rebellion, Leaders, Events"
    ],
    "Ethics": [
        "Ethics - Definition, Theories, Determinants of Ethics",
        "Attitude - Structure, Formation, Change, Moral Attitudes",
        "Aptitude and Values for Civil Services - Integrity, Impartiality",
        "Emotional Intelligence - Components, Application in Administration",
        "Ethics in Public Administration - Code of Conduct, Rules",
        "Corruption - Types, Causes, Impact, Anti-corruption Measures",
        "Ethical Dilemmas and Case Studies in Governance",
        "Corporate Governance and Business Ethics",
        "Environmental Ethics and Sustainable Development",
        "Information Technology and Ethical Issues",
        "Contributions of Moral Thinkers - Gandhi, Ambedkar, Vivekananda",
        "Ethics in International Relations and Diplomacy"
    ],
    "Science and Technology": [
        "Physics - Mechanics, Thermodynamics, Optics, Electricity, Magnetism",
        "Chemistry - Elements, Compounds, Chemical Reactions, Everyday Chemistry",
        "Biology - Cell, Genetics, Evolution, Human Physiology, Diseases",
        "ISRO and Space Technology - Missions, Satellites, Launch Vehicles",
        "Nuclear Science - Reactors, Applications, Nuclear Policy",
        "IT and Emerging Technologies - AI, ML, Blockchain, IoT, Cybersecurity",
        "Biotechnology - DNA, Genetic Engineering, Applications, Ethics",
        "Defence Technology - Missiles, Fighter Jets, Naval Systems",
        "Health and Medical Sciences - Diseases, Vaccines, Medical Advances",
        "Agriculture Technology - GM Crops, Precision Farming",
        "Energy Technology - Solar, Wind, Nuclear, Hydrogen",
        "Recent Scientific Discoveries and Innovations 2020-2024"
    ],
    "Economics": [
        "Basic Concepts - GDP, GNP, NNP, National Income Accounting",
        "Indian Economy Structure - Sectors, Employment, Growth",
        "Economic Planning - Five Year Plans to NITI Aayog",
        "Fiscal Policy - Union Budget, Taxation, Deficit, Public Debt",
        "Monetary Policy - RBI Functions, Interest Rates, Inflation Control",
        "Banking System - Commercial Banks, RBI, NPAs, Financial Inclusion",
        "Agriculture - MSP, Procurement, Subsidies, Reforms",
        "Industrial Policy - Make in India, PLI, Industrial Development",
        "External Sector - Trade Policy, WTO, FTAs, Balance of Payments",
        "Economic Reforms - LPG 1991, Recent Reforms, GST, IBC",
        "Poverty and Employment - Measurement, Programs, MGNREGA",
        "Odisha Economy - Agriculture, Industries, Mining, Development"
    ],
    "Environment and Ecology": [
        "Ecology Fundamentals - Ecosystems, Food Chain, Ecological Pyramids",
        "Biodiversity - Hotspots, Endemic Species, Conservation Strategies",
        "Climate Change - Global Warming, Paris Agreement, IPCC Reports",
        "Air Pollution - Sources, Effects, Control, NAQI",
        "Water Pollution - Sources, Treatment, Ganga Action Plan",
        "Environmental Laws - EPA 1986, Wildlife Act, Forest Act, NGT",
        "International Environmental Conventions - CBD, Ramsar, CITES",
        "Protected Areas - National Parks, Sanctuaries, Biosphere Reserves",
        "Sustainable Development - SDGs, Circular Economy, Green Finance",
        "Renewable Energy and Clean Technology",
        "Waste Management - MSW Rules, E-waste, Plastic Ban",
        "Environmental Issues in Odisha - Forests, Wildlife, Coastal Zones"
    ],
    "Ancient & Medieval History": [
        "Indus Valley Civilization - Sites, Town Planning, Decline Theories",
        "Vedic Period - Rigvedic and Later Vedic Society, Economy, Religion",
        "Rise of Jainism and Buddhism - Teachings, Councils, Spread",
        "Mauryan Empire - Administration, Economy, Ashoka's Dhamma",
        "Post-Mauryan Period - Indo-Greeks, Kushanas, Satavahanas",
        "Gupta Empire - Administration, Art, Literature, Science",
        "Regional Kingdoms - Vakatakas, Pallavas, Chalukyas, Cholas",
        "Delhi Sultanate - Administration, Economy, Architecture",
        "Mughal Empire - Administration, Art, Culture, Economy",
        "Bhakti and Sufi Movements - Saints, Teachings, Impact",
        "Art and Architecture - Temples, Mosques, Paintings",
        "History of Odisha - Kalinga, Bhauma-Kara, Ganga, Gajapati"
    ],
    "Indian Society": [
        "Social Structure - Caste System, Varna, Jati, Class",
        "Religious Diversity - Hinduism, Islam, Christianity, Sikhism, Buddhism",
        "Tribal Society - Constitutional Provisions, Development, Issues",
        "Women in Indian Society - Status, Issues, Empowerment, Laws",
        "Population - Trends, Dividend, Policy, Census 2011",
        "Urbanization - Growth, Problems, Smart Cities, Slums",
        "Globalization - Impact on Culture, Economy, Society",
        "Communalism, Regionalism, Secularism",
        "Social Movements - Farmers, Women, Tribal, Environmental",
        "Role of Civil Society and NGOs",
        "Social Welfare Schemes - Education, Health, Employment",
        "Youth and Demographic Dividend"
    ],
    "Odisha Studies": [
        "Ancient Odisha - Kalinga, Kharavela, Bhauma-Kara Dynasty",
        "Medieval Odisha - Gangas, Gajapatis, Temple Building",
        "Modern Odisha - British Rule, Freedom Movement, Merger",
        "Geography of Odisha - Physical Features, Rivers, Climate",
        "Economy of Odisha - Agriculture, Industries, Minerals, Ports",
        "Art and Culture - Odissi, Chhau, Pattachitra, Tribal Art",
        "Temples of Odisha - Konark, Jagannath, Lingaraj, Mukteswara",
        "Festivals - Rath Yatra, Durga Puja, Tribal Festivals",
        "Odia Literature - Poetry, Prose, Modern Literature",
        "Tribal Communities - PVTG, Development, Issues",
        "Administration and Governance of Odisha",
        "Current Affairs of Odisha 2020-2024"
    ],
    "Current Affairs": [
        "National Politics and Governance 2023-2024",
        "International Relations - India's Foreign Policy, Bilateral Relations",
        "United Nations and International Organizations",
        "G20, BRICS, SCO, QUAD Summits and Developments",
        "Government Schemes and Programs 2023-2024",
        "Awards - Padma, National, International Awards",
        "Sports - Olympics, Asian Games, Commonwealth Games",
        "Science and Technology Developments 2023-2024",
        "Environment and Climate - COP, Agreements, Events",
        "Economy - Budget 2024, Economic Survey, Reforms",
        "Defence - Exercises, Acquisitions, Security",
        "Important Days, Themes, and Observances"
    ]
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_batch.py <subject_name>")
        print("Available subjects:", list(SUBJECTS.keys()))
        sys.exit(1)
    
    subject = sys.argv[1]
    
    if subject not in SUBJECTS:
        print(f"Unknown subject: {subject}")
        print("Available subjects:", list(SUBJECTS.keys()))
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"Generating questions for: {subject}")
    print(f"{'='*60}\n")
    
    questions = generate_subject_questions(subject, SUBJECTS[subject], questions_per_topic=25)
    
    # Save to file
    filename = f"/app/backend/questions_{subject.lower().replace(' ', '_').replace('&', 'and')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"Generated {len(questions)} questions for {subject}")
    print(f"Saved to: {filename}")
    print(f"{'='*60}")
