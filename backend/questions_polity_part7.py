"""
OPSC Questions Database - Polity (Part 7 of 10)
State Government - Governor, Chief Minister, State Legislature, State Council of Ministers
Questions 1061-1320 (Unique, Non-Repeating)
"""

POLITY_QUESTIONS_PART7 = [
    # ==================== GOVERNOR (1-70) ====================
    {
        "question_text": "The Governor of a State is appointed by:",
        "options": ["Elected by people", "Elected by State Legislature", "Appointed by President", "Nominated by Chief Minister"],
        "correct_option": 2,
        "explanation": "Article 155 provides that Governor is appointed by President by warrant under his hand and seal.",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Governor holds office:",
        "options": ["For 5 years", "During pleasure of President", "During pleasure of State Legislature", "Both A and B"],
        "correct_option": 3,
        "explanation": "Article 156 provides Governor holds office for 5 years but serves during pleasure of President who can remove anytime.",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Minimum age to be appointed Governor is:",
        "options": ["25 years", "30 years", "35 years", "40 years"],
        "correct_option": 2,
        "explanation": "Article 157 prescribes minimum age of 35 years for appointment as Governor.",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Which is NOT a qualification for Governor?",
        "options": ["Citizen of India", "35 years of age", "Not holding office of profit", "Resident of the state"],
        "correct_option": 3,
        "explanation": "Constitution doesn't require Governor to be resident of the state. But convention is to appoint outsider.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "A person can be Governor of:",
        "options": ["One state only", "Two states", "Two or more states", "All states simultaneously"],
        "correct_option": 2,
        "explanation": "Article 153 allows same person to be Governor of two or more states. This has been done in practice.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's oath is administered by:",
        "options": ["President", "Chief Minister", "Chief Justice of High Court", "Speaker of State Assembly"],
        "correct_option": 2,
        "explanation": "Article 159 provides Governor takes oath before Chief Justice of High Court (or senior-most judge).",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Governor can be removed by:",
        "options": ["Impeachment", "President at will", "State Legislature resolution", "Chief Minister's advice"],
        "correct_option": 1,
        "explanation": "Governor holds office during pleasure of President. No impeachment needed. President can remove without assigning reasons.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "In B.P. Singhal case (2010), Supreme Court held that:",
        "options": ["Governor's removal is unreviewable", "Removal must be for valid reasons", "Governor has fixed tenure", "Only PM can remove Governor"],
        "correct_option": 1,
        "explanation": "SC held that though grounds need not be communicated, removal cannot be arbitrary and should have valid reasons.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's emoluments are charged on:",
        "options": ["Consolidated Fund of India", "Consolidated Fund of State", "Both funds equally", "Contingency Fund"],
        "correct_option": 1,
        "explanation": "Governor's emoluments are charged on Consolidated Fund of the State concerned.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's discretionary powers include:",
        "options": ["Appointing CM when no clear majority", "Reserving bills for President", "Dissolving assembly", "All of the above"],
        "correct_option": 3,
        "explanation": "Governor exercises discretion in appointing CM when no party has majority, reserving bills, recommending President's rule, etc.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "When must Governor act in discretion?",
        "options": ["When Constitution says so", "When directed by President", "When advised by CM", "Both A and B"],
        "correct_option": 3,
        "explanation": "Governor exercises discretion when Constitution expressly requires it or when President directs (like in certain tribal areas).",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's ordinance making power is under:",
        "options": ["Article 123", "Article 213", "Article 214", "Article 356"],
        "correct_option": 1,
        "explanation": "Article 213 empowers Governor to promulgate ordinances when State Legislature is not in session.",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's ordinance requires President's prior instruction for matters relating to:",
        "options": ["High Court", "Money Bills", "Matters requiring President's assent", "All of the above"],
        "correct_option": 2,
        "explanation": "Article 213(1) requires President's prior instructions for ordinances on matters for which Governor would have reserved bill for President.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Governor can reserve a bill for President's consideration under:",
        "options": ["Article 200", "Article 201", "Article 213", "Article 356"],
        "correct_option": 0,
        "explanation": "Article 200 empowers Governor to reserve a bill for President's consideration instead of giving assent.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "When bill is reserved for President, President can:",
        "options": ["Assent or withhold", "Assent, withhold or return to Governor", "Return to State Legislature", "All of the above"],
        "correct_option": 0,
        "explanation": "Article 201 provides President can assent, withhold assent, or direct Governor to return to Legislature. But President cannot return directly.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Governor's pardoning power is under:",
        "options": ["Article 72", "Article 161", "Article 162", "Article 163"],
        "correct_option": 1,
        "explanation": "Article 161 gives Governor power to grant pardons, reprieves, respites, remission in state law matters.",
        "difficulty": "easy",
        "topic": "Governor"
    },
    {
        "question_text": "Governor CANNOT pardon:",
        "options": ["State law sentences", "Court martial sentences", "Death sentence", "Both B and C"],
        "correct_option": 3,
        "explanation": "Governor cannot pardon death sentence or court martial sentence. Only President can pardon these under Article 72.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Governor is Chancellor of:",
        "options": ["All universities in state", "State universities", "Central universities in state", "Private universities"],
        "correct_option": 1,
        "explanation": "Governor is Chancellor of state universities by virtue of respective State University Acts, not Constitution.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "Governor addresses State Legislature:",
        "options": ["At every session", "At first session each year", "Only budget session", "When CM advises"],
        "correct_option": 1,
        "explanation": "Article 176 provides Governor addresses first session each year and first session after each general election.",
        "difficulty": "medium",
        "topic": "Governor"
    },
    {
        "question_text": "Governor nominates to Legislative Council:",
        "options": ["6 members", "1/12th of total members", "12 members", "1/6th of total members"],
        "correct_option": 3,
        "explanation": "Article 171(3)(e) provides Governor nominates 1/6th of total Legislative Council strength from literature, science, art, co-operative, social service fields.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "The Sarkaria Commission on Governor recommended:",
        "options": ["Abolish the post", "Elected Governor", "Eminent persons should be appointed", "Remove discretionary powers"],
        "correct_option": 2,
        "explanation": "Sarkaria Commission (1988) recommended that eminent persons detached from local politics should be appointed as Governors.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    {
        "question_text": "Punchhi Commission on Governor recommended:",
        "options": ["Fixed 5-year tenure", "Removal only by State Legislature", "Deletion of pleasure doctrine", "Governor should resign with change of Central government"],
        "correct_option": 2,
        "explanation": "Punchhi Commission recommended deletion of pleasure doctrine and fixed tenure to ensure Governor's independence.",
        "difficulty": "hard",
        "topic": "Governor"
    },
    # ==================== CHIEF MINISTER (71-110) ====================
    {
        "question_text": "Chief Minister is appointed by:",
        "options": ["President", "Governor", "State Legislature", "Elected directly"],
        "correct_option": 1,
        "explanation": "Article 164 provides Chief Minister is appointed by Governor. Usually leader of majority party is appointed.",
        "difficulty": "easy",
        "topic": "Chief Minister"
    },
    {
        "question_text": "CM must be member of:",
        "options": ["Legislative Assembly only", "Legislative Council only", "Either House", "No such requirement"],
        "correct_option": 2,
        "explanation": "CM can be from either LA or LC. But if not member of any House, must become member within 6 months.",
        "difficulty": "medium",
        "topic": "Chief Minister"
    },
    {
        "question_text": "Term of Chief Minister is:",
        "options": ["5 years", "Co-terminus with Assembly", "During pleasure of Governor", "Fixed 5 years"],
        "correct_option": 2,
        "explanation": "Article 164(1) provides CM holds office during pleasure of Governor. Practically depends on Assembly confidence.",
        "difficulty": "medium",
        "topic": "Chief Minister"
    },
    {
        "question_text": "CM's salary is determined by:",
        "options": ["Constitution", "Parliament", "State Legislature", "Governor"],
        "correct_option": 2,
        "explanation": "State Legislature determines salaries and allowances of CM and other ministers.",
        "difficulty": "easy",
        "topic": "Chief Minister"
    },
    {
        "question_text": "CM's duty to communicate Cabinet decisions to Governor is under:",
        "options": ["Article 163", "Article 164", "Article 166", "Article 167"],
        "correct_option": 3,
        "explanation": "Article 167 provides CM's duties: communicate Cabinet decisions, furnish information requested by Governor, submit matters for Cabinet.",
        "difficulty": "medium",
        "topic": "Chief Minister"
    },
    {
        "question_text": "Which state had first non-Congress CM after independence?",
        "options": ["Kerala", "Odisha", "Tamil Nadu", "West Bengal"],
        "correct_option": 0,
        "explanation": "Kerala had first non-Congress CM when E.M.S. Namboodiripad (Communist) became CM in 1957.",
        "difficulty": "medium",
        "topic": "Chief Minister"
    },
    {
        "question_text": "Longest serving CM in Indian history is:",
        "options": ["Jyoti Basu", "Pawan Kumar Chamling", "Naveen Patnaik", "Bhupesh Baghel"],
        "correct_option": 1,
        "explanation": "Pawan Kumar Chamling of Sikkim served as CM for about 24 years (1994-2019), longest in Indian history.",
        "difficulty": "hard",
        "topic": "Chief Minister"
    },
    {
        "question_text": "CM recommends to Governor regarding:",
        "options": ["Appointment of ministers", "Allocation of portfolios", "Dismissal of ministers", "All of the above"],
        "correct_option": 3,
        "explanation": "CM advises Governor on appointment, portfolio allocation, reshuffling, and dismissal of ministers.",
        "difficulty": "easy",
        "topic": "Chief Minister"
    },
    {
        "question_text": "Can CM from Legislative Council face no-confidence motion?",
        "options": ["Yes, in Assembly", "Yes, in Council", "No, as not Assembly member", "Only if Assembly so decides"],
        "correct_option": 0,
        "explanation": "No-confidence motion is in Assembly regardless of which House CM belongs to, as Council of Ministers is responsible to Assembly.",
        "difficulty": "hard",
        "topic": "Chief Minister"
    },
    {
        "question_text": "First woman Chief Minister in India was:",
        "options": ["Indira Gandhi", "Sucheta Kripalani", "Jayalalithaa", "Mayawati"],
        "correct_option": 1,
        "explanation": "Sucheta Kripalani became first woman CM of Uttar Pradesh in 1963.",
        "difficulty": "easy",
        "topic": "Chief Minister"
    },
    # ==================== STATE LEGISLATURE (111-180) ====================
    {
        "question_text": "States with bicameral legislature currently are:",
        "options": ["4 states", "5 states", "6 states", "7 states"],
        "correct_option": 2,
        "explanation": "Currently 6 states have bicameral legislature: Andhra Pradesh, Bihar, Karnataka, Maharashtra, Telangana, Uttar Pradesh.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Legislative Council can be created or abolished by:",
        "options": ["State Legislature alone", "Parliament alone", "Parliament on state resolution", "President"],
        "correct_option": 2,
        "explanation": "Article 169 provides Parliament can create/abolish LC if State LA passes resolution by special majority.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Maximum strength of Legislative Assembly is:",
        "options": ["400", "450", "500", "550"],
        "correct_option": 2,
        "explanation": "Article 170 provides maximum LA strength of 500 and minimum of 60 (except small states).",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Legislative Council strength should not exceed:",
        "options": ["1/4th of LA", "1/3rd of LA", "1/2 of LA", "Equal to LA"],
        "correct_option": 1,
        "explanation": "Article 171 provides LC strength not more than 1/3rd of LA strength and not less than 40.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "How are LC members elected?",
        "options": ["Direct election", "Indirect election", "Mixed election", "All nominated"],
        "correct_option": 2,
        "explanation": "LC members are elected by MLAs, local bodies, graduates, teachers (indirect) and nominated by Governor. Mixed method.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Tenure of LC member is:",
        "options": ["4 years", "5 years", "6 years", "Permanent"],
        "correct_option": 2,
        "explanation": "LC member serves for 6 years with 1/3rd retiring every 2 years, like Rajya Sabha.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "Minimum age for LA membership is:",
        "options": ["21 years", "25 years", "30 years", "35 years"],
        "correct_option": 1,
        "explanation": "Minimum age for Legislative Assembly is 25 years (same as Lok Sabha).",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "Minimum age for LC membership is:",
        "options": ["25 years", "30 years", "35 years", "40 years"],
        "correct_option": 1,
        "explanation": "Minimum age for Legislative Council is 30 years (same as Rajya Sabha).",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "Speaker of LA is elected by:",
        "options": ["Governor", "Chief Minister", "Members of LA", "All MLAs and MLCs"],
        "correct_option": 2,
        "explanation": "Speaker is elected by members of Legislative Assembly from among themselves.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "Chairman of LC is elected by:",
        "options": ["Governor", "LC members", "LA members", "Both LA and LC members"],
        "correct_option": 1,
        "explanation": "Unlike Rajya Sabha (VP is Chairman), Legislative Council elects its Chairman from among members.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Money Bill in state can be introduced only in:",
        "options": ["LA only", "LC only", "Either House", "Joint sitting"],
        "correct_option": 0,
        "explanation": "Like Parliament, State Money Bills can only be introduced in Legislative Assembly.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "LC can delay Money Bill for maximum:",
        "options": ["7 days", "14 days", "30 days", "Cannot delay"],
        "correct_option": 1,
        "explanation": "Article 198 provides LC must return Money Bill within 14 days. If not, deemed passed.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Can there be joint sitting of LA and LC?",
        "options": ["Yes, like Parliament", "No, not provided", "Only for deadlock", "Governor's discretion"],
        "correct_option": 1,
        "explanation": "No provision for joint sitting of State Legislature. If deadlock on ordinary bill, LA prevails eventually.",
        "difficulty": "hard",
        "topic": "State Legislature"
    },
    {
        "question_text": "Quorum in State Legislature is:",
        "options": ["1/5th", "1/10th", "1/3rd", "Majority"],
        "correct_option": 1,
        "explanation": "Article 189 provides quorum of 10 members or 1/10th of total, whichever is greater.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Gap between two sessions of State Legislature should not exceed:",
        "options": ["3 months", "6 months", "9 months", "1 year"],
        "correct_option": 1,
        "explanation": "Article 174 mandates that gap between sessions should not exceed 6 months.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Who decides whether state bill is Money Bill?",
        "options": ["Governor", "Chief Minister", "Speaker of LA", "Finance Minister"],
        "correct_option": 2,
        "explanation": "Speaker of Legislative Assembly certifies whether a bill is Money Bill and decision is final.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "LA can be dissolved by:",
        "options": ["President", "Governor", "Chief Minister", "Speaker"],
        "correct_option": 1,
        "explanation": "Article 174 empowers Governor to dissolve LA, usually on CM's advice but can be discretionary.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "During President's rule, state legislative powers are with:",
        "options": ["Governor", "President", "Parliament", "Union Cabinet"],
        "correct_option": 2,
        "explanation": "Under Article 357, Parliament exercises state legislative powers during President's rule.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    {
        "question_text": "Advocate General of State is appointed by:",
        "options": ["Chief Minister", "Governor", "President", "State Bar Council"],
        "correct_option": 1,
        "explanation": "Article 165 provides Governor appoints Advocate General who must be qualified for High Court judge.",
        "difficulty": "easy",
        "topic": "State Legislature"
    },
    {
        "question_text": "Advocate General holds office:",
        "options": ["For 5 years", "During Governor's pleasure", "Till age 65", "Co-terminus with government"],
        "correct_option": 1,
        "explanation": "Advocate General holds office during pleasure of Governor. Usually changes with change of government.",
        "difficulty": "medium",
        "topic": "State Legislature"
    },
    # ==================== STATE COUNCIL OF MINISTERS (181-210) ====================
    {
        "question_text": "State Council of Ministers is collectively responsible to:",
        "options": ["Governor", "Legislative Assembly", "Legislative Council", "Both Houses"],
        "correct_option": 1,
        "explanation": "Article 164(2) provides Council of Ministers is collectively responsible to Legislative Assembly.",
        "difficulty": "easy",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "Size of State Council of Ministers is limited to:",
        "options": ["10% of LA", "15% of LA", "20% of LA", "No limit"],
        "correct_option": 1,
        "explanation": "91st Amendment (2003) limits State Council of Ministers to 15% of LA strength (minimum 12).",
        "difficulty": "medium",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "In states with small assemblies, minimum Council size is:",
        "options": ["6", "10", "12", "15"],
        "correct_option": 2,
        "explanation": "Even if 15% works out to less, minimum Council of Ministers strength is 12 members.",
        "difficulty": "hard",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "State ministers take oath before:",
        "options": ["Chief Minister", "Speaker", "Governor", "Chief Justice of HC"],
        "correct_option": 2,
        "explanation": "Governor administers oath of office and secrecy to state ministers as per Third Schedule.",
        "difficulty": "easy",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "A minister not member of either House must become member within:",
        "options": ["3 months", "6 months", "1 year", "Before next session"],
        "correct_option": 1,
        "explanation": "Article 164(4) requires minister to become member of Legislature within 6 consecutive months.",
        "difficulty": "easy",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "Can LC member be Chief Minister?",
        "options": ["Yes", "No", "Only temporarily", "Only in bicameral states"],
        "correct_option": 0,
        "explanation": "CM can be from either House. But if from LC, still accountable to LA through collective responsibility.",
        "difficulty": "medium",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "State Cabinet is headed by:",
        "options": ["Governor", "Chief Minister", "Cabinet Secretary", "Chief Secretary"],
        "correct_option": 1,
        "explanation": "Chief Minister heads the State Cabinet and presides over Cabinet meetings.",
        "difficulty": "easy",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "Chief Secretary is:",
        "options": ["Constitutional authority", "Administrative head of state", "Elected official", "Appointed by CM"],
        "correct_option": 1,
        "explanation": "Chief Secretary is senior-most IAS officer in state, administrative head, not a constitutional authority.",
        "difficulty": "medium",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "Parliamentary Secretary in states is:",
        "options": ["Constitutional post", "Statutory post", "Non-constitutional post", "Deputy to minister"],
        "correct_option": 2,
        "explanation": "Parliamentary Secretaries are not constitutional. 91st Amendment discourages them by capping Council size.",
        "difficulty": "hard",
        "topic": "State Council of Ministers"
    },
    {
        "question_text": "Disqualified MLAs cannot be ministers for:",
        "options": ["5 years", "During disqualification period", "Forever", "Till next election"],
        "correct_option": 1,
        "explanation": "91st Amendment prohibits disqualified members from being appointed ministers during disqualification period.",
        "difficulty": "hard",
        "topic": "State Council of Ministers"
    },
]
