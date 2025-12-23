"""
OPSC Questions Database - Polity
High-quality, OPSC-level questions based on actual exam patterns
"""

POLITY_QUESTIONS = [
    # Constitution Basics - Multi-statement format
    {
        "question_text": "Consider the following statements regarding the Preamble of the Indian Constitution:\n(1) The Preamble was adopted on 26th November, 1949\n(2) The words 'Socialist' and 'Secular' were added by the 42nd Amendment\n(3) The Preamble is not justiciable in a court of law\n(4) The Preamble is a part of the Constitution\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "2, 3 and 4 only", "1, 2 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The Preamble was adopted on 26th November 1949, 'Socialist' and 'Secular' were added by 42nd Amendment (1976), the Preamble is not justiciable (Berubari case), and it is part of the Constitution (Kesavananda Bharati case).",
        "difficulty": "hard",
        "topic": "Indian Constitution - Preamble"
    },
    {
        "question_text": "Which of the following is NOT a feature borrowed from the British Constitution for the Indian Constitution?",
        "options": ["Parliamentary form of government", "Rule of Law", "Bicameralism", "Judicial Review"],
        "correct_option": 3,
        "explanation": "Judicial Review was borrowed from the USA, not Britain. Parliamentary government, Rule of Law, and Bicameralism were borrowed from Britain.",
        "difficulty": "medium",
        "topic": "Indian Constitution - Sources"
    },
    {
        "question_text": "Consider the following pairs:\n\nConstitutional Provision : Source Country\n(1) Fundamental Duties : USSR\n(2) Directive Principles : Ireland\n(3) Concurrent List : Australia\n(4) Procedure for Amendment : South Africa\n\nWhich of the above pairs are correctly matched?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. Fundamental Duties from USSR (added by 42nd Amendment), DPSPs from Ireland, Concurrent List from Australia, and Amendment procedure from South Africa.",
        "difficulty": "hard",
        "topic": "Indian Constitution - Sources"
    },
    {
        "question_text": "Article 13 of the Constitution deals with:",
        "options": ["Laws inconsistent with Fundamental Rights", "Right to Equality", "Protection against arrest and detention", "Right to Constitutional Remedies"],
        "correct_option": 0,
        "explanation": "Article 13 declares that all laws inconsistent with or in derogation of Fundamental Rights shall be void. It is the basis of judicial review of laws.",
        "difficulty": "medium",
        "topic": "Fundamental Rights"
    },
    {
        "question_text": "Consider the following statements about Article 14:\n(1) It guarantees equality before law\n(2) It guarantees equal protection of laws\n(3) The concept of 'equality before law' is of British origin\n(4) The concept of 'equal protection of laws' is of American origin\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "1, 2 and 3 only", "1, 2 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Article 14 guarantees both equality before law (British concept) and equal protection of laws (American concept).",
        "difficulty": "medium",
        "topic": "Fundamental Rights - Right to Equality"
    },
    {
        "question_text": "Which of the following Fundamental Rights is available ONLY to citizens and NOT to foreigners?",
        "options": ["Right to Life and Personal Liberty", "Protection against Double Jeopardy", "Freedom of speech and expression", "Right to freedom of religion"],
        "correct_option": 2,
        "explanation": "Article 19 (including freedom of speech) is available only to citizens. Articles 20, 21, and 25 are available to all persons including foreigners.",
        "difficulty": "medium",
        "topic": "Fundamental Rights"
    },
    {
        "question_text": "The 'Right to Privacy' was declared a Fundamental Right under Article 21 by the Supreme Court in:",
        "options": ["Maneka Gandhi case (1978)", "Vishakha case (1997)", "K.S. Puttaswamy case (2017)", "Navtej Singh Johar case (2018)"],
        "correct_option": 2,
        "explanation": "In Justice K.S. Puttaswamy (Retd.) vs Union of India (2017), a nine-judge bench unanimously declared Right to Privacy as a fundamental right under Article 21.",
        "difficulty": "medium",
        "topic": "Fundamental Rights - Article 21"
    },
    {
        "question_text": "Consider the following statements regarding Preventive Detention:\n(1) It is provided under Article 22 of the Constitution\n(2) Maximum period of detention without Advisory Board is 3 months\n(3) Grounds of detention must be communicated to the detenue\n(4) The right to consult a lawyer is allowed from the moment of arrest\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. However, under preventive detention (Article 22(3)), the right to consult a lawyer is NOT available from the moment of arrest.",
        "difficulty": "hard",
        "topic": "Fundamental Rights - Article 22"
    },
    {
        "question_text": "The Right to Education (Article 21A) provides free and compulsory education for children in the age group of:",
        "options": ["5-14 years", "6-14 years", "6-16 years", "5-16 years"],
        "correct_option": 1,
        "explanation": "Article 21A, inserted by the 86th Amendment (2002), provides free and compulsory education for children between 6-14 years of age.",
        "difficulty": "easy",
        "topic": "Fundamental Rights - Right to Education"
    },
    {
        "question_text": "Which of the following writs can be issued ONLY against a public authority and NOT against a private individual?",
        "options": ["Habeas Corpus", "Mandamus", "Certiorari", "Both B and C"],
        "correct_option": 3,
        "explanation": "Both Mandamus and Certiorari can only be issued against public authorities. Habeas Corpus can be issued against both public authorities and private individuals.",
        "difficulty": "medium",
        "topic": "Fundamental Rights - Writs"
    },
    {
        "question_text": "Assertion (A): Directive Principles are not enforceable by courts.\nReason (R): They are fundamental in governance and it is the duty of the State to apply them in making laws.\n\nSelect the correct answer:",
        "options": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
        "correct_option": 1,
        "explanation": "Both statements are true but R does not explain why DPSPs are non-justiciable. The non-justiciability is because they require resources and positive action by the State.",
        "difficulty": "hard",
        "topic": "Directive Principles"
    },
    {
        "question_text": "Consider the following Directive Principles:\n(1) Uniform Civil Code - Article 44\n(2) Prohibition of Cow Slaughter - Article 48\n(3) Separation of Judiciary from Executive - Article 50\n(4) Protection of Monuments - Article 49\n\nWhich of the above are correctly matched?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All pairs are correctly matched. Article 44 (UCC), Article 48 (Cow slaughter), Article 50 (Separation of Judiciary), Article 49 (Protection of monuments).",
        "difficulty": "medium",
        "topic": "Directive Principles"
    },
    {
        "question_text": "The Fundamental Duties were added to the Constitution by which Amendment?",
        "options": ["42nd Amendment (1976)", "44th Amendment (1978)", "86th Amendment (2002)", "97th Amendment (2011)"],
        "correct_option": 0,
        "explanation": "Fundamental Duties were added by the 42nd Amendment (1976) on the recommendation of the Swaran Singh Committee.",
        "difficulty": "easy",
        "topic": "Fundamental Duties"
    },
    {
        "question_text": "Which Fundamental Duty was added by the 86th Constitutional Amendment Act, 2002?",
        "options": ["To protect and improve the natural environment", "To develop scientific temper", "To provide opportunities for education to child between 6-14 years", "To safeguard public property"],
        "correct_option": 2,
        "explanation": "The 86th Amendment (2002) added Article 51A(k) - duty of parents/guardians to provide opportunities for education to children between 6-14 years.",
        "difficulty": "medium",
        "topic": "Fundamental Duties"
    },
    {
        "question_text": "Consider the following statements about the President of India:\n(1) The President must be a citizen of India\n(2) The President must have completed 35 years of age\n(3) The President must be qualified to be a member of the Lok Sabha\n(4) The President holds office for a term of 5 years from the date of assuming office\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct as per Article 58 (qualifications) and Article 56 (term of office).",
        "difficulty": "medium",
        "topic": "Union Executive - President"
    },
    {
        "question_text": "Which of the following is NOT a discretionary power of the President?",
        "options": ["Appointment of Prime Minister when no party has clear majority", "Dissolution of Lok Sabha", "Appointment of Judges", "Return of a bill for reconsideration"],
        "correct_option": 2,
        "explanation": "Appointment of Judges is done on the advice of the Collegium (after NJAC was struck down), not at President's discretion. Other options involve situational discretion.",
        "difficulty": "hard",
        "topic": "Union Executive - President"
    },
    {
        "question_text": "The President's rule in a state can be imposed under Article 356 for a maximum period of:",
        "options": ["6 months", "1 year", "2 years", "3 years"],
        "correct_option": 3,
        "explanation": "President's Rule under Article 356 can be extended up to a maximum of 3 years with Parliamentary approval every 6 months, subject to conditions in Article 356(5).",
        "difficulty": "medium",
        "topic": "Emergency Provisions"
    },
    {
        "question_text": "Consider the following statements about the Vice-President of India:\n(1) He is elected by an electoral college consisting of members of both Houses of Parliament\n(2) He is the ex-officio Chairman of the Rajya Sabha\n(3) He can be removed by a resolution passed by effective majority of Rajya Sabha\n(4) He must be qualified to be a member of the Rajya Sabha\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "1, 2 and 4 only", "1, 2 and 3 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The VP is elected by MPs of both Houses, is ex-officio Chairman of RS, can be removed by effective majority of RS, and must be qualified to be RS member.",
        "difficulty": "hard",
        "topic": "Union Executive - Vice President"
    },
    {
        "question_text": "Which Article of the Constitution deals with the appointment of the Prime Minister?",
        "options": ["Article 74", "Article 75", "Article 76", "Article 77"],
        "correct_option": 1,
        "explanation": "Article 75 deals with appointment of Prime Minister and other Ministers. Article 74 deals with Council of Ministers to aid and advise President.",
        "difficulty": "easy",
        "topic": "Union Executive - Prime Minister"
    },
    {
        "question_text": "The Council of Ministers is collectively responsible to:",
        "options": ["The President", "The Lok Sabha", "The Rajya Sabha", "Both Houses of Parliament"],
        "correct_option": 1,
        "explanation": "Under Article 75(3), the Council of Ministers is collectively responsible to the Lok Sabha, not the President or Rajya Sabha.",
        "difficulty": "easy",
        "topic": "Union Executive - Council of Ministers"
    },
    {
        "question_text": "Which of the following is NOT a Parliamentary Committee?",
        "options": ["Public Accounts Committee", "Estimates Committee", "Committee on Public Undertakings", "Finance Commission"],
        "correct_option": 3,
        "explanation": "Finance Commission is a Constitutional body under Article 280, not a Parliamentary Committee. The other three are financial committees of Parliament.",
        "difficulty": "medium",
        "topic": "Parliament - Committees"
    },
    {
        "question_text": "Consider the following statements about Money Bills:\n(1) A Money Bill can be introduced only in the Lok Sabha\n(2) The Speaker certifies whether a bill is a Money Bill\n(3) Rajya Sabha can suggest amendments but cannot reject it\n(4) Rajya Sabha must return it within 14 days\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct as per Articles 109 and 110. Money Bills can only be introduced in LS, certified by Speaker, RS can only suggest amendments, and must return within 14 days.",
        "difficulty": "hard",
        "topic": "Parliament - Money Bills"
    },
    {
        "question_text": "A joint sitting of both Houses of Parliament can be called for:",
        "options": ["Ordinary bills only", "Money bills only", "Constitutional Amendment bills only", "Both ordinary and Money bills"],
        "correct_option": 0,
        "explanation": "Joint sitting under Article 108 can only be called for ordinary bills where there is a deadlock. It cannot be called for Money Bills or Constitutional Amendment Bills.",
        "difficulty": "medium",
        "topic": "Parliament - Joint Sitting"
    },
    {
        "question_text": "The maximum gap between two sessions of Parliament should not be more than:",
        "options": ["3 months", "6 months", "9 months", "12 months"],
        "correct_option": 1,
        "explanation": "Article 85 provides that the gap between two sessions of Parliament should not exceed 6 months.",
        "difficulty": "easy",
        "topic": "Parliament - Sessions"
    },
    {
        "question_text": "Consider the following about Anti-Defection Law:\n(1) It was added by the 52nd Amendment (1985)\n(2) It is contained in the Tenth Schedule\n(3) The decision on disqualification is made by the Speaker/Chairman\n(4) Merger requires at least 2/3rd members of the legislative party\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The Anti-Defection Law was added by 52nd Amendment, contained in Tenth Schedule, decided by Speaker/Chairman, and merger requires 2/3rd majority.",
        "difficulty": "hard",
        "topic": "Parliament - Anti-Defection"
    },
    {
        "question_text": "Which of the following is NOT a qualification for appointment as a Judge of the Supreme Court?",
        "options": ["Must be a citizen of India", "Must have been a Judge of a High Court for at least 5 years", "Must have been an advocate of a High Court for at least 10 years", "Must have completed 65 years of age"],
        "correct_option": 3,
        "explanation": "65 years is the retirement age of SC Judge, not a qualification. The qualifications are: citizenship, HC Judge for 5 years OR HC advocate for 10 years OR distinguished jurist.",
        "difficulty": "medium",
        "topic": "Judiciary - Supreme Court"
    },
    {
        "question_text": "The concept of 'Basic Structure' of the Constitution was propounded in:",
        "options": ["Shankari Prasad case (1951)", "Golak Nath case (1967)", "Kesavananda Bharati case (1973)", "Minerva Mills case (1980)"],
        "correct_option": 2,
        "explanation": "The Basic Structure doctrine was propounded in Kesavananda Bharati vs State of Kerala (1973) by a 13-judge bench of the Supreme Court.",
        "difficulty": "medium",
        "topic": "Judiciary - Basic Structure"
    },
    {
        "question_text": "Consider the following statements about the High Courts:\n(1) Article 214 provides for a High Court for each State\n(2) The retirement age of HC Judge is 62 years\n(3) HC Judges are appointed by the President in consultation with CJI and Governor\n(4) Parliament can extend the jurisdiction of HC to Union Territories\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. Article 214 provides for HC in each state, retirement age is 62, appointment involves President, CJI and Governor, and Parliament can extend jurisdiction to UTs.",
        "difficulty": "hard",
        "topic": "Judiciary - High Courts"
    },
    {
        "question_text": "Public Interest Litigation (PIL) can be filed in:",
        "options": ["Supreme Court only under Article 32", "High Courts only under Article 226", "Both Supreme Court and High Courts", "Any court including District Courts"],
        "correct_option": 2,
        "explanation": "PIL can be filed in both Supreme Court (Article 32) and High Courts (Article 226). It was developed by Justice P.N. Bhagwati and Justice V.R. Krishna Iyer.",
        "difficulty": "easy",
        "topic": "Judiciary - PIL"
    },
    {
        "question_text": "Which Constitutional body is responsible for the conduct of elections to the offices of President and Vice-President?",
        "options": ["Election Commission of India", "Central Election Tribunal", "Parliament", "Supreme Court"],
        "correct_option": 0,
        "explanation": "Under Article 324, the Election Commission of India is responsible for superintendence, direction and control of elections to President, VP, Parliament and State Legislatures.",
        "difficulty": "easy",
        "topic": "Constitutional Bodies - Election Commission"
    },
    {
        "question_text": "Consider the following about the Comptroller and Auditor General (CAG):\n(1) He is appointed by the President\n(2) He can be removed only by impeachment\n(3) His salary is charged upon the Consolidated Fund of India\n(4) He audits only accounts of the Central Government\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1 and 3 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect as CAG audits accounts of both Central and State Governments.",
        "difficulty": "hard",
        "topic": "Constitutional Bodies - CAG"
    },
    {
        "question_text": "The Finance Commission is constituted by the President under Article:",
        "options": ["Article 270", "Article 275", "Article 280", "Article 281"],
        "correct_option": 2,
        "explanation": "The Finance Commission is constituted by the President under Article 280 every five years or earlier.",
        "difficulty": "easy",
        "topic": "Constitutional Bodies - Finance Commission"
    },
    {
        "question_text": "Which of the following is NOT a function of the Union Public Service Commission?",
        "options": ["Conduct examinations for appointments to All India Services", "Advise on promotion and transfer matters", "Advise on disciplinary matters affecting civil servants", "Appointment of civil servants"],
        "correct_option": 3,
        "explanation": "UPSC only conducts examinations and advises on various matters. Actual appointments are made by the President/appropriate authority, not by UPSC.",
        "difficulty": "medium",
        "topic": "Constitutional Bodies - UPSC"
    },
    {
        "question_text": "The National Commission for Scheduled Castes (NCSC) was established under which Article?",
        "options": ["Article 338", "Article 338A", "Article 340", "Article 342"],
        "correct_option": 0,
        "explanation": "NCSC was established under Article 338 (after 89th Amendment, 2003). Article 338A is for NCST, Article 340 for Backward Classes Commission.",
        "difficulty": "medium",
        "topic": "Constitutional Bodies - NCSC"
    },
    {
        "question_text": "Consider the following about National Emergency (Article 352):\n(1) It can be proclaimed on grounds of war, external aggression, or armed rebellion\n(2) It must be approved by Parliament within one month\n(3) During Emergency, Article 19 is automatically suspended\n(4) The 44th Amendment changed 'internal disturbance' to 'armed rebellion'\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The 44th Amendment (1978) replaced 'internal disturbance' with 'armed rebellion' and made other significant changes.",
        "difficulty": "hard",
        "topic": "Emergency Provisions"
    },
    {
        "question_text": "Financial Emergency under Article 360 has been proclaimed in India:",
        "options": ["Once (1975)", "Twice (1962 and 1971)", "Thrice (1962, 1971, and 1975)", "Never"],
        "correct_option": 3,
        "explanation": "Financial Emergency under Article 360 has never been proclaimed in India. National Emergency has been proclaimed thrice (1962, 1971, 1975).",
        "difficulty": "medium",
        "topic": "Emergency Provisions - Financial Emergency"
    },
    {
        "question_text": "Which of the following rights cannot be suspended even during National Emergency?",
        "options": ["Right to Life and Personal Liberty (Article 21)", "Right against exploitation (Article 23)", "Right to Constitutional Remedies (Article 32)", "All of the above"],
        "correct_option": 0,
        "explanation": "After the 44th Amendment, Article 20 (protection against conviction) and Article 21 (right to life) cannot be suspended even during emergency.",
        "difficulty": "hard",
        "topic": "Emergency Provisions"
    },
    {
        "question_text": "The procedure for amendment of the Constitution is given in:",
        "options": ["Article 356", "Article 368", "Article 370", "Article 395"],
        "correct_option": 1,
        "explanation": "Article 368 deals with the power of Parliament to amend the Constitution and the procedure thereof.",
        "difficulty": "easy",
        "topic": "Amendment Procedure"
    },
    {
        "question_text": "Which of the following requires ratification by at least half of the State Legislatures for Constitutional Amendment?\n(1) Election of President\n(2) Seventh Schedule\n(3) Article 368 itself\n(4) Representation of States in Parliament\n\nSelect the correct answer:",
        "options": ["1, 2 and 3 only", "2, 3 and 4 only", "1, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All these provisions require special majority plus ratification by at least half of state legislatures as they affect federal structure.",
        "difficulty": "hard",
        "topic": "Amendment Procedure"
    },
    {
        "question_text": "Consider the following statements about the Governor:\n(1) He is appointed by the President on the advice of the Central Government\n(2) He holds office during the pleasure of the President\n(3) He can be removed only by impeachment\n(4) His term is normally 5 years\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 4 only", "1 and 2 only", "2, 3 and 4 only", "1, 3 and 4 only"],
        "correct_option": 0,
        "explanation": "Statements 1, 2, and 4 are correct. Statement 3 is wrong - the Governor holds office during the pleasure of the President and can be removed at any time.",
        "difficulty": "hard",
        "topic": "State Executive - Governor"
    },
    {
        "question_text": "The Governor's power to reserve a bill for President's consideration is:",
        "options": ["Mentioned in Article 200", "A discretionary power", "Subject to judicial review", "All of the above"],
        "correct_option": 3,
        "explanation": "The power to reserve bills is mentioned in Article 200, is discretionary in nature, and is subject to judicial review (though courts are reluctant to interfere).",
        "difficulty": "medium",
        "topic": "State Executive - Governor"
    },
    {
        "question_text": "Which Schedule of the Constitution contains provisions regarding disqualification on grounds of defection?",
        "options": ["Eighth Schedule", "Ninth Schedule", "Tenth Schedule", "Eleventh Schedule"],
        "correct_option": 2,
        "explanation": "The Tenth Schedule (added by 52nd Amendment, 1985) contains provisions relating to disqualification on grounds of defection.",
        "difficulty": "easy",
        "topic": "Schedules of Constitution"
    },
    {
        "question_text": "The 73rd Constitutional Amendment Act (1992) relating to Panchayati Raj:\n(1) Added Part IX to the Constitution\n(2) Added Eleventh Schedule containing 29 subjects\n(3) Made it mandatory to hold Panchayat elections every 5 years\n(4) Reserved seats for SC/ST and Women\n\nWhich of the above statements are correct?",
        "options": ["1, 2 and 3 only", "1, 3 and 4 only", "2, 3 and 4 only", "All of the above"],
        "correct_option": 3,
        "explanation": "All statements are correct. The 73rd Amendment added Part IX and Eleventh Schedule, mandated 5-yearly elections, and provided reservations for SC/ST and women.",
        "difficulty": "hard",
        "topic": "Panchayati Raj"
    },
    {
        "question_text": "Which of the following is NOT a Constitutional body?",
        "options": ["National Human Rights Commission", "Election Commission of India", "Union Public Service Commission", "Comptroller and Auditor General"],
        "correct_option": 0,
        "explanation": "NHRC is a statutory body created by the Protection of Human Rights Act, 1993, not a Constitutional body. EC, UPSC, and CAG are Constitutional bodies.",
        "difficulty": "medium",
        "topic": "Constitutional vs Statutory Bodies"
    },
    {
        "question_text": "The Inter-State Council is established under which Article?",
        "options": ["Article 262", "Article 263", "Article 264", "Article 265"],
        "correct_option": 1,
        "explanation": "The Inter-State Council is established under Article 263 to inquire into and advise upon disputes between States and to investigate subjects of common interest.",
        "difficulty": "medium",
        "topic": "Centre-State Relations"
    },
    {
        "question_text": "Consider the following about Cooperative Societies (97th Amendment, 2011):\n(1) It made Right to form Cooperative Societies a Fundamental Right\n(2) It added Part IXB to the Constitution\n(3) It made cooperative societies a State subject\n(4) It added DPSP relating to cooperatives\n\nWhich of the above statements are correct?",
        "options": ["1 and 2 only", "1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"],
        "correct_option": 1,
        "explanation": "The 97th Amendment added Part IXB, modified Article 19(1)(c) to include right to form cooperatives, and added Article 43B as DPSP. Cooperatives were already a State subject.",
        "difficulty": "hard",
        "topic": "Cooperative Societies"
    },
    {
        "question_text": "Which of the following Constitutional Amendment Acts dealt with the provisions related to GST?",
        "options": ["99th Amendment Act", "100th Amendment Act", "101st Amendment Act", "102nd Amendment Act"],
        "correct_option": 2,
        "explanation": "The 101st Constitutional Amendment Act, 2016, introduced the Goods and Services Tax (GST) regime in India.",
        "difficulty": "medium",
        "topic": "Recent Amendments"
    },
    {
        "question_text": "Article 370 providing special status to Jammu and Kashmir was abrogated by:",
        "options": ["Constitutional Amendment", "Presidential Order", "Parliamentary Resolution", "Supreme Court Order"],
        "correct_option": 1,
        "explanation": "Article 370 was rendered inoperative through Presidential Order C.O. 272 (August 5, 2019), using the power under Article 370(3) itself.",
        "difficulty": "medium",
        "topic": "Recent Constitutional Developments"
    },
]

# Export
if __name__ == "__main__":
    print(f"Total Polity questions: {len(POLITY_QUESTIONS)}")
