# Practice Engine, Exam Rules and Gamification

## 1. Principle
There are **no pre-built "Paper 1…100" documents.** Every attempt is assembled on the server from `live` questions at the moment the student starts it. A student gets effectively unlimited, non-repeating practice. The only fixed papers are previous-year papers (`pyq_papers`).

## 2. Modes

| Mode | Size | Timer | Marking | Pick rule | Free / Pro |
|---|---|---|---|---|---|
| **Daily Quiz** | 10 Q | none (shows time taken) | +1 / 0 | Same 10 Q for everyone that IST day. Mixed subjects, mostly easy/medium. Chosen at 00:00 IST, admin can override. | Free |
| **Practice Set** | 10 / 20 / 30 (student picks) | optional | practice (no negative) | One subject + the student's current level; unseen first | Easy: Free · Medium/Hard: Pro |
| **Level Test** | 25 Q | 30 min | exam marking | Subject + level; used to unlock the next level | Easy test Free · others Pro |
| **Full Mock — Paper I** | 100 Q | 120 min | +2 / −0.66 | OCS Paper I blueprint (§3) | 1 per month Free · unlimited Pro |
| **Full Mock — Paper II (CSAT)** | 80 Q | 120 min | +2.5 / −0.83 | OCS Paper II blueprint | 1 per month Free · unlimited Pro |
| **Previous Year Paper** | as set | as set | as set | Fixed paper and order | Latest year Free · all years Pro |
| **Weak-Topic Practice** | 20 Q | optional | practice | Topics with accuracy < 50% over ≥ 10 answered | Pro |
| **Revision** | up to 30 | optional | practice | Bookmarked + previously wrong | Pro |
| **Centre Test** | set by centre | set by centre | exam marking | Generated once by the centre admin, then identical for every student in the batch | Centre students |

All limits come from `settings` so the owner can change them without a release.

## 3. OCS exam rules (official, from the OCS 2025 test booklets and the scheme & syllabus)

| | Paper I — General Studies | Paper II — General Studies (CSAT) |
|---|---|---|
| Questions | 100 | 80 |
| Marks | 200 (2 per question) | 200 (2.5 per question) |
| Time | 2 hours | 2 hours |
| Wrong answer | −⅓ of the question's marks (−0.66) | −⅓ of the question's marks (−0.83) |
| Multiple responses | treated as wrong (penalty applies) | same |
| Unanswered | 0 | 0 |
| Merit | counts | **qualifying only: 33% = 66 / 200** |
| Language | English and Odia in the same booklet; English prevails if the meaning differs | same |

**Paper I blueprint (provisional — counts per subject in a 100-Q mock).** The question pipeline will recompute these from the 2015–2025 papers and the owner will update them in Settings.

| current_affairs | history_india | history_odisha | geography | polity | public_policy | economy | environment | science |
|---|---|---|---|---|---|---|---|---|
| 15 | 12 | 8 | 15 | 14 | 4 | 12 | 10 | 10 |

Difficulty mix inside a mock: 25% easy / 50% medium / 25% hard (Setting).

**Paper II blueprint (provisional):** comprehension 20, interpersonal 8, reasoning 16, decision_making 8, mental_ability 12, numeracy_di 16.

## 4. Assembly algorithm (server)
1. Build the candidate pool: `status = live`, matches the subject / level / exam / blueprint slot.
2. Remove questions this user has seen (`seen` collection). If a slot's unseen pool is too small, fall back to the oldest-seen questions, preferring ones the user got wrong.
3. Choose randomly within each slot, spreading across topics (no more than 3 from the same topic in a 20-Q set unless the pool is exhausted).
4. Comprehension (`passage_id`): pick whole passages, never split one.
5. For each item, if `shuffle_ok`, store a random `option_order` on the attempt; otherwise keep the original order.
6. Store the attempt with question ids + versions + option order; return the full paper to the client in one response (for offline resilience).
7. Target: < 500 ms for a 100-Q mock on a bank of 50k questions (indexes on `status, subject_key, difficulty, exams`).

