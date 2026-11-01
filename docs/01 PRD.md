# Bubbl — Product Requirements Document (Phase 1)

**Version:** 1.0 · **Date:** 1 Nov 2026 · **Owner:** Prashant Rana
**Product:** Bubbl — exam practice app for Indian competitive exams (launch exam: OPSC Odisha Civil Services, OCS)
**Codebase starting point:** this GitHub repo (previously "Preppbuddy"; an Expo + FastAPI + MongoDB app). Read `02 Current State Audit.md` before changing anything.

---

## 1. Why this exists

Aspirants for state civil-services exams practise from printed booklets and PDFs. They have no way to:
- take endless fresh mock tests at the right difficulty,
- see which topics they are weak in,
- practise past papers exactly as the exam runs (timer, negative marking, OMR-style answering),
- do all of this in **Odia as well as English**.

Bubbl turns that into a habit-forming app: short daily practice, levels, streaks, full mocks and real past papers.

**Name and idea:** every aspirant knows the OMR answer sheet. "Fill the right bubble" is the moment that decides the exam. The brand leans on that shared, nostalgic memory (see `07 Brand and UI Guide.md`).

## 2. Goals for Phase 1 (launch: January 2027)

| Goal | Measure |
|---|---|
| Launch OCS practice before the OCS 2026 notification (expected around Dec 2026 to Jan 2027) | Live on Play Store + web by **5 Jan 2027** |
| Students build a daily habit | 30% of new users on a 3-day streak or longer in week 1 |
| Content can be trusted | Fewer than 1 confirmed error report per 500 questions served |
| Turn free users into paying users | 3–5% of active users upgrade to Pro by the prelims |
| Coaching centres | 5 paid centre licences by March 2027 |
| Owner effort | Running the product takes Prashant at most 5–10 hrs/week, all from the Admin Command Center |

## 3. Users

1. **Aspirant (student):** 21–32, preparing for OCS (often for OSSC/OSSSC and UPSC too). Uses an Android phone, often on patchy data. Reads in English and/or Odia.
2. **Coaching-centre admin:** runs a batch of 30–300 students in Bhubaneswar, Cuttack, Berhampur, Sambalpur and similar cities. Wants a ready test platform and batch reports.
3. **Owner / admin (Prashant):** reviews content, watches sales, approves marketing. Does everything from one dashboard.
4. **Automations (machine user):** the question pipeline, Current Affairs updater and marketing generator. They talk to the app **only** through the Admin Automation API (`05`).

## 4. Scope

### 4.1 In scope (Phase 1)
1. **Exam-agnostic question bank** with an exam module for OCS (the design must make adding UPSC and other state exams a data change, not a rewrite). See `03`.
2. **Practice engine** that builds a fresh paper every time. Modes are Daily Quiz, Practice Set, Full Mock (OCS Paper I / Paper II simulation), Previous Year Papers (PYQ), Weak-Topic Practice and Revision (bookmarked / wrong answers). See `04`.
3. **Levels and gamification:** an Easy → Medium → Hard ladder per subject, XP, streaks, badges, titles and weekly leaderboards. See `04` §6.
4. **Bilingual content:** each question has English and Odia text, and students can switch language per question or set a default.
5. **Results and review:** score with negative marking, time per question, topic breakdown, explanations, and a "Report an error" button on every question.
6. **Accounts:** email + password, Google sign-in, guest mode (guest progress moves over when they sign up), and real password reset by email.
7. **Plans and payments:** free tier, Bubbl Pro (₹149), and coaching-centre licences. Razorpay on web, Google Play Billing on Android. See `06`.
8. **Admin Command Center (web)** for the owner: review queues, content, reports, users, sales, centres, marketing queue and settings. See `05`.
9. **Admin Automation API** so external automations can push pending content and read decisions. See `05`.
10. **Landing website + legal pages + SEO pages** for previous-year papers (web build of the same app).
11. **Android release** on Google Play. The web app works on iPhone browsers; a native iOS app is out of scope for Phase 1.

### 4.2 Out of scope (Phase 1)
- Writing questions inside Emergent. **All question content arrives through the import API or a JSON file.** Do not generate questions in code or ask the agent to write question files.
- Video lessons, live classes, doubt chat.
- Mains (descriptive) answer writing.
- UPSC / other state exam modules. The design must allow them, but they ship in Phase 2.
- Native iOS app.

## 5. Key user journeys

1. **First open:** pick exam (OCS), language (English / ଓଡ଼ିଆ / both) and target year → 10-question Daily Quiz right away with no signup (guest) → result card with a "Save your streak — sign up" prompt.
2. **Daily habit:** home shows streak, today's Daily Quiz, "Continue Level" per subject and one weak topic → 10–20 questions → XP + streak update.
3. **Level up:** finish Easy sets in Polity → Medium unlocks. **Medium and Hard are Pro**, so the unlock moment is the main upgrade prompt.
4. **Full mock:** OCS Paper I simulation (100 Q, 2 hrs, +2 / −0.66) with an OMR-style answer panel → result with estimated score, cut-off comparison (admin-configurable) and topic breakdown.
5. **PYQ:** pick year 2015–2025 → take the paper as it was set (fixed order), English/Odia → review with explanations.
6. **Report an error:** on any question → choose reason (wrong answer / wrong translation / typo / outdated / other) + optional note → it goes to the admin Reports queue.
7. **Upgrade:** paywall sheet → Razorpay (web) or Play Billing (Android) → Pro active straight away on every device.
8. **Coaching student:** enters a centre code → joins the batch → gets Pro for as long as the centre licence lasts → sees centre-assigned tests and the batch leaderboard.
9. **Owner weekly loop:** opens Command Center → approves/fixes flagged questions → clears reports → approves marketing items → checks KPIs.

