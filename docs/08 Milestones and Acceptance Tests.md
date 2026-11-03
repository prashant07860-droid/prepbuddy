# Milestones and Acceptance Tests

Build **one milestone at a time**. At the end of each one, run its tests, report pass/fail per item, anything skipped and any secrets needed, then **stop** for the owner's go-ahead.

---

# Part A: Bubbl Mobile

## E1: Read and plan
Read the docs and reply with a plan for E2 in 10 lines or fewer. **No code.**

## E2: Rename, brand, clean-up
**Build:** rename to Bubbl (display name, `app.json` slug and name, Android package and iOS bundle `in.bubblprep.app`). Use the icon, adaptive icon, monochrome, notification icon and splash from `Brand Assets/`, and load `Fonts/`. Delete `frontend/.metro-cache/` and add it to `.gitignore`. Move `backend/questions_*.py`, `real_questions.py`, `extreme_questions.py`, `generate_*.py` to `backend/legacy/` (not imported at runtime). Trim `requirements.txt`. Copy `App Text/` into `i18n/`.
**Tests**
- [ ] The app shows the Bubbl name, icon and splash; Odia text shows with no empty boxes.
- [ ] Repo size < 20 MB (excluding `node_modules`); no `.metro-cache` in git.
- [ ] The backend starts without the legacy files being imported.

## E3: Split the server and fix defects
**Build:** split `server.py` into `routers/auth.py`, `routers/practice.py`, `routers/admin.py`, `models/`, `services/`, with no behaviour change beyond the fixes. Fix D1, D2, D4, D5 and D12 from `02`, and the D3 response leak (the email itself comes in E5).
**Tests**
- [ ] App boots without `/seed` or `/reseed`; those routes return 404.
- [ ] Server refuses to start if `JWT_SECRET` is missing.
- [ ] `/api/analytics` (or its replacement) returns only the caller's data (two test users, no leakage).
- [ ] The forgot-password response never contains the code.
- [ ] Scoring applies negative marking.

## E4: Data, roles and import
**Build:** collections and indexes per `03`, including `passages`. Load `Starter Data/`. Roles `student`, `centre_admin`, `admin`; `python -m scripts.make_admin <email>`. JSON import service + CLI (`python -m scripts.import_questions file.json`) with `03` validation. One-time legacy migration to `pending` (`02` §4).
**Tests**
- [ ] Importing `sample questions.json` inserts 5 `pending` questions and 1 passage; re-importing inserts 0.
- [ ] Legacy migration count equals the counts in `02` §1, minus exact duplicates; all are `pending`.
- [ ] A question with `correct` missing can be stored as `pending` but can't go `live`.

## E5: Accounts
**Build:** Google sign-in (Expo AuthSession) alongside email/password; reset email via a provider set in env; keep guest mode and guest → account conversion; delete-account endpoint and Settings button that removes the user's data.
**Tests**
- [ ] A forgot-password email arrives and the code works.
- [ ] Google sign-in works on a preview device, or say exactly what can only be tested after a build.
- [ ] Guest progress carries over on sign-up.
- [ ] Deleting an account removes its data, and that login no longer works.

## E6: Admin and automation APIs
**Build:** every `/api/admin/*` endpoint the screens in `05` need (at launch: 1–6, 8, 11, 12), every `/api/admin/v1` endpoint for questions, reports, coverage, metrics, media and coupons; a public `POST /api/waitlist` with rate limit and an admin CSV export; review workflow; auto-pause; API keys; audit log; rate limits. Allow cross-site calls for now (see `09`).
**Tests**
- [ ] Non-admins get 403 on every admin endpoint.
- [ ] Approve, fix-with-note and reject work through the API; approved → `live` (immediate mode).
- [ ] A question `fix`ed shows in `GET /api/admin/v1/questions?status=fix` with the note; re-import of the same `ext_id` returns it to `pending` with version + 1.
- [ ] Bulk approve is refused for flagged questions and before 20 manual reviews in the batch.
- [ ] Three "wrong answer" reports from three users auto-pause a live question.
- [ ] A key without `questions:write` gets 403 on import; every API call appears in the audit log.
- [ ] Coverage returns live/pending counts per subject × topic × difficulty.

**→ P1: the owner publishes here, on the owner's yes.**

## E7: Practice engine (server)
**Build:** all modes in `04` §2 at launch, OCS rules and blueprints from Settings, assembly algorithm, PYQ papers, scoring, seen tracking, bookmarks, error reports.
**Tests**
- [ ] 20 consecutive Practice Sets for one user in a subject with ≥ 400 live questions have **no repeats**.
- [ ] Full Mock Paper I has exactly 100 Q and follows the blueprint ±1 per subject.
- [ ] 60 correct, 20 wrong, 20 skipped on Paper I = **106.67**. Paper II: 50 correct, 15 wrong = **112.5**, "Qualified (≥ 66)".
- [ ] `shuffle_ok: false` options never reorder; shuffled scoring is correct.
- [ ] PYQs come in original order; only `live` questions are served in any mode.
- [ ] Comprehension passages are never split.
- [ ] Generation < 500 ms (log it) on a seeded bank of 20k test questions, in preview only.

## E8: Exam screen and results
**Build:** OMR-style answering and answer sheet, timer with auto-submit, EN/ଓ toggle, passage, figure and picture-based PYQ display (`03` §4), offline-safe attempts, results, review with explanations, unofficial-key notice, bookmark, report-an-error.
**Tests**
- [ ] 120-minute timer auto-submits at 0.
- [ ] Airplane mode on and off mid-mock keeps all answers and submits correctly.
- [ ] Every question shows the EN/ଓ toggle; "Odia coming soon" shows when Odia is empty.
- [ ] A picture-based PYQ is readable on a small phone (pinch to zoom), and A–D bubbles work below it.
- [ ] Screen-reader labels and 44 px tap targets per `07`.

