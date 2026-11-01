# Milestones and Acceptance Tests

Build **one milestone at a time**. At the end of each milestone:
1. Run the acceptance tests below (backend testing agent + frontend checks).
2. Report: what was built, test results (pass/fail per item), anything skipped, and env vars the owner must set.
3. **Stop and wait for the owner's go-ahead** before starting the next milestone.

Target pace: about one milestone per week (8 Nov → 20 Dec 2026).

---

## M1 — Foundation and cleanup
**Build**
- Rename the app to Bubbl (display name, `app.json` slug/name, Android package and iOS bundle `in.bubblprep.app`).
- Repo cleanup: delete `frontend/.metro-cache/`, add it to `.gitignore`; move `backend/questions_*.py`, `real_questions.py`, `extreme_questions.py`, `generate_*.py` to `backend/legacy/` (not imported at runtime); trim `requirements.txt`.
- Split `server.py` into modules (`routers/auth.py`, `routers/practice.py`, `routers/admin.py`, `models/`, `services/`). No behaviour change beyond the fixes below.
- Fix D1–D5 and D12 from `02 Current State Audit.md`.
- New collections and indexes per `03`. Roles: `student`, `centre_admin`, `admin`. A CLI `python -m scripts.make_admin <email>` to grant admin.
- JSON import: a service + CLI (`python -m scripts.import_questions file.json`) using the `03` validation rules.
- One-time migration of the legacy banks to `pending` (see `02` §4).
- Google sign-in (Expo AuthSession) alongside email/password; email via a provider set in env (`EMAIL_PROVIDER`, `EMAIL_API_KEY`, `EMAIL_FROM`).

**Acceptance**
- [ ] App boots without `/seed` or `/reseed`; those routes return 404.
- [ ] Server refuses to start if `JWT_SECRET` is missing.
- [ ] Forgot-password sends an email; the API response never contains the code.
- [ ] `/api/analytics` (or its replacement) returns only the caller's data (two test users, no leakage).
- [ ] Importing `sample questions.json` inserts 3 `pending` questions; re-importing the same file inserts 0 (idempotent).
- [ ] Legacy migration: count of imported Agriculture + Polity + other banks equals the counts in `02` §1, minus exact duplicates; all are `pending`.
- [ ] Repo size < 20 MB (excluding `node_modules`); no `.metro-cache` in git.

## M2 — Admin Command Center + Automation API
**Build:** screens 1–6, 8, 11, 12 from `05` (marketing queue and centres come later), review workflow, auto-pause, API keys, every `/api/admin/v1` endpoint for questions, reports, coverage and metrics, and the audit log.

**Acceptance**
- [ ] Non-admin users get 403 on every `/admin` route and every `/api/admin/*` endpoint.
- [ ] Review: approve / fix-with-note / reject work by click and keyboard (A/F/R); approved → `live` (immediate mode).
- [ ] A question `fix`ed in the UI shows up in `GET /api/admin/v1/questions?status=fix` with the note; re-import of the same `ext_id` returns it to `pending` with version + 1.
- [ ] Bulk approve is refused for flagged questions and before 20 manual reviews in the batch.
- [ ] Three "wrong answer" reports from three users auto-pause a live question.
- [ ] An API key without `questions:write` gets 403 on import; every API call appears in the audit log.
- [ ] Coverage endpoint returns live/pending counts per subject × topic × difficulty.

## M3 — Practice engine and exam experience
**Build:** all modes in `04` §2 (except Centre Test), OCS rules and blueprints, assembly algorithm, PYQ papers, results and review, bilingual toggle, report-an-error, bookmarks, offline-resilient attempts, new Home (chalkboard header, Daily Quiz, Continue Level, weak topics), OMR-style answering.

