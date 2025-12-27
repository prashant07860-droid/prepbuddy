"""
OPSC Questions Database - Polity (Part 4 of 10)
President, Vice President, Prime Minister, Council of Ministers
Questions 280-540 (Unique, Non-Repeating)
"""

POLITY_QUESTIONS_PART4 = [
    # ==================== THE PRESIDENT (1-80) ====================
    {
        "question_text": "The President of India is:",
        "options": ["Head of State", "Head of Government", "Both Head of State and Government", "Neither"],
        "correct_option": 0,
        "explanation": "The President is the Head of State while the Prime Minister is the Head of Government. India follows parliamentary system with nominal and real executives.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "Articles relating to the President are contained in:",
        "options": ["Articles 52-62", "Articles 52-78", "Articles 52-72", "Articles 50-70"],
        "correct_option": 0,
        "explanation": "Articles 52 to 62 deal with the President of India in Part V of the Constitution.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The President is elected by:",
        "options": ["Direct election by people", "Indirect election by electoral college", "Parliament alone", "State legislatures alone"],
        "correct_option": 1,
        "explanation": "The President is elected by an electoral college consisting of elected members of both Houses of Parliament and State Legislative Assemblies.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "Which members are NOT part of the electoral college for President's election?",
        "options": ["Elected MPs", "Elected MLAs", "Nominated MPs", "MLCs"],
        "correct_option": 2,
        "explanation": "Nominated members of Parliament and State Legislatures and elected members of Legislative Councils are NOT part of the electoral college.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The system of proportional representation with single transferable vote is used for:",
        "options": ["Lok Sabha elections", "Rajya Sabha elections only", "Presidential election", "Both B and C"],
        "correct_option": 3,
        "explanation": "Proportional representation with single transferable vote is used for both Rajya Sabha and Presidential elections.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The value of vote of an MLA in Presidential election is calculated using:",
        "options": ["Total population of state / Total MLAs", "Total state population / (Total MLAs × 1000)", "State population as per 1971 census / (Total MLAs × 1000)", "State population as per 2011 census / Total MLAs"],
        "correct_option": 2,
        "explanation": "Value of MLA's vote = Total population of state (1971 census) ÷ (Total elected MLAs × 1000). The 84th Amendment froze 1971 census figures until 2026.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "The value of an MP's vote in Presidential election is calculated as:",
        "options": ["Total value of all MLAs' votes / Total MPs", "Total value of all MLAs' votes / Total elected MPs", "Fixed value for all MPs", "Varies by state"],
        "correct_option": 1,
        "explanation": "Value of MP's vote = Total value of votes of all elected MLAs ÷ Total number of elected MPs of both Houses.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "To be elected President, a candidate must secure:",
        "options": ["Simple majority", "Absolute majority", "2/3rd majority", "Quota of votes (50% + 1)"],
        "correct_option": 3,
        "explanation": "A candidate must secure a quota of votes, calculated as (Total valid votes cast / 2) + 1. This is determined through counting of first and subsequent preferences.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The minimum age to be elected as President is:",
        "options": ["25 years", "30 years", "35 years", "40 years"],
        "correct_option": 2,
        "explanation": "Article 58 prescribes minimum age of 35 years to be eligible for election as President of India.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "Which of the following is NOT a qualification for President?",
        "options": ["Citizen of India", "Completed 35 years of age", "Qualified for Lok Sabha membership", "Should have served as Governor"],
        "correct_option": 3,
        "explanation": "Qualifications under Article 58: citizen of India, 35 years age, qualified for Lok Sabha election. Prior service as Governor is not required.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "The oath of office to the President is administered by:",
        "options": ["Outgoing President", "Chief Justice of India", "Vice President", "Speaker of Lok Sabha"],
        "correct_option": 1,
        "explanation": "Under Article 60, the Chief Justice of India (or senior-most judge of Supreme Court in CJI's absence) administers oath to the President.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "The term of office of the President is:",
        "options": ["4 years", "5 years", "6 years", "Until successor enters office"],
        "correct_option": 1,
        "explanation": "The President holds office for 5 years from the date of entering office. However, continues until successor enters office.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "The President can resign by addressing the resignation to:",
        "options": ["Chief Justice of India", "Prime Minister", "Vice President", "Speaker of Lok Sabha"],
        "correct_option": 2,
        "explanation": "Under Article 56, the President may resign by writing addressed to the Vice President.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "The President can be removed from office by:",
        "options": ["No-confidence motion", "Impeachment", "Simple majority in Parliament", "Supreme Court order"],
        "correct_option": 1,
        "explanation": "Article 61 provides for removal of President by impeachment for 'violation of Constitution'. It requires special majority in both Houses.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "Impeachment charges against President can be initiated by:",
        "options": ["Only Lok Sabha", "Only Rajya Sabha", "Either House of Parliament", "Only Cabinet"],
        "correct_option": 2,
        "explanation": "Impeachment can be initiated by either House. It requires 1/4th members' notice, 2/3rd majority to pass in initiating House, and 2/3rd in other House after investigation.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "What majority is required to pass impeachment charges in both Houses?",
        "options": ["Simple majority", "Absolute majority", "2/3rd majority of total membership", "3/4th majority"],
        "correct_option": 2,
        "explanation": "Impeachment requires resolution passed by 2/3rd majority of total membership of the House (not just present and voting).",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "If both President and Vice President are absent, who acts as President?",
        "options": ["Prime Minister", "Chief Justice of India", "Speaker of Lok Sabha", "Senior-most Governor"],
        "correct_option": 1,
        "explanation": "If offices of both President and Vice President are vacant, Chief Justice of India acts as President. This happened in 1969 when V.V. Giri resigned.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "Vacancy in President's office must be filled within:",
        "options": ["1 month", "3 months", "6 months", "1 year"],
        "correct_option": 2,
        "explanation": "Article 62 mandates that election to fill vacancy must be held within 6 months. The new President serves full 5-year term.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The President's emoluments are charged on:",
        "options": ["Contingency Fund", "Consolidated Fund of India", "Public Account", "Reserve Fund"],
        "correct_option": 1,
        "explanation": "President's salary, allowances and pension are charged on Consolidated Fund of India and are non-votable.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "Which President was elected unopposed?",
        "options": ["Dr. Rajendra Prasad (1952)", "Dr. S. Radhakrishnan (1962)", "Neelam Sanjiva Reddy (1977)", "Both A and C"],
        "correct_option": 2,
        "explanation": "Neelam Sanjiva Reddy was the only President elected unopposed (1977). Dr. Rajendra Prasad faced elections both times.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "Who was the first President of India?",
        "options": ["Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "C. Rajagopalachari", "Jawaharlal Nehru"],
        "correct_option": 0,
        "explanation": "Dr. Rajendra Prasad was the first President of India (1950-1962). He is the only President to serve two complete terms.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "Who was the first woman President of India?",
        "options": ["Indira Gandhi", "Pratibha Patil", "Sonia Gandhi", "Droupadi Murmu"],
        "correct_option": 1,
        "explanation": "Pratibha Devisingh Patil was the first woman President of India (2007-2012).",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "The President's discretionary powers are:",
        "options": ["Absolute and unlimited", "Limited and situational", "Non-existent", "Same as British monarch"],
        "correct_option": 1,
        "explanation": "President has limited discretionary powers in appointing PM when no clear majority, dismissing ministry, returning bills (once), etc.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The President can return a bill for reconsideration:",
        "options": ["Any number of times", "Only once", "Twice", "Cannot return bills"],
        "correct_option": 1,
        "explanation": "President can return a bill (except Money Bill) for reconsideration only once. If passed again, President must give assent.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "Which type of bill cannot be returned by President for reconsideration?",
        "options": ["Ordinary bills", "Money bills", "Constitutional amendment bills", "Both B and C"],
        "correct_option": 3,
        "explanation": "President cannot return Money Bills and Constitutional Amendment Bills for reconsideration. These must be assented to or withheld.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "The President's 'pocket veto' refers to:",
        "options": ["Rejecting a bill outright", "Keeping a bill pending indefinitely", "Returning bill with amendments", "Referring bill to Supreme Court"],
        "correct_option": 1,
        "explanation": "Pocket veto is keeping a bill pending indefinitely without taking action. Constitution prescribes no time limit for President's assent.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "President Zail Singh used pocket veto for:",
        "options": ["TADA Bill", "Indian Post Office (Amendment) Bill", "Anti-Defection Bill", "National Security Bill"],
        "correct_option": 1,
        "explanation": "President Zail Singh exercised pocket veto on Indian Post Office (Amendment) Bill 1986, keeping it pending indefinitely.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "The President's ordinance-making power is under:",
        "options": ["Article 121", "Article 122", "Article 123", "Article 124"],
        "correct_option": 2,
        "explanation": "Article 123 empowers President to promulgate ordinances when Parliament is not in session, with same force as Act of Parliament.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "An ordinance promulgated by President must be laid before Parliament within:",
        "options": ["15 days", "30 days", "6 weeks of reassembly", "3 months"],
        "correct_option": 2,
        "explanation": "Ordinance must be laid before both Houses and ceases to operate 6 weeks after Parliament reassembles unless approved earlier.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "Maximum life of an ordinance without Parliamentary approval is:",
        "options": ["6 months", "6 weeks", "6 months + 6 weeks", "No fixed period"],
        "correct_option": 2,
        "explanation": "Maximum ordinance life = 6 months (max gap between sessions) + 6 weeks (approval period) = 7.5 months approximately.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "President's pardoning power is under:",
        "options": ["Article 70", "Article 71", "Article 72", "Article 73"],
        "correct_option": 2,
        "explanation": "Article 72 grants President power to grant pardons, reprieves, respites, remission of punishment or suspension of sentence.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "President can pardon death sentence awarded by:",
        "options": ["Supreme Court only", "Court martial only", "Any court in India", "All of the above"],
        "correct_option": 3,
        "explanation": "President's pardoning power under Article 72 extends to all cases including court martial sentences and death sentences by any court.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The difference between 'pardon' and 'commutation' is:",
        "options": ["Pardon is conditional, commutation is absolute", "Pardon removes conviction, commutation reduces sentence", "Both are same", "Pardon is temporary, commutation is permanent"],
        "correct_option": 1,
        "explanation": "Pardon completely absolves the convict. Commutation substitutes lighter punishment for the original (e.g., death to life imprisonment).",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "'Reprieve' as Presidential power means:",
        "options": ["Reducing sentence", "Temporary suspension of sentence", "Cancelling conviction", "Changing nature of punishment"],
        "correct_option": 1,
        "explanation": "Reprieve means temporary suspension of sentence (especially death sentence) to enable convict to seek pardon or commutation.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "'Respite' as Presidential power means:",
        "options": ["Awarding lesser sentence due to special circumstances", "Suspending sentence temporarily", "Removing conviction completely", "Reducing rigorous to simple imprisonment"],
        "correct_option": 0,
        "explanation": "Respite means awarding lesser sentence in place of prescribed sentence due to special circumstances like pregnancy, old age, etc.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "President's pardoning power is subject to judicial review after:",
        "options": ["Kehar Singh case (1989)", "Maru Ram case (1980)", "Epuru Sudhakar case (2006)", "All established judicial review"],
        "correct_option": 2,
        "explanation": "In Epuru Sudhakar case (2006), SC held that pardoning power is subject to limited judicial review for arbitrariness.",
        "difficulty": "hard",
        "topic": "President"
    },
    {
        "question_text": "The President appoints all of the following EXCEPT:",
        "options": ["Prime Minister", "Chief Justice of India", "Chairman of UPSC", "Speaker of Lok Sabha"],
        "correct_option": 3,
        "explanation": "Speaker is elected by Lok Sabha members. President appoints PM, CJI, CAG, UPSC Chairman, Election Commissioners, etc.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "President nominates how many members to Rajya Sabha?",
        "options": ["10", "12", "14", "15"],
        "correct_option": 1,
        "explanation": "President nominates 12 members to Rajya Sabha from persons having special knowledge in literature, science, art, social service.",
        "difficulty": "easy",
        "topic": "President"
    },
    {
        "question_text": "President nominates how many Anglo-Indians to Lok Sabha?",
        "options": ["0 (provision deleted)", "2", "4", "12"],
        "correct_option": 0,
        "explanation": "The 104th Amendment (2019) deleted the provision for nomination of Anglo-Indians to Lok Sabha and State Assemblies.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "The President's address to Parliament is under:",
        "options": ["Article 85", "Article 86", "Article 87", "Article 88"],
        "correct_option": 2,
        "explanation": "Article 87 provides for President's special address at commencement of first session each year and first session of new Lok Sabha.",
        "difficulty": "medium",
        "topic": "President"
    },
    {
        "question_text": "Money Bill can be introduced only with prior recommendation of:",
        "options": ["Prime Minister", "Finance Minister", "President", "Speaker"],
        "correct_option": 2,
        "explanation": "Article 117 requires President's prior recommendation for introduction of Money Bills and certain Financial Bills.",
        "difficulty": "easy",
        "topic": "President"
    },
    # ==================== VICE PRESIDENT (81-110) ====================
    {
        "question_text": "The Vice President is:",
        "options": ["Part of executive", "Part of legislature", "Both executive and legislative role", "Neither"],
        "correct_option": 2,
        "explanation": "Vice President is ex-officio Chairman of Rajya Sabha (legislative role) and acts as President when vacancy arises (executive role).",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "The Vice President is elected by:",
        "options": ["Same electoral college as President", "Members of both Houses of Parliament", "Elected members of Parliament only", "Lok Sabha only"],
        "correct_option": 1,
        "explanation": "Vice President is elected by members of an electoral college consisting of both elected and nominated members of both Houses of Parliament.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "Which is NOT a qualification for Vice President?",
        "options": ["Citizen of India", "35 years of age", "Qualified for Rajya Sabha membership", "Qualified for Lok Sabha membership"],
        "correct_option": 3,
        "explanation": "Vice President must be qualified for Rajya Sabha membership (not Lok Sabha), citizen of India, and 35 years of age.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "The term of Vice President is:",
        "options": ["4 years", "5 years", "6 years", "Co-terminus with President"],
        "correct_option": 1,
        "explanation": "Vice President holds office for 5 years, but continues until successor enters office. Term is independent of President's term.",
        "difficulty": "easy",
        "topic": "Vice President"
    },
    {
        "question_text": "Vice President can be removed by:",
        "options": ["Impeachment", "Resolution of Rajya Sabha agreed by Lok Sabha", "No-confidence motion", "President's order"],
        "correct_option": 1,
        "explanation": "Vice President can be removed by resolution of Rajya Sabha passed by majority and agreed to by Lok Sabha. No impeachment needed.",
        "difficulty": "hard",
        "topic": "Vice President"
    },
    {
        "question_text": "Notice for removal of Vice President must be given by:",
        "options": ["At least 1/4th members of Rajya Sabha", "At least 14 days in advance", "Both A and B", "Neither"],
        "correct_option": 2,
        "explanation": "Removal resolution requires 14 days advance notice and can only be moved by Rajya Sabha members.",
        "difficulty": "hard",
        "topic": "Vice President"
    },
    {
        "question_text": "When acting as President, Vice President:",
        "options": ["Continues as Rajya Sabha Chairman", "Ceases to be Rajya Sabha Chairman", "Performs both functions", "Appoints Deputy Chairman as acting Chairman"],
        "correct_option": 1,
        "explanation": "When acting as President, Vice President ceases to perform functions of Rajya Sabha Chairman. Deputy Chairman presides over Rajya Sabha.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "Vice President acting as President is entitled to:",
        "options": ["Same salary as Vice President", "Same salary as President", "Combined salary", "No separate salary"],
        "correct_option": 1,
        "explanation": "When discharging President's functions, Vice President is entitled to emoluments, allowances and privileges of President.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "Who was the first Vice President of India?",
        "options": ["Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Dr. Zakir Hussain", "V.V. Giri"],
        "correct_option": 1,
        "explanation": "Dr. Sarvepalli Radhakrishnan was the first Vice President (1952-1962). He later became President (1962-1967).",
        "difficulty": "easy",
        "topic": "Vice President"
    },
    {
        "question_text": "The salary of Vice President as Chairman of Rajya Sabha is:",
        "options": ["Fixed by Constitution", "Fixed by Parliament by law", "Same as Supreme Court judge", "Decided by President"],
        "correct_option": 1,
        "explanation": "Vice President's salary as Rajya Sabha Chairman is determined by Parliament. Constitution doesn't fix the amount.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "Vice President takes oath before:",
        "options": ["Chief Justice of India", "President of India", "Outgoing Vice President", "Speaker of Lok Sabha"],
        "correct_option": 1,
        "explanation": "Vice President takes oath or affirmation before the President of India or someone appointed by President.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    {
        "question_text": "Election dispute regarding Vice President is decided by:",
        "options": ["Election Commission", "High Court", "Supreme Court", "Parliament"],
        "correct_option": 2,
        "explanation": "Article 71 provides that all doubts and disputes regarding Vice President's election shall be decided by Supreme Court.",
        "difficulty": "medium",
        "topic": "Vice President"
    },
    # ==================== PRIME MINISTER (111-160) ====================
    {
        "question_text": "The Prime Minister is:",
        "options": ["Head of State", "Head of Government", "Both", "Neither"],
        "correct_option": 1,
        "explanation": "Prime Minister is the Head of Government (real executive) while President is the Head of State (nominal executive).",
        "difficulty": "easy",
        "topic": "Prime Minister"
    },
    {
        "question_text": "The Prime Minister is appointed by:",
        "options": ["Elected by Parliament", "Elected by people", "Appointed by President", "Nominated by Lok Sabha Speaker"],
        "correct_option": 2,
        "explanation": "Article 75 provides that Prime Minister is appointed by the President. Usually, the leader of majority party in Lok Sabha is appointed.",
        "difficulty": "easy",
        "topic": "Prime Minister"
    },
    {
        "question_text": "There is no constitutional requirement that PM must be from:",
        "options": ["Lok Sabha only", "Rajya Sabha only", "Either House of Parliament", "All are eligible"],
        "correct_option": 3,
        "explanation": "Constitution doesn't mandate that PM must be from Parliament. However, if not a member, must become one within 6 months.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "If PM is not a member of Parliament, he must become one within:",
        "options": ["3 months", "6 months", "1 year", "No such requirement"],
        "correct_option": 1,
        "explanation": "A non-member appointed as Minister (including PM) must become member of either House within 6 months, else ceases to be Minister.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "Which PM was from Rajya Sabha?",
        "options": ["Jawaharlal Nehru", "Indira Gandhi", "Manmohan Singh", "Atal Bihari Vajpayee"],
        "correct_option": 2,
        "explanation": "Dr. Manmohan Singh was Prime Minister from Rajya Sabha (2004-2014). He was never a Lok Sabha member while being PM.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "PM's salary and allowances are determined by:",
        "options": ["Constitution", "Parliament by law", "President", "Cabinet"],
        "correct_option": 1,
        "explanation": "Parliament determines salary, allowances and privileges of PM and other ministers under Article 75(6).",
        "difficulty": "easy",
        "topic": "Prime Minister"
    },
    {
        "question_text": "The PM communicates to President all decisions of Council of Ministers relating to:",
        "options": ["Administration and legislation", "Appointments", "Foreign policy", "All of the above"],
        "correct_option": 0,
        "explanation": "Under Article 78, PM communicates decisions relating to administration and proposals for legislation. President can seek any information.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "If President so requires, PM shall submit for Cabinet consideration:",
        "options": ["Any matter decided by a minister", "Budget proposals", "Appointments", "Foreign policy decisions"],
        "correct_option": 0,
        "explanation": "Article 78(c) enables President to require PM to submit for Cabinet consideration any matter on which minister has decided but Cabinet hasn't considered.",
        "difficulty": "hard",
        "topic": "Prime Minister"
    },
    {
        "question_text": "The first Prime Minister of India was:",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Dr. Rajendra Prasad"],
        "correct_option": 1,
        "explanation": "Jawaharlal Nehru was the first Prime Minister of India (1947-1964), serving for over 17 years, the longest tenure.",
        "difficulty": "easy",
        "topic": "Prime Minister"
    },
    {
        "question_text": "Who was the first PM to resign after losing confidence motion?",
        "options": ["V.P. Singh", "Morarji Desai", "Charan Singh", "I.K. Gujral"],
        "correct_option": 0,
        "explanation": "V.P. Singh was the first PM to lose and resign after a no-confidence motion in November 1990.",
        "difficulty": "hard",
        "topic": "Prime Minister"
    },
    {
        "question_text": "Who was the shortest serving Prime Minister?",
        "options": ["V.P. Singh", "Charan Singh", "H.D. Deve Gowda", "I.K. Gujral"],
        "correct_option": 1,
        "explanation": "Charan Singh served as PM for only 170 days (1979-80) and never faced Parliament as PM.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "The PM presides over meetings of:",
        "options": ["Cabinet only", "Council of Ministers only", "Both Cabinet and Cabinet Committees", "Parliament"],
        "correct_option": 2,
        "explanation": "PM presides over Cabinet meetings and Cabinet Committee meetings. PM also chairs Planning Commission/NITI Aayog meetings.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "PM is responsible to:",
        "options": ["President", "Lok Sabha", "Parliament", "People"],
        "correct_option": 1,
        "explanation": "Council of Ministers including PM is collectively responsible to Lok Sabha (Article 75). PM must maintain confidence of Lok Sabha.",
        "difficulty": "easy",
        "topic": "Prime Minister"
    },
    {
        "question_text": "PM allocates portfolios among ministers on whose behalf?",
        "options": ["His own authority", "On behalf of President", "On behalf of Parliament", "On behalf of Cabinet"],
        "correct_option": 1,
        "explanation": "PM advises President on allocation and reshuffling of portfolios among ministers. President makes allocation on PM's advice.",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    {
        "question_text": "PM can recommend to President to dismiss:",
        "options": ["Only Cabinet ministers", "Any minister", "Chief Justice", "Governors only"],
        "correct_option": 1,
        "explanation": "PM can recommend dismissal of any minister to President. This makes PM 'first among equals' (primus inter pares).",
        "difficulty": "medium",
        "topic": "Prime Minister"
    },
    # ==================== COUNCIL OF MINISTERS (161-210) ====================
    {
        "question_text": "Council of Ministers consists of:",
        "options": ["Cabinet Ministers only", "Cabinet and State Ministers only", "Cabinet, State and Deputy Ministers", "All MPs supporting government"],
        "correct_option": 2,
        "explanation": "Council of Ministers has three categories: Cabinet Ministers, Ministers of State (independent or attached), and Deputy Ministers.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The maximum size of Council of Ministers is limited to:",
        "options": ["10% of Lok Sabha strength", "15% of Lok Sabha strength", "20% of Lok Sabha strength", "No limit"],
        "correct_option": 1,
        "explanation": "91st Amendment (2003) limits Council of Ministers to 15% of total strength of Lok Sabha (i.e., maximum 81 ministers).",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The 15% limit on Council of Ministers was introduced by:",
        "options": ["42nd Amendment", "73rd Amendment", "91st Amendment", "97th Amendment"],
        "correct_option": 2,
        "explanation": "91st Amendment (2003) introduced Article 75(1A) limiting Council of Ministers to 15% of Lok Sabha strength.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Ministers are individually responsible to:",
        "options": ["President", "Prime Minister", "Lok Sabha", "Parliament"],
        "correct_option": 0,
        "explanation": "Ministers hold office during pleasure of President (Article 75). They are individually responsible to President and collectively to Lok Sabha.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Collective responsibility of Council of Ministers is to:",
        "options": ["President", "Prime Minister", "Lok Sabha", "Both Houses of Parliament"],
        "correct_option": 2,
        "explanation": "Article 75(3) provides that Council of Ministers is collectively responsible to Lok Sabha, not Rajya Sabha or President.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The doctrine of collective responsibility means:",
        "options": ["All ministers think alike", "Cabinet decisions bind all ministers", "All ministers must resign together", "Both B and C"],
        "correct_option": 3,
        "explanation": "Collective responsibility means Cabinet decisions bind all ministers who must defend them publicly, and vote of no-confidence requires all to resign.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Who administers oath to ministers?",
        "options": ["Prime Minister", "Chief Justice", "President", "Speaker"],
        "correct_option": 2,
        "explanation": "President administers oath of office and secrecy to all ministers. The oath is in Third Schedule of Constitution.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Cabinet is:",
        "options": ["Mentioned in Constitution originally", "Added by amendment", "Non-constitutional body", "Statutory body"],
        "correct_option": 0,
        "explanation": "Cabinet is mentioned in Article 352 originally. 44th Amendment inserted Article 352(3) specifically mentioning Cabinet.",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The term 'Kitchen Cabinet' refers to:",
        "options": ["Food Ministry", "PM's close informal advisors", "Cabinet sub-committee", "All cabinet ministers"],
        "correct_option": 1,
        "explanation": "Kitchen Cabinet refers to PM's inner circle of unofficial advisors who may be more influential than formal Cabinet members.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Cabinet Secretary is:",
        "options": ["A Cabinet Minister", "A constitutional authority", "Senior-most civil servant", "Secretary to PM only"],
        "correct_option": 2,
        "explanation": "Cabinet Secretary is senior-most civil servant (IAS officer), head of civil services, secretary to Cabinet and coordinates ministries.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Which is NOT a Cabinet Committee?",
        "options": ["Cabinet Committee on Security", "Cabinet Committee on Economic Affairs", "Cabinet Committee on Political Affairs", "Cabinet Committee on Administration"],
        "correct_option": 3,
        "explanation": "Key Cabinet Committees include CCS, CCEA, ACC, CCPA. Cabinet Committee on Administration is not a standard standing committee.",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Appointment Committee of Cabinet (ACC) is headed by:",
        "options": ["Home Minister", "Cabinet Secretary", "Prime Minister", "President"],
        "correct_option": 2,
        "explanation": "ACC is headed by PM and decides appointments to top posts in civil services, public enterprises, and related matters.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "A person can remain minister without being MP for maximum:",
        "options": ["3 months", "6 months", "1 year", "No limit"],
        "correct_option": 1,
        "explanation": "Article 75(5) provides that a minister who is not member of either House for 6 consecutive months ceases to be minister.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "A member of one House can speak in the other House:",
        "options": ["Only if he is a minister", "Any MP can", "Only with Speaker's permission", "Not allowed"],
        "correct_option": 0,
        "explanation": "Under Article 88, ministers can speak in either House and participate in proceedings but can vote only in the House of which they are members.",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Shadow Cabinet exists in:",
        "options": ["India", "UK", "USA", "Both A and B"],
        "correct_option": 1,
        "explanation": "Shadow Cabinet (opposition cabinet to scrutinize government) is a feature of UK. India doesn't have formal shadow cabinet system.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Minister of State (Independent Charge) means:",
        "options": ["A Cabinet Minister", "State Minister heading a ministry independently", "Deputy Minister", "Parliamentary Secretary"],
        "correct_option": 1,
        "explanation": "Minister of State (Independent Charge) heads a ministry independently without a Cabinet Minister above them, though not Cabinet rank.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "No-confidence motion can be moved in:",
        "options": ["Lok Sabha only", "Rajya Sabha only", "Either House", "Joint sitting only"],
        "correct_option": 0,
        "explanation": "No-confidence motion can be moved only in Lok Sabha since Council of Ministers is collectively responsible to Lok Sabha.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Minimum members needed to introduce no-confidence motion is:",
        "options": ["25", "50", "75", "100"],
        "correct_option": 1,
        "explanation": "At least 50 members must support admitting a no-confidence motion in Lok Sabha under Rules of Procedure.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Cut motions can be moved during:",
        "options": ["Budget discussion", "President's Address", "Question Hour", "Zero Hour"],
        "correct_option": 0,
        "explanation": "Cut motions (Policy cut, Economy cut, Token cut) can be moved during discussion on Demands for Grants in budget session.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Censure motion differs from no-confidence motion as:",
        "options": ["It needs reasons", "It can be against individual minister", "Both A and B", "There is no difference"],
        "correct_option": 2,
        "explanation": "Censure motion must state reasons, can be against individual minister or Council, doesn't require government to resign if passed.",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Which of the following strengthens PM's position?",
        "options": ["Coalition government", "Single party majority", "Minority government", "Caretaker government"],
        "correct_option": 1,
        "explanation": "Single party majority in Lok Sabha strengthens PM as they don't need allies' support. Coalition weakens PM's authority.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The concept of 'collective responsibility' is borrowed from:",
        "options": ["USA", "UK", "Canada", "Australia"],
        "correct_option": 1,
        "explanation": "India borrowed cabinet system including collective responsibility from British Westminster model of parliamentary democracy.",
        "difficulty": "easy",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Anti-Defection Law disqualifies a minister if:",
        "options": ["They switch parties", "They vote against party whip", "They abstain from voting", "All of the above"],
        "correct_option": 3,
        "explanation": "Under 10th Schedule, voting against party direction, abstaining despite direction, or voluntarily giving up membership leads to disqualification.",
        "difficulty": "medium",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "The 91st Amendment (2003) also mandated:",
        "options": ["Ministers must be MPs", "Disqualified members cannot be ministers", "Both A and B", "Neither"],
        "correct_option": 1,
        "explanation": "91st Amendment added that members disqualified under 10th Schedule cannot be appointed as ministers (Article 75(1B)).",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
    {
        "question_text": "Parliamentary Secretary is:",
        "options": ["A constitutional post", "Appointed by PM to assist ministers", "Senior to Deputy Minister", "Same as Minister of State"],
        "correct_option": 1,
        "explanation": "Parliamentary Secretaries are non-constitutional, appointed by CM/PM to assist ministers. 91st Amendment discouraged this practice.",
        "difficulty": "hard",
        "topic": "Council of Ministers"
    },
]
