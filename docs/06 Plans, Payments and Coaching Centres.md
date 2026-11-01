# Plans, Payments and Coaching Centres

All prices and limits live in `settings` (editable in the Command Center). The server enforces every limit; the client only displays it.

## 1. Plans

| | **Free** | **Bubbl Pro** |
|---|---|---|
| Price | ₹0 | **₹149** for 12 months from purchase (launch price) |
| Daily Quiz (10 Q) | ✅ every day | ✅ |
| Easy level, every subject | ✅ unlimited | ✅ |
| Medium + Hard levels | 🔒 | ✅ |
| Full mocks (Paper I & II) | 1 of each per calendar month | Unlimited |
| Previous-year papers | Latest year (2025) | All years 2015–2025 |
| Weak-topic practice, Revision | 🔒 | ✅ |
| Detailed analytics (topic trends, time analysis) | Basic score only | ✅ |
| Streak freeze | — | 1 per week |
| Odia language | ✅ (always free) | ✅ |
| Leaderboard, badges, XP | ✅ | ✅ |
| Ads | None | None |

**Why this split:** the free tier is good enough to build a daily habit and be shared (Daily Quiz, Easy levels, 1 mock/month, latest PYQ). The natural upgrade moments are Medium unlocking, the 2nd mock in a month, and older PYQ years. Each one shows a paywall sheet saying exactly what Pro adds.

**Referral:** each user has a code. When a friend buys Pro with it, the referrer gets +1 month of Pro (max 6 months/year) and the friend gets ₹20 off (Settings).

**Refunds (proposed):** full refund on request within 7 days of purchase. Handled by the owner in Razorpay / Play Console; the app records it and ends the entitlement.

## 2. Entitlements (single source of truth)
- Access is decided only by the `entitlements` collection: a user is Pro if any entitlement has `starts_at ≤ now < ends_at`.
- Sources: `razorpay`, `play`, `centre`, `grant` (owner), `coupon` (100%-off codes), `referral`.
- Overlapping purchases extend: the new `ends_at` = max(current `ends_at`, now) + 12 months.

## 3. Payments

### 3.1 Web (and iPhone users via the web app) — Razorpay
- Razorpay **Orders API**: the server creates the order (amount from Settings, `receipt` = user id); the client opens Razorpay Checkout (UPI, cards, netbanking, wallets).
- **Verify on the server**:
  - checkout callback: payment signature (HMAC-SHA256 with the key secret)
  - the **webhook** (`payment.captured`, `refund.processed`): its signature, with the webhook secret
- The entitlement is created only by a verified webhook or a verified callback, and is idempotent per `payment_id`.
- Keys from env: `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET`. Use **test mode** keys until launch.
- Razorpay needs a live website with Terms, Privacy, Refund and Contact pages before activation (built in M6).

### 3.2 Android app — Google Play Billing
- Google Play requires Play's billing system (or its India "alternative billing" programme) for digital content sold **inside** the Android app. Use **Play Billing** for the Pro pass.
- Implement with **RevenueCat** (`react-native-purchases`, works with Expo dev builds / EAS). Product: one-time in-app product `pro_pass_12m` at ₹149.
- RevenueCat webhook → our server → entitlement `source: play`.
- Inside the Android app, **do not link or point to the web checkout** (Play policy). Users who bought on the web simply sign in, and Pro is recognised (entitlement is server-side).
- Testing needs an EAS development build + Play Console internal testing track (Emergent's Expo preview cannot test real billing). Keep a server-side "fake purchase" endpoint for preview/testing, enabled only when `APP_ENV != production`.

### 3.3 Invoices
- Email a simple receipt after every purchase (amount, date, plan, validity, payment id).
- GST is not charged at launch (owner not GST-registered yet). Settings gets a `gst_enabled` flag and GSTIN field for later.

## 4. Coaching-centre licences

### 4.1 Tiers (yearly, owner-editable)
| Tier | Seats | Price / year | Per student |
|---|---|---|---|
| Starter | up to 50 | ₹3,999 | ~₹80 |
| Growth | up to 150 | ₹9,999 | ~₹67 |
| Institute | up to 400 | ₹19,999 | ~₹50 |
| Extra seats | — | ₹59 / seat | — |

**Founding Partner offer:** the first 10 centres get 50% off year 1, plus their logo on the Bubbl website ("Partner institutes").

### 4.2 What a centre gets
- **Pro for every enrolled student** for the licence period (entitlement `source: centre`, ends with the licence).
- A **Centre Dashboard** (web, role `centre_admin`):
  - Batches with join codes; seats used / total
  - Assign a test: pick mode (mock / subject set / PYQ) and settings. The paper is generated **once** and is identical for the whole batch. Set an open/close date-time.
  - Batch results per test: ranks, average, topic-wise weak areas, students who didn't attempt
  - Batch leaderboard; CSV download of results
- Their name on the student's home screen ("Bubbl × Sai Coaching, Bhubaneswar").

### 4.3 Sales flow (Phase 1, manual)
1. The owner agrees the deal and creates the centre + licence in the Command Center.
2. Payment is taken by Razorpay **Payment Link** or bank transfer (outside the app). The owner marks it paid; this activates the licence.
3. The centre admin gets an invite email; students join with the batch code.
4. 30 days before expiry: renewal reminder email to the centre admin and the owner.