**Acceptance**
- [ ] 20 consecutive Practice Sets for one user in a subject with ≥ 400 live questions contain **no repeated question**.
- [ ] Full Mock Paper I has exactly 100 Q, follows the blueprint ±1 per subject, 120-min timer, auto-submits at 0.
- [ ] Scoring: 60 correct, 20 wrong, 20 skipped on Paper I = 120 − 13.33 = **106.67**. Paper II: 50 correct, 15 wrong = 125 − 12.5 = **112.5** and shows "Qualified (≥ 66)".
- [ ] `shuffle_ok: false` questions never have reordered options; scoring is correct for shuffled ones.
- [ ] PYQ papers appear in original order with the "PYQ 2025" label; only `live` questions are served in any mode.
- [ ] Turning airplane mode on mid-mock and back on keeps all answers and submits correctly.
- [ ] Every question shows EN/ଓ toggle; Odia renders without missing glyphs on a low-end Android device.
- [ ] Paper generation < 500 ms (log timing) on a seeded bank of 20k questions.

## M4 — Gamification
**Build:** levels and unlock rules, XP, streaks (IST) with freeze, titles, badges, weekly leaderboards (global + batch), weak-topic cards, shareable result card, streak reminder notifications, events in `04` §8.

**Acceptance**
- [ ] Medium unlocks after 5 Easy sets averaging ≥ 60%, or an Easy Level Test ≥ 70%; not before.
- [ ] Streak counts at ≥ 10 answers per IST day; a day boundary test at 23:59 → 00:01 IST works; a freeze is consumed on a missed day for Pro only.
- [ ] XP values match `04` §6.2 for a scripted session (log the expected total in the test).
- [ ] Leaderboard resets Monday 00:00 IST; hidden users don't appear.
- [ ] The share card renders with score, date and referral code and opens the native share sheet.

## M5 — Plans, payments, coaching centres
**Build:** everything in `06`: limits enforced on the server, paywall sheets at each upgrade moment, Razorpay (test mode) with webhook, RevenueCat/Play Billing, entitlements, coupons, referrals, receipts, centre licences, Centre Dashboard, centre tests, marketing queue (screen 7) + its API.

**Acceptance**
- [ ] Free user: 2nd Paper I mock in the same month → paywall; Medium set → paywall; PYQ 2019 → paywall; Odia always works.
- [ ] Razorpay test payment → webhook → Pro active within 10 s; replaying the same webhook doesn't extend twice; a bad signature is rejected (400) and logged.
- [ ] Buying again while Pro extends `ends_at` by 12 months from the current end.
- [ ] A Razorpay purchase on the web shows Pro after logging into the Android app; the Android app has no link to the web checkout.
- [ ] Centre: create centre (Starter, 50 seats) → 51st student join is refused with a clear message; assigned test is identical for 2 students in the batch; CSV export works.
- [ ] Coupon 100% off creates an entitlement with `source: coupon`.

## M6 — Launch readiness
**Build:**
- Public website on the web build:
  - landing page with the waitlist form (stored in DB, CSV export) for the pre-launch period
  - pricing
  - Terms, Privacy, Refund policy, Contact
  - SEO pages: one per PYQ year ("OCS Prelims 2023 Paper I — questions with answers and explanations"), server-rendered/static so Google can index them; first 10 questions visible, then "practise the full paper free in the app"
- Final brand assets, app icon, splash, store listing text.
- EAS build for Android (AAB), Play Console internal testing.
- Sentry error tracking; MongoDB daily backup; production env checklist.

**Acceptance**
- [ ] Lighthouse (mobile) ≥ 85 performance, ≥ 95 accessibility on the landing page.
- [ ] SEO pages have a unique title, meta description and canonical URL; they are in `sitemap.xml`.
- [ ] Legal pages are reachable from the footer and the app's Settings.
- [ ] Signed AAB uploads to the internal testing track; a test purchase works on a real device.
- [ ] A forced error appears in Sentry with the release version.
- [ ] Restoring last night's backup into a scratch DB works (documented steps).

---

## Accounts and secrets the owner provides (set as env vars in Emergent)
`MONGO_URL`, `DB_NAME`, `JWT_SECRET`, `APP_ENV`, `EMAIL_PROVIDER`, `EMAIL_API_KEY`, `EMAIL_FROM`, `GOOGLE_OAUTH_CLIENT_ID(S)`, `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET`, `REVENUECAT_API_KEY`, `REVENUECAT_WEBHOOK_SECRET`, `SENTRY_DSN`, `PUBLIC_WEB_URL`.
Never commit secrets. Never paste them into chat logs or docs.
