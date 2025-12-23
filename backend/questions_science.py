"""
OPSC Questions Database - Science and Technology
High-quality, OPSC-level questions based on actual exam patterns
Categories: Space Technology, Nuclear Technology, Defence Technology, Biotechnology,
IT & Computers, Health & Medicine, Agriculture Technology, Important Days & Themes,
Important Books, Miscellaneous
"""

SCIENCE_TECHNOLOGY_QUESTIONS = [
    # ==================== SPACE TECHNOLOGY ====================
    {
        "question_text": "Consider the following statements about ISRO's missions:\n(1) Chandrayaan-3 successfully landed near the lunar south pole in 2023\n(2) Aditya-L1 is India's first solar observation mission\n(3) Gaganyaan will be India's first crewed space mission\n(4) PSLV is used for launching heavy satellites to GTO\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - GSLV (not PSLV) is used for heavy satellites to Geosynchronous Transfer Orbit.",
        "difficulty": "hard",
        "topic": "Space Technology"
    },
    {
        "question_text": "The Lagrange Point L1, where Aditya-L1 is positioned, is significant because:",
        "options": ["It is the closest point to the Sun", "Objects here can maintain stable position relative to Earth and Sun", "It has zero gravity", "It is the coldest point in space"],
        "correct_option": 1,
        "explanation": "L1 is one of five Lagrange points where gravitational forces of Sun and Earth balance, allowing spacecraft to maintain stable position with minimal fuel.",
        "difficulty": "medium",
        "topic": "Space Technology"
    },
    {
        "question_text": "Which of the following launch vehicles of ISRO is cryogenic?\n(1) PSLV\n(2) GSLV Mk II\n(3) GSLV Mk III (LVM3)\n(4) SSLV\n\nSelect the correct answer:",
        "options": ["2 only", "2 and 3 only", "1 and 2 only", "All of the above"],
        "correct_option": 1,
        "explanation": "GSLV Mk II and GSLV Mk III (LVM3) use cryogenic upper stages. PSLV uses solid and liquid stages but not cryogenic.",
        "difficulty": "hard",
        "topic": "Space Technology"
    },
    {
        "question_text": "NavIC (Navigation with Indian Constellation) covers:",
        "options": ["Only India", "India and 1500 km beyond its borders", "Entire Asia", "Global coverage"],
        "correct_option": 1,
        "explanation": "NavIC has 7 satellites covering India and region up to 1500 km from Indian boundary with position accuracy of less than 20 meters.",
        "difficulty": "medium",
        "topic": "Space Technology"
    },

    # ==================== NUCLEAR TECHNOLOGY ====================
    {
        "question_text": "Consider the following about nuclear power plants in India:\n(1) Tarapur was India's first nuclear power plant\n(2) India follows a three-stage nuclear programme\n(3) Kudankulam uses Russian VVER reactors\n(4) BARC is responsible for nuclear research\n\nWhich of the above are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Tarapur (1969) was first, three-stage programme uses U-Pu-Th cycle, Kudankulam has Russian VVER reactors.",
        "difficulty": "hard",
        "topic": "Nuclear Technology"
    },
    {
        "question_text": "India's three-stage nuclear power programme is based on:",
        "options": ["Uranium-Plutonium-Thorium cycle", "Uranium-Thorium-Plutonium cycle", "Thorium-Uranium-Plutonium cycle", "Only Uranium cycle"],
        "correct_option": 0,
        "explanation": "The three stages are: Stage 1 (PHWR using natural uranium), Stage 2 (FBR using plutonium), Stage 3 (using thorium-U233).",
        "difficulty": "medium",
        "topic": "Nuclear Technology"
    },

    # ==================== DEFENCE TECHNOLOGY ====================
    {
        "question_text": "The Agni-V missile with MIRV technology was successfully tested under which mission?",
        "options": ["Mission Shakti", "Mission Divyastra", "Mission Astra", "Mission Trinetra"],
        "correct_option": 1,
        "explanation": "India successfully tested Agni-5 with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology under 'Mission Divyastra' in March 2024.",
        "difficulty": "medium",
        "topic": "Defence Technology"
    },
    {
        "question_text": "Consider the following missiles and their types:\n(1) BrahMos - Cruise Missile\n(2) Prithvi - Ballistic Missile\n(3) Akash - Surface-to-Air Missile\n(4) Nag - Anti-Tank Guided Missile\n\nWhich of the above pairs are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. BrahMos is supersonic cruise missile, Prithvi is short-range ballistic missile, Akash is SAM, and Nag is ATGM.",
        "difficulty": "medium",
        "topic": "Defence Technology"
    },
    {
        "question_text": "INS Vikrant, commissioned in 2022, is:",
        "options": ["India's first nuclear submarine", "India's first indigenous aircraft carrier", "India's first destroyer", "India's first frigate"],
        "correct_option": 1,
        "explanation": "INS Vikrant (IAC-1) is India's first indigenously built aircraft carrier, commissioned on September 2, 2022.",
        "difficulty": "easy",
        "topic": "Defence Technology"
    },
    {
        "question_text": "The Light Combat Aircraft (LCA) Tejas is manufactured by:",
        "options": ["DRDO", "HAL", "BEL", "BHEL"],
        "correct_option": 1,
        "explanation": "HAL (Hindustan Aeronautics Limited) manufactures the LCA Tejas, while DRDO was involved in its design and development.",
        "difficulty": "easy",
        "topic": "Defence Technology"
    },

    # ==================== BIOTECHNOLOGY ====================
    {
        "question_text": "CRISPR-Cas9 technology is used for:",
        "options": ["Gene editing", "Cloning", "PCR testing", "Protein synthesis"],
        "correct_option": 0,
        "explanation": "CRISPR-Cas9 is a revolutionary gene-editing tool that allows precise modification of DNA sequences. It won the Nobel Prize in Chemistry 2020.",
        "difficulty": "medium",
        "topic": "Biotechnology"
    },
    {
        "question_text": "Consider the following statements about GM crops in India:\n(1) Bt Cotton is the only GM crop commercially cultivated\n(2) GM Mustard (DMH-11) has been approved for environmental release\n(3) Bt Brinjal cultivation is banned in India\n\nWhich of the above statements are correct?",
        "options": ["1 only", "1 and 2 only", "1 and 3 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Bt Cotton is the only commercially grown GM crop, GM Mustard was approved in 2022, and Bt Brinjal has a moratorium since 2010.",
        "difficulty": "hard",
        "topic": "Biotechnology"
    },
    {
        "question_text": "The Covaxin vaccine developed by Bharat Biotech uses which platform?",
        "options": ["mRNA technology", "Viral vector", "Inactivated virus", "Protein subunit"],
        "correct_option": 2,
        "explanation": "Covaxin is an inactivated whole virus vaccine developed using traditional vaccine technology by Bharat Biotech in collaboration with ICMR.",
        "difficulty": "medium",
        "topic": "Biotechnology"
    },

    # ==================== IT & COMPUTERS ====================
    {
        "question_text": "Consider the following about Artificial Intelligence:\n(1) Machine Learning is a subset of AI\n(2) Deep Learning uses neural networks\n(3) ChatGPT is based on Large Language Models\n(4) AI was coined by John McCarthy\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. ML is a subset of AI, Deep Learning uses neural networks, ChatGPT is based on GPT-4 (LLM), and McCarthy coined 'AI' in 1956.",
        "difficulty": "medium",
        "topic": "IT & Computers"
    },
    {
        "question_text": "Blockchain technology is characterized by:",
        "options": ["Centralized database", "Decentralized and immutable ledger", "Only used for cryptocurrency", "Controlled by single authority"],
        "correct_option": 1,
        "explanation": "Blockchain is a decentralized, distributed, and immutable digital ledger technology used for cryptocurrencies, supply chain, voting, etc.",
        "difficulty": "medium",
        "topic": "IT & Computers"
    },
    {
        "question_text": "The National Quantum Mission launched in 2023 aims to develop:\n(1) Quantum computers\n(2) Quantum communication\n(3) Quantum sensing\n\nSelect the correct answer:",
        "options": ["1 only", "1 and 2 only", "2 and 3 only", "All of the above"],
        "correct_option": 3,
        "explanation": "The National Quantum Mission (Rs. 6000 crore) covers quantum computing, communication, sensing and metrology, and materials and devices.",
        "difficulty": "medium",
        "topic": "IT & Computers"
    },
    {
        "question_text": "5G technology operates in which frequency bands?",
        "options": ["Only low band (below 1 GHz)", "Only mid band (1-6 GHz)", "Only high band (above 24 GHz)", "All three bands"],
        "correct_option": 3,
        "explanation": "5G operates in three bands: Low band (<1 GHz) for coverage, Mid band (1-6 GHz) for balance, and High band/mmWave (>24 GHz) for speed.",
        "difficulty": "medium",
        "topic": "IT & Computers"
    },

    # ==================== HEALTH & MEDICINE ====================
    {
        "question_text": "Consider the following diseases and their causative agents:\n(1) Malaria - Plasmodium\n(2) Dengue - Virus\n(3) Tuberculosis - Bacteria\n(4) COVID-19 - Virus\n\nWhich of the above pairs are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All are correctly matched. Malaria (Plasmodium protozoa), Dengue (Flavivirus), TB (Mycobacterium tuberculosis), COVID-19 (SARS-CoV-2 virus).",
        "difficulty": "easy",
        "topic": "Health & Medicine"
    },
    {
        "question_text": "The R21/Matrix-M malaria vaccine approved by WHO in 2023 was developed by:",
        "options": ["Pfizer", "Oxford University and Serum Institute", "Bharat Biotech", "Moderna"],
        "correct_option": 1,
        "explanation": "The R21/Matrix-M vaccine was developed by Oxford University and manufactured by Serum Institute of India. It's the second WHO-approved malaria vaccine.",
        "difficulty": "hard",
        "topic": "Health & Medicine"
    },
    {
        "question_text": "Which vitamin deficiency causes Night Blindness?",
        "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
        "correct_option": 0,
        "explanation": "Vitamin A (Retinol) deficiency causes night blindness (nyctalopia) as it is essential for the production of rhodopsin in rod cells.",
        "difficulty": "easy",
        "topic": "Health & Medicine"
    },

    # ==================== IMPORTANT DAYS & THEMES ====================
    {
        "question_text": "World Environment Day is celebrated on:",
        "options": ["June 5", "April 22", "March 21", "September 16"],
        "correct_option": 0,
        "explanation": "World Environment Day is celebrated on June 5 every year. It was established by the UN in 1972 at the Stockholm Conference.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "National Science Day is celebrated on February 28 to commemorate:",
        "options": ["Birth of C.V. Raman", "Discovery of Raman Effect", "Foundation of CSIR", "Launch of Aryabhata satellite"],
        "correct_option": 1,
        "explanation": "National Science Day (Feb 28) commemorates the discovery of the Raman Effect by Sir C.V. Raman in 1928, for which he won the Nobel Prize in 1930.",
        "difficulty": "medium",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "The theme of World Environment Day 2024 was:",
        "options": ["Beat Plastic Pollution", "Land Restoration, Desertification and Drought Resilience", "Only One Earth", "Ecosystem Restoration"],
        "correct_option": 1,
        "explanation": "World Environment Day 2024 theme was 'Land Restoration, Desertification and Drought Resilience' with the slogan 'Our land. Our future.'",
        "difficulty": "medium",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "World Health Day is celebrated on:",
        "options": ["April 7", "May 31", "December 1", "October 10"],
        "correct_option": 0,
        "explanation": "World Health Day is celebrated on April 7, marking the founding of WHO in 1948. It focuses on specific health themes each year.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "National Technology Day (May 11) commemorates:",
        "options": ["Launch of first satellite", "Pokhran nuclear tests 1998", "First computer in India", "ISRO foundation"],
        "correct_option": 1,
        "explanation": "National Technology Day (May 11) marks the Pokhran-II nuclear tests of 1998, when India conducted five nuclear tests (Operation Shakti).",
        "difficulty": "medium",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "World Water Day is observed on:",
        "options": ["March 22", "March 21", "June 5", "April 22"],
        "correct_option": 0,
        "explanation": "World Water Day is observed on March 22 since 1993, focusing on the importance of freshwater. The 2024 theme was 'Water for Peace'.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "Earth Day is celebrated on:",
        "options": ["March 21", "April 22", "June 5", "September 16"],
        "correct_option": 1,
        "explanation": "Earth Day is celebrated on April 22 since 1970. It focuses on environmental protection and awareness about climate change.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "World Ozone Day is observed on September 16 to commemorate:",
        "options": ["Discovery of ozone layer", "Signing of Montreal Protocol", "Closure of ozone hole", "Formation of UNEP"],
        "correct_option": 1,
        "explanation": "World Ozone Day (September 16) commemorates the signing of the Montreal Protocol in 1987, which aimed to phase out ozone-depleting substances.",
        "difficulty": "medium",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "International Day of Yoga is celebrated on:",
        "options": ["June 21", "August 15", "October 2", "January 12"],
        "correct_option": 0,
        "explanation": "International Day of Yoga is celebrated on June 21 since 2015, following a proposal by PM Modi at the UN General Assembly in 2014.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "World AIDS Day is observed on:",
        "options": ["October 1", "November 1", "December 1", "January 1"],
        "correct_option": 2,
        "explanation": "World AIDS Day is observed on December 1 since 1988, dedicated to raising awareness about HIV/AIDS and remembering those who have died from it.",
        "difficulty": "easy",
        "topic": "Important Days & Themes"
    },
    {
        "question_text": "The theme of World Health Day 2024 was:",
        "options": ["Universal Health Coverage", "My health, my right", "Build a fairer, healthier world", "Health for All"],
        "correct_option": 1,
        "explanation": "World Health Day 2024 theme was 'My health, my right' focusing on the right of everyone to access quality health services.",
        "difficulty": "medium",
        "topic": "Important Days & Themes"
    },

    # ==================== IMPORTANT BOOKS ====================
    {
        "question_text": "The book 'The Origin of Species' was written by:",
        "options": ["Charles Darwin", "Gregor Mendel", "Alfred Wallace", "Jean-Baptiste Lamarck"],
        "correct_option": 0,
        "explanation": "'On the Origin of Species' (1859) by Charles Darwin introduced the theory of evolution by natural selection.",
        "difficulty": "easy",
        "topic": "Important Books"
    },
    {
        "question_text": "The book 'A Brief History of Time' was written by:",
        "options": ["Albert Einstein", "Stephen Hawking", "Richard Feynman", "Carl Sagan"],
        "correct_option": 1,
        "explanation": "'A Brief History of Time' (1988) by Stephen Hawking explains complex cosmological concepts like black holes and the Big Bang for general readers.",
        "difficulty": "easy",
        "topic": "Important Books"
    },
    {
        "question_text": "'Silent Spring', the book that sparked the environmental movement, was written by:",
        "options": ["Rachel Carson", "Al Gore", "David Attenborough", "Jane Goodall"],
        "correct_option": 0,
        "explanation": "'Silent Spring' (1962) by Rachel Carson documented the environmental damage caused by pesticides, especially DDT, and sparked the modern environmental movement.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "The book 'Principia Mathematica' was written by:",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Johannes Kepler"],
        "correct_option": 1,
        "explanation": "'Philosophiæ Naturalis Principia Mathematica' (1687) by Isaac Newton laid the foundations for classical mechanics including laws of motion and gravitation.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "'The Selfish Gene', which introduced the concept of memes, was written by:",
        "options": ["Charles Darwin", "Richard Dawkins", "E.O. Wilson", "Stephen Jay Gould"],
        "correct_option": 1,
        "explanation": "'The Selfish Gene' (1976) by Richard Dawkins introduced the gene-centered view of evolution and coined the term 'meme'.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "The book 'Cosmos' was written by:",
        "options": ["Stephen Hawking", "Carl Sagan", "Neil deGrasse Tyson", "Richard Feynman"],
        "correct_option": 1,
        "explanation": "'Cosmos' (1980) by Carl Sagan accompanied the famous TV series and covered various scientific topics from the origin of life to space exploration.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "Who wrote the book 'The Double Helix', describing the discovery of DNA structure?",
        "options": ["Francis Crick", "James Watson", "Rosalind Franklin", "Maurice Wilkins"],
        "correct_option": 1,
        "explanation": "'The Double Helix' (1968) by James Watson is a personal account of the discovery of the DNA structure, for which Watson, Crick and Wilkins won the Nobel Prize.",
        "difficulty": "hard",
        "topic": "Important Books"
    },
    {
        "question_text": "The book 'Sapiens: A Brief History of Humankind' was written by:",
        "options": ["Jared Diamond", "Yuval Noah Harari", "Steven Pinker", "Matt Ridley"],
        "correct_option": 1,
        "explanation": "'Sapiens' (2011) by Yuval Noah Harari explores the history of humankind from the Stone Age to the present, covering cognitive, agricultural, and scientific revolutions.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "'An Inconvenient Truth' about climate change was written by:",
        "options": ["Barack Obama", "Al Gore", "Bill Gates", "Elon Musk"],
        "correct_option": 1,
        "explanation": "'An Inconvenient Truth' (2006) by Al Gore discusses climate change and global warming. It was also adapted into an Oscar-winning documentary.",
        "difficulty": "medium",
        "topic": "Important Books"
    },
    {
        "question_text": "The book 'Ignited Minds' was written by:",
        "options": ["Vikram Sarabhai", "A.P.J. Abdul Kalam", "Homi Bhabha", "C.V. Raman"],
        "correct_option": 1,
        "explanation": "'Ignited Minds: Unleashing the Power Within India' (2002) by A.P.J. Abdul Kalam discusses India's potential and ways to transform it into a developed nation.",
        "difficulty": "easy",
        "topic": "Important Books"
    },

    # ==================== MISCELLANEOUS ====================
    {
        "question_text": "Which gas is known as 'Laughing Gas'?",
        "options": ["Carbon dioxide", "Nitrous oxide", "Nitrogen", "Oxygen"],
        "correct_option": 1,
        "explanation": "Nitrous oxide (N2O) is called 'Laughing Gas' due to its euphoric effects. It is used as an anesthetic and also contributes to global warming.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Diamond and Graphite are allotropes of:",
        "options": ["Silicon", "Carbon", "Nitrogen", "Phosphorus"],
        "correct_option": 1,
        "explanation": "Diamond and graphite are allotropes of carbon. Diamond has tetrahedral structure (hardest), while graphite has layered structure (soft, conductive).",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The pH value of human blood is approximately:",
        "options": ["5.4 - 6.4", "6.4 - 7.0", "7.35 - 7.45", "8.0 - 8.5"],
        "correct_option": 2,
        "explanation": "Normal human blood pH is maintained between 7.35-7.45 (slightly alkaline). Deviation from this range can be life-threatening.",
        "difficulty": "medium",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The ozone layer is present in which layer of the atmosphere?",
        "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
        "correct_option": 1,
        "explanation": "The ozone layer is in the stratosphere (15-35 km altitude). It absorbs 97-99% of the Sun's harmful UV radiation.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["Mars", "Venus", "Mercury", "Jupiter"],
        "correct_option": 1,
        "explanation": "Venus is called 'Morning Star' or 'Evening Star' because it appears in the eastern sky before sunrise and in the western sky after sunset.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The SI unit of electric current is:",
        "options": ["Volt", "Ohm", "Ampere", "Watt"],
        "correct_option": 2,
        "explanation": "Ampere (A) is the SI unit of electric current. Volt is for potential difference, Ohm for resistance, and Watt for power.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Which metal is liquid at room temperature?",
        "options": ["Sodium", "Mercury", "Lead", "Zinc"],
        "correct_option": 1,
        "explanation": "Mercury (Hg) is the only metal that is liquid at room temperature (melting point -39°C). Gallium melts just above room temperature (30°C).",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The chemical formula of common salt is:",
        "options": ["NaCl", "KCl", "CaCl2", "MgCl2"],
        "correct_option": 0,
        "explanation": "Common salt is Sodium Chloride (NaCl). It is an ionic compound formed by sodium and chlorine.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Which is the largest organ in the human body?",
        "options": ["Liver", "Brain", "Skin", "Heart"],
        "correct_option": 2,
        "explanation": "Skin is the largest organ, covering about 20 square feet and weighing about 3.6 kg in adults. Liver is the largest internal organ.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The speed of light in vacuum is approximately:",
        "options": ["3 × 10^6 m/s", "3 × 10^8 m/s", "3 × 10^10 m/s", "3 × 10^5 m/s"],
        "correct_option": 1,
        "explanation": "The speed of light in vacuum is approximately 3 × 10^8 m/s (299,792,458 m/s exactly). It is denoted by 'c' and is the universal speed limit.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The process of conversion of solid directly to gas is called:",
        "options": ["Evaporation", "Condensation", "Sublimation", "Deposition"],
        "correct_option": 2,
        "explanation": "Sublimation is the process where a solid converts directly to gas without passing through the liquid phase. Example: dry ice (solid CO2).",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Which element has the highest electrical conductivity?",
        "options": ["Copper", "Gold", "Silver", "Aluminum"],
        "correct_option": 2,
        "explanation": "Silver has the highest electrical conductivity among all elements, followed by copper, gold, and aluminum.",
        "difficulty": "medium",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The number of bones in an adult human body is:",
        "options": ["206", "300", "180", "256"],
        "correct_option": 0,
        "explanation": "An adult human body has 206 bones. Babies are born with about 270-300 bones, many of which fuse together as they grow.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "Which vitamin is synthesized by the human body when exposed to sunlight?",
        "options": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"],
        "correct_option": 3,
        "explanation": "Vitamin D is synthesized in the skin when exposed to UVB rays from sunlight. It is essential for calcium absorption and bone health.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    },
    {
        "question_text": "The hardest natural substance on Earth is:",
        "options": ["Quartz", "Topaz", "Diamond", "Corundum"],
        "correct_option": 2,
        "explanation": "Diamond is the hardest natural substance, rating 10 on the Mohs hardness scale. It is made of carbon atoms in a tetrahedral crystal structure.",
        "difficulty": "easy",
        "topic": "Miscellaneous"
    }
]
