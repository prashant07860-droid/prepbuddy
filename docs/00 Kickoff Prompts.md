# Kickoff Prompts

Bubbl is two Emergent projects (see `09 Two Project Setup.md`). A project reads its repo only when the job starts, so the docs must be final first. Later files go in through "Upload file or assets" in the chat. Use E-1, never Maxx.

---

## Bubbl Mobile: new Mobile app job, imported from github.com/prashant07860-droid/prepbuddy

```
This is an existing Expo (React Native, expo-router, TypeScript) + FastAPI + MongoDB app, once called "Preppbuddy", now being rebuilt as "Bubbl", an exam-practice app for the OPSC Odisha Civil Services exam. This project is the Android app AND the only backend and database. A separate web project will call this backend.

Read /docs in this order: 09, 01, 02, 03, sample questions.json, 04, 05, 06, 07, 08 (Part A). Then reply with your plan for milestone E1 only, in 10 lines or fewer. Don't write code yet.

Rules:
1. Build ONE milestone at a time from 08 Part A. Run its tests, report each as pass/fail in a short list with anything skipped and any secrets I must add. Then STOP until I say "Go E<n>".
2. Never write or generate exam questions. Use only sample questions.json for testing.
3. Keep the stack. Don't edit eas.json. Never put secrets in code or chat.
4. Use /docs/App Text for all wording, /docs/Brand Assets and /docs/Fonts for visuals, /docs/Starter Data for setup data.
5. If the docs are unclear or something isn't possible here, ask me in one short question. Don't guess.
6. Keep replies short, and do only what the milestone asks.
```

**Follow-ups**
- Next milestone: `Go E2` (and so on)
- Tests skipped: `Run every test for this milestone in 08 and show pass/fail for each.`
- Writing questions: `Stop. Rule 2. Remove any question content you created.`
- Brand drift: `Re-check 07 and fix the colours, fonts and OMR bubbles on the screens you changed.`

---

## Bubbl Web: new Web app job (E-1, not NextJS), from github.com/prashant07860-droid/bubbl-web

Start only after the backend is published (P1). Fill in the live address first.

```
This is "Bubbl Web", the website and admin dashboard for Bubbl, an exam-practice app. It has no backend logic or database of its own. Every feature calls the live Bubbl backend at <LIVE BACKEND ADDRESS>, read from an environment variable. Don't build a FastAPI backend, and don't use a database.

Read /docs in this order: 09, 01, 03, 05, 06 (section 3.1), 07, 08 (Part B). Then reply with your plan for milestone W1 only, in 10 lines or fewer. Don't write code yet.

Rules:
1. Build ONE milestone at a time from 08 Part B. Run its tests, report each as pass/fail in a short list with anything skipped and any secrets I must add. Then STOP until I say "Go W<n>".
2. Never write or generate exam questions.
3. If you need a backend change, don't work around it. Tell me exactly which endpoint is missing, and I'll get it added in the backend project.
4. Use /docs/App Text, /docs/Brand Assets, /docs/Fonts and /docs/Legal Pages. Follow 07.
5. If the docs are unclear or something isn't possible here, ask me in one short question. Don't guess.
6. Never put secrets in code or chat. Keep replies short, and do only what the milestone asks.
```

**Follow-ups:** `Go W2` (and so on), and the same test and brand prompts as above.
