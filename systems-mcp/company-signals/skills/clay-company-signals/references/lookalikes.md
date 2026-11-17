# From one seed company to a lookalike list

All of this runs through the Clay connector's companies search (search quota, no credits). Its query language is the one the connector's search tool describes.

## 1. Read the seed company

Ask for the seed's website. Pull just that one company:

```
select from companies where clay.include_company_identifiers(("acme.com"))
```

Note its industry, size bucket, headquarters country and description. Say back in two lines what makes it a good customer, using the GTM context (why it bought, what it bought). That is what the lookalikes must share.

## 2. Draft the search

Combine the seed and the ICP card. Show the person the filters in plain words before running anything:

| Filter | Where it comes from |
|---|---|
| `industry in (...)` | The seed's industry plus 1 to 3 close ones the ICP card names |
| `company_size in (...)` | The ICP card's headcount range, as Clay's size buckets |
| `locations.any(is_headquarters = true and ...)` | The ICP card's geography. If geography is only a preference, start with the preferred regions |
| `products_and_services is_similar_to (...)` | 2 or 3 short phrases for what the seed sells, in the buyer's words |
| `clay.exclude_company_identifiers(@audience_segment("ALL"))` | Leaves out every company already in your Clay Audiences |
| `clay.exclude_company_identifiers((...))` | Customers, open deals, competitors (step 4 below) |

Use `industry` for verticals, not description keywords. Keep it to what the ICP actually requires: every extra filter shrinks the list.

**Careful with "uses our category" filters**, for example "an employee mentions the tool you train on". They tend to return companies that build or sell that tool, not companies that buy help with it. Prefer the ICP's firmographics, and let the signals find the buying moment.

## 3. Sample, then adjust

Results come 20 to a page. Read the first page, show 10 as a short table (name, website, industry, size, country, one line on fit) and ask what's off. Typical fixes: too many competitors (exclude their industry or add a `not products_and_services is_similar_to`), too big or small (size buckets), wrong country. Repeat until the person says the sample looks right. The connector doesn't show the search quota: if a search stops with a quota or limit error, stop and say so. Never start extra searches to get round it.

## 4. Exclusions

Collect the domains that must never be on the list:

- **Customers** from the GTM context. A company client blocks its whole domain. A person who bought on their own blocks only themselves, not their employer.
- **Open and recent deals** in the CRM, if the person has one: anyone at a stage past first contact, plus lost deals.
- **Competitors** from the GTM context.
- **Do-not-contact**: if the person has the list, run check-do-not-contact on the final CSV instead (step 6).

Put company domains into one `clay.exclude_company_identifiers((...))` call. Rows with a company name but no domain are matched by name after the pull. Test the check once with a domain you know is a customer, so an empty result means clear, not broken.

## 5. Pull the list

About half of the search results survive a fit check. To end with N companies, read about N × 1.5, page by page (ask for the next page while there are more). Every page lands in the chat, about 12,000 tokens each: for more than a few pages, give the pages to a helper agent that writes short rows to `$STATE` (`connector.md`, "Big runs").

## 6. Fit check and save

Go through every company and drop clear misfits against the ICP card's disqualifiers: competitors, companies that sell what you sell, subsidiaries of big groups when the ICP wants founder-led firms, nonprofits or schools when the ICP is commercial, and so on. Keep borderline ones and flag them.

Save `$STATE/<YYYY-MM-DD>-signals-watchlist.csv` with columns: `domain, company_name, linkedin_url, industry, size, country, why_fit, source`. Use `lookalike: <seed name>` as the source.

If the do-not-contact list exists, run check-do-not-contact on the CSV and keep only its keep file.

Show: how many were read, dropped (with reasons) and kept, and the top 10. Wait for an OK before step 3.
