# The watchlist

One company field decides who is watched. One segment shows every watched company in one place. One small workflow adds companies, now and later, each with its full company record. Keeping the watch tag separate from where a company came from (lookalike, website visitor, CRM) means you can always add or remove a company without touching anything else.

Show the person this list and wait for a yes before creating anything.

## 1. Build it with the Clay Agent

The watchlist prompt in `clay-agent.md` creates:

- **Company fields** "Signals: watch", "Signals: why fit" and "Signals: source" (reused when they exist). The watch value is a short watchlist name, such as `agencies`. One field can hold several watchlists, each with its own value.
- **The segment** "Signals watchlist · <short offer name>", filtered on Signals: watch equals the value. If the person already has a live segment that should always be watched (for example website visitors that fit the ICP), ask the Clay Agent to add it to the filter with an "or", so new members join on their own. Ask first.
- **The "Signals: add to watchlist" workflow**: a manual trigger with every column of the record as an input, and one step that creates or updates the company by domain, skipping empty values. Record fields must come from an input, not a fixed value: Clay rejects a fixed value there. That is why `watch` is an input. It is registered as a routine, so the connector can run it, and it doesn't need publishing.

## 2. Full records first: Enrich Company

Every company gets its full record before it is added. Signals only need the domain, but the buyer workflow and the copy read the industry, size and country.

Forecast Enrich Company for the list (count times the price in settings) and ask. Run it through the connector in batches of up to 100 (`connector.md`), and save the fields the workflow takes to `$STATE`: name, website, LinkedIn page, industry, size, headcount, founded, revenue, description, logo, and headquarters city, state and country. When Enrich Company answers for a different company (another domain, a sister company), warn and show both. No data at all: the company is added with what the search gave.

## 3. Add the companies

Run the "add to watchlist" workflow through the connector, one input set per company, in batches of up to 100: the record from step 2, the watch value, the "why fit" line and the source (`lookalike: <seed name>`). It spends no data credits.

Test one company first, and check its record shows the watch value, website, headcount and city. Then the rest. Follow progress on one record rather than reading every result (`connector.md`). Then ask the Clay Agent to count the segment, and compare with the CSV. Clay's index lags a few seconds: if it is short, wait and count again before looking for who is missing.

## Adding and removing later

- **Add:** the person says "add acme.com to my signals watchlist". Enrich Company, then the workflow, for each domain.
- **Remove:** clear the company's watch field in Clay (Companies, open the company). Sending an empty `watch` through the workflow doesn't clear it, because the save step skips empty values.
- **See it:** Companies, Segments, the watchlist segment.
