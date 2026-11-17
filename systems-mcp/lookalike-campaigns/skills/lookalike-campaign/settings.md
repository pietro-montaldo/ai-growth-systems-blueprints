# Settings: lookalike campaigns (Clay connector + Clay Agent)

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
- `candidates_per_company`: 4 (plan about 4 companies searched per company that ends with an email; up to 20 with a strict bar in a small market)

## Clay

- `clay_agent`: {{CLAY_AGENT}} (yes: Claude types the prompts into the Clay Agent in the built-in browser; no: Claude walks you through the same steps in Clay by hand)
- "Lookalikes: add people to list" workflow id: (added in setup, from the connector's list of routines). Adds the company by domain first with its full record (website, LinkedIn, city, state, country, industry, headcount, founded, description, revenue, logo), then the person, linked to that company, with the person's own city, state, country and location. Required: `company_domain`, `email`, `campaign`. `company_headcount` and `company_founded` are numbers.
- People fields (made in setup): Lookalike campaign, Lookalike opener, Lookalike company, Lookalike seed, Lookalike second contact, Lookalike second contact title
- Prices, data credits per run (added in setup, step 3; the connector can't read them):
  - Find company lookalikes: (per company returned; no charge per call, so a call that returns nothing costs nothing)
  - Enrich Company: (every keep and check company)
  - Find People at Company: (only kept companies the people search found no leader for; at most 10 people each)
  - Work Email: (main contacts only)
- Connector spend cap per user: (read in Clay settings, Agent users)

## Copy

- Opener with a second person: "I wasn't sure if you or [second first name] was the right one to contact for this."
- Opener without: "Not sure if you're the right one to contact for this at [company]."
- Nudge after: 3 days
- Banned phrases: saw your post, I noticed you, hope this finds you well, quick question, touching base, circle back, leverage, synergy, unlock, game changer

## Expand rule

{{EXPAND_RULE}}

## Campaigns

Find People at Company doesn't skip people already on a campaign list, so before it runs, read the people on the lists below and leave them out. Filled when you copied the system if you had past campaigns then, and after each run.

| Campaign | Seed | People list | People | Date | Status |
| --- | --- | --- | --- | --- | --- |
