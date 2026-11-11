# Enrich, score and check

Search gives a person, a title and a company **name** only. Domains come from Enrich Person, headcount from Enrich Company. Run each routine on an items file and read the results with a high page limit: results come about 20 at a time by default, and without paging you silently lose rows. Save every result file in `$RUN`.

## 1. Domains: Enrich Person

- Build one item per person (their LinkedIn link). Percent-encode accented characters in links: one raw accent can make Clay reject the whole batch.
- Test on 2 people first.
- Many founders hold several current jobs. Take the domain of the experience at the company the search found, not another one.
- Blank a domain that is a social network or a platform (linkedin.com and the like), then check by hand.

## 2. Headcount: Enrich Company

One item per domain. The CLI accepts only a domain as the company identifier, not a LinkedIn link. People with no domain stay out: say who.

## 3. Score

- **Drop:** no domain, no headcount, outside `min_staff` to `max_staff`, or a title that isn't a decision maker.
- **Keep:** recognition at `keep_recognition` or more (see `seed-and-search.md`).
- **Check:** everything else. Read each check company's description and decide with the person. Typical calls: companies that serve consumers when the seed serves businesses, software vendors that sell to the seed's kind of company, and one-person consultancies are out, even when the description uses the right words.

The score reads Clay's description words, so it misses some. Record hand decisions in `people.json`; a hand decision survives a re-score. Clean company names that would read badly in a subject line ("Acme Marketing Inc", "Acme - B2B Ads Agency").

Show: kept companies with score and reason, the check list, and dropped counts by reason.

## 4. Exclusions (free)

For each list in settings "Already targeted", read its companies' domains and drop them here, with the reason "already on another list".

## 5. Customers and open deals (free)

1. **Test first.** Run the check on one known customer domain and confirm it hits. Only then does an empty result mean clear.
2. Check every kept domain against the customers list and the CRM (anything past the first stage, partnerships, won). Every match drops the company. You decide if one should come back.
3. Optional: if you have a do-not-contact list, run check-do-not-contact on the list too.

## 6. Second decision maker (search quota only)

One search for the second decision maker titles, limited to the kept companies. Rank: co-founder and founder, then president, managing partner, COO and MD, then partner, then operations heads, then VPs. Skip partnership and channel roles. A second person at the same company from the main search is used first. Check the picks: this search returns noise (partner managers, namesake companies). The second person is only named in the opener, never emailed.

## 7. Work emails (main contacts only)

Inputs: full name, company domain, company name. Read the real spend from the credit balance before and after. An email at another domain is fine when it's the company's other domain; otherwise ask.
