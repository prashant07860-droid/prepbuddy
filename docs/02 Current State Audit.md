# Current State Audit (repo as of 31 Oct 2026)

Read this before changing code. It records what exists, what is broken, and what to keep.

## 1. What exists
- **Frontend:** Expo SDK 54 / React Native, expo-router, TypeScript. Screens in `frontend/app/`:
  - `index.tsx` (home / subjects), `auth.tsx`, `forgot-password.tsx`
  - `subject/[id].tsx` (papers list), `exam/[paperId].tsx` (exam screen, ~1,775 lines)
  - `results/[attemptId].tsx`, `dashboard.tsx`, `profile.tsx`, `settings.tsx`
  - State: `src/AuthContext.tsx` (JWT + guest mode in AsyncStorage), `src/store.ts` (bookmarks, settings), `src/api.ts`.
- **Backend:** FastAPI + Motor (MongoDB) in a single `backend/server.py` (~1,300 lines). JWT auth, subjects, papers, questions, attempts, analytics, settings, seed/reseed.
- **Content:** 70+ Python files of hard-coded questions in `backend/`:

| Bank | Questions | Used by the app? |
|---|---|---|
| Agriculture (Odisha), `questions_agriculture_odisha_part1..48.py` | 2,600 (8 duplicate texts) | Yes |
| Polity, `questions_polity_part1..22.py` | 1,386 (14 duplicate texts) | **No — not wired in** |
| 10 other subjects, one file each | 35–82 each | Yes, recycled to fill 2,600 slots |

## 2. Defects to fix (all in Milestone M1)

| # | Defect | Where | Fix |
|---|---|---|---|
| D1 | `POST /api/reseed` has no auth and **deletes all users' attempts** | server.py `/reseed` | Remove the public seed/reseed endpoints. Content comes in through the admin import only. |
| D2 | `GET /api/analytics` is hard-coded to `user_id: "default_user"` | server.py `/analytics` | Scope to the logged-in user |
| D3 | Password reset returns the reset code in the API response (mocked) | `/auth/forgot-password` | Send the code by email (Resend / Brevo / SMTP via env); never return it |
| D4 | `JWT_SECRET` falls back to a random value at boot → everyone is logged out on restart | top of server.py | Required env var; fail fast if missing |
| D5 | Negative marking is shown in the UI but not applied to the score | `/attempts` scoring | Apply exam marking rules (`04` §3) |
| D6 | Papers overlap: each paper reshuffles the whole pool and takes the first 100; small banks repeat each question 30–75× | `generate_questions_for_subject` | Replace with the practice engine (`04`) |
| D7 | Answer key skew in the generated banks: option B correct in 55% of questions | content | Rebalance during import (the pipeline fixes this before import); shuffle options at runtime where `shuffle_ok` |
| D8 | ~2,900 Metro cache files (`frontend/.metro-cache/`) committed; repo is 151 MB | repo | Delete; add to `.gitignore` |
| D9 | App identifiers are `com.emergent.agriquestionhub.l55jkk` | `frontend/app.json` | Change to `in.bubblprep.app` (Android package and iOS bundle id) |
| D10 | Placeholder React logos / splash in `frontend/assets/images` | assets | Replace with the Bubbl brand assets (`07`) |
| D11 | Questions stored as Python source files | backend | Move to MongoDB via the JSON import; delete the Python question files from the runtime path (keep them in `legacy/` for the one-time import) |
| D12 | `Subject` model hard-codes `total_papers=26`, `total_questions=2600` | models | Remove; counts are computed from live questions |
| D13 | Unused heavy dependencies in `requirements.txt` (boto3, pandas, numpy, jq, typer, black, mypy…) | backend | Trim to what is used |

## 3. Keep
- The exam screen's interaction ideas: question palette, mark-for-review, bookmarks, timer modes (whole paper / per question). Restyle them to the brand.
- Guest mode and guest → account conversion (`/auth/guest/convert`).
- The FastAPI + MongoDB + Expo stack. No stack change.

## 4. One-time content migration (M1)
1. Export the existing Agriculture and Polity banks to the JSON format in `03` using a one-off script in `backend/scripts/migrate_legacy.py`.
2. Import them with `status: "pending"` and `source.kind: "legacy"`. **Do not mark them live.** They go through the same automated checks and owner review as new content (via the Command Center).
3. The other 10 small single-file banks: import as `pending` too. The question pipeline will add to them.
