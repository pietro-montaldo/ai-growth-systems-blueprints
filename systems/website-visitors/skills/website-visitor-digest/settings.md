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
