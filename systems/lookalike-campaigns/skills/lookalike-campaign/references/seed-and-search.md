# The seed and the search

## 1. Confirm the seed

Find the seed in your customers list by domain, then by company name. Read only company-level fields: company, offer bought, industry, size, website, value, best customer, may we name them, quote, notes. Never print people's names or emails from it.

- **Check the name.** If the name you were given doesn't match a customer exactly, say what you found and ask. Similar names are often different companies.
- **Proof allowed.** Name only, or a quote. A quote needs the exact words on record, or your confirmation in this session that the person agreed.
- **Why it's a good seed.** One line: what they bought, the value, any result.

## 2. Read the seed in Clay

```bash
clay searches query-mode create --query 'select from companies where clay.include_company_identifiers(("<seed domain>"))'
clay searches query-mode run <searchId> --limit 1
```

Note industry, size bucket, HQ country and the description. The description often holds the best recognition hook (an award, a known client, a niche).

## 3. Write seed.json (the recognition profile)

In `$RUN`. Country codes as ISO-2, as Clay's Enrich Company returns them.

```json
{
  "name": "Acme",
  "domain": "acme.example",
  "why": "60-person B2B agency, bought the team program, may be named",
  "proof": "Sam, CEO: \"<exact quote, only if allowed>\"",
  "hook": "<a public fact from its own description>",
  "market_core": ["NL", "BE"],
  "market_wide": ["DE", "FR", "GB", "IE"],
  "size_min": 20,
  "size_max": 250,
  "service_phrases": ["demand generation", "b2b marketing", "account-based"],
  "buyer_phrases": ["b2b"]
}
```

- `market_core`: where the seed is based and plainly known. 2 points.
- `market_wide`: where the seed sells, has an office, or where its press reaches. 1 point. Keep to the seed's market unless you agree otherwise.
- `size_min` / `size_max`: roughly a third to four times the seed's headcount, inside the ICP card's range.
- `service_phrases`: what the seed sells, in the words companies use in their own descriptions.
- `buyer_phrases`: who the seed sells to.

**Recognition score (0 to 5):** same service +1, same buyer +1, similar size +1, market +2 (core) or +1 (wide). Keep at `keep_recognition` or more. Below that is "check": you decide.

## 4. The search

People search, one decision maker per company. A shape that works:

```
select from people where experiences.any(is_current = true
  and job_title is_similar_to (<main decision maker titles>)
  and company.industry in (<the seed's industry and its neighbours>)
  and company.company_size in (<size buckets around the seed>)
  and company.products_and_services is_similar_to (<3 or 4 phrases from service_phrases>)
  and company.description contains (<one buyer phrase>)
  and company.domain != "<seed domain>"
  and company.locations.any(is_headquarters = true and country_name in (<seed market countries>)))
  and clay.exclude_people_identifiers(@audience_segment("ALL"))
```

- The description filter is what keeps the wrong kind of company out. Without it, about half of a first sample can be off.
- Country names are full English names ("Netherlands", "United Kingdom"). Check the allowed values in the search reference.
- `@audience_segment("ALL")` skips people already in your Clay Audiences. It doesn't skip their colleagues: that's step 4.
- Save the search reference first and read it in parts.

## 5. Sample, then pull

1. `create`, then `run <id> --limit 10`. Save every page in `$RUN` and merge them into `people.json` by LinkedIn link.
2. Show the 10: company, HQ, decision maker, title, one line on fit and recognition. Adjust and resample until you say yes. Exclude people already pulled so a resample doesn't repeat them.
3. Pull the rest, 50 at a time, while there are more. Aim for about 2.5 people per company wanted, because about half survive and some are co-founders at the same company.
4. After each page, read the quota. If a page would leave under 15% of it, stop and ask. If Clay reports a per-search cap, stop and report it. Don't start a new search to dodge it.
