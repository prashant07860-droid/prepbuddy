# Brand and UI Guide

## 1. Name and idea
- **Name:** **Bubbl** (all lowercase in the logo: `bubbl`). Store title: **"Bubbl: OCS & OPSC Exam Practice"**.
- **Idea:** the OMR answer sheet. Every aspirant has spent hours darkening bubbles with a blue or black ball pen. Bubbl turns that ritual into daily practice. Tagline: **"Fill the right bubble."** Odia tagline: **"ଠିକ୍ ବବଲ୍ ଭରନ୍ତୁ।"** (owner to confirm the Odia wording).
- **Nostalgia cues:**
  - chalkboard green (every classroom)
  - OMR coral-red (the colour answer sheets are printed in)
  - pencil yellow
  - ball-pen blue
  - cream exam-paper
- **Name checks still open (owner):** a trademark search on IP India (class 41 education / class 9 software), and buying `bubblprep.com` (available on 1 Nov 2026) and `bubblprep.in`. `bubbl.in` is already registered by someone else, so the web address is **bubblprep.in** / **bubblprep.com**.

## 2. Colour tokens

| Token | Light | Dark | Use |
|---|---|---|---|
| `board` | `#1E4D3B` | `#0F2A20` | Primary: headers, primary buttons, app bar |
| `chalk` | `#F6F3EA` | `#E9E5D8` | Text on board; light surfaces |
| `paper` | `#FBF8F1` | `#121A16` | App background |
| `card` | `#FFFFFF` | `#1A2520` | Cards, question surface |
| `omr` | `#E5484D` | `#FF6369` | Accent: the filled bubble, selected answer, CTAs like "Start mock" |
| `pencil` | `#F5B83D` | `#F7C55E` | XP, streak flame, badges, highlights |
| `ink` | `#2747C6` | `#7C93FF` | Links, info, "marked for review" |
| `graphite` | `#1F2328` | `#E6E8E6` | Body text |
| `muted` | `#6B7069` | `#9AA39D` | Secondary text |
| `correct` | `#1F9D55` | `#3CCB7F` | Correct answer in review |
| `wrong` | `#D93636` | `#FF6B6B` | Wrong answer in review |

Rules:
- `omr` is for the single most important action on a screen and the chosen answer. Never use it for large backgrounds.
- In review, wrong answers use `wrong`, not `omr`, so a selection doesn't read as an error.
- Contrast: body text ≥ 4.5:1 in both themes.

## 3. Type
- **Headings / numbers:** *Baloo Bhaina 2* (Google Fonts). It covers **Odia and Latin** in one family and has a friendly, rounded, Indian-designed feel. Weights 600/700.
- **Body / questions:** *Noto Sans* + *Noto Sans Oriya* (Google Fonts), 16–17 px question text, line-height 1.5. Questions must be very readable; no decorative fonts in question text.
- Never set Odia in a font without Odia glyphs (no tofu boxes). Load fonts with `expo-font`.

## 4. Signature UI elements
- **OMR answer options:** each option starts with a circle labelled A/B/C/D. Tapping fills the circle in `omr` with a quick "ink fill" animation (150 ms). This is the brand moment; keep it consistent everywhere.
- **OMR palette** in mocks: a grid of numbered bubbles (filled = answered, ring in `ink` = marked for review, empty = not visited), like the real sheet.
- **Chalkboard header** on Home: board-green panel with chalk-white text showing streak, XP and title.
- **Pencil-yellow streak flame** and XP chips.
- **Language switch:** a small `EN | ଓ` toggle on every question.
- Rounded corners 14 px on cards, 999 px on chips. Soft shadows only in light mode.

## 5. Logo and icon (files in `Brand Assets/`)
- `logo-wordmark.svg`: "bubbl" in Baloo-style rounded type. The bowl of the final **b** is a filled OMR coral bubble.
- `app-icon-1024.png` / `app-icon.svg`: board-green rounded square with a row of four OMR bubbles labelled A B C D, **B** filled coral (B for Bubbl).
- `adaptive-icon-foreground.png` (Android), `favicon.png`, `splash.png`, `play-feature-graphic-1024x500.png`.

## 6. Voice and tone
- Like a senior who cleared the exam: direct, warm, a little playful, never childish.
- Short sentences. Encourage, never shame ("7/10 — two away from Medium!" not "You failed").
- English UI with full Odia translation. Odia strings come from a single `i18n/or.json` that the owner reviews.
- Avoid: "guaranteed selection", fake urgency, fake "MRP" strike-throughs, unverifiable claims ("10 lakh students").

## 7. Accessibility
- Minimum tap target 44 px; supports system font scaling up to 130% without overlap.
- Colour is never the only signal (correct/wrong also show ✓/✗ icons).
- Screen-reader labels on bubbles: "Option B, selected".
