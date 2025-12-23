"""
OPSC Questions Database - Geography
High-quality, OPSC-level questions based on actual exam patterns
Covers Physical, Indian, World Geography, Maps, Climate, Resources
"""

GEOGRAPHY_QUESTIONS = [
    # Physical Geography
    {
        "question_text": "Consider the following statements about Plate Tectonics:\n(1) The theory was proposed by Alfred Wegener\n(2) The lithosphere is divided into 7 major and several minor plates\n(3) The Pacific Plate is the largest tectonic plate\n(4) Convergent boundaries create new oceanic crust\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "2 and 3 only", "1, 2 and 3 only", "All of the above"],
        "correct_option": 2,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - divergent boundaries create new oceanic crust, while convergent boundaries destroy it through subduction.",
        "difficulty": "hard",
        "topic": "Physical Geography - Plate Tectonics"
    },
    {
        "question_text": "Match the following mountain ranges with their formation type:\n\nMountain Range : Formation Type\n(A) Himalayas : (1) Volcanic\n(B) Andes : (2) Fold Mountains\n(C) Rockies : (3) Block Mountains\n(D) Vosges : (4) Residual Mountains\n\nSelect the correct answer:",
        "options": ["A-2, B-2, C-2, D-3", "A-2, B-1, C-2, D-3", "A-1, B-2, C-2, D-4", "A-2, B-2, C-1, D-4"],
        "correct_option": 0,
        "explanation": "Himalayas, Andes, and Rockies are all fold mountains formed by tectonic collision. Vosges (France) are block mountains formed by faulting.",
        "difficulty": "hard",
        "topic": "Physical Geography - Mountain Formation"
    },
    {
        "question_text": "Which of the following is NOT a characteristic of the Deccan Plateau?",
        "options": ["It is composed of basaltic lava flows", "It slopes from west to east", "It is bordered by Western Ghats on the east", "Major rivers flow eastward into Bay of Bengal"],
        "correct_option": 2,
        "explanation": "The Deccan Plateau is bordered by Western Ghats on the WEST, not east. Eastern Ghats border it on the east. Other statements are correct.",
        "difficulty": "medium",
        "topic": "Indian Geography - Deccan Plateau"
    },
    {
        "question_text": "Consider the following rivers:\n(1) Godavari\n(2) Krishna\n(3) Mahanadi\n(4) Kaveri\n\nArrange them from North to South based on their delta location:",
        "options": ["1-3-2-4", "3-1-2-4", "1-2-3-4", "3-2-1-4"],
        "correct_option": 1,
        "explanation": "From North to South: Mahanadi (Odisha), Godavari (AP), Krishna (AP), Kaveri (TN). Their deltas follow this order along the eastern coast.",
        "difficulty": "medium",
        "topic": "Indian Geography - Rivers"
    },
    {
        "question_text": "The Brahmaputra River is known by different names in different regions. Match the following:\n\nRegion : Name\n(A) Tibet : (1) Dihang\n(B) Arunachal Pradesh : (2) Yarlung Tsangpo\n(C) Assam : (3) Jamuna\n(D) Bangladesh : (4) Brahmaputra\n\nSelect the correct answer:",
        "options": ["A-2, B-1, C-4, D-3", "A-1, B-2, C-4, D-3", "A-2, B-1, C-3, D-4", "A-1, B-2, C-3, D-4"],
        "correct_option": 0,
        "explanation": "In Tibet it's Yarlung Tsangpo, in Arunachal it's Dihang/Siang, in Assam it's Brahmaputra, and in Bangladesh it's Jamuna before joining Ganga.",
        "difficulty": "hard",
        "topic": "Indian Geography - Brahmaputra"
    },
    {
        "question_text": "Which of the following statements about the Indian Monsoon is/are correct?\n(1) Southwest monsoon is caused by the differential heating of land and sea\n(2) The monsoon trough is an area of low pressure over the Indo-Gangetic Plain\n(3) Western Disturbances bring winter rainfall to North India\n(4) October-November rainfall in Tamil Nadu is due to Northeast monsoon\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The Indian monsoon system involves differential heating, monsoon trough formation, western disturbances in winter, and retreating NE monsoon.",
        "difficulty": "hard",
        "topic": "Indian Geography - Monsoon"
    },
    {
        "question_text": "The phenomenon of 'October Heat' in India is caused by:",
        "options": ["High humidity and temperature during retreating monsoon", "El Niño effect", "Western disturbances", "Tropical cyclones"],
        "correct_option": 0,
        "explanation": "October Heat refers to the oppressive weather conditions caused by high temperature and humidity during the retreating monsoon (October-November).",
        "difficulty": "medium",
        "topic": "Indian Geography - Climate"
    },
    {
        "question_text": "Consider the following soil types:\n(1) Black soil - Cotton cultivation\n(2) Laterite soil - Tea and Coffee\n(3) Alluvial soil - Rice and Wheat\n(4) Red soil - Groundnut and Millets\n\nWhich of the above pairs are correctly matched?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "1, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. Black soil is ideal for cotton, laterite for plantation crops, alluvial for cereals, and red soil for groundnut and millets.",
        "difficulty": "medium",
        "topic": "Indian Geography - Soils"
    },
    {
        "question_text": "Which of the following National Parks is NOT correctly matched with its state?",
        "options": ["Kaziranga - Assam", "Ranthambore - Rajasthan", "Periyar - Tamil Nadu", "Sundarbans - West Bengal"],
        "correct_option": 2,
        "explanation": "Periyar National Park is in Kerala, not Tamil Nadu. Other matches are correct.",
        "difficulty": "easy",
        "topic": "Indian Geography - National Parks"
    },
    {
        "question_text": "Consider the following passes:\n(1) Khyber Pass - Afghanistan-Pakistan\n(2) Bolan Pass - Pakistan-Afghanistan\n(3) Nathu La - India-China (Sikkim)\n(4) Shipki La - India-China (Himachal Pradesh)\n\nWhich of the above are correctly matched?",
        "options": ["1 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 1,
        "explanation": "Statements 1, 3, and 4 are correct. Bolan Pass connects Pakistan and Afghanistan through Balochistan, not directly between them.",
        "difficulty": "hard",
        "topic": "Physical Geography - Passes"
    },
    {
        "question_text": "The Western Ghats are a UNESCO World Heritage Site. Which of the following is NOT a characteristic of Western Ghats?",
        "options": ["They are older than the Himalayas", "They are a biodiversity hotspot", "They are higher on average than Eastern Ghats", "They receive more rainfall than Eastern Ghats"],
        "correct_option": 0,
        "explanation": "Western Ghats are NOT older than Himalayas. They were formed about 150 million years ago due to the breakup of Gondwanaland, while the origin predates Himalayas but the current form is similar age.",
        "difficulty": "hard",
        "topic": "Indian Geography - Western Ghats"
    },
    {
        "question_text": "Which of the following straits connects the Bay of Bengal with the Andaman Sea?",
        "options": ["Palk Strait", "Ten Degree Channel", "Malacca Strait", "Sunda Strait"],
        "correct_option": 1,
        "explanation": "Ten Degree Channel (between Andaman and Nicobar Islands) connects Bay of Bengal with Andaman Sea. Palk Strait is between India and Sri Lanka.",
        "difficulty": "medium",
        "topic": "World Geography - Straits"
    },
    {
        "question_text": "Arrange the following ocean currents from North to South along the Atlantic Ocean's western coast:\n(1) Gulf Stream\n(2) Labrador Current\n(3) Brazil Current\n(4) North Atlantic Drift",
        "options": ["2-1-4-3", "2-4-1-3", "1-2-4-3", "4-2-1-3"],
        "correct_option": 0,
        "explanation": "From North to South: Labrador Current (cold, Canada), Gulf Stream (warm, USA), North Atlantic Drift (warm, N. Atlantic), Brazil Current (warm, S. America).",
        "difficulty": "hard",
        "topic": "World Geography - Ocean Currents"
    },
    {
        "question_text": "Consider the following statements about El Niño:\n(1) It is characterized by unusually warm ocean temperatures in the equatorial Pacific\n(2) It typically causes drought conditions in India\n(3) It occurs every 2-7 years\n(4) La Niña is the opposite phase with cooler temperatures\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "1, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. El Niño causes warming in Pacific, often leads to weak monsoon in India, occurs every 2-7 years, and La Niña is its opposite phase.",
        "difficulty": "medium",
        "topic": "World Geography - El Niño"
    },
    {
        "question_text": "Which country shares the longest land border with India?",
        "options": ["China", "Pakistan", "Bangladesh", "Nepal"],
        "correct_option": 2,
        "explanation": "Bangladesh shares the longest border with India (4,096 km), followed by China (3,488 km), Pakistan (3,323 km), and Nepal (1,751 km).",
        "difficulty": "easy",
        "topic": "Indian Geography - Borders"
    },
    {
        "question_text": "Consider the following lakes:\n(1) Chilika - Odisha (Lagoon)\n(2) Wular - Jammu & Kashmir (Freshwater)\n(3) Loktak - Manipur (Freshwater)\n(4) Pulicat - Andhra Pradesh/Tamil Nadu (Brackish)\n\nWhich of the above pairs are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. Chilika is Asia's largest lagoon, Wular is India's largest freshwater lake, Loktak has floating islands (phumdis), Pulicat is a brackish water lagoon.",
        "difficulty": "hard",
        "topic": "Indian Geography - Lakes"
    },
    {
        "question_text": "The 'Great Barrier Reef' is located off the coast of:",
        "options": ["Brazil", "Australia", "Philippines", "Indonesia"],
        "correct_option": 1,
        "explanation": "The Great Barrier Reef, the world's largest coral reef system, is located off the coast of Queensland, Australia in the Coral Sea.",
        "difficulty": "easy",
        "topic": "World Geography - Coral Reefs"
    },
    {
        "question_text": "Which of the following statements about the Siachen Glacier is/are correct?\n(1) It is the longest glacier in the Karakoram Range\n(2) It is located in the Ladakh region\n(3) Nubra River originates from this glacier\n(4) It is controlled by India since Operation Meghdoot (1984)\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Siachen is the longest Karakoram glacier (76 km), located in Ladakh, source of Nubra River, and controlled by India since 1984.",
        "difficulty": "hard",
        "topic": "Indian Geography - Glaciers"
    },
    {
        "question_text": "Match the following mineral-producing regions with their states:\n\nMineral Region : State\n(A) Kolar Gold Fields : (1) Jharkhand\n(B) Singhbhum Copper Belt : (2) Karnataka\n(C) Balaghat Manganese : (3) Odisha\n(D) Mayurbhanj Iron Ore : (4) Madhya Pradesh\n\nSelect the correct answer:",
        "options": ["A-2, B-1, C-4, D-3", "A-1, B-2, C-3, D-4", "A-2, B-3, C-4, D-1", "A-2, B-1, C-3, D-4"],
        "correct_option": 0,
        "explanation": "Kolar is in Karnataka, Singhbhum in Jharkhand, Balaghat in MP, and Mayurbhanj in Odisha. All are major mineral belts in India.",
        "difficulty": "hard",
        "topic": "Indian Geography - Minerals"
    },
    {
        "question_text": "Which of the following crops is NOT grown during the Rabi season in India?",
        "options": ["Wheat", "Mustard", "Rice", "Gram"],
        "correct_option": 2,
        "explanation": "Rice is primarily a Kharif crop (sown in June-July, harvested in September-October). Wheat, Mustard, and Gram are Rabi crops (sown in October-November, harvested in March-April).",
        "difficulty": "easy",
        "topic": "Indian Geography - Agriculture"
    },
    {
        "question_text": "Consider the following statements about the Sundarbans:\n(1) It is the largest mangrove forest in the world\n(2) It is shared between India and Bangladesh\n(3) The Royal Bengal Tiger is the keystone species\n(4) It is a UNESCO World Heritage Site\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Sundarbans is the world's largest mangrove forest, shared by India and Bangladesh, home to Royal Bengal Tiger, and a UNESCO WHS.",
        "difficulty": "medium",
        "topic": "Indian Geography - Sundarbans"
    },
    {
        "question_text": "The 'Ring of Fire' is associated with:",
        "options": ["Volcanic activity around the Atlantic Ocean", "Earthquake zones in the Mediterranean", "Volcanic and seismic activity around the Pacific Ocean", "Rift valley formation in Africa"],
        "correct_option": 2,
        "explanation": "The Ring of Fire is a horseshoe-shaped zone around the Pacific Ocean characterized by frequent earthquakes and volcanic eruptions due to tectonic plate boundaries.",
        "difficulty": "easy",
        "topic": "World Geography - Ring of Fire"
    },
    {
        "question_text": "Which of the following Indian states does NOT share a border with Myanmar?",
        "options": ["Arunachal Pradesh", "Nagaland", "Manipur", "Tripura"],
        "correct_option": 3,
        "explanation": "Tripura shares borders with Bangladesh, not Myanmar. Arunachal Pradesh, Nagaland, Manipur, and Mizoram share borders with Myanmar.",
        "difficulty": "medium",
        "topic": "Indian Geography - Borders"
    },
    {
        "question_text": "Consider the following rivers and their origins:\n(1) Ganga - Gangotri Glacier\n(2) Yamuna - Yamunotri Glacier\n(3) Indus - Mansarovar Lake\n(4) Sutlej - Rakas Lake\n\nWhich of the above pairs are correctly matched?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "1, 2 and 4 only", "All of the above"],
        "correct_option": 2,
        "explanation": "Ganga originates from Gangotri, Yamuna from Yamunotri, Sutlej from Rakas Lake. Indus originates from Bokhar Chu glacier near Mansarovar, not from the lake itself.",
        "difficulty": "hard",
        "topic": "Indian Geography - River Origins"
    },
    {
        "question_text": "The Tropic of Cancer passes through how many Indian states?",
        "options": ["6", "7", "8", "9"],
        "correct_option": 2,
        "explanation": "The Tropic of Cancer passes through 8 Indian states: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram.",
        "difficulty": "medium",
        "topic": "Indian Geography - Tropic of Cancer"
    },
    {
        "question_text": "Which of the following is the correct sequence of atmospheric layers from Earth's surface upwards?",
        "options": ["Troposphere-Stratosphere-Mesosphere-Thermosphere-Exosphere", "Troposphere-Mesosphere-Stratosphere-Thermosphere-Exosphere", "Stratosphere-Troposphere-Mesosphere-Thermosphere-Exosphere", "Troposphere-Stratosphere-Thermosphere-Mesosphere-Exosphere"],
        "correct_option": 0,
        "explanation": "The correct sequence from Earth's surface is: Troposphere (0-12 km), Stratosphere (12-50 km), Mesosphere (50-80 km), Thermosphere (80-700 km), Exosphere (700+ km).",
        "difficulty": "medium",
        "topic": "Physical Geography - Atmosphere"
    },
    {
        "question_text": "Consider the following about Indian ports:\n(1) Mumbai - Natural harbour, largest port\n(2) Chennai - Artificial harbour\n(3) Kandla - Tidal port in Gulf of Kutch\n(4) Paradip - Major port in Odisha\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "2, 3 and 4 only", "1, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Mumbai is a natural harbour, Chennai is artificial, Kandla is a tidal port, and Paradip is the major port in Odisha.",
        "difficulty": "medium",
        "topic": "Indian Geography - Ports"
    },
    {
        "question_text": "The Narmada and Tapti rivers flow westward because:",
        "options": ["They originate in Western Ghats", "They flow through rift valleys", "The western coast is steeper", "Monsoon winds push them westward"],
        "correct_option": 1,
        "explanation": "Narmada and Tapti flow through rift valleys (fault troughs) that slope westward, unlike most peninsular rivers that flow eastward due to the general tilt of the peninsula.",
        "difficulty": "medium",
        "topic": "Indian Geography - Rivers"
    },
    {
        "question_text": "Which of the following biosphere reserves in India is NOT part of the UNESCO World Network of Biosphere Reserves?",
        "options": ["Nilgiri", "Sundarbans", "Nanda Devi", "Simlipal"],
        "correct_option": 3,
        "explanation": "Simlipal (Odisha) is not yet part of UNESCO's World Network. Nilgiri, Sundarbans, and Nanda Devi are all UNESCO-designated biosphere reserves.",
        "difficulty": "hard",
        "topic": "Indian Geography - Biosphere Reserves"
    },
    {
        "question_text": "The 'Pampas' grasslands are found in:",
        "options": ["North America", "Australia", "South America", "Africa"],
        "correct_option": 2,
        "explanation": "Pampas are temperate grasslands found in South America, mainly in Argentina, Uruguay, and Brazil. Similar grasslands are Prairies (N. America), Steppes (Eurasia), and Veld (S. Africa).",
        "difficulty": "easy",
        "topic": "World Geography - Grasslands"
    },
    {
        "question_text": "Consider the following statements about the Dead Sea:\n(1) It is the lowest point on Earth's land surface\n(2) It lies between Israel and Jordan\n(3) Its high salinity prevents any life forms\n(4) The Jordan River flows into it\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 1,
        "explanation": "Statements 1, 2, and 4 are correct. Statement 3 is incorrect - despite high salinity, some bacteria and microbial fungi can survive in the Dead Sea.",
        "difficulty": "medium",
        "topic": "World Geography - Dead Sea"
    },
    {
        "question_text": "Which of the following countries does NOT share a border with the Caspian Sea?",
        "options": ["Russia", "Iran", "Turkey", "Kazakhstan"],
        "correct_option": 2,
        "explanation": "Turkey does NOT border the Caspian Sea. The five countries bordering it are: Russia, Kazakhstan, Turkmenistan, Iran, and Azerbaijan.",
        "difficulty": "medium",
        "topic": "World Geography - Caspian Sea"
    },
    {
        "question_text": "The Thar Desert is expanding primarily due to:\n(1) Overgrazing\n(2) Deforestation\n(3) Excessive groundwater extraction\n(4) Climate change\n\nWhich of the above are correct causes?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All factors contribute to desertification in the Thar region - overgrazing, deforestation, groundwater depletion, and climate change are all documented causes.",
        "difficulty": "medium",
        "topic": "Indian Geography - Desertification"
    },
    {
        "question_text": "Arrange the following peaks from highest to lowest elevation:\n(1) Mt. Everest\n(2) K2\n(3) Kangchenjunga\n(4) Nanga Parbat",
        "options": ["1-2-3-4", "1-2-4-3", "1-3-2-4", "2-1-3-4"],
        "correct_option": 0,
        "explanation": "The correct order is: Mt. Everest (8,849m), K2 (8,611m), Kangchenjunga (8,586m), Nanga Parbat (8,126m).",
        "difficulty": "easy",
        "topic": "Physical Geography - Mountain Peaks"
    },
    {
        "question_text": "Which of the following is NOT a west-flowing river of India?",
        "options": ["Mahi", "Sabarmati", "Pennar", "Luni"],
        "correct_option": 2,
        "explanation": "Pennar is an east-flowing river that originates in Karnataka and flows through Andhra Pradesh into the Bay of Bengal. Mahi, Sabarmati, and Luni all flow westward.",
        "difficulty": "medium",
        "topic": "Indian Geography - Rivers"
    },
    {
        "question_text": "The Konkan Coast extends from:",
        "options": ["Goa to Kanyakumari", "Daman to Goa", "Mumbai to Mangalore", "Surat to Kochi"],
        "correct_option": 1,
        "explanation": "The Konkan Coast extends from Daman in Gujarat to Goa. The coast south of Goa is called the Malabar Coast (Goa to Kanyakumari).",
        "difficulty": "medium",
        "topic": "Indian Geography - Coasts"
    },
    {
        "question_text": "Consider the following about cyclones:\n(1) Cyclones rotate clockwise in Northern Hemisphere\n(2) The eye of the cyclone is calm with clear skies\n(3) Cyclones are called Hurricanes in the Atlantic\n(4) Bay of Bengal experiences more cyclones than Arabian Sea\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "2, 3 and 4 only", "1, 3 and 4 only", "All of the above"],
        "correct_option": 1,
        "explanation": "Statements 2, 3, and 4 are correct. Statement 1 is incorrect - cyclones rotate anti-clockwise in Northern Hemisphere and clockwise in Southern Hemisphere.",
        "difficulty": "hard",
        "topic": "Physical Geography - Cyclones"
    },
    {
        "question_text": "Which Schedule of the Constitution contains the list of states and their territorial jurisdiction?",
        "options": ["First Schedule", "Second Schedule", "Fourth Schedule", "Seventh Schedule"],
        "correct_option": 0,
        "explanation": "The First Schedule contains the list of States and Union Territories and their territorial jurisdiction.",
        "difficulty": "easy",
        "topic": "Indian Geography - Constitutional Provisions"
    },
    {
        "question_text": "The major iron ore producing regions of Odisha include:\n(1) Mayurbhanj\n(2) Keonjhar\n(3) Sundargarh\n(4) Koraput\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 1,
        "explanation": "Mayurbhanj, Keonjhar, and Sundargarh districts form the iron ore belt of Odisha. Koraput is known for bauxite, not iron ore.",
        "difficulty": "medium",
        "topic": "Odisha Geography - Minerals"
    },
    {
        "question_text": "The Chilika Lake is important for which of the following reasons?\n(1) It is the largest brackish water lagoon in Asia\n(2) It is a Ramsar site (Wetland of International Importance)\n(3) It hosts the Irrawaddy Dolphins\n(4) Nalabana Island is a bird sanctuary within it\n\nWhich of the above are correct?",
        "options": ["1 and 2 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Chilika is Asia's largest brackish water lagoon, a Ramsar site, home to Irrawaddy Dolphins, and contains Nalabana Bird Sanctuary.",
        "difficulty": "medium",
        "topic": "Odisha Geography - Chilika Lake"
    },
    {
        "question_text": "Which of the following rivers of Odisha does NOT originate within the state?",
        "options": ["Mahanadi", "Brahmani", "Baitarani", "Subarnarekha"],
        "correct_option": 3,
        "explanation": "Subarnarekha originates in Jharkhand (Ranchi Plateau) and flows through Odisha before entering the Bay of Bengal. Mahanadi, Brahmani, and Baitarani all originate in Chhattisgarh or Odisha.",
        "difficulty": "hard",
        "topic": "Odisha Geography - Rivers"
    },
    {
        "question_text": "The Simlipal National Park in Odisha is famous for:",
        "options": ["One-horned Rhinoceros", "Asiatic Lions", "Melanistic Tigers (Black Tigers)", "Snow Leopards"],
        "correct_option": 2,
        "explanation": "Simlipal is famous for its Melanistic Tigers (pseudo-melanistic, appearing black due to dense stripes). It is one of the few places where black tigers have been spotted.",
        "difficulty": "medium",
        "topic": "Odisha Geography - Wildlife"
    },
    {
        "question_text": "Consider the following about India's maritime boundaries:\n(1) India has an Exclusive Economic Zone (EEZ) of 200 nautical miles\n(2) The territorial waters extend to 12 nautical miles\n(3) The contiguous zone extends to 24 nautical miles\n(4) India's coastline is approximately 7,500 km\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct as per UNCLOS. India's EEZ is 200 nm, territorial waters 12 nm, contiguous zone 24 nm, and coastline is approximately 7,516.6 km.",
        "difficulty": "hard",
        "topic": "Indian Geography - Maritime Boundaries"
    },
    {
        "question_text": "The International Date Line passes through:",
        "options": ["180° longitude mostly", "0° longitude (Prime Meridian)", "90° East longitude", "90° West longitude"],
        "correct_option": 0,
        "explanation": "The International Date Line roughly follows the 180° longitude through the Pacific Ocean, with some deviations to avoid splitting countries.",
        "difficulty": "easy",
        "topic": "Physical Geography - Date Line"
    },
    {
        "question_text": "Which of the following statements about the Andaman and Nicobar Islands is/are correct?\n(1) They are of volcanic origin\n(2) Barren Island has India's only active volcano\n(3) The capital is Port Blair\n(4) The Ten Degree Channel separates Andaman from Nicobar Islands\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "2, 3 and 4 only", "1, 2 and 3 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The islands are volcanic, Barren Island is India's only active volcano, Port Blair is the capital, and Ten Degree Channel separates the groups.",
        "difficulty": "medium",
        "topic": "Indian Geography - Islands"
    },
    {
        "question_text": "The phenomenon of temperature inversion is most commonly observed in:",
        "options": ["Coastal areas", "Mountain valleys", "Plains during summer", "Tropical forests"],
        "correct_option": 1,
        "explanation": "Temperature inversion (where temperature increases with altitude instead of decreasing) is most common in mountain valleys during winter nights due to cold air sinking and pooling.",
        "difficulty": "medium",
        "topic": "Physical Geography - Temperature Inversion"
    },
    {
        "question_text": "Which among the following is the correct sequence of coal types in order of increasing carbon content?",
        "options": ["Lignite-Peat-Bituminous-Anthracite", "Peat-Lignite-Bituminous-Anthracite", "Peat-Bituminous-Lignite-Anthracite", "Lignite-Bituminous-Peat-Anthracite"],
        "correct_option": 1,
        "explanation": "The correct sequence of increasing carbon content is: Peat (60%)-Lignite (70%)-Bituminous (80%)-Anthracite (90%+). This represents the coalification process.",
        "difficulty": "medium",
        "topic": "Economic Geography - Coal"
    },
    {
        "question_text": "Consider the following industrial regions of India:\n(1) Hooghly Industrial Region - Jute and Engineering\n(2) Mumbai-Pune Region - Cotton and Petrochemicals\n(3) Chennai-Bangalore Region - Automobiles and IT\n(4) Gujarat Industrial Region - Textiles and Petrochemicals\n\nWhich of the above pairs are correctly matched?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. Each region has developed specialization in the mentioned industries based on resource availability and historical factors.",
        "difficulty": "hard",
        "topic": "Economic Geography - Industries"
    },
]

# Export
if __name__ == "__main__":
    print(f"Total Geography questions: {len(GEOGRAPHY_QUESTIONS)}")