## 6. Functional requirements (summary — details in docs 03–06)

| # | Requirement | Detail doc |
|---|---|---|
| F1 | Question bank with subjects → topics → subtopics, difficulty, bilingual fields, source (generated / PYQ), status workflow | 03 |
| F2 | Only questions with status `live` are ever served to students | 03 |
| F3 | Paper engine: fresh paper per attempt, no repeats for a user until their pool runs out, topic spread follows the exam blueprint | 04 |
| F4 | OCS exam rules: Paper I 100 Q / 200 marks / 2 h; Paper II 80 Q / 200 marks / 2 h, qualifying at 33%; negative marking of one-third of the question's marks | 04 |
| F5 | Options shuffled per attempt where the question allows it (`shuffle_ok`) | 03, 04 |
| F6 | Gamification: levels, XP, streaks (IST days), badges, titles, weekly leaderboards | 04 |
| F7 | Report-an-error flow; questions auto-pause on a report threshold | 04, 05 |
| F8 | Free vs Pro limits enforced on the **server** | 06 |
| F9 | Payments: Razorpay (web) + Play Billing (Android) giving the same server-side entitlement | 06 |
| F10 | Coaching centres: licences, seats, batches, join codes, assigned tests, batch dashboard | 06 |
| F11 | Admin Command Center with review queues and KPIs | 05 |
| F12 | Admin Automation API with scoped API keys and an audit log | 05 |
| F13 | Bilingual UI (English + Odia) for all student-facing strings | 07 |
| F14 | Landing site, legal pages (Terms, Privacy, Refund, Contact), PYQ SEO pages | 08 |

## 7. Non-functional requirements
- **Performance:** paper generation < 500 ms; question screen works on low-end Android (2 GB RAM) and 3G. Pre-fetch the whole paper at the start of an attempt, and if the connection drops mid-attempt, save answers locally and sync later.
- **Security:**
  - JWT secret from env (never random at boot)
  - no unauthenticated destructive endpoints
  - admin routes need the `admin` role
  - the automation API needs a scoped key
  - rate limits on auth and import
  - passwords hashed with bcrypt
- **Privacy:** collect only email, name and optional phone. Leaderboards show a display name, never an email. Deleting an account deletes the user's data.
- **Content integrity:** every question edit creates a new `version`. Attempts store the question version they used.
- **Observability:** error tracking (Sentry or similar), an event log for funnel analytics (`04` §8), and a daily backup of MongoDB.
- **Time zone:** all streaks, daily quizzes and leaderboards use **IST**.

## 8. Launch timeline (working backwards from the exam)

OPSC's own recruitment calendar shows the OCS 2025 cycle as: advertisement 31 Dec 2025 → prelims 7 Jun 2026 → mains 31 Oct–7 Nov 2026. If OCS 2026 follows the same rhythm, its notification lands around **late Dec 2026 to Jan 2027**, with prelims around **May–June 2027**. Most buying happens between the notification and the prelims.

| Window | What happens |
|---|---|
| 1–7 Nov 2026 | Docs signed off; Emergent M1; question pipeline built; brand assets |
| 8 Nov – 20 Dec 2026 | Emergent M2–M6 (about one milestone a week); content pipeline fills subjects; **pre-launch noise starts** (Telegram, Instagram, waitlist) |
| 20–31 Dec 2026 | Closed beta: the friend's circle plus 50–100 waitlist users, free |
| **~5 Jan 2027** | Public launch on Play Store + web, Pro on sale at the launch price |
| Jan–May 2027 | Peak season: daily content, mock-test weekends, coaching outreach |
| ~June 2027 | OCS prelims → review results, then start Phase 2 (UPSC + other states) |

## 9. Success metrics tracked in the Command Center
- DAU / WAU, day-1 and day-7 retention, average streak length
- Questions answered per day, mocks completed
- Free → Pro conversion %, revenue (gross, net of fees), refunds
- Centre licences sold, seats used
- Content: live questions per subject/level, pending reviews, open reports, error rate per 1,000 questions served

## 10. Open items (owner)
- Final check that the name "Bubbl" is free to trademark and buying `bubblprep.com` / `bubblprep.in` (see `07`).
- Google Play developer account, Razorpay account, domain, email-sending account (see `08` §Accounts).
- Confirm the OCS 2026 notification date when OPSC publishes it, and set the cut-off reference marks in Settings.

## 11. Document map
| File | Purpose |
|---|---|
| `00 Emergent Kickoff Prompt.md` | What to paste into Emergent first |
| `01 PRD.md` | This document |
| `02 Current State Audit.md` | What exists in the repo and what is broken |
| `03 Data Model and Question Format.md` | Collections, question JSON, statuses; sample in `sample questions.json` |
| `04 Practice Engine, Exam Rules and Gamification.md` | Paper building, OCS rules, levels, XP, streaks, badges, events |
| `05 Admin Command Center and Automation API.md` | Dashboard screens, review workflow, API endpoints |
| `06 Plans, Payments and Coaching Centres.md` | Free vs Pro, prices, Razorpay, Play Billing, centre licences |
| `07 Brand and UI Guide.md` | Name, colours, fonts, logo, tone, Odia |
| `08 Milestones and Acceptance Tests.md` | Build order M1–M6 with done-checks |
