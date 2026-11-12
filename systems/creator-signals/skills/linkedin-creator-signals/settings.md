# Settings: creator signals

Shared by all three creator signals skills. Change any value here.

## Context and destinations

- **GTM context:** {{GTM_CONTEXT}}
- **Offers in scope:** {{OFFERS_IN_SCOPE}}
- **Known people (skip them):** {{KNOWN_PEOPLE_SOURCES}}
- **Outreach file:** {{OUTREACH_FILE}}, made only on the LinkedIn path
- **Outreach folder:** {{DRIVE_FOLDER}} (folder id: added the first time you pick LinkedIn, if you use Google Drive)
- **Outreach file name:** "{{DRIVE_FOLDER}} YYYY-MM-DD"
- **Pause notes go to:** {{NOTIFY}}
- **Weekly run:** {{RUN_DAY}}

## Creators

You pick them. The first ones come from your answer when you copy the system; add more with the creators mode. Each one is checked against your competitors first.

| Name | Profile link | Why they fit | Competitor check | Added |
| --- | --- | --- | --- | --- |
{{CREATORS}}

## Apify

- `posts_actor`: harvestapi/linkedin-profile-posts
- `comments_actor`: harvestapi/linkedin-post-comments
- `comments_fallback_actor`: apimaestro/linkedin-post-comments-replies-engagements-scraper-no-cookies
- `posted_limit`: week
- `max_posts_per_creator`: 7
- `max_comments_per_post`: 500
- `price_usd_per_post`: 0.002
- `price_usd_per_comment`: 0.002
- `max_usd_posts`: 0.50 (the posts scrape runs without asking under this)
- `max_usd_month`: 20

Actor names and prices change. Check them in Apify during setup.

## Clay

- `enrich_function`: Enrich Person (input: the LinkedIn profile link)
- `email_function`: Work Email (inputs: full name, company name, company domain, profile link, and the company LinkedIn page when there is one)
- `company_function`: Enrich Company (input: the company domain)
- Routine ids for the three: (added in setup; run through the Clay CLI, at most 100 items per run)
- `never_use`: any "find contact details" bundle, any phone lookup
- `credits_per_enrich`: (read from Clay in setup)
- `credits_per_email`: (read from Clay in setup)
- `credits_per_company`: (read from Clay in setup)
- `action_credits_per_enrich`, `action_credits_per_email`, `action_credits_per_company`: (read from Clay in setup; a separate balance from data credits)
- `max_people_per_run`: 60
- `test_first`: 2

## Screening

- `min_words`: 5
- `ai_review_score`: 3 (3 or 4 goes to review)
- `ai_drop_score`: 5
- `keep_keyword_comments`: no

## Outreach

- `linkedin_max_chars`: 200 (fits a connection note and a DM)
- `email_steps`: 3 (first email plus 2 follow-ups)
- `banned_phrases`: saw your post, I noticed you, impressive to see, hope this finds you well, spot on, leverage, compelling, game changer, quick question, touching base, circle back, synergy, unlock, delve

## Saved campaigns

Agreed message versions, reused next week. Added by the outreach skills.

| Short name | Goal | CTA and link | Channel | Your template | Agreed version | Saved |
| --- | --- | --- | --- | --- | --- | --- |

## Email (filled by `creator-signals-email` setup)

- Clay people fields: campaign, company, post, cta, cta_date, cta_link (ids added in setup)
- "Add to campaign list" routine id: (added in setup)
- Routine inputs: email, first_name, last_name, full_name, linkedin_url, title, company, company_domain, company_linkedin, campaign, post, cta, cta_date, cta_link, and the company record: company_website, company_city, company_state, company_country, company_industry, company_headcount, company_founded, company_description, company_revenue, company_logo_url, and the person's own person_city, person_state, person_country, person_location, person_seniority (onto the person's City, State, Country, Location and Seniority). Required: email, campaign, company_domain. It adds the company by domain first with its full record (from Enrich Company), then the person, linked to that company. Items are built by the rule in `creator-signals-email/references/campaign.md`.
- Past campaigns and their one-off lists:

| Campaign | List | Run | People | Status |
| --- | --- | --- | --- | --- |