**→ R1: first Android build from the Publish panel, on the owner's yes, tested on the owner's phone.**

## E9: Home, onboarding, modes
**Build:** first-open flow, Home (chalkboard header, Daily Quiz, Continue Level, weak topics), subject and mode screens, profile, settings with legal links.
**Tests**
- [ ] A new user reaches a 10-question Daily Quiz without signing up.
- [ ] All student text comes from `i18n/`; switching to Odia leaves no hard-coded English.
- [ ] Daily Quiz is the same for two users on one IST day.

## E10: Gamification
**Build:** levels and unlock rules, XP, streaks (IST) with freeze, titles, badges, weekly All Odisha leaderboard, weak-topic cards, share card (`result-card-reference.png`), streak reminder, events in `04` §8.
**Tests**
- [ ] Medium unlocks after 5 Easy sets averaging ≥ 60%, or an Easy Level Test ≥ 70%; not before.
- [ ] A streak counts at ≥ 10 answers per IST day; 23:59 → 00:01 IST works; a freeze is used for Pro only.
- [ ] XP matches `04` §6.2 for a scripted session.
- [ ] Leaderboard resets Monday 00:00 IST; hidden users don't appear.
- [ ] The share card renders and opens the share sheet.

## E11: Limits, paywall, Play Billing
**Build:** server-side limits, paywall sheets at each upgrade moment, RevenueCat/Play Billing, entitlements, coupon redemption.
**Tests**
- [ ] Free user: 2nd Paper I mock in a month → paywall; Medium set → paywall; PYQ 2019 opens free; Odia always works.
- [ ] A test purchase on a real device through internal testing gives Pro.
- [ ] A 100%-off code creates an entitlement with `source: coupon`.
- [ ] The Android app has no link to web checkout.

## E12: Razorpay server side
**Build:** Orders API, signature checks, webhook, receipts, referral, for Bubbl Web to call.
**Tests**
- [ ] Test payment → webhook → Pro active within 10 s; replaying the webhook doesn't extend twice; a bad signature is rejected (400) and logged.
- [ ] Buying while Pro extends `ends_at` by 12 months from the current end.

## E13: Production readiness
**Build:** Sentry, nightly backup (or tell the owner plainly that it isn't possible here and what can export instead), allowed-website lock (`09`), production checklist.
**Tests**
- [ ] A forced error appears in Sentry with the release version.
- [ ] Other websites are refused by the backend; Bubbl Web still works.
- [ ] Restoring a backup into a scratch database works (documented steps), or the alternative is agreed.
- [ ] The fake-purchase route is off in production.

---

# Part B: Bubbl Web

## W1: Connect
**Build:** project shell with brand, admin login against the live backend, backend address from env.
**Tests**
- [ ] An admin logs in through the live backend; a non-admin is blocked.
- [ ] No database or backend logic was added here.

## W2: Command Center, content
**Build:** screens 2, 3, 5, 6 in `05`.
**Tests**
- [ ] Approve, fix and reject work by click and keyboard (A/F/R), and the next card loads.
- [ ] English and Odia show side by side, with flags, passage and figure.
- [ ] Bulk approve shows the backend's refusal for flagged questions.
- [ ] Manual JSON upload shows per-item results.

## W3: Command Center, operations
**Build:** screens 1, 4, 8, 11, 12 in `05`.
**Tests**
- [ ] Reports group by question, and a report can fix, pause or dismiss.
- [ ] Settings changes take effect on the backend and appear in the audit log.
- [ ] A new API key is shown once.
- [ ] Today shows real counts.

## W4: Public site
**Build:** landing with waitlist, pricing, legal pages from `Legal Pages/` at `/terms`, `/privacy`, `/refund`, `/contact`, `/delete-account`, one SEO page per PYQ paper (our own summary of the paper's pattern and topics, the first 10 question pictures with alt text, then "practise the full paper free in the app"), using Emergent's Enable SEO setting.
**Tests**
- [ ] Lighthouse (mobile) ≥ 85 performance, ≥ 95 accessibility on the landing page.
- [ ] SEO pages have a unique title, description and canonical URL, are in `sitemap.xml`, and their text is visible to crawlers.
- [ ] Legal pages are reachable from the footer.
- [ ] A waitlist entry is stored through the backend and exports as CSV.

## W5: Web checkout
**Build:** student login and Razorpay checkout page with Pro status (no practice screens), in test mode.
**Tests**
- [ ] A test payment on the web shows Pro after logging into the Android app.
- [ ] A failed payment shows a clear message and no Pro.

---

## Secrets the owner provides (Secrets panel only)
**Bubbl Mobile:** `JWT_SECRET`, `APP_ENV`, `EMAIL_PROVIDER`, `EMAIL_API_KEY`, `EMAIL_FROM`, `GOOGLE_OAUTH_CLIENT_ID(S)`, `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET`, `REVENUECAT_API_KEY`, `REVENUECAT_WEBHOOK_SECRET`, `SENTRY_DSN`, `PUBLIC_WEB_URL`. The database connection is set by Emergent.
**Bubbl Web:** the backend address and `RAZORPAY_KEY_ID` (the public key only).
Never commit secrets, or paste them into chat or docs.
