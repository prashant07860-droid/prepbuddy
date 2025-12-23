"""
OPSC Questions Database - Agriculture
High-quality, OPSC-level questions based on actual exam patterns
Categories: Agronomy, Soil Science, Horticulture, Nematology, Plant Pathology,
Entomology, Plant Breeding & Genetics, Plant Physiology, Agri Extension,
Agri Economics, Agri Statistics, General Agriculture, Agroforestry
"""

AGRICULTURE_QUESTIONS = [
    # ==================== AGRONOMY ====================
    {
        "question_text": "Consider the following statements about crop rotation:\n(1) It helps in maintaining soil fertility\n(2) It breaks the cycle of pests and diseases\n(3) Legumes in rotation fix atmospheric nitrogen\n(4) It always increases crop yield\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Crop rotation doesn't always increase yield - it depends on the crops chosen and soil conditions.",
        "difficulty": "medium",
        "topic": "Agronomy"
    },
    {
        "question_text": "The optimum plant population for paddy cultivation under transplanted conditions is:",
        "options": ["20-25 hills/m²", "25-30 hills/m²", "30-35 hills/m²", "35-40 hills/m²"],
        "correct_option": 1,
        "explanation": "For transplanted paddy, the optimum plant population is 25-30 hills/m² with a spacing of 20×15 cm or 20×10 cm.",
        "difficulty": "medium",
        "topic": "Agronomy"
    },
    {
        "question_text": "Which of the following is a C4 plant?",
        "options": ["Rice", "Wheat", "Maize", "Soybean"],
        "correct_option": 2,
        "explanation": "Maize is a C4 plant with Kranz anatomy. Rice, wheat, and soybean are C3 plants. C4 plants are more efficient in photosynthesis under high temperature and light.",
        "difficulty": "medium",
        "topic": "Agronomy"
    },
    {
        "question_text": "The concept of 'Law of Minimum' was given by:",
        "options": ["Liebig", "Mitscherlich", "Blackman", "Sprengel"],
        "correct_option": 0,
        "explanation": "Liebig's Law of Minimum states that plant growth is determined by the scarcest 'limiting' factor, not by the total amount of resources available.",
        "difficulty": "medium",
        "topic": "Agronomy"
    },
    {
        "question_text": "Which cropping system involves growing two or more crops simultaneously on the same field?",
        "options": ["Relay cropping", "Sequential cropping", "Intercropping", "Ratoon cropping"],
        "correct_option": 2,
        "explanation": "Intercropping involves growing two or more crops simultaneously in the same field. It increases land use efficiency and reduces risk.",
        "difficulty": "easy",
        "topic": "Agronomy"
    },
    {
        "question_text": "The critical stage of water requirement in wheat is:",
        "options": ["Tillering", "Crown Root Initiation (CRI)", "Flowering", "Both B and C"],
        "correct_option": 3,
        "explanation": "Crown Root Initiation (CRI) and flowering are critical stages for irrigation in wheat. Water stress at these stages significantly reduces yield.",
        "difficulty": "medium",
        "topic": "Agronomy"
    },

    # ==================== SOIL SCIENCE ====================
    {
        "question_text": "Consider the following about soil pH:\n(1) Acidic soil has pH below 7\n(2) Alkaline soil has pH above 7\n(3) Most crops grow best at pH 6.0-7.0\n(4) Lime is used to correct alkaline soils\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Lime is used to correct ACIDIC soils (not alkaline). Gypsum is used for alkaline soils.",
        "difficulty": "medium",
        "topic": "Soil Science"
    },
    {
        "question_text": "Which of the following is a primary macronutrient for plants?",
        "options": ["Calcium", "Magnesium", "Nitrogen", "Iron"],
        "correct_option": 2,
        "explanation": "Nitrogen is a primary macronutrient (N, P, K). Calcium and Magnesium are secondary macronutrients. Iron is a micronutrient.",
        "difficulty": "easy",
        "topic": "Soil Science"
    },
    {
        "question_text": "The ideal soil for most crops should have approximately what percentage of organic matter?",
        "options": ["1-2%", "2-5%", "5-10%", "10-15%"],
        "correct_option": 1,
        "explanation": "Ideal agricultural soil should contain 2-5% organic matter. It improves soil structure, water-holding capacity, and nutrient availability.",
        "difficulty": "medium",
        "topic": "Soil Science"
    },
    {
        "question_text": "Cation Exchange Capacity (CEC) is highest in:",
        "options": ["Sandy soil", "Silt soil", "Clay soil", "Loamy soil"],
        "correct_option": 2,
        "explanation": "Clay soils have the highest CEC due to their large surface area and negative charges on clay particles. Sandy soils have the lowest CEC.",
        "difficulty": "medium",
        "topic": "Soil Science"
    },
    {
        "question_text": "Which soil order is most suitable for paddy cultivation?",
        "options": ["Vertisols", "Alfisols", "Entisols", "Inceptisols"],
        "correct_option": 0,
        "explanation": "Vertisols (black cotton soils) are ideal for paddy due to high clay content and water-holding capacity. They shrink and swell with moisture changes.",
        "difficulty": "hard",
        "topic": "Soil Science"
    },
    {
        "question_text": "Zinc deficiency in rice is known as:",
        "options": ["Whiptail", "Khaira disease", "White bud", "Little leaf"],
        "correct_option": 1,
        "explanation": "Khaira disease in rice is caused by zinc deficiency. Symptoms include dusty brown spots on leaves. It's common in calcareous and waterlogged soils.",
        "difficulty": "medium",
        "topic": "Soil Science"
    },

    # ==================== HORTICULTURE ====================
    {
        "question_text": "Which of the following fruits is climacteric?",
        "options": ["Citrus", "Grapes", "Mango", "Litchi"],
        "correct_option": 2,
        "explanation": "Mango is a climacteric fruit that shows a rise in respiration rate during ripening. Citrus, grapes, and litchi are non-climacteric fruits.",
        "difficulty": "medium",
        "topic": "Horticulture"
    },
    {
        "question_text": "The technique of joining two plant parts (scion and rootstock) to grow as one plant is called:",
        "options": ["Budding", "Layering", "Grafting", "Cutting"],
        "correct_option": 2,
        "explanation": "Grafting involves joining a scion (upper part) to a rootstock (lower part). It's used to propagate improved varieties and obtain disease-resistant plants.",
        "difficulty": "easy",
        "topic": "Horticulture"
    },
    {
        "question_text": "Consider the following about vegetable classification:\n(1) Tomato is a fruit vegetable\n(2) Carrot is a root vegetable\n(3) Cauliflower is a flower vegetable\n(4) Spinach is a leaf vegetable\n\nWhich of the above are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All are correctly classified. Tomato (fruit), carrot (root), cauliflower (flower), and spinach (leaf) represent different edible parts.",
        "difficulty": "easy",
        "topic": "Horticulture"
    },
    {
        "question_text": "Which plant growth regulator is used to induce flowering in pineapple?",
        "options": ["Auxin", "Gibberellin", "Ethylene", "Cytokinin"],
        "correct_option": 2,
        "explanation": "Ethylene or ethephon (which releases ethylene) is used to induce uniform flowering in pineapple for synchronized harvesting.",
        "difficulty": "medium",
        "topic": "Horticulture"
    },
    {
        "question_text": "The national fruit of India is:",
        "options": ["Banana", "Mango", "Apple", "Guava"],
        "correct_option": 1,
        "explanation": "Mango (Mangifera indica) is the national fruit of India. India is the largest producer of mangoes in the world.",
        "difficulty": "easy",
        "topic": "Horticulture"
    },
    {
        "question_text": "Parthenocarpy refers to:",
        "options": ["Fruit development without seeds", "Seed development without fertilization", "Flower development without pollination", "Multiple fruit formation"],
        "correct_option": 0,
        "explanation": "Parthenocarpy is the development of fruit without fertilization, resulting in seedless fruits. Examples include seedless grapes and bananas.",
        "difficulty": "medium",
        "topic": "Horticulture"
    },

    # ==================== NEMATOLOGY ====================
    {
        "question_text": "Root-knot nematode belongs to the genus:",
        "options": ["Heterodera", "Meloidogyne", "Pratylenchus", "Radopholus"],
        "correct_option": 1,
        "explanation": "Root-knot nematodes belong to the genus Meloidogyne. They cause characteristic galls or knots on plant roots.",
        "difficulty": "medium",
        "topic": "Nematology"
    },
    {
        "question_text": "Which of the following is a symptom of nematode infestation in plants?",
        "options": ["Gall formation on roots", "Leaf spots", "Powdery growth on leaves", "Vascular discoloration"],
        "correct_option": 0,
        "explanation": "Gall formation on roots is a characteristic symptom of root-knot nematode infestation. Other symptoms include stunting and yellowing.",
        "difficulty": "easy",
        "topic": "Nematology"
    },
    {
        "question_text": "Cyst nematode affecting potato belongs to the genus:",
        "options": ["Meloidogyne", "Globodera", "Heterodera", "Pratylenchus"],
        "correct_option": 1,
        "explanation": "Potato cyst nematode belongs to Globodera (G. rostochiensis and G. pallida). The female body transforms into a cyst containing eggs.",
        "difficulty": "hard",
        "topic": "Nematology"
    },
    {
        "question_text": "Which crop rotation helps in reducing nematode population?",
        "options": ["Rice-wheat", "Maize-sorghum", "Mustard-paddy", "Groundnut-groundnut"],
        "correct_option": 2,
        "explanation": "Including non-host crops like paddy (flooded conditions) and mustard (releases nematicidal compounds) helps reduce nematode population.",
        "difficulty": "medium",
        "topic": "Nematology"
    },
    {
        "question_text": "The economic threshold level concept in nematology was given by:",
        "options": ["Seinhorst", "Cobb", "Chitwood", "Thorne"],
        "correct_option": 0,
        "explanation": "Seinhorst (1965) developed the concept of relating nematode population density to crop yield loss and economic threshold levels.",
        "difficulty": "hard",
        "topic": "Nematology"
    },

    # ==================== PLANT PATHOLOGY ====================
    {
        "question_text": "Late blight of potato is caused by:",
        "options": ["Alternaria solani", "Phytophthora infestans", "Fusarium oxysporum", "Rhizoctonia solani"],
        "correct_option": 1,
        "explanation": "Late blight of potato is caused by Phytophthora infestans. It caused the Irish Potato Famine (1845-49). Early blight is caused by Alternaria solani.",
        "difficulty": "medium",
        "topic": "Plant Pathology"
    },
    {
        "question_text": "Consider the following plant diseases:\n(1) Rust - Fungal disease\n(2) Citrus canker - Bacterial disease\n(3) Tobacco mosaic - Viral disease\n(4) Bunchy top of banana - Viral disease\n\nWhich of the above pairs are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All are correctly matched. Rust (Puccinia sp.), Citrus canker (Xanthomonas citri), TMV (Tobacco mosaic virus), Bunchy top (Banana bunchy top virus).",
        "difficulty": "hard",
        "topic": "Plant Pathology"
    },
    {
        "question_text": "Koch's postulates are used to:",
        "options": ["Identify plant nutrients", "Prove disease causation by a pathogen", "Classify plant diseases", "Measure disease severity"],
        "correct_option": 1,
        "explanation": "Koch's postulates (1890) are four criteria to establish a causal relationship between a microorganism and a disease.",
        "difficulty": "medium",
        "topic": "Plant Pathology"
    },
    {
        "question_text": "Bordeaux mixture is a fungicide containing:",
        "options": ["Copper and lime", "Sulphur and lime", "Copper and sulphur", "Zinc and lime"],
        "correct_option": 0,
        "explanation": "Bordeaux mixture (developed in 1885) contains copper sulphate (CuSO4) and lime (CaO/Ca(OH)2). It's used against fungal diseases.",
        "difficulty": "easy",
        "topic": "Plant Pathology"
    },
    {
        "question_text": "The causal organism of blast disease of rice is:",
        "options": ["Xanthomonas oryzae", "Pyricularia oryzae", "Helminthosporium oryzae", "Ustilaginoidea virens"],
        "correct_option": 1,
        "explanation": "Rice blast is caused by Pyricularia oryzae (also called Magnaporthe oryzae). It affects leaves, nodes, and panicles.",
        "difficulty": "medium",
        "topic": "Plant Pathology"
    },
    {
        "question_text": "Systemic Acquired Resistance (SAR) in plants is associated with:",
        "options": ["Gibberellic acid", "Salicylic acid", "Abscisic acid", "Jasmonic acid"],
        "correct_option": 1,
        "explanation": "Salicylic acid plays a key role in SAR, providing broad-spectrum resistance against pathogens. It triggers defense gene expression.",
        "difficulty": "hard",
        "topic": "Plant Pathology"
    },

    # ==================== ENTOMOLOGY ====================
    {
        "question_text": "Which of the following is a sucking pest?",
        "options": ["Stem borer", "Armyworm", "Aphid", "Leaf folder"],
        "correct_option": 2,
        "explanation": "Aphids have piercing-sucking mouthparts. Stem borer, armyworm, and leaf folder are chewing/biting pests with mandibles.",
        "difficulty": "easy",
        "topic": "Entomology"
    },
    {
        "question_text": "Integrated Pest Management (IPM) includes:\n(1) Cultural control\n(2) Biological control\n(3) Chemical control\n(4) Genetic control\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "IPM integrates all available pest control methods: cultural, biological, chemical, genetic, mechanical, and regulatory controls.",
        "difficulty": "medium",
        "topic": "Entomology"
    },
    {
        "question_text": "Trichogramma is used for biological control of:",
        "options": ["Aphids", "Lepidopteran pests", "Nematodes", "Fungal diseases"],
        "correct_option": 1,
        "explanation": "Trichogramma is an egg parasitoid used against lepidopteran pests like bollworms, stem borers, and fruit borers.",
        "difficulty": "medium",
        "topic": "Entomology"
    },
    {
        "question_text": "The most serious pest of stored grains is:",
        "options": ["Rice weevil", "Khapra beetle", "Lesser grain borer", "Pulse beetle"],
        "correct_option": 1,
        "explanation": "Khapra beetle (Trogoderma granarium) is the most destructive stored grain pest. It can survive adverse conditions and is difficult to control.",
        "difficulty": "medium",
        "topic": "Entomology"
    },
    {
        "question_text": "Economic Injury Level (EIL) in pest management refers to:",
        "options": ["Maximum pest population", "Pest density at which control should start", "Pest density causing economic damage equal to control cost", "Minimum pest population"],
        "correct_option": 2,
        "explanation": "EIL is the lowest pest population density that causes economic damage equal to the cost of control measures. ETL is slightly below EIL.",
        "difficulty": "hard",
        "topic": "Entomology"
    },
    {
        "question_text": "Which insecticide acts on the nervous system by inhibiting acetylcholinesterase?",
        "options": ["Pyrethroids", "Organophosphates", "Neonicotinoids", "Growth regulators"],
        "correct_option": 1,
        "explanation": "Organophosphates (like malathion, chlorpyrifos) inhibit acetylcholinesterase enzyme, causing nerve impulse accumulation and death.",
        "difficulty": "hard",
        "topic": "Entomology"
    },

    # ==================== PLANT BREEDING & GENETICS ====================
    {
        "question_text": "Mendel's Law of Segregation states that:",
        "options": ["Genes are inherited independently", "Alleles separate during gamete formation", "Dominant traits mask recessive traits", "Chromosomes pair during meiosis"],
        "correct_option": 1,
        "explanation": "Law of Segregation states that two alleles for each trait separate during gamete formation and randomly unite at fertilization.",
        "difficulty": "medium",
        "topic": "Plant Breeding & Genetics"
    },
    {
        "question_text": "Heterosis or hybrid vigor is maximum in:",
        "options": ["F1 generation", "F2 generation", "F3 generation", "F4 generation"],
        "correct_option": 0,
        "explanation": "Heterosis is maximum in F1 generation and declines by 50% with each subsequent selfed generation due to segregation.",
        "difficulty": "medium",
        "topic": "Plant Breeding & Genetics"
    },
    {
        "question_text": "Which breeding method is most suitable for self-pollinated crops?",
        "options": ["Mass selection", "Pure line selection", "Recurrent selection", "Synthetic variety"],
        "correct_option": 1,
        "explanation": "Pure line selection is most suitable for self-pollinated crops like wheat, rice, and pulses. It involves selecting superior homozygous lines.",
        "difficulty": "medium",
        "topic": "Plant Breeding & Genetics"
    },
    {
        "question_text": "Green Revolution in India was primarily due to:",
        "options": ["Improved irrigation", "High Yielding Varieties (HYVs)", "Chemical fertilizers", "All of the above"],
        "correct_option": 3,
        "explanation": "Green Revolution involved HYVs (dwarf wheat and rice), irrigation expansion, chemical fertilizers, and pesticides working together.",
        "difficulty": "easy",
        "topic": "Plant Breeding & Genetics"
    },
    {
        "question_text": "The technique of transferring genes from one organism to another is called:",
        "options": ["Hybridization", "Mutation breeding", "Genetic engineering", "Polyploidy"],
        "correct_option": 2,
        "explanation": "Genetic engineering involves direct manipulation and transfer of genes between organisms using recombinant DNA technology.",
        "difficulty": "easy",
        "topic": "Plant Breeding & Genetics"
    },
    {
        "question_text": "Backcross breeding is used to:",
        "options": ["Create new varieties", "Transfer a single gene to a good variety", "Increase genetic variation", "Develop hybrids"],
        "correct_option": 1,
        "explanation": "Backcross breeding transfers one or few desirable genes from a donor parent to an otherwise good recurrent parent variety.",
        "difficulty": "medium",
        "topic": "Plant Breeding & Genetics"
    },

    # ==================== PLANT PHYSIOLOGY ====================
    {
        "question_text": "The process by which green plants make food using sunlight is called:",
        "options": ["Respiration", "Transpiration", "Photosynthesis", "Fermentation"],
        "correct_option": 2,
        "explanation": "Photosynthesis is the process by which plants use sunlight, CO2, and water to produce glucose and oxygen in chloroplasts.",
        "difficulty": "easy",
        "topic": "Plant Physiology"
    },
    {
        "question_text": "Which plant hormone is known as the 'stress hormone'?",
        "options": ["Auxin", "Gibberellin", "Abscisic acid", "Cytokinin"],
        "correct_option": 2,
        "explanation": "Abscisic acid (ABA) is called the stress hormone. It increases during water stress and promotes stomatal closure and dormancy.",
        "difficulty": "medium",
        "topic": "Plant Physiology"
    },
    {
        "question_text": "The phenomenon of flowering in response to day length is called:",
        "options": ["Vernalization", "Photoperiodism", "Thermoperiodicty", "Phototropism"],
        "correct_option": 1,
        "explanation": "Photoperiodism is the response of plants to the relative length of day and night. Plants are classified as short-day, long-day, or day-neutral.",
        "difficulty": "medium",
        "topic": "Plant Physiology"
    },
    {
        "question_text": "Transpiration mainly occurs through:",
        "options": ["Roots", "Stem", "Stomata on leaves", "Flowers"],
        "correct_option": 2,
        "explanation": "About 90-95% of transpiration occurs through stomata on leaves (stomatal transpiration). The rest occurs through cuticle and lenticels.",
        "difficulty": "easy",
        "topic": "Plant Physiology"
    },
    {
        "question_text": "Which element is essential for chlorophyll synthesis?",
        "options": ["Calcium", "Magnesium", "Potassium", "Phosphorus"],
        "correct_option": 1,
        "explanation": "Magnesium is the central atom in the chlorophyll molecule. Its deficiency causes interveinal chlorosis in older leaves.",
        "difficulty": "medium",
        "topic": "Plant Physiology"
    },
    {
        "question_text": "The movement of water from soil to plant roots is by:",
        "options": ["Active transport", "Osmosis", "Diffusion", "Mass flow"],
        "correct_option": 1,
        "explanation": "Water moves from soil to root cells by osmosis - movement from higher water potential (soil) to lower water potential (root cells).",
        "difficulty": "medium",
        "topic": "Plant Physiology"
    },

    # ==================== AGRI EXTENSION ====================
    {
        "question_text": "The concept of 'Extension Education' was first used in:",
        "options": ["USA", "UK", "India", "Japan"],
        "correct_option": 1,
        "explanation": "The term 'Extension' originated from England in 1866 when Cambridge and Oxford universities extended their educational activities beyond campus.",
        "difficulty": "medium",
        "topic": "Agri Extension"
    },
    {
        "question_text": "Krishi Vigyan Kendra (KVK) functions under:",
        "options": ["State Agriculture Department", "ICAR", "Ministry of Agriculture", "NABARD"],
        "correct_option": 1,
        "explanation": "KVKs are district-level farm science centers established by ICAR for technology assessment, refinement, and demonstration.",
        "difficulty": "easy",
        "topic": "Agri Extension"
    },
    {
        "question_text": "The Training and Visit (T&V) system of extension was introduced in India in:",
        "options": ["1974", "1979", "1984", "1989"],
        "correct_option": 0,
        "explanation": "The T&V system was introduced in India in 1974 with World Bank support. It emphasized regular training and systematic village visits.",
        "difficulty": "medium",
        "topic": "Agri Extension"
    },
    {
        "question_text": "ATMA (Agricultural Technology Management Agency) operates at:",
        "options": ["National level", "State level", "District level", "Block level"],
        "correct_option": 2,
        "explanation": "ATMA is a district-level autonomous organization for integrating extension activities and ensuring farmer participation in planning.",
        "difficulty": "medium",
        "topic": "Agri Extension"
    },
    {
        "question_text": "Which of the following is a mass contact method in extension?",
        "options": ["Farm visit", "Method demonstration", "Radio broadcast", "Group discussion"],
        "correct_option": 2,
        "explanation": "Radio broadcast is a mass contact method reaching large audiences. Farm visits are individual contact; method demonstrations and group discussions are group contact methods.",
        "difficulty": "easy",
        "topic": "Agri Extension"
    },
    {
        "question_text": "The first Krishi Vigyan Kendra was established in:",
        "options": ["Puducherry (1974)", "Ludhiana (1976)", "New Delhi (1970)", "Coimbatore (1980)"],
        "correct_option": 0,
        "explanation": "The first KVK was established at Puducherry in 1974 under Tamil Nadu Agricultural University. Currently, there are over 700 KVKs across India.",
        "difficulty": "hard",
        "topic": "Agri Extension"
    },

    # ==================== AGRI ECONOMICS ====================
    {
        "question_text": "Minimum Support Price (MSP) is announced by:",
        "options": ["RBI", "NABARD", "Government of India", "State Governments"],
        "correct_option": 2,
        "explanation": "MSP is announced by the Government of India based on recommendations of the Commission for Agricultural Costs and Prices (CACP).",
        "difficulty": "easy",
        "topic": "Agri Economics"
    },
    {
        "question_text": "Consider the following about agricultural marketing:\n(1) APMC Acts regulate agricultural markets\n(2) e-NAM is an online trading platform\n(3) FPOs help in collective marketing\n(4) Contract farming eliminates middlemen\n\nWhich of the above are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. APMC regulates mandis, e-NAM provides online trading, FPOs enable collective bargaining, and contract farming reduces middlemen.",
        "difficulty": "medium",
        "topic": "Agri Economics"
    },
    {
        "question_text": "Which scheme provides crop insurance to farmers?",
        "options": ["PM-KISAN", "PMFBY", "PM-KUSUM", "PMGSY"],
        "correct_option": 1,
        "explanation": "Pradhan Mantri Fasal Bima Yojana (PMFBY) launched in 2016 provides comprehensive crop insurance coverage against crop losses.",
        "difficulty": "easy",
        "topic": "Agri Economics"
    },
    {
        "question_text": "The share of agriculture in India's GDP (2022-23) is approximately:",
        "options": ["8-10%", "14-16%", "18-20%", "22-24%"],
        "correct_option": 2,
        "explanation": "Agriculture and allied sectors contribute about 18-20% to India's GDP while employing about 42% of the workforce.",
        "difficulty": "medium",
        "topic": "Agri Economics"
    },
    {
        "question_text": "Kisan Credit Card (KCC) scheme was launched in:",
        "options": ["1996", "1998", "2000", "2002"],
        "correct_option": 1,
        "explanation": "KCC was launched in 1998 to provide adequate and timely credit to farmers for agricultural operations. It includes crop loans and term loans.",
        "difficulty": "medium",
        "topic": "Agri Economics"
    },
    {
        "question_text": "Which organization provides refinance for agricultural credit?",
        "options": ["RBI", "NABARD", "SIDBI", "EXIM Bank"],
        "correct_option": 1,
        "explanation": "NABARD (National Bank for Agriculture and Rural Development) provides refinance support to banks and financial institutions for agricultural credit.",
        "difficulty": "easy",
        "topic": "Agri Economics"
    },

    # ==================== AGRI STATISTICS ====================
    {
        "question_text": "In statistics, the measure of central tendency that divides data into two equal halves is:",
        "options": ["Mean", "Median", "Mode", "Range"],
        "correct_option": 1,
        "explanation": "Median is the middle value that divides the data into two equal halves when arranged in order. 50% of values are above and 50% below it.",
        "difficulty": "easy",
        "topic": "Agri Statistics"
    },
    {
        "question_text": "Randomized Complete Block Design (RCBD) is used when:",
        "options": ["Experimental material is homogeneous", "There is one source of variation", "There are two sources of variation", "No replication is needed"],
        "correct_option": 1,
        "explanation": "RCBD is used when there is one known source of variation (blocks). It controls heterogeneity in one direction and is widely used in field experiments.",
        "difficulty": "medium",
        "topic": "Agri Statistics"
    },
    {
        "question_text": "The coefficient of variation (CV) is used to measure:",
        "options": ["Central tendency", "Relative variability", "Correlation", "Regression"],
        "correct_option": 1,
        "explanation": "CV = (Standard Deviation/Mean) × 100. It measures relative variability and allows comparison of variability between different datasets.",
        "difficulty": "medium",
        "topic": "Agri Statistics"
    },
    {
        "question_text": "A probability value (p-value) less than 0.05 indicates:",
        "options": ["Non-significant result", "Significant result at 5% level", "Highly significant result", "No relationship"],
        "correct_option": 1,
        "explanation": "p < 0.05 means the result is statistically significant at 5% level (95% confidence). p < 0.01 indicates highly significant results.",
        "difficulty": "medium",
        "topic": "Agri Statistics"
    },
    {
        "question_text": "In a 2x2 factorial experiment, the number of treatment combinations is:",
        "options": ["2", "4", "6", "8"],
        "correct_option": 1,
        "explanation": "In factorial experiments, treatment combinations = levels^factors. For 2x2 factorial: 2² = 4 treatment combinations.",
        "difficulty": "easy",
        "topic": "Agri Statistics"
    },
    {
        "question_text": "The correlation coefficient (r) ranges from:",
        "options": ["0 to 1", "-1 to 0", "-1 to +1", "0 to infinity"],
        "correct_option": 2,
        "explanation": "Correlation coefficient ranges from -1 (perfect negative) to +1 (perfect positive). r = 0 indicates no linear correlation.",
        "difficulty": "easy",
        "topic": "Agri Statistics"
    },

    # ==================== GENERAL AGRICULTURE ====================
    {
        "question_text": "Which state is the largest producer of rice in India?",
        "options": ["Punjab", "West Bengal", "Uttar Pradesh", "Andhra Pradesh"],
        "correct_option": 1,
        "explanation": "West Bengal is the largest rice-producing state in India, followed by Uttar Pradesh and Punjab.",
        "difficulty": "easy",
        "topic": "General Agriculture"
    },
    {
        "question_text": "The father of Green Revolution in India is:",
        "options": ["Norman Borlaug", "M.S. Swaminathan", "Verghese Kurien", "C. Subramaniam"],
        "correct_option": 1,
        "explanation": "M.S. Swaminathan is known as the father of Green Revolution in India. Norman Borlaug is the global father of Green Revolution.",
        "difficulty": "easy",
        "topic": "General Agriculture"
    },
    {
        "question_text": "Operation Flood is related to:",
        "options": ["Fisheries", "Dairy development", "Flood management", "Irrigation"],
        "correct_option": 1,
        "explanation": "Operation Flood (1970-1996), also called the White Revolution, was the world's largest dairy development program launched by Verghese Kurien.",
        "difficulty": "easy",
        "topic": "General Agriculture"
    },
    {
        "question_text": "Which crop is known as 'King of Cereals'?",
        "options": ["Rice", "Wheat", "Maize", "Barley"],
        "correct_option": 1,
        "explanation": "Wheat is known as the 'King of Cereals' due to its nutritive value and wide cultivation. Rice is the 'Queen of Cereals'.",
        "difficulty": "easy",
        "topic": "General Agriculture"
    },
    {
        "question_text": "The largest exporter of rice in the world is:",
        "options": ["China", "India", "Thailand", "Vietnam"],
        "correct_option": 1,
        "explanation": "India is the largest exporter of rice in the world, accounting for about 40% of global rice exports.",
        "difficulty": "medium",
        "topic": "General Agriculture"
    },
    {
        "question_text": "Rabi crops are sown in:",
        "options": ["June-July", "October-November", "February-March", "August-September"],
        "correct_option": 1,
        "explanation": "Rabi crops (wheat, gram, mustard) are sown in October-November and harvested in March-April. Kharif crops are sown in June-July.",
        "difficulty": "easy",
        "topic": "General Agriculture"
    },

    # ==================== AGROFORESTRY ====================
    {
        "question_text": "Agroforestry is the practice of:",
        "options": ["Growing only forest trees", "Integrating trees with crops and/or livestock", "Only silviculture", "Deforestation for agriculture"],
        "correct_option": 1,
        "explanation": "Agroforestry integrates trees with crops, livestock, or both to create sustainable and diversified farming systems.",
        "difficulty": "easy",
        "topic": "Agroforestry"
    },
    {
        "question_text": "Consider the following agroforestry systems:\n(1) Agri-silviculture - Trees + Crops\n(2) Silvopastoral - Trees + Animals\n(3) Agri-silvo-pastoral - Trees + Crops + Animals\n(4) Taungya - Trees + Annual crops initially\n\nWhich of the above are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All are correctly matched. Taungya involves growing annual crops between tree rows during early tree growth stages.",
        "difficulty": "hard",
        "topic": "Agroforestry"
    },
    {
        "question_text": "Which tree is commonly used in boundary planting in agroforestry?",
        "options": ["Teak", "Poplar", "Eucalyptus", "All of the above"],
        "correct_option": 3,
        "explanation": "Teak, poplar, eucalyptus, and other trees like casuarina and melia are commonly used in boundary planting for timber, fuelwood, and windbreak.",
        "difficulty": "easy",
        "topic": "Agroforestry"
    },
    {
        "question_text": "Sub-Mission on Agroforestry was launched in:",
        "options": ["2010", "2014", "2016", "2018"],
        "correct_option": 2,
        "explanation": "Sub-Mission on Agroforestry (SMAF) was launched in 2016 under the National Mission for Sustainable Agriculture to expand tree coverage.",
        "difficulty": "medium",
        "topic": "Agroforestry"
    },
    {
        "question_text": "Which nitrogen-fixing tree is commonly used in agroforestry?",
        "options": ["Eucalyptus", "Teak", "Gliricidia", "Poplar"],
        "correct_option": 2,
        "explanation": "Gliricidia sepium is a nitrogen-fixing tree used in agroforestry for green manure, fodder, and live fencing. It improves soil fertility.",
        "difficulty": "medium",
        "topic": "Agroforestry"
    },
    {
        "question_text": "The concept of 'Trees Outside Forests (TOF)' includes:\n(1) Trees in agroforestry\n(2) Urban trees\n(3) Trees along roads and canals\n(4) Trees in forests\n\nSelect the correct answer:",
        "options": ["1, 2 and 3 only", "1 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "TOF includes trees outside recorded forest areas - in farms, urban areas, along roads/canals, and homesteads. It excludes forest trees.",
        "difficulty": "medium",
        "topic": "Agroforestry"
    }
]
