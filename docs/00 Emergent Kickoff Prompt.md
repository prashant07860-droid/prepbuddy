# Emergent Kickoff Prompt

**How to use:**
1. Upload this whole folder to the GitHub repo as `/docs` (GitHub → repo → Add file → Upload files → drag the folder → Commit). Keep `Brand Assets/` inside it.
2. In Emergent, start a **new** project from the GitHub repo (pull/import the repo).
3. Paste the prompt below as the first message.
4. After each milestone report, reply with "Go M2", "Go M3"… (or with corrections).

---

## Prompt to paste

```
You are continuing an existing Expo (React Native, expo-router, TypeScript) + FastAPI + MongoDB app from this GitHub repo. It was called "Preppbuddy" and is being rebuilt as "Bubbl", an exam-practice app for the OPSC Odisha Civil Services (OCS) exam, launching in January 2027.

Before writing any code, read every file in /docs in this order:
01 PRD.md, 02 Current State Audit.md, 03 Data Model and Question Format.md, sample questions.json, 04 Practice Engine, Exam Rules and Gamification.md, 05 Admin Command Center and Automation API.md, 06 Plans, Payments and Coaching Centres.md, 07 Brand and UI Guide.md, 08 Milestones and Acceptance Tests.md.

Rules for this project:
1. Build ONE milestone at a time, in the order given in 08 Milestones and Acceptance Tests.md. Start with M1 only.
2. At the end of each milestone: run its acceptance tests, then report what you built, each test as pass/fail, anything you skipped, and any environment variables I must set. Then STOP and wait for me to say "Go M<next>".
3. Do NOT write or generate exam questions, and do not create question files. All question content comes in through the JSON import / Admin Automation API described in the docs. Use only sample questions.json for testing.
4. Keep the existing stack (Expo + FastAPI + MongoDB). Do not switch frameworks.
5. Never commit secrets. Read all keys from environment variables listed in 08.
6. If something in the docs is unclear or conflicts, ask me before guessing. If a requirement is impossible in Emergent's environment (for example real Google Play Billing tests), say so and build the testable stand-in described in the docs.
7. Follow 07 Brand and UI Guide.md for every screen you touch (colours, fonts, OMR-style answer bubbles, English + Odia).

Start now: read the docs, give me a short summary of your understanding and your M1 plan (10 lines max), then build M1.
```

---

## Follow-up prompts (copy when needed)
- **After a milestone report you're happy with:** `Go M2` (then M3 … M6)
- **If it skipped tests:** `Run every acceptance test listed for this milestone in 08 and show me pass/fail for each before we continue.`
- **If it starts writing questions:** `Stop. Per rule 3 we never generate questions in the app. Remove any question content you created except sample questions.json.`
- **If it drifts from the brand:** `Re-check 07 Brand and UI Guide.md and fix colours, fonts and the OMR answer bubbles on the screens you changed.`
