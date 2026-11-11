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

- `target_companies`: {{TARGET_COMPANIES}} (companies with a Clay-found work email, not candidates; keep searching until reached)
- `min_staff`: {{MIN_STAFF}} (checked on Enrich Company's exact headcount; under it drops unless you keep it; no headcount goes to check)
- `max_staff`: 250 (over it is judged by hand: communities and networks often count members as staff)
- `keep_recognition`: 4 (4 or 5 is kept; below is "check", you decide)
- `candidates_per_company`: 4 (plan about 4 companies searched per company that ends with an email)
- `survival_estimate`: 0.5 (people-first flow only: about half the people pulled end up on the list)

## Clay

- `enrich_company`: Enrich Company, `credits_each`: (read from Clay in setup; every keep and check company)
- `find_people`: Find People at Company, `credits_each`: (read from Clay in setup; only kept companies the people search found no leader for; at most 10 people each)
- `work_email`: Work Email, `credits_each`: (read from Clay in setup; main contacts only)
- `enrich_person`: Enrich Person, `credits_each`: (read from Clay in setup; people-first flow only)
- `find_lookalikes`: Find company lookalikes, the first source in every run, `credits_each`: (read from Clay in setup; per company returned, plus a little per call)
- `competitors`: competitor lookups, `credits_each`: (read from Clay in setup; per lookup)
- Action credits per run of each of the above: (read from Clay in setup; a separate balance, quoted in every forecast)
- People fields: campaign tag, company display name, opener, seed, second contact, second contact title, and the company record: domain, website, LinkedIn page, city, state, country, industry, headcount, founded, description, revenue, logo (ids added in setup)
- Company fields: list tag, ICP fit, seed, main contact, second contact, website, description, founded (ids added in setup)
- "Lookalikes: add people to list" routine id: (added in setup). Adds the company by domain first with its full record, then the person, linked to that company. `company_domain` is required.
- "Lookalikes: add companies to list" routine id: (added in setup)

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

Find People at Company doesn't skip people already on a campaign list, so before it runs, read the people lists below (and creator signals' past campaign lists, if you have them) and leave those people out.

| Campaign | Seed | Campaign id | People list | Company list | People | Date | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
