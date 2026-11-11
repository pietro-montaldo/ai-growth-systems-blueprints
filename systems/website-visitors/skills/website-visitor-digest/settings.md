# Settings: website visitor digest

Change any value here. The skill reads this file on every run.

## Sources

- **Website:** {{WEBSITE}}
- **GTM context:** {{GTM_CONTEXT}}
- **Visitor tool:** {{VISITOR_TOOL}}
- **How to read it:** {{VISITOR_SOURCE}}
- **Focus offer:** {{FOCUS_OFFER}}

## Destination

- **Send the summary to:** {{DESTINATION}}
- Send nowhere else.

## Window

- `lookback_hours`: {{LOOKBACK_HOURS}} (first run only; later runs start at the last run time)
- `return_window_days`: 30

## High-intent pages

A page counts as high intent when its path contains one of these words (the home page never counts):

{{HIGH_INTENT_PAGES}}

## Scoring in your visitor tool (optional)

Only if your visitor tool enriches and scores companies itself (`references/scoring.md`, section 4).

- `icp_version`: (added in setup; bump only when the scoring changes)
- `unknown_retry_days`: 7 (one retry for companies with no headcount, never a second)
- `enrich_company_price`: (read from Clay in setup; spent on every new company, on its own)
- Fields for the stored tier, ICP version and "enrich attempted" date: (ids added in setup)

## LinkedIn (read-only)

- `linkedin.tool`: {{LINKEDIN_TOOL}}
- `max_companies_per_run`: 8
- `max_people_per_company`: 2
- `company_cache_days`: 14
- Daily caps per kind of call: `limits`: 2, `search`: 15, `lead_activity`: 16, `recent_posts`: 1, `post_engagers`: 8
- `daily_total`: 40
- `min_seconds_between_calls`: 12, plus a random 0 to 8 seconds
- `stop_if_remaining_below`: 100 (when the tool reports how many calls are left)

These caps sit far below what LinkedIn tools allow, on purpose. Low, slow reads keep your account safe and leave room for anything else that uses it. Raise them only if you know what else runs on your account.
