# Settings: lookalike campaigns

## Context

- **GTM context:** {{GTM_CONTEXT}}
- **Customers (with naming and quote permission):** {{CUSTOMERS_SOURCE}}
- **CRM:** {{CRM}}
- **Offer:** {{OFFER}}
- **Main decision maker titles:** {{BUYER_TITLES}}
- **Second decision maker titles:** {{SECOND_TITLES}}
- **Credibility line for version A:** {{CREDIBILITY_LINE}}

## Fit

- `min_staff`: 10
- `max_staff`: 250
- `keep_recognition`: 4 (4 or 5 is kept; below is "check", you decide)
- `survival_estimate`: 0.5 (about half the people pulled end up on the list)
- `target_companies`: 100

## Clay

- `enrich_person`: Enrich Person, `credits_each`: (read from Clay in setup)
- `enrich_company`: Enrich Company, `credits_each`: (read from Clay in setup)
- `work_email`: Work Email, `credits_each`: (read from Clay in setup)
- People fields: campaign tag, company display name, opener (ids added in setup)
- Company fields: list tag, ICP fit, seed, main contact, second contact (ids added in setup)
- "Add to campaign list" routine id: (added in setup)
- "Add to company list" routine id: (added in setup)

## Copy

- Opener with a second person: "I wasn't sure if you or [second first name] was the right one to contact for this."
- Opener without: "Not sure if you're the right one to contact for this at [company]."
- Nudge after: 3 days
- Banned phrases: saw your post, I noticed you, hope this finds you well, quick question, touching base, circle back, leverage, synergy, unlock, game changer

## Expand rule

{{EXPAND_RULE}}

## Already targeted

Company lists already used by this or another campaign. Their companies are never added again.

| List | Id | Campaign | Date |
| --- | --- | --- | --- |

## Campaigns

| Campaign | Seed | Campaign id | People list | Company list | People | Date | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
