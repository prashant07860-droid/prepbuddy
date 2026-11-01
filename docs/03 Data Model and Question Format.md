# Data Model and Question Format

The bank is **exam-agnostic**. A question belongs to a subject/topic and is *tagged* with the exams it suits. An **exam module** (OCS now, UPSC and other states later) is configuration: which subjects, which paper blueprints and which marking rules.

## 1. Subjects for launch (OCS Prelims syllabus, official)

Source: OPSC "Scheme and Syllabus" (Advt. 07 of 2024-25), Preliminary Examination.

**Paper I — General Studies (bank `gs`)**
| key | Subject (English) | Syllabus line |
|---|---|---|
| `current_affairs` | Current Affairs | Current events of national and international importance |
| `history_india` | History of India & National Movement | History of India and Indian National Movement |
| `history_odisha` | History of Odisha & Odia Nationalism | History of Odisha and Odia Nationalism |
| `geography` | Geography (Odisha, India, World) | Odisha and Indian Geography — physical, social, economic geography of India and the World |
| `polity` | Polity & Governance | Indian Polity and Governance — Constitution, Political System, Panchayati Raj |
| `public_policy` | Public Policy & Rights | Public Policy, Rights Issues, etc. |
| `economy` | Economic & Social Development | Sustainable development, poverty, inclusion, demographics, social sector initiatives |
| `environment` | Environment, Ecology & Climate | Environmental ecology, biodiversity and climate change |
| `science` | General Science | General Science |

**Paper II — CSAT (bank `csat`), qualifying**
| key | Subject |
|---|---|
| `comprehension` | Comprehension |
| `interpersonal` | Interpersonal & Communication Skills |
| `reasoning` | Logical Reasoning & Analytical Ability |
| `decision_making` | Decision Making & Problem Solving |
| `mental_ability` | General Mental Ability |
| `numeracy_di` | Basic Numeracy & Data Interpretation (Class X level) |

**Extra subjects (not in the OCS prelims syllabus, kept as "Extra practice")**
`agriculture` (useful for OPSC Assistant Agriculture Officer and OSSSC exams; the existing 2,600-question Agriculture bank goes here).

Each subject has **topics** (and optional subtopics). Topics are data in the `topics` collection; the pipeline creates them on import.

## 2. Collections (MongoDB)

| Collection | Purpose | Key fields |
|---|---|---|
| `exams` | Exam modules | `key` (`ocs`), `name`, `papers[]` (blueprints, `04` §3), `active` |
| `subjects` | Subject list | `key`, `bank` (`gs`/`csat`/`extra`), `name{en,or}`, `icon`, `color`, `order`, `exams[]` |
| `topics` | Topics per subject | `key`, `subject_key`, `name{en,or}`, `parent_key?` |
| `questions` | The bank (see §3) | |
| `pyq_papers` | Fixed past papers | `exam`, `year`, `paper` (`I`/`II`), `question_ids[]` in exam order, `duration_min`, `marking` |
| `attempts` | One practice session / mock | `user_id`, `mode`, `exam`, `paper?`, `subject?`, `level?`, `items[] {question_id, version, option_order[], answer?, time_ms, marked}`, `score`, `started_at`, `submitted_at` |
| `seen` | Per-user seen-question index | `user_id`, `question_id`, `last_seen_at`, `times`, `last_correct` |
| `progress` | Per user × subject | `level` (`easy`/`medium`/`hard`), `sets_done{easy,medium,hard}`, `accuracy{...}`, `unlocked[]` |
| `topic_stats` | Per user × topic | `answered`, `correct`, `accuracy`, `updated_at` |
| `gamification` | Per user | `xp`, `title`, `streak{current,best,last_day_ist,freezes_left}`, `badges[]` |
| `leaderboard_weekly` | Weekly XP rollup | `week_ist`, `scope` (`global`/`batch:<id>`), `user_id`, `display_name`, `xp` |
| `users` | Accounts | `email`, `name`, `display_name`, `phone?`, `password_hash?`, `google_id?`, `roles[]` (`student`,`centre_admin`,`admin`), `lang` (`en`/`or`/`both`), `exam`, `target_year`, `centre_id?`, `batch_id?` |
| `entitlements` | Pro access | `user_id`, `plan` (`pro`), `source` (`razorpay`/`play`/`centre`/`grant`/`coupon`), `starts_at`, `ends_at`, `ref` |
| `payments` | Every payment event | `provider`, `order_id`, `payment_id`, `amount_paise`, `status`, `raw` |
| `coupons` | Discount codes | `code`, `percent_off`/`amount_off`, `max_uses`, `used`, `valid_until` |
| `centres` | Coaching centres | `name`, `city`, `contact`, `licence{tier,seats,starts_at,ends_at}`, `join_code` |
| `batches` | Groups inside a centre | `centre_id`, `name`, `join_code`, `assigned_tests[]` |
| `reports` | Student error reports | `question_id`, `user_id`, `reason`, `note`, `status` (`open`/`fixed`/`dismissed`), `resolved_by` |
| `marketing_items` | Marketing review queue | see `05` §4 |
| `events` | Analytics events | `user_id?`, `name`, `props`, `ts` |
| `settings` | Admin-editable config | prices, free limits, cut-off marks, feature flags, blueprint weights |
| `api_keys` | Automation keys | `name`, `hash`, `scopes[]`, `created_at`, `last_used_at`, `revoked` |
| `audit_log` | Every admin/API write | `actor`, `action`, `target`, `before?`, `after?`, `ts` |

