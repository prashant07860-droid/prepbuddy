"""
OPSC Questions Database - Science and Technology
High-quality, OPSC-level questions based on actual exam patterns
Covers Physics, Chemistry, Biology, Space, IT, Defence, Health
"""

SCIENCE_TECHNOLOGY_QUESTIONS = [
    {
        "question_text": "Consider the following statements about ISRO's missions:\n(1) Chandrayaan-3 successfully landed near the lunar south pole in 2023\n(2) Aditya-L1 is India's first solar observation mission\n(3) Gaganyaan will be India's first crewed space mission\n(4) PSLV is used for launching heavy satellites to GTO\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - GSLV (not PSLV) is used for heavy satellites to Geosynchronous Transfer Orbit. PSLV is for polar orbits.",
        "difficulty": "hard",
        "topic": "Space Technology - ISRO"
    },
    {
        "question_text": "The Lagrange Point L1, where Aditya-L1 is positioned, is significant because:",
        "options": ["It is the closest point to the Sun", "Objects here can maintain stable position relative to Earth and Sun", "It has zero gravity", "It is the coldest point in space"],
        "correct_option": 1,
        "explanation": "L1 is one of five Lagrange points where gravitational forces of Sun and Earth balance, allowing spacecraft to maintain stable position with minimal fuel for continuous solar observation.",
        "difficulty": "medium",
        "topic": "Space Technology - Lagrange Points"
    },
    {
        "question_text": "Which of the following launch vehicles of ISRO is cryogenic?\n(1) PSLV\n(2) GSLV Mk II\n(3) GSLV Mk III (LVM3)\n(4) SSLV\n\nSelect the correct answer:",
        "options": ["2 only", "2 and 3 only", "1 and 2 only", "All of the above"],
        "correct_option": 1,
        "explanation": "GSLV Mk II and GSLV Mk III (LVM3) use cryogenic upper stages. PSLV uses solid and liquid stages but not cryogenic. SSLV is a small satellite launch vehicle.",
        "difficulty": "hard",
        "topic": "Space Technology - Launch Vehicles"
    },
    {
        "question_text": "NavIC (Navigation with Indian Constellation) is India's regional navigation system. Which of the following statements is correct?",
        "options": ["It covers only India", "It has 7 satellites covering India and 1500 km beyond", "It is equivalent to GPS in coverage", "It uses only geostationary satellites"],
        "correct_option": 1,
        "explanation": "NavIC has 7 satellites (3 in GEO, 4 in GSO) covering India and region up to 1500 km from Indian boundary. It provides position accuracy of less than 20 meters.",
        "difficulty": "medium",
        "topic": "Space Technology - NavIC"
    },
    {
        "question_text": "Consider the following about nuclear power plants in India:\n(1) Tarapur was India's first nuclear power plant\n(2) India follows a three-stage nuclear programme\n(3) Kudankulam uses Russian VVER reactors\n(4) BARC is responsible for nuclear research\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Tarapur (1969) was first, three-stage programme uses U-Pu-Th cycle, Kudankulam has Russian VVER reactors, and BARC handles nuclear research.",
        "difficulty": "hard",
        "topic": "Nuclear Technology"
    },
    {
        "question_text": "India's three-stage nuclear power programme is based on:",
        "options": ["Uranium-Plutonium-Thorium cycle", "Uranium-Thorium-Plutonium cycle", "Thorium-Uranium-Plutonium cycle", "Plutonium-Thorium-Uranium cycle"],
        "correct_option": 0,
        "explanation": "Stage 1 uses natural Uranium (PHWR), Stage 2 uses Plutonium (Fast Breeder Reactors), Stage 3 will use Thorium. This was designed by Homi Bhabha to utilize India's vast thorium reserves.",
        "difficulty": "medium",
        "topic": "Nuclear Technology - Three Stage Programme"
    },
    {
        "question_text": "Which of the following is NOT a ballistic missile of India?",
        "options": ["Agni-V", "Prithvi", "BrahMos", "K-4"],
        "correct_option": 2,
        "explanation": "BrahMos is a cruise missile (supersonic), not a ballistic missile. Agni series, Prithvi, and K-4 (submarine-launched) are ballistic missiles.",
        "difficulty": "medium",
        "topic": "Defence Technology - Missiles"
    },
    {
        "question_text": "Consider the following about India's missile defence systems:\n(1) Prithvi Air Defence (PAD) intercepts missiles at high altitude\n(2) Advanced Air Defence (AAD) intercepts at lower altitude\n(3) S-400 is an indigenous missile system\n(4) India has demonstrated ASAT capability\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 4 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 4 are correct. Statement 3 is incorrect - S-400 is a Russian air defence system purchased by India, not indigenous.",
        "difficulty": "hard",
        "topic": "Defence Technology"
    },
    {
        "question_text": "The fifth-generation stealth fighter aircraft being developed by India is called:",
        "options": ["Tejas", "AMCA", "Rafale", "Sukhoi"],
        "correct_option": 1,
        "explanation": "AMCA (Advanced Medium Combat Aircraft) is India's indigenous fifth-generation stealth fighter under development by DRDO and HAL. Tejas is 4th gen, Rafale is French.",
        "difficulty": "medium",
        "topic": "Defence Technology - Aircraft"
    },
    {
        "question_text": "Which of the following technologies is used in Quantum Computing?",
        "options": ["Binary bits (0 and 1)", "Qubits (superposition of 0 and 1)", "Analog signals", "Hexadecimal system"],
        "correct_option": 1,
        "explanation": "Quantum computers use qubits which can exist in superposition of both 0 and 1 simultaneously, enabling massive parallel processing unlike classical binary computers.",
        "difficulty": "medium",
        "topic": "Information Technology - Quantum Computing"
    },
    {
        "question_text": "Consider the following about Artificial Intelligence:\n(1) Machine Learning is a subset of AI\n(2) Deep Learning uses neural networks\n(3) GPT models are based on Transformer architecture\n(4) AI cannot generate new content\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - Generative AI (like GPT, DALL-E) can create new content including text, images, code etc.",
        "difficulty": "hard",
        "topic": "Information Technology - AI"
    },
    {
        "question_text": "Blockchain technology is characterized by:",
        "options": ["Centralized database", "Immutable and distributed ledger", "Single point of failure", "Requires trusted intermediary"],
        "correct_option": 1,
        "explanation": "Blockchain is a decentralized, distributed, and immutable ledger technology. It eliminates single point of failure and doesn't require trusted intermediaries.",
        "difficulty": "medium",
        "topic": "Information Technology - Blockchain"
    },
    {
        "question_text": "5G technology operates in which frequency bands?",
        "options": ["Only sub-6 GHz", "Only millimeter wave (mmWave)", "Both sub-6 GHz and mmWave", "Only 2.4 GHz"],
        "correct_option": 2,
        "explanation": "5G operates in both sub-6 GHz bands (better coverage) and millimeter wave bands 24-100 GHz (higher speeds, shorter range). India's 5G uses 3.3-3.67 GHz and 26 GHz bands.",
        "difficulty": "medium",
        "topic": "Information Technology - 5G"
    },
    {
        "question_text": "Which of the following is NOT a feature of Internet of Things (IoT)?",
        "options": ["Connected devices", "Data collection and analysis", "Requires human intervention for all decisions", "Machine-to-machine communication"],
        "correct_option": 2,
        "explanation": "IoT enables automated decision-making without constant human intervention. Connected devices collect data, communicate with each other, and can act autonomously.",
        "difficulty": "easy",
        "topic": "Information Technology - IoT"
    },
    {
        "question_text": "Consider the following about biotechnology in India:\n(1) Bt Cotton is the only GM crop commercially cultivated\n(2) DBT is the nodal agency for biotechnology\n(3) GEAC approves GM crops\n(4) India is self-sufficient in insulin production\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - India still imports significant quantities of insulin though domestic production has increased.",
        "difficulty": "hard",
        "topic": "Biotechnology"
    },
    {
        "question_text": "CRISPR-Cas9 technology is used for:",
        "options": ["Drug delivery", "Gene editing", "Vaccine production", "Protein synthesis"],
        "correct_option": 1,
        "explanation": "CRISPR-Cas9 is a revolutionary gene-editing tool that allows precise modification of DNA sequences. It has applications in treating genetic diseases, crop improvement, etc.",
        "difficulty": "easy",
        "topic": "Biotechnology - Gene Editing"
    },
    {
        "question_text": "Which of the following vaccines uses mRNA technology?",
        "options": ["Covishield", "Covaxin", "Pfizer-BioNTech COVID vaccine", "Sputnik V"],
        "correct_option": 2,
        "explanation": "Pfizer-BioNTech (and Moderna) COVID vaccines use mRNA technology. Covishield is viral vector, Covaxin is inactivated virus, Sputnik V is viral vector.",
        "difficulty": "medium",
        "topic": "Health Technology - Vaccines"
    },
    {
        "question_text": "Consider the following about India's COVID-19 vaccines:\n(1) Covaxin was developed by Bharat Biotech with ICMR\n(2) Covishield is manufactured by Serum Institute under license from Oxford-AstraZeneca\n(3) ZyCoV-D is a DNA-based vaccine\n(4) Corbevax is a protein subunit vaccine\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. India developed multiple COVID vaccines using different platforms - inactivated virus (Covaxin), viral vector (Covishield), DNA (ZyCoV-D), and protein subunit (Corbevax).",
        "difficulty": "hard",
        "topic": "Health Technology - COVID Vaccines"
    },
    {
        "question_text": "Nanotechnology deals with materials at the scale of:",
        "options": ["1-100 millimeters", "1-100 micrometers", "1-100 nanometers", "1-100 picometers"],
        "correct_option": 2,
        "explanation": "Nanotechnology involves manipulation of matter at 1-100 nanometer scale (1 nanometer = 10^-9 meters). At this scale, materials exhibit unique properties.",
        "difficulty": "easy",
        "topic": "Nanotechnology"
    },
    {
        "question_text": "Carbon nanotubes are used in which of the following applications?\n(1) Electronics\n(2) Composites for aerospace\n(3) Drug delivery systems\n(4) Sports equipment\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "Carbon nanotubes have exceptional strength and electrical properties, making them useful in electronics, aerospace composites, drug delivery, and sports equipment.",
        "difficulty": "medium",
        "topic": "Nanotechnology - Carbon Nanotubes"
    },
    {
        "question_text": "Which of the following is the correct order of electromagnetic spectrum from lowest to highest frequency?",
        "options": ["Radio-Microwave-Infrared-Visible-UV-X-ray-Gamma", "Gamma-X-ray-UV-Visible-Infrared-Microwave-Radio", "Infrared-Visible-Radio-Microwave-UV-X-ray-Gamma", "Radio-Infrared-Microwave-Visible-UV-X-ray-Gamma"],
        "correct_option": 0,
        "explanation": "The correct order from lowest to highest frequency is: Radio waves < Microwaves < Infrared < Visible light < Ultraviolet < X-rays < Gamma rays.",
        "difficulty": "medium",
        "topic": "Physics - Electromagnetic Spectrum"
    },
    {
        "question_text": "Consider the following about semiconductors:\n(1) Silicon is the most commonly used semiconductor\n(2) N-type semiconductors have excess electrons\n(3) P-type semiconductors have excess holes\n(4) Semiconductors have conductivity between conductors and insulators\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Silicon is most used, n-type has extra electrons (from pentavalent doping), p-type has holes (from trivalent doping), conductivity is intermediate.",
        "difficulty": "hard",
        "topic": "Physics - Semiconductors"
    },
    {
        "question_text": "The phenomenon of 'Total Internal Reflection' is used in:",
        "options": ["Microscopes", "Optical fibers", "Periscopes", "Projectors"],
        "correct_option": 1,
        "explanation": "Optical fibers use total internal reflection to transmit light signals over long distances with minimal loss. Light is trapped inside the fiber core due to TIR.",
        "difficulty": "easy",
        "topic": "Physics - Optics"
    },
    {
        "question_text": "Which of the following is NOT a renewable source of energy?",
        "options": ["Solar", "Wind", "Natural Gas", "Geothermal"],
        "correct_option": 2,
        "explanation": "Natural Gas is a fossil fuel (non-renewable). Solar, Wind, and Geothermal are renewable energy sources.",
        "difficulty": "easy",
        "topic": "Energy Technology"
    },
    {
        "question_text": "Consider the following about hydrogen as fuel:\n(1) Green hydrogen is produced using renewable energy\n(2) Blue hydrogen is produced from natural gas with carbon capture\n(3) Grey hydrogen is produced from fossil fuels without carbon capture\n(4) Hydrogen fuel cells produce water as byproduct\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Hydrogen is color-coded based on production method, and fuel cells combine hydrogen with oxygen to produce electricity and water.",
        "difficulty": "hard",
        "topic": "Energy Technology - Hydrogen"
    },
    {
        "question_text": "The National Green Hydrogen Mission was launched in India in:",
        "options": ["2021", "2022", "2023", "2024"],
        "correct_option": 2,
        "explanation": "The National Green Hydrogen Mission was launched in January 2023 with an outlay of Rs. 19,744 crore to make India a global hub for green hydrogen production.",
        "difficulty": "medium",
        "topic": "Energy Technology - Green Hydrogen"
    },
    {
        "question_text": "Which of the following diseases is caused by a virus?",
        "options": ["Tuberculosis", "Typhoid", "Dengue", "Cholera"],
        "correct_option": 2,
        "explanation": "Dengue is caused by Dengue virus (transmitted by Aedes mosquitoes). TB is bacterial (Mycobacterium), Typhoid is bacterial (Salmonella), Cholera is bacterial (Vibrio cholerae).",
        "difficulty": "easy",
        "topic": "Biology - Diseases"
    },
    {
        "question_text": "Consider the following about the human immune system:\n(1) Antibodies are proteins produced by B-lymphocytes\n(2) T-cells are responsible for cell-mediated immunity\n(3) Vaccines provide active immunity\n(4) Mother's milk provides passive immunity to infants\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. B-cells produce antibodies (humoral immunity), T-cells handle cellular immunity, vaccines trigger active immunity, and maternal antibodies provide passive immunity.",
        "difficulty": "hard",
        "topic": "Biology - Immune System"
    },
    {
        "question_text": "The human genome contains approximately how many genes?",
        "options": ["3,000", "20,000-25,000", "100,000", "500,000"],
        "correct_option": 1,
        "explanation": "The Human Genome Project revealed that humans have approximately 20,000-25,000 protein-coding genes, much fewer than earlier estimates of 100,000.",
        "difficulty": "medium",
        "topic": "Biology - Genetics"
    },
    {
        "question_text": "Which of the following is NOT a greenhouse gas?",
        "options": ["Carbon dioxide", "Methane", "Nitrogen", "Nitrous oxide"],
        "correct_option": 2,
        "explanation": "Nitrogen (N2) makes up 78% of atmosphere but is not a greenhouse gas. CO2, CH4, and N2O are greenhouse gases that trap heat in the atmosphere.",
        "difficulty": "easy",
        "topic": "Chemistry - Greenhouse Gases"
    },
    {
        "question_text": "Consider the following about superconductivity:\n(1) Superconductors have zero electrical resistance\n(2) They exhibit Meissner effect (expelling magnetic fields)\n(3) Room temperature superconductors are commercially available\n(4) MRI machines use superconducting magnets\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 4 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 4 are correct. Statement 3 is incorrect - room temperature superconductors are still in research stage and not commercially available.",
        "difficulty": "hard",
        "topic": "Physics - Superconductivity"
    },
    {
        "question_text": "The Large Hadron Collider (LHC) is used for:",
        "options": ["Space exploration", "Particle physics research", "Nuclear power generation", "Weather prediction"],
        "correct_option": 1,
        "explanation": "LHC at CERN is the world's largest particle accelerator used for fundamental particle physics research. It discovered the Higgs boson in 2012.",
        "difficulty": "easy",
        "topic": "Physics - Particle Physics"
    },
    {
        "question_text": "Which of the following statements about Graphene is/are correct?\n(1) It is a single layer of carbon atoms\n(2) It is the strongest known material\n(3) It is an excellent conductor of electricity\n(4) It was discovered in 2004\n\nSelect the correct answer:",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Graphene is a 2D material made of single-layer carbon atoms, extremely strong, excellent conductor, discovered by Geim and Novoselov in 2004 (Nobel Prize 2010).",
        "difficulty": "hard",
        "topic": "Materials Science - Graphene"
    },
    {
        "question_text": "The 'Doppler Effect' is used in which of the following applications?",
        "options": ["Radar speed detection", "Ultrasound imaging", "Astronomy (red shift)", "All of the above"],
        "correct_option": 3,
        "explanation": "Doppler Effect (change in frequency due to relative motion) is used in radar guns, medical ultrasound, and astronomy to measure velocities and distances.",
        "difficulty": "medium",
        "topic": "Physics - Doppler Effect"
    },
    {
        "question_text": "India's first indigenous aircraft carrier is:",
        "options": ["INS Vikrant", "INS Vikramaditya", "INS Vishal", "INS Viraat"],
        "correct_option": 0,
        "explanation": "INS Vikrant (IAC-1) is India's first indigenously built aircraft carrier, commissioned in 2022. INS Vikramaditya was purchased from Russia.",
        "difficulty": "easy",
        "topic": "Defence Technology - Navy"
    },
    {
        "question_text": "Consider the following about India's Semiconductor Mission:\n(1) It aims to establish semiconductor fabs in India\n(2) It has an outlay of Rs. 76,000 crore\n(3) ISM is under Ministry of Electronics and IT\n(4) India Semiconductor Mission was launched in 2021\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. ISM was launched in 2021 with Rs. 76,000 crore outlay under MeitY to develop semiconductor ecosystem in India.",
        "difficulty": "hard",
        "topic": "Information Technology - Semiconductor Mission"
    },
    {
        "question_text": "Which of the following is the unit of radioactivity?",
        "options": ["Joule", "Becquerel", "Watt", "Newton"],
        "correct_option": 1,
        "explanation": "Becquerel (Bq) is the SI unit of radioactivity (1 disintegration per second). Curie (Ci) is the older unit. Joule is energy, Watt is power, Newton is force.",
        "difficulty": "easy",
        "topic": "Physics - Radioactivity"
    },
    {
        "question_text": "The 'Event Horizon Telescope' captured the first image of:",
        "options": ["A pulsar", "A black hole", "A neutron star", "A supernova"],
        "correct_option": 1,
        "explanation": "The Event Horizon Telescope captured the first image of a black hole (M87*) in 2019, and later the black hole at the center of our Milky Way (Sagittarius A*) in 2022.",
        "difficulty": "medium",
        "topic": "Space Technology - Black Holes"
    },
    {
        "question_text": "Consider the following about telemedicine in India:\n(1) eSanjeevani is a government telemedicine platform\n(2) Telemedicine Practice Guidelines were issued in 2020\n(3) It enables doctor-patient consultation through video\n(4) It requires physical examination for all consultations\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - telemedicine allows remote consultation without physical examination for many conditions.",
        "difficulty": "medium",
        "topic": "Health Technology - Telemedicine"
    },
    {
        "question_text": "Which of the following is NOT an application of LIDAR technology?",
        "options": ["Autonomous vehicles", "Archaeological surveys", "Atmospheric studies", "Submarine communication"],
        "correct_option": 3,
        "explanation": "LIDAR (Light Detection and Ranging) uses laser light which doesn't penetrate water well. It's used for mapping, autonomous vehicles, archaeology, but not submarine communication.",
        "difficulty": "hard",
        "topic": "Technology - LIDAR"
    },
    {
        "question_text": "The 'Digital Personal Data Protection Act' was passed in India in:",
        "options": ["2021", "2022", "2023", "2024"],
        "correct_option": 2,
        "explanation": "The Digital Personal Data Protection Act, 2023 was passed by Parliament in August 2023 to regulate digital personal data processing in India.",
        "difficulty": "medium",
        "topic": "Information Technology - Data Protection"
    },
    {
        "question_text": "Consider the following about Unified Payments Interface (UPI):\n(1) It was developed by NPCI\n(2) It enables instant real-time payments\n(3) It uses Virtual Payment Address (VPA)\n(4) It can only be used for domestic transactions\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - UPI has been linked with payment systems of Singapore, UAE, and other countries for international transactions.",
        "difficulty": "hard",
        "topic": "Information Technology - UPI"
    },
    {
        "question_text": "Which organization is responsible for India's cybersecurity?",
        "options": ["CERT-In", "NPCI", "UIDAI", "NASSCOM"],
        "correct_option": 0,
        "explanation": "CERT-In (Indian Computer Emergency Response Team) under MeitY is the nodal agency for cybersecurity in India, handling cyber incidents and issuing advisories.",
        "difficulty": "easy",
        "topic": "Information Technology - Cybersecurity"
    },
    {
        "question_text": "The term 'Dark Matter' in cosmology refers to:",
        "options": ["Black holes", "Matter that doesn't emit light but has gravitational effects", "Antimatter", "Cosmic radiation"],
        "correct_option": 1,
        "explanation": "Dark Matter is invisible matter that doesn't emit or absorb light but exerts gravitational force. It constitutes about 27% of the universe's mass-energy content.",
        "difficulty": "medium",
        "topic": "Physics - Cosmology"
    },
]

# Export
if __name__ == "__main__":
    print(f"Total Science & Technology questions: {len(SCIENCE_TECHNOLOGY_QUESTIONS)}")
