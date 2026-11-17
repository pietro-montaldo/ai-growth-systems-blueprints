# Enrich, check and find the people

Companies first. `companies.json` in `$RUN` holds every candidate; `people.json` is built from it once each company has its contacts. Run each function through the connector in batches of up to 100 and read every page of results until the task is complete (`connector.md`): without paging you silently lose rows. For big batches, a helper agent runs the function, writes the fields the skill uses to `$RUN` and sends back short rows. After each step, set each company's `stage` in `companies.json`. Save every result in `$RUN`. To report real spend, ask the person to read the credit balance in Clay before and after a paid step.

## 1. Exclusions (free, before Enrich Company)

The companies searches already skip companies in your Clay Audiences. Run this before any credits are spent. Companies from the lookalike search, the named list or added by hand need a check: run one companies search through the connector for exactly those domains, leaving out Audiences:

```
select from companies where clay.include_company_identifiers((<domains>))
  and clay.exclude_company_identifiers(@audience_segment("ALL"))
```

The domains that come back are new. The ones that don't are already in Clay: drop them with the reason "already in Clay". Test it once with a domain you know is in Audiences (the seed, after setup's test run, or any earlier list), so a short answer means "already there", not "broken".

## 2. Customers and open deals (free)

1. **Test first.** Put a known customer in the same check (the seed's domain, and one known customer person's LinkedIn link for the people check) and confirm both hit. Only then does an empty result mean clear.
2. Check every keep and check company against the customers list and the CRM (anything past the first stage, partnerships, won). Match companies by email domain, website and a cleaned company name (6 letters or more, so short names don't match everything), and people by LinkedIn link. Every real match drops the company. Short name keys give false matches: check each hit before dropping. You decide if one should come back.
3. Run the people part again once decision makers are found (step 5).
4. Optional: if you have a do-not-contact list, run check-do-not-contact on the companies before any people are found, and on companies and people after.
5. **Drops stick.** A company dropped by this check, by the do-not-contact list or for an email at another business is marked dropped in `companies.json`, so rebuilding `people.json` never brings it back.

## 3. Full company record: Enrich Company

- One run per keep and check company, by domain.
- Test on 2 first.
- It fills website, LinkedIn page, exact headcount, founded, company type, industry, revenue range, description, HQ city, state and country, and logo. Every company that reaches Clay carries this record: the "add people" workflow writes it, and the campaign can use it as merge fields.
- Under `min_staff` drops: too small for the offer. If you want to keep one anyway, record it, so a later run doesn't drop it again.
- No headcount at all: the company goes to check, not keep. You decide.
- Over `max_staff` is often members, not staff (communities and networks). Judge by hand; don't drop on it.
- Enrich Company sometimes resolves to a sister company or a different office. When the domain it returns is not the one you asked for, warn and show both. Check the name it returns on the companies you keep.

## 4. Fit (free)

Read the full descriptions of keep and check companies again, now with their full records, and confirm each decision. The recognition score in `seed-and-search.md` still applies: same service, same buyer, similar size, the seed's market.

- **Keep:** recognition at `keep_recognition` or more.
- **Check:** everything else. Read each check company's description and decide with the person. Typical calls: companies that serve consumers when the seed serves businesses, software vendors that sell to the seed's kind of company, and one-person consultancies are out, even when the description uses the right words.

Record hand decisions in `companies.json`; a hand decision is never overwritten. Clean company names that would read badly in a subject line ("Acme Marketing Inc", "Acme - B2B Ads Agency").

Show: kept companies with recognition points (and which points: service, buyer, size, market) and reason, the check list, and dropped counts by reason. Every check company waits for your keep or drop. Only kept companies go on to the people search.

## 5. Decision makers

### People search first

People searches through the connector, up to 10 kept companies per call, limited to the kept companies that have no main contact and were not searched yet, for current roles with {{BUYER_TITLES}} and {{SECOND_TITLES}}. Check companies wait for your call first. The people search doesn't skip people already on your campaign lists: before step 8, compare the picks with the people on every list in settings "Campaigns" (read through the connector) by the profile part of their LinkedIn link, and leave them out. Running the search again only fills or improves contacts: earlier finds, Find People leaders and hand fixes stay, unless you ask to start over.

- **Main contact rank:** CEO, then founder, then managing director, president, executive director or general manager, then COO, then other chiefs and partners.
- **Second decision maker:** the next best person at the same company. Skip partnership and channel roles. Only named in the opener, never emailed.
- **Judge the first part of a title only**, before a "|", "·", "•" or " - ". "CEO | Keynote Speaker" counts as a CEO. "Speaker | Coach" has no leader word, so it doesn't.
- **Never a leader:** a first part with member, board, chapter, advisor, ambassador, volunteer, participant, emeritus, former, past, honorary, trustee, region or regional, assistant, vice, chief of staff, or partnership ("Head of Partnerships", "Partner Manager", "Channel Partner"). A community's chapter volunteers and board members look like leaders in search.
- **Employer names differ.** The name on a profile is often not Clay's company name ("Acme Network" for "The Acme Association"). List the names that matched no company, and map the right ones to their domain by hand before picking again. A short or blank employer name (under 4 letters) never matches anything, and partial matches need 6 letters or more on both sides.

Check the picks before moving on: this search returns noise (a chapter co-founder, a founder's assistant, a membership tier written as a job, a namesake company). Fix any pick by hand, or clear it.

### Find People at Company for the rest (credits, ask first)

For kept companies with no leader after the search, forecast Find People at Company from settings and ask. It returns at most 10 people per company, mostly staff and board, so it finds a leader at only a minority of companies: say so in the forecast. Unlike the search, it doesn't skip people already on a campaign list. Send the company's LinkedIn page with the domain when you have it. Before it runs, read the LinkedIn links of the people on every list in settings "Campaigns" (and creator signals' past lists, if you have them) and leave those people out. Compare by the profile part of the link (`/in/<name>`), not the whole link, and say who was left out.

Then build `people.json` from `companies.json` (one main row, plus the second person, per kept company with a leader, each carrying the full company record), and run the people part of the customers check. Check companies stay out until you decide; dropped companies never come back.

## 6. Work emails (main contacts only)

Inputs: full name, company domain, company name (all three are required).

- An email at the company's own other domain is fine (acme.co.uk for acme.com).
- An email at another business (the founder's other company) drops the company, and the drop sticks.
- A personal address (a free email provider) is not a work email: drop the person or find another.
- Run in batches of up to 100, and quote the credits in the forecast.
- Then count companies with an email against `target_companies`, and say where the rest dropped out (no leader, no email). Below the target, go back to `seed-and-search.md` and change the strategy before building. Each new batch is a new forecast and a new yes.

## People-first (the older flow)

Use it only when the seed's lookalikes are best found by job title rather than by company. It costs more and reads fit from less.

1. A people search for {{BUYER_TITLES}} with the same company filters (`company.industry`, `company.description`, `company.locations`) under `experiences.any(is_current = true ...)`. Pull about 2.5 people per company wanted, because about half survive.
2. **Domains: Enrich Person.** One item per person (their LinkedIn link). Percent-encode accented characters in links: one raw accent can make Clay reject the whole batch. Many founders hold several current jobs: take the domain of the experience at the company the search found. Blank a domain that is a social network or a platform, then check by hand.
3. **Headcount: Enrich Company**, one item per domain. People with no domain stay out: say who.
4. Score, exclude and check as above, then one search for the second decision maker at the kept companies.