## 3. Question document

```json
{
  "id": "q_01J9ZK3M2X...",          // server-generated ULID
  "ext_id": "pipe-polity-000123",   // id from the importer; unique; makes import idempotent
  "bank": "gs",
  "subject_key": "polity",
  "topic_key": "fundamental_rights",
  "subtopic": "Article 21",
  "exams": ["ocs", "upsc"],
  "difficulty": "medium",            // easy | medium | hard
  "type": "statements",              // single | statements | how_many | match | assertion_reason | passage
  "passage_id": null,                // for comprehension sets: questions sharing a passage
  "text":        { "en": "...", "or": "..." },
  "options":     { "en": ["...","...","...","..."], "or": ["...","...","...","..."] },
  "correct": 2,                      // 0-3, index into options BEFORE any runtime shuffle
  "shuffle_ok": true,                // false when options refer to each other ("Both A and B", "All of the above") or are ordered (1 only / 1 and 2 only …)
  "explanation": { "en": "...", "or": "..." },
  "source": { "kind": "generated", "exam": null, "year": null, "paper": null, "qno": null },
                                     // kind: generated | pyq | legacy | manual
  "status": "pending",               // pending | approved | fix | rejected | live | paused
  "review": {
    "checks": { "duplicate_of": null, "ai_agree": true, "ai_answer": 2, "flags": [] },
                                     // flags e.g. ["ai_disagrees","near_duplicate","odisha_fact","date_sensitive","translation_low_conf"]
    "note": null,                    // owner's note when status = fix
    "decided_by": null, "decided_at": null
  },
  "stats": { "served": 0, "answered": 0, "correct": 0, "reports_open": 0, "avg_time_ms": 0 },
  "version": 1,
  "created_at": "2026-11-01T10:00:00Z",
  "updated_at": "2026-11-01T10:00:00Z"
}
```

Rules:
- `text.or`, `options.or` and `explanation.or` may be empty at import; the UI falls back to English and shows a small "Odia coming soon" tag.
- `options.en` and `options.or` must have the same length (4).
- Editing text/options/correct/explanation increments `version`; attempts keep the version they used.
- **Status workflow:**
  - `pending` → owner decides `approved` / `fix` / `rejected`
  - `approved` → goes `live` automatically (or in a nightly batch, per the Settings toggle)
  - `fix` → the automation reads the note, sends a corrected version back → `pending`
  - `live` → `paused` automatically on the report threshold (`05` §3) or manually
  - `paused` → `live` after review
- Only `live` questions are served to students.

## 4. PYQ (previous-year) questions
- Stored as normal questions with `source.kind = "pyq"`, `source.exam = "ocs"`, `source.year`, `source.paper`, `source.qno`.
- A `pyq_papers` document holds the fixed order. PYQ papers are served in their original order and are **never** shuffled.
- PYQ questions are also eligible for practice sets, marked with a "PYQ 2023" chip.
- Official OCS papers are bilingual (English + Odia), so Odia text comes from the paper itself.

## 5. Import format
- Import accepts a JSON array of question objects in the §3 shape, minus server fields (`id`, `stats`, `version`, timestamps).
- Validation errors are returned per item; valid items are inserted, invalid ones rejected with reasons.
- An `ext_id` that already exists is an update when its status is `fix`, and skipped otherwise.
- See `sample questions.json` for three valid examples.
