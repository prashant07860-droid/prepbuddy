"""
OPSC Questions Database - Economics
High-quality, OPSC-level questions based on actual exam patterns
Covers Indian Economy, Fiscal Policy, Monetary Policy, Banking, Trade
"""

ECONOMICS_QUESTIONS = [
    {
        "question_text": "Consider the following statements about GDP:\n(1) GDP at market price includes indirect taxes\n(2) GDP at factor cost excludes subsidies\n(3) NDP = GDP - Depreciation\n(4) GNP = GDP + Net Factor Income from Abroad\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 1,
        "explanation": "Statements 1, 3, and 4 are correct. Statement 2 is incorrect - GDP at factor cost is calculated by subtracting indirect taxes and adding subsidies to GDP at market price.",
        "difficulty": "hard",
        "topic": "National Income Accounting"
    },
    {
        "question_text": "The base year for calculating India's GDP was revised to:",
        "options": ["2004-05", "2011-12", "2015-16", "2017-18"],
        "correct_option": 1,
        "explanation": "India revised its GDP base year to 2011-12 from 2004-05 in January 2015. The new series also adopted GVA (Gross Value Added) at basic prices.",
        "difficulty": "medium",
        "topic": "National Income Accounting"
    },
    {
        "question_text": "Which of the following is NOT included in India's Foreign Exchange Reserves?",
        "options": ["Foreign Currency Assets", "Gold", "SDRs", "Currency in circulation"],
        "correct_option": 3,
        "explanation": "Currency in circulation is part of money supply, not forex reserves. Forex reserves include Foreign Currency Assets (FCA), Gold, SDRs, and Reserve Tranche Position in IMF.",
        "difficulty": "medium",
        "topic": "External Sector"
    },
    {
        "question_text": "Consider the following about the Fiscal Responsibility and Budget Management (FRBM) Act:\n(1) It was enacted in 2003\n(2) It aims to eliminate revenue deficit\n(3) It targets fiscal deficit at 3% of GDP\n(4) FRBM Review Committee was headed by N.K. Singh\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. FRBM Act 2003 targets fiscal prudence, and the N.K. Singh Committee reviewed it in 2017.",
        "difficulty": "hard",
        "topic": "Fiscal Policy - FRBM"
    },
    {
        "question_text": "The 'Fiscal Deficit' is the difference between:",
        "options": ["Total expenditure and total receipts excluding borrowings", "Revenue expenditure and revenue receipts", "Capital expenditure and capital receipts", "Total expenditure and total non-debt receipts"],
        "correct_option": 0,
        "explanation": "Fiscal Deficit = Total Expenditure - Total Receipts (excluding borrowings). It indicates the total borrowing requirements of the government.",
        "difficulty": "medium",
        "topic": "Fiscal Policy"
    },
    {
        "question_text": "Which of the following taxes go DIRECTLY to the State Governments without being shared with the Centre?",
        "options": ["GST", "Corporation Tax", "Stamp Duty on land transactions", "Customs Duty"],
        "correct_option": 2,
        "explanation": "Stamp Duty on land transactions is collected by State Governments exclusively. GST, Corporation Tax, and Customs Duty involve Centre or are shared.",
        "difficulty": "medium",
        "topic": "Fiscal Federalism"
    },
    {
        "question_text": "Consider the following about the Reserve Bank of India:\n(1) It was established in 1935\n(2) It was nationalized in 1949\n(3) It is the banker to Central and State Governments\n(4) It regulates the forex market\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. RBI was established in 1935, nationalized in 1949, acts as banker to governments, and regulates forex market under FEMA.",
        "difficulty": "medium",
        "topic": "Monetary Policy - RBI"
    },
    {
        "question_text": "The Monetary Policy Committee (MPC) of RBI consists of how many members?",
        "options": ["3", "5", "6", "7"],
        "correct_option": 2,
        "explanation": "MPC has 6 members - 3 from RBI (including Governor as Chairman) and 3 external members appointed by the Central Government.",
        "difficulty": "easy",
        "topic": "Monetary Policy - MPC"
    },
    {
        "question_text": "Which of the following is NOT a tool of Monetary Policy?",
        "options": ["Repo Rate", "CRR", "Government Expenditure", "Open Market Operations"],
        "correct_option": 2,
        "explanation": "Government Expenditure is a fiscal policy tool, not monetary policy. Repo Rate, CRR, and OMO are monetary policy instruments used by RBI.",
        "difficulty": "easy",
        "topic": "Monetary Policy"
    },
    {
        "question_text": "Consider the following about inflation indices in India:\n(1) CPI is used for inflation targeting by RBI\n(2) WPI is used for deflating GDP\n(3) CPI-Combined is compiled by CSO\n(4) WPI base year is 2011-12\n\nWhich of the above statements are correct?",
        "options": ["1 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. CPI is used for inflation targeting (RBI), WPI for GDP deflator, CPI-C by CSO, and WPI base year is 2011-12.",
        "difficulty": "hard",
        "topic": "Inflation"
    },
    {
        "question_text": "The 'Core Inflation' excludes which of the following components?",
        "options": ["Food and Energy prices", "Housing prices", "Transport costs", "Healthcare costs"],
        "correct_option": 0,
        "explanation": "Core Inflation excludes volatile components like food and energy (fuel) prices to measure underlying inflation trends more accurately.",
        "difficulty": "medium",
        "topic": "Inflation"
    },
    {
        "question_text": "Which bank is known as the 'Bankers' Bank'?",
        "options": ["State Bank of India", "Reserve Bank of India", "NABARD", "IDBI Bank"],
        "correct_option": 1,
        "explanation": "RBI is called the Bankers' Bank as it provides banking services to commercial banks - maintaining their accounts, lending to them, and acting as lender of last resort.",
        "difficulty": "easy",
        "topic": "Banking"
    },
    {
        "question_text": "Consider the following about Payment Banks:\n(1) They can accept deposits up to Rs. 2 lakh\n(2) They cannot issue loans or credit cards\n(3) They were recommended by Nachiket Mor Committee\n(4) Paytm Payments Bank is an example\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "2, 3 and 4 only", "1, 2 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Payment banks have deposit limit of Rs. 2 lakh, cannot lend, were recommended by Nachiket Mor Committee, and include Paytm, Airtel etc.",
        "difficulty": "hard",
        "topic": "Banking - Payment Banks"
    },
    {
        "question_text": "The 'Bad Bank' set up in India is officially known as:",
        "options": ["Asset Reconstruction Company (India) Limited", "National Asset Reconstruction Company Limited", "India Debt Resolution Company Limited", "Stressed Assets Resolution Company"],
        "correct_option": 1,
        "explanation": "NARCL (National Asset Reconstruction Company Limited) is India's bad bank set up in 2021 to take over stressed assets from banks.",
        "difficulty": "medium",
        "topic": "Banking - Bad Bank"
    },
    {
        "question_text": "Which of the following is NOT a function of NABARD?",
        "options": ["Refinancing rural credit institutions", "Supervising cooperative banks", "Providing direct loans to farmers", "Development functions in rural areas"],
        "correct_option": 2,
        "explanation": "NABARD does not provide direct loans to farmers. It provides refinance to lending institutions. Direct loans to farmers are given by commercial banks and cooperatives.",
        "difficulty": "medium",
        "topic": "Banking - NABARD"
    },
    {
        "question_text": "The Insurance Regulatory and Development Authority of India (IRDAI) was established in:",
        "options": ["1999", "2000", "2002", "2005"],
        "correct_option": 0,
        "explanation": "IRDAI was established in 1999 under the IRDA Act, 1999 to regulate the insurance sector in India.",
        "difficulty": "medium",
        "topic": "Financial Regulators"
    },
    {
        "question_text": "Consider the following about India's Balance of Payments:\n(1) Current Account includes trade balance and invisibles\n(2) Capital Account includes FDI and FPI\n(3) CAD is Current Account Deficit\n(4) A surplus in Capital Account can finance CAD\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. BOP has Current Account (trade + invisibles), Capital Account (FDI, FPI, loans), and capital surplus can offset current deficit.",
        "difficulty": "hard",
        "topic": "External Sector - BOP"
    },
    {
        "question_text": "Foreign Direct Investment (FDI) is different from Foreign Portfolio Investment (FPI) because:",
        "options": ["FDI is in government securities", "FDI involves lasting interest and significant control", "FPI is more stable than FDI", "FDI can only be in manufacturing sector"],
        "correct_option": 1,
        "explanation": "FDI involves lasting interest in an enterprise with significant degree of influence (usually 10% or more equity), while FPI is passive investment in financial assets.",
        "difficulty": "medium",
        "topic": "External Sector - FDI/FPI"
    },
    {
        "question_text": "Which of the following is NOT a feature of GST in India?",
        "options": ["Dual GST model", "Destination-based consumption tax", "Cascading effect of taxes", "Subsumed multiple indirect taxes"],
        "correct_option": 2,
        "explanation": "GST eliminated the cascading effect (tax on tax) that existed under the previous indirect tax regime. That's one of its key benefits.",
        "difficulty": "medium",
        "topic": "GST"
    },
    {
        "question_text": "The GST Council is headed by:",
        "options": ["Prime Minister", "Finance Minister", "RBI Governor", "Chairman of CBIC"],
        "correct_option": 1,
        "explanation": "The GST Council is headed by the Union Finance Minister. It includes Finance Ministers of all states and is a constitutional body under Article 279A.",
        "difficulty": "easy",
        "topic": "GST"
    },
    {
        "question_text": "Consider the following about NITI Aayog:\n(1) It replaced Planning Commission in 2015\n(2) The PM is its Chairman\n(3) It has a Governing Council with all CMs\n(4) It prepares Five Year Plans\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - NITI Aayog does not prepare Five Year Plans; instead it formulates Vision documents and Action Agendas.",
        "difficulty": "hard",
        "topic": "Economic Planning"
    },
    {
        "question_text": "The Minimum Support Price (MSP) is announced for how many crops?",
        "options": ["14", "22", "23", "25"],
        "correct_option": 2,
        "explanation": "MSP is announced for 23 crops - 7 cereals, 5 pulses, 7 oilseeds, and 4 commercial crops (sugarcane, cotton, raw jute, copra).",
        "difficulty": "medium",
        "topic": "Agriculture - MSP"
    },
    {
        "question_text": "Which committee recommended the formula of MSP based on comprehensive cost (C2) plus 50% margin?",
        "options": ["Swaminathan Committee", "Shanta Kumar Committee", "Ashok Dalwai Committee", "Ramesh Chand Committee"],
        "correct_option": 0,
        "explanation": "The M.S. Swaminathan Committee (National Commission on Farmers) recommended MSP at C2 cost plus 50% margin to ensure remunerative prices for farmers.",
        "difficulty": "hard",
        "topic": "Agriculture - MSP"
    },
    {
        "question_text": "The PM-KISAN scheme provides:",
        "options": ["Crop insurance to farmers", "Rs. 6000 per year to small farmers", "Loan waiver to farmers", "Free seeds to farmers"],
        "correct_option": 1,
        "explanation": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi) provides Rs. 6000 per year in three installments to all land-holding farmer families.",
        "difficulty": "easy",
        "topic": "Agriculture - Schemes"
    },
    {
        "question_text": "Consider the following about the Production Linked Incentive (PLI) scheme:\n(1) It was launched to boost domestic manufacturing\n(2) It covers 14 sectors\n(3) It provides incentives based on incremental production\n(4) Mobile manufacturing is included\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. PLI scheme covers 14 sectors including mobile, pharmaceuticals, automobiles, etc., and provides incentives on incremental production.",
        "difficulty": "hard",
        "topic": "Industrial Policy - PLI"
    },
    {
        "question_text": "The term 'Unicorn' in startup ecosystem refers to:",
        "options": ["Startups with revenue over Rs. 100 crore", "Startups with valuation over $1 billion", "Startups that have gone public", "Startups with over 1000 employees"],
        "correct_option": 1,
        "explanation": "Unicorn refers to privately held startup companies with a valuation of over $1 billion. India has over 100 unicorns as of 2023.",
        "difficulty": "easy",
        "topic": "Startup Ecosystem"
    },
    {
        "question_text": "Which of the following is NOT a pillar of Digital India programme?",
        "options": ["Digital Infrastructure", "Digital Services", "Digital Literacy", "Digital Currency"],
        "correct_option": 3,
        "explanation": "Digital India has three pillars: Digital Infrastructure, Digital Services (governance & services on demand), and Digital Empowerment (literacy). Digital Currency is separate.",
        "difficulty": "medium",
        "topic": "Digital Economy"
    },
    {
        "question_text": "The Insolvency and Bankruptcy Code (IBC) was enacted in:",
        "options": ["2015", "2016", "2017", "2018"],
        "correct_option": 1,
        "explanation": "The Insolvency and Bankruptcy Code was enacted in 2016 to consolidate and amend laws relating to insolvency resolution of corporate persons, partnership firms and individuals.",
        "difficulty": "easy",
        "topic": "Economic Reforms - IBC"
    },
    {
        "question_text": "Consider the following about India's trade with WTO:\n(1) India is a founding member of WTO\n(2) WTO was established in 1995\n(3) India has signed all WTO agreements\n(4) TRIPS agreement is about intellectual property\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 4 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 4 are correct. India has not signed all WTO agreements - for example, it has not signed the Trade Facilitation Agreement fully.",
        "difficulty": "hard",
        "topic": "International Trade - WTO"
    },
    {
        "question_text": "Which of the following correctly describes 'Demographic Dividend'?",
        "options": ["High birth rate in a country", "Population growth rate", "Working-age population larger than dependent population", "Equal distribution of population across age groups"],
        "correct_option": 2,
        "explanation": "Demographic Dividend refers to economic growth potential when working-age population (15-64) is larger than dependent population (0-14 and 65+), providing more labor and less burden.",
        "difficulty": "medium",
        "topic": "Indian Economy - Demographics"
    },
    {
        "question_text": "The Human Development Index (HDI) is compiled by:",
        "options": ["World Bank", "IMF", "UNDP", "ILO"],
        "correct_option": 2,
        "explanation": "The Human Development Index is compiled by UNDP (United Nations Development Programme) since 1990. It measures life expectancy, education, and standard of living.",
        "difficulty": "easy",
        "topic": "Development Indicators"
    },
    {
        "question_text": "Consider the following about the Multidimensional Poverty Index (MPI):\n(1) It is calculated by NITI Aayog for India\n(2) It covers health, education, and standard of living\n(3) It has 12 indicators\n(4) A person is MPI poor if deprived in at least one-third of indicators\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. India's National MPI by NITI Aayog uses 12 indicators across 3 dimensions, and person is MPI poor if deprived in 1/3rd or more weighted indicators.",
        "difficulty": "hard",
        "topic": "Poverty Measurement"
    },
    {
        "question_text": "The Gini Coefficient measures:",
        "options": ["Economic growth", "Income inequality", "Human development", "Financial inclusion"],
        "correct_option": 1,
        "explanation": "Gini Coefficient measures income/wealth inequality. It ranges from 0 (perfect equality) to 1 (perfect inequality).",
        "difficulty": "easy",
        "topic": "Inequality"
    },
    {
        "question_text": "Which of the following schemes is related to financial inclusion?",
        "options": ["Make in India", "Skill India", "Jan Dhan Yojana", "Startup India"],
        "correct_option": 2,
        "explanation": "Pradhan Mantri Jan Dhan Yojana is the flagship financial inclusion scheme aimed at providing universal access to banking facilities.",
        "difficulty": "easy",
        "topic": "Financial Inclusion"
    },
    {
        "question_text": "The 'Twin Balance Sheet Problem' in India refers to:",
        "options": ["Fiscal deficit and trade deficit", "NPAs in banks and corporate debt", "Revenue deficit and capital deficit", "Current account deficit and fiscal deficit"],
        "correct_option": 1,
        "explanation": "Twin Balance Sheet Problem refers to stressed balance sheets of both banks (high NPAs) and corporates (high debt levels), affecting credit flow and investment.",
        "difficulty": "hard",
        "topic": "Banking - NPAs"
    },
    {
        "question_text": "Consider the following about Special Economic Zones (SEZs):\n(1) They are governed by SEZ Act, 2005\n(2) They provide tax holidays to units\n(3) They are outside India's customs territory\n(4) SEBI regulates SEZs\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect - SEZs are regulated by the Ministry of Commerce, not SEBI.",
        "difficulty": "medium",
        "topic": "Industrial Policy - SEZs"
    },
    {
        "question_text": "Which of the following sectors contributes the maximum to India's GDP?",
        "options": ["Agriculture", "Industry", "Services", "Mining"],
        "correct_option": 2,
        "explanation": "Services sector contributes about 55% to India's GDP, followed by Industry (~25%) and Agriculture (~18%).",
        "difficulty": "easy",
        "topic": "Indian Economy - Sectoral Contribution"
    },
    {
        "question_text": "The 'Laffer Curve' shows the relationship between:",
        "options": ["Inflation and unemployment", "Tax rate and tax revenue", "Interest rate and investment", "Exchange rate and exports"],
        "correct_option": 1,
        "explanation": "Laffer Curve shows that beyond a certain point, increasing tax rates leads to lower tax revenue due to reduced economic activity and tax evasion.",
        "difficulty": "hard",
        "topic": "Taxation"
    },
    {
        "question_text": "Consider the following about India's disinvestment:\n(1) It involves sale of government's stake in PSUs\n(2) Strategic disinvestment involves transfer of management control\n(3) DIPAM handles disinvestment\n(4) LIC IPO was the largest disinvestment in India\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Disinvestment is handled by DIPAM, involves PSU stake sale, strategic disinvestment transfers control, and LIC IPO (2022) was largest.",
        "difficulty": "hard",
        "topic": "Disinvestment"
    },
    {
        "question_text": "Which committee recommended direct transfer of subsidies to beneficiaries?",
        "options": ["Kelkar Committee", "Chelliah Committee", "Sukhamoy Chakravarty Committee", "Nandan Nilekani Committee"],
        "correct_option": 3,
        "explanation": "Nandan Nilekani Committee (Task Force on Direct Transfer of Subsidies) recommended using Aadhaar for direct benefit transfer to eliminate leakages.",
        "difficulty": "hard",
        "topic": "Subsidies"
    },
    {
        "question_text": "The term 'Stagflation' refers to:",
        "options": ["High growth with high inflation", "Low growth with low inflation", "High inflation with low growth", "Zero inflation with zero growth"],
        "correct_option": 2,
        "explanation": "Stagflation is an economic situation where there is stagnant economic growth combined with high inflation - the worst of both worlds.",
        "difficulty": "medium",
        "topic": "Inflation"
    },
    {
        "question_text": "Which of the following is NOT a Public Sector Bank?",
        "options": ["Punjab National Bank", "Bank of Baroda", "ICICI Bank", "Central Bank of India"],
        "correct_option": 2,
        "explanation": "ICICI Bank is a private sector bank. Punjab National Bank, Bank of Baroda, and Central Bank of India are public sector banks.",
        "difficulty": "easy",
        "topic": "Banking"
    },
    {
        "question_text": "Consider the following about the 15th Finance Commission:\n(1) It was headed by N.K. Singh\n(2) Its recommendations are for 2021-26\n(3) It recommended 41% share to states from divisible pool\n(4) It created a separate fund for defence\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 2 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. 15th FC headed by N.K. Singh recommended 41% share for states and created a fund for defence and internal security.",
        "difficulty": "hard",
        "topic": "Finance Commission"
    },
    {
        "question_text": "The 'Real Effective Exchange Rate' (REER) is used to measure:",
        "options": ["Trade balance", "Competitiveness of exports", "FDI inflows", "External debt"],
        "correct_option": 1,
        "explanation": "REER is used to measure the competitiveness of a country's exports by comparing exchange rates adjusted for inflation differentials with trading partners.",
        "difficulty": "hard",
        "topic": "External Sector"
    },
    {
        "question_text": "Which of the following is the largest source of tax revenue for the Government of India?",
        "options": ["Corporate Tax", "Income Tax", "GST", "Customs Duty"],
        "correct_option": 2,
        "explanation": "GST (Central + Integrated) is now the largest source of tax revenue for the Centre, followed by Corporate Tax and Income Tax.",
        "difficulty": "medium",
        "topic": "Government Revenue"
    },
    {
        "question_text": "The 'Open Market Operations' (OMO) are conducted by RBI to:",
        "options": ["Control forex rates", "Regulate stock market", "Manage liquidity in the economy", "Control gold prices"],
        "correct_option": 2,
        "explanation": "OMO involves buying/selling of government securities by RBI in the open market to inject or absorb liquidity in the banking system.",
        "difficulty": "medium",
        "topic": "Monetary Policy - OMO"
    },
]

# Export
if __name__ == "__main__":
    print(f"Total Economics questions: {len(ECONOMICS_QUESTIONS)}")