## 5. Scoring and results
- Score with the mode's marking rule. Store correct / wrong / skipped / marked / time per question.
- Results screen shows:
  - score and accuracy
  - for mocks: the estimated score vs the admin-set "last year's cut-off" reference
  - subject and topic breakdown
  - fastest/slowest questions
  - the full review with explanations, in the student's language
- Update `seen`, `topic_stats` and `progress`; award XP (§6).
- Every question in review has **Bookmark** and **Report an error** buttons.

## 6. Gamification

### 6.1 Levels (per subject)
- Every subject starts at **Easy** (unlocked).
- **Medium unlocks** when either: 5 Easy practice sets done with ≥ 60% average accuracy, **or** an Easy Level Test passed at ≥ 70%.
- **Hard unlocks** the same way on Medium (≥ 65% avg over 5 sets, or a Level Test ≥ 70%).
- Medium and Hard need Pro. The unlock moment shows: "Medium unlocked! Continue with Pro" (the main paywall moment).
- The student can always go back down a level.

### 6.2 XP
| Action | XP |
|---|---|
| Question answered | +2 |
| Correct answer | +10 (× 1.2 Medium, × 1.5 Hard) |
| Practice set completed | +20 |
| Full mock completed | +100 |
| PYQ paper completed | +100 |
| Daily Quiz completed | +30 |
| Streak day (from day 3) | +20 |
| Error report confirmed by admin | +50 (rewards careful students) |

### 6.3 Streaks
- A streak day counts when the student answers **≥ 10 questions** in that IST day.
- Pro gets 1 **streak freeze** per week (auto-applied once on a missed day).
- At 21:00 IST, send a push reminder if today's streak isn't done (opt-in; Expo notifications).

### 6.4 Titles (civil-services ladder — nostalgia + aspiration)
| XP | Title (EN) | Title (OR) |
|---|---|---|
| 0 | Aspirant | ପରୀକ୍ଷାର୍ଥୀ |
| 1,000 | Prelims Ready | ପ୍ରାରମ୍ଭିକ ପ୍ରସ୍ତୁତ |
| 5,000 | Mains Ready | ମୁଖ୍ୟ ପ୍ରସ୍ତୁତ |
| 15,000 | Interview Ready | ସାକ୍ଷାତକାର ପ୍ରସ୍ତୁତ |
| 40,000 | Collector Saheb | କଲେକ୍ଟର ସାହେବ |

(The Odia titles are placeholders — the owner reviews all Odia UI strings.)

### 6.5 Badges (first set)
First Bubble (first answer) · Daily Dose (7-day streak) · Iron Habit (30-day streak) · Mock Master (10 full mocks) · Time Traveller (all PYQ papers of 3 different years) · Odisha Gyani (≥ 80% over 200 Odisha-history questions) · Subject Topper (≥ 75% over 100 Hard questions in a subject) · Bug Hunter (first confirmed error report) · Night Owl (mock submitted after 22:00 IST).

### 6.6 Leaderboards
- Weekly XP, resets Monday 00:00 IST. Scopes: **All Odisha**, **My batch** (centre students), **Friends** (invite code; Phase 2 if needed).
- Show a display name + title only. Students can hide themselves from leaderboards in Settings.

### 6.7 Weak topics
- Home and Results show the 3 weakest topics (accuracy < 50%, ≥ 10 answered) with a "Fix it — 20 questions" button.

## 7. Shareable result card (marketing loop)
After the Daily Quiz and mocks, the student can share an image card ("I scored 8/10 on today's Bubbl OCS quiz — can you beat me?") with the app link and their referral code. Render it client-side; share via the native share sheet (WhatsApp first).

## 8. Analytics events (stored in `events`, shown in the Command Center)
`app_open`, `signup`, `guest_start`, `quiz_start`, `quiz_complete`, `set_start`, `set_complete`, `mock_start`, `mock_submit`, `pyq_start`, `level_unlocked`, `paywall_view`, `checkout_start`, `purchase_success`, `purchase_fail`, `report_submitted`, `share_card`, `streak_extended`, `streak_lost`, `centre_join`.
