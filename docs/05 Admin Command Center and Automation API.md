# Admin Command Center and Automation API

The owner runs the whole business from one web dashboard, the **Command Center**, in about 5–10 hours a week. External automations (question pipeline, Current Affairs updater, marketing generator) do the heavy work and put items into **review queues**. The owner approves, asks for a fix, or rejects. The automations read those decisions and act on them.

Every queue uses the same status language: **pending → approved / fix (with a note) / rejected → live (or posted)**.

## 1. Where it lives
- Routes under `/admin/*` in the **same Expo project**, used on the web build (desktop layout, min width 1024 px). It needs the `admin` role.
- Backend routes under `/api/admin/*` (session JWT with the `admin` role) and `/api/admin/v1/*` for automations (API key).

## 2. Screens

| # | Screen | What it shows / does |
|---|---|---|
| 1 | **Today** (home) | KPI tiles: new users, DAU, Pro purchases + revenue (today / 7d / 30d), questions answered, mocks completed. To-do counts: pending reviews, open reports, marketing items waiting. Content coverage table: live questions per subject × level (red when < 200). |
| 2 | **Question Review** | Queue of `pending` questions, flagged ones first. Card shows: English + Odia side by side, options with the marked answer, explanation, the AI cross-check result, flags (`ai_disagrees`, `near_duplicate`, `odisha_fact`, `date_sensitive`, `translation_low_conf`), source and topic. Actions: **Approve (A)**, **Fix (F)** → note box, **Reject (R)**, **Edit inline** (saves as a new version, then approve). Keyboard shortcuts; next card loads automatically. Bulk: "Approve all unflagged in this batch" — this needs a typed confirmation and is allowed only after at least 20 of that batch have been reviewed by hand. Filters: subject, topic, flag, batch id, source. |
| 3 | **Question Bank** | Search all questions (text, id, subject, status). Per question: live stats (served, % correct, avg time, reports), version history, pause/unpause, edit. Highlights: questions with % correct < 15% or > 97% (likely wrong key or too easy). |
| 4 | **Error Reports** | Open reports grouped by question (count, reasons, notes). Actions: **Fix** (edit → live), **Pause question**, **Dismiss**. Confirming a report awards the reporter XP (`04` §6.2). **Auto-pause:** a question with ≥ 3 open reports with reason "wrong answer" from different users is set to `paused` until reviewed. |
| 5 | **Imports** | Log of every import (API or file upload): time, source key, counts (inserted / updated / skipped / invalid), downloadable error list. Manual JSON upload for one-off files. |
| 6 | **PYQ Papers** | List per exam/year/paper; mark a paper published once all its questions are `live`. |
| 7 | **Marketing Queue** | Items from the marketing automation (§4): quiz cards, Reels/Shorts scripts, Telegram/WhatsApp posts, blog/SEO pages. Preview image/video, caption, planned date/channel. Actions: Approve / Fix + note / Reject; after posting, the automation (or owner) marks it `posted` with a link. |
| 8 | **Users & Plans** | Search users; view plan, entitlement history, payments, attempts. Actions: grant Pro (with reason), revoke, refund marker (refunds are done in Razorpay; the app records them). |
| 9 | **Coaching Centres** | Create centre, set licence tier/seats/dates, generate join codes, see seats used, batch list, batch performance. |
| 10 | **Coupons** | Create/disable codes, see redemptions. |
| 11 | **Settings** | Prices, free-tier limits, mock blueprints, difficulty mix, cut-off reference marks, auto-pause threshold, auto-publish (immediate vs nightly), daily quiz override, feature flags (leaderboard on/off, Odia on/off, centre tests on/off). |
| 12 | **API Keys & Audit Log** | Create/revoke scoped keys (key shown once); audit log of every admin and API write. |

## 3. Review rules (built into the app)
- Questions with **no flags** that pass automated checks still need owner approval, but can be bulk-approved under the rule in Screen 2.
- Questions flagged `ai_disagrees`, `odisha_fact` or `date_sensitive` **must** be reviewed one at a time (no bulk approve).
- `approved` becomes `live` immediately, or at 02:00 IST nightly if auto-publish is set to nightly.
- The Today screen shows the **weekly owner time estimate**: pending flagged × 1 min + reports × 2 min + marketing × 1 min.

## 4. Marketing item document (`marketing_items`)
```json
{
  "id": "mk_...", "ext_id": "auto-2026-11-20-quizcard",
  "kind": "quiz_card | reel_script | reel_video | telegram_post | whatsapp_post | seo_page",
  "channel": "instagram | youtube | telegram | whatsapp | web",
  "title": "...", "body": "...", "caption": "...",
  "media": [{ "type": "image|video", "url": "https://..." }],
  "planned_for": "2026-11-20T09:00:00+05:30",
  "status": "pending | approved | fix | rejected | posted",
  "note": null, "posted_at": null, "permalink": null
}
```
The app stores and displays these; it does **not** post to social networks itself in Phase 1.

## 5. Automation API (`/api/admin/v1`)
Auth: header `X-Api-Key: <key>`. Keys are stored hashed and have scopes. Every call is written to `audit_log`. Rate limit: 60 req/min per key. JSON in/out. Times in ISO-8601 UTC.

| Method & path | Scope | Purpose |
|---|---|---|
| `POST /questions/import` | `questions:write` | Body `{batch_id, items:[question…]}` (max 500 items). Inserts as `pending`; `ext_id` makes it idempotent; an `ext_id` whose current status is `fix` is updated and returns to `pending`. Response: per-item result `{ext_id, id?, result: inserted|updated|skipped|invalid, errors[]}`. |
| `GET /questions?status=&updated_since=&subject_key=&limit=&cursor=` | `questions:read` | Read decisions (e.g. all `fix` questions with notes, all `rejected` since a time). |
| `PATCH /questions/{id}` | `questions:write` | Partial update of content fields (new version → `pending`). Cannot set `live`. |
| `GET /reports?status=open` | `reports:read` | Lets the pipeline pre-check reported questions and suggest fixes. |
| `POST /reports/{id}/suggestion` | `reports:write` | Attach a suggested correction for the owner to approve. |
| `POST /marketing/items` | `marketing:write` | Create pending marketing items (max 50). |
| `GET /marketing/items?status=&updated_since=` | `marketing:read` | Read decisions. |
| `PATCH /marketing/items/{id}` | `marketing:write` | Set `posted`, `posted_at`, `permalink`, or update content after `fix`. |
| `POST /media` | `marketing:write` | Upload an image/video (≤ 50 MB) → returns a URL for marketing items. |
| `GET /metrics/summary?from=&to=` | `metrics:read` | KPIs for the weekly business report (users, DAU, purchases, revenue, content coverage, report counts). |
| `GET /coverage` | `questions:read` | Live/pending counts per subject × topic × difficulty, so the pipeline knows what to generate next. |
| `GET /settings/blueprints` / `PUT /settings/blueprints` | `settings:write` | Read/update mock blueprints (the PUT is logged and visible in Settings). |

The automation API **cannot**: set questions `live`, delete anything, read user personal data, or change prices.
