# Enrich, check and find the people

Companies first. `companies.json` in `$RUN` holds every candidate; `people.json` is built from it once each company has its contacts. Run each routine on an items file (up to 100 items; split above that) and read the results with a high page limit: results come about 20 at a time by default, and without paging you silently lose rows. Save every result file in `$RUN`, and read the credit balance before and after each paid step.

## 1. Full company record: Enrich Company

- One item per keep and check company, by domain. The CLI accepts only a domain as the company identifier, not a LinkedIn link.
- Test on 2 first.
- It fills website, LinkedIn page, exact headcount, founded, company type, industry, revenue range, description, HQ city, state and country, and logo. Every company that reaches Clay carries this record: the people and company routines write it, and the campaign can use it as tokens.
- Under `min_staff` drops: too small for the offer.
- Over `max_staff` is often members, not staff (communities and networks). Judge by hand; don't drop on it.
- Enrich Company sometimes resolves to a sister company or a different office. Check the name it returns on the companies you keep.

## 2. Fit (free)

Read the full descriptions of keep and check companies again and confirm each decision. The recognition score in `seed-and-search.md` still applies: same service, same buyer, similar size, the seed's market.

- **Keep:** recognition at `keep_recognition` or more.
- **Check:** everything else. Read each check company's description and decide with the person. Typical calls: companies that serve consumers when the seed serves businesses, software vendors that sell to the seed's kind of company, and one-person consultancies are out, even when the description uses the right words.

Record hand decisions in `companies.json`; a hand decision is never overwritten. Clean company names that would read badly in a subject line ("Acme Marketing Inc", "Acme - B2B Ads Agency").

Show: kept companies with score and reason, the check list, and dropped counts by reason.

## 3. Exclusions (free)

The search already skips companies in your Clay Audiences. For companies added another way (the named list, by hand), read the domains of each list in settings "Already targeted" and drop matches, with the reason "already on another list".

## 4. Customers and open deals (free)

1. **Test first.** Put a known customer in the same check (the seed's domain, and one known customer person's LinkedIn link for the people check) and confirm both hit. Only then does an empty result mean clear.
2. Check every kept company against the customers list and the CRM (anything past the first stage, partnerships, won). Match companies by email domain, website and a cleaned company name (6 letters or more, so short names don't match everything), and people by LinkedIn link. Every real match drops the company. Short name keys give false matches: check each hit before dropping. You decide if one should come back.
3. Run the people part again once decision makers are found (step 5).
4. Optional: if you have a do-not-contact list, run check-do-not-contact on the list too.

## 5. Decision makers

### People search first

One people search limited to the kept and check companies, for current roles with {{BUYER_TITLES}} and {{SECOND_TITLES}}, skipping people already in your Clay Audiences.

- **Main contact rank:** CEO, then founder, then managing director, president, executive director or general manager, then COO, then other chiefs and partners.
- **Second decision maker:** the next best person at the same company. Skip partnership and channel roles. Only named in the opener, never emailed.
- **Never a leader:** titles with member, board, chapter, advisor, ambassador, fellow, volunteer, mentor, speaker, host, faculty, alumni, former, honorary, trustee, chair, region, assistant or vice. A community's chapter volunteers and board members look like leaders in search.
- **Employer names differ.** The name on a profile is often not Clay's company name ("Acme Network" for "The Acme Association"). List the names that matched no company, and map the right ones to their domain by hand before picking again.

Check the picks before moving on: this search returns noise (a chapter co-founder, a founder's assistant, a membership tier written as a job, a namesake company). Fix any pick by hand, or clear it.

### Find People at Company for the rest (credits, ask first)

For kept companies with no leader after the search, forecast Find People at Company from settings and ask. It returns at most 10 people per company, mostly staff and board, so it finds a leader at only a minority of companies: say so in the forecast. Unlike the search, it doesn't skip people already on a campaign list. Before it runs, read the LinkedIn links of the people on every list in settings "Campaigns" (and creator signals' past lists, if you have them) and leave those people out.

Then build `people.json` from `companies.json` (one main row, plus the second person, per company with a leader, each carrying the full company record), and run the people part of the customers check.

## 6. Work emails (main contacts only)

Inputs: full name, company domain, company name. Read the real spend from the credit balance before and after.

- An email at the company's own other domain is fine (acme.co.uk for acme.com).
- An email at another business (the founder's other company) drops the company.
- Then count companies with an email against `target_companies`, and say where the rest dropped out (no leader, no email). Below the target, go back to `seed-and-search.md` and change the strategy before building.

## People-first (the older flow)

Use it only when the seed's lookalikes are best found by job title rather than by company. It costs more and reads fit from less.

1. A people search for {{BUYER_TITLES}} with the same company filters (`company.industry`, `company.description`, `company.locations`) under `experiences.any(is_current = true ...)`. Pull about 2.5 people per company wanted, because about half survive.
2. **Domains: Enrich Person.** One item per person (their LinkedIn link). Percent-encode accented characters in links: one raw accent can make Clay reject the whole batch. Many founders hold several current jobs: take the domain of the experience at the company the search found. Blank a domain that is a social network or a platform, then check by hand.
3. **Headcount: Enrich Company**, one item per domain. People with no domain stay out: say who.
4. Score, exclude and check as above, then one search for the second decision maker at the kept companies.
