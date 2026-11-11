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
  "buyer_phrases": ["b2b"],
  "model_words": ["agency"],
  "group_domains": ["acme-labs.example"]
}
```

- `market_core`: where the seed is based and plainly known. 2 points.
- `market_wide`: where the seed sells, has an office, or where its press reaches. 1 point. Keep to the seed's market unless you agree otherwise.
- `size_min` / `size_max`: roughly a third to four times the seed's headcount, inside the ICP card's range.
- `service_phrases`: what the seed sells, in the words companies use in their own descriptions.
- `buyer_phrases`: who the seed sells to.
- `model_words`: words for the seed's business model as companies write it in their own descriptions ("agency", "community", "members", "network", "association"). Clay's industry alone pulls in the wrong model.
- `group_domains`: the seed's sister companies and parent. They are the seed's own company, not lookalikes: exclude them.

**Recognition score (0 to 5):** same service +1, same buyer +1, similar size +1, market +2 (core) or +1 (wide). Keep at `keep_recognition` or more. Below that is "check": you decide.

## 4. Finding the lookalikes: pick the best strategy for this seed

The goal is the best possible list, not the cheapest. Use the full range of Clay and spend credits where they buy quality: forecast each paid step (count times price, from settings) and ask once. **Clay's lookalike feature comes first**; the other tools fill its gaps. Show the plan (which tools, in what order, the forecast) before running it. Save the search reference first and read it in parts.

### 1. Find company lookalikes (first)

A Clay workflow action you run directly with the Clay CLI (`clay workflows actions search "lookalike companies"` finds it; `clay workflows actions schema` shows its inputs; `clay workflows actions test` runs it once). Inputs: the seed's domain, the seed market's countries, size buckets, and a `limit`.

- It charges per company returned (up to 50 a call), plus a little per call. Forecast it.
- Start with 10 and read them. Steer with description keywords (the model words), excluded keywords, industries and sub-industries, headquarters only. Keyword filters that are too tight return nothing and still cost the call.
- It takes several domains at once. Once you have confirmed fits, seed it with the seed plus 3 to 5 of the best, and also with each strong fit on its own: each seed pulls a different neighbourhood.
- It matches on Clay's industry, topic and size. When Clay files the seed under an industry that doesn't describe its model (a community filed under Education, say), the first batch is off. Fix the seed set or the keywords before pulling more, and lean on the tools below.
- Save each result in `$RUN` and merge it into `companies.json` with the search results, by domain.

### 2. The tools that fill the gaps

- **Clay companies search.** It returns domain, size bucket, HQ, industry, description and LinkedIn page per company, so fit can be read before people are pulled. A base query:

  ```
  select from companies where industry in (<the seed's industry and its neighbours>)
    and products_and_services is_similar_to ("<what the seed sells>", "<to whom>", "<a third angle>")
    and (description contains ("<model word>") or description contains ("<another model word>"))
    and company_size in (<size buckets around the seed>)
    and locations.any(is_headquarters = true and country_name in (<seed market countries>))
    and clay.exclude_company_identifiers((<seed domain>, <group_domains>, <domains already pulled>))
    and clay.exclude_company_identifiers(@audience_segment("ALL"))
  ```

  `products_and_services` takes at most 3 short values per query. The description filter carries the business model: without it, about half of a first sample can be off. Country names are full English names ("Netherlands", "United Kingdom"). `@audience_segment("ALL")` skips every company already in your Clay Audiences, which covers your earlier lookalike and signals lists.
- **Several narrower searches** when one broad query buries the fits. Split by whatever divides the seed's world (the segments it serves, specialties, sub-industries) and exclude every domain already pulled. For example, for a community of one profession the best fits were communities of other professions, one search each; for an agency it might be one search per specialty.
- **Competitor lookups** (Clay's CB Insights and Crunchbase actions) name the seed's direct peers for a fixed number of credits each. Run them on the seed and on the best fits.
- **A named list**: ask for, and add from your own knowledge, the seed's best-known peers. Check each one in Clay (`clay.include_company_identifiers((...))`). Never assume a domain: drop a name Clay resolves to a different company.
- **Enrich Company** on candidates you're unsure about, to judge from the full record (exact headcount, website, full description) instead of a short description.
- **People-first** (`enrich-and-check.md`, last section) when the lookalikes are best found by job title rather than by company.

Companies the lookalike action returns may already be in your Clay Audiences or on another list: the exclusion and customer checks (`enrich-and-check.md`) catch them, and the companies search skips them by itself.

Exclude the seed's own group (`group_domains`): a parent often runs several sister brands that look like perfect lookalikes. The estimated employee count can count members for communities and networks: judge exact headcount after Enrich Company.

## 5. Sample, pull, read

1. For each tool, start with 10 results. Show them with a one-line fit read each (company, HQ, size, what it does, recognition). Adjust and resample until you say yes.
2. Pull every page, 50 at a time, while there are more. Save every page in `$RUN` and merge them into `companies.json` by domain, noting which search found each one.
3. Read every description and mark each company with a reason:
   - **Keep:** same model as the seed, same kind of buyer, the seed's market.
   - **Check:** close but a different model (for example events-led media next to a community, or a body far from the seed's buyers). You decide.
   - **Drop:** a different business (agencies next to a community, venues, chambers, coaches, schools, software vendors that sell to the seed's kind of company, consumer brands).
   A decision made by hand is never overwritten later.
4. After each page, read the quota. If a page would leave under 15% of it, stop and ask. If Clay reports a per-search cap, stop and report it. Don't start a new search to dodge it.
5. Plan about `candidates_per_company` candidates per company wanted. Most drop on the description read, and some later have no leader or no email. Below the target after emails, come back here and change the strategy, not just the page count.
