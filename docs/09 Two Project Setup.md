# Two Project Setup

| | **Bubbl Mobile** | **Bubbl Web** |
|---|---|---|
| Emergent job | Mobile app, imported from `prepbuddy` | Web app (E-1, not NextJS), repo `bubbl-web` |
| Builds | Android app; FastAPI backend; MongoDB; all business logic | Command Center, landing, pricing, legal, SEO pages, web login, Razorpay checkout |
| Data | The only database | None. It calls the Bubbl Mobile backend |
| Students practise here | Yes | No (decided for launch) |

## Rules
- **One backend.** All data, limits, scoring, entitlements, webhooks and admin APIs live on Bubbl Mobile. Bubbl Web never copies that logic.
- **Backend address.** Bubbl Web reads the published backend address from an environment variable.
- **Allowed websites.** The backend starts open during the build. Before launch (E13) it must allow only bubblprep.in, www.bubblprep.in, the published Bubbl Web address and its preview address.
- **Preview and production data are separate.** Testing in preview uses sample data only. Real questions are imported only into the published backend.
- **Fake purchases** work only when `APP_ENV` isn't `production`.

## Platform limits to respect
- A project reads its repo only when the job starts, with no later pull. Later files arrive through chat upload.
- Android builds come from Emergent's Publish panel, using the last published code. Don't edit `eas.json` or run EAS directly.
- There are no over-the-air updates. An app change needs a new build and Play review; a backend change doesn't. So anything likely to change (prices, limits, blueprints, wording of notices) should be server-side settings, and the app should handle new setting values safely.
- Preview sleeps after 30 minutes.
- The database is managed by Emergent. Report if a feature needs anything it can't provide.

## Secrets
Entered by the owner in the Secrets panel only. See `08`.
