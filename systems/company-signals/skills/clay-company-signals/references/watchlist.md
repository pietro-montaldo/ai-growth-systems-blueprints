# The watchlist

One company field decides who is watched. One segment shows every watched company in one place. One small workflow adds companies, now and later, each with its full company record. Keeping the watch tag separate from where a company came from (lookalike, website visitor, CRM) means you can always add or remove a company without touching anything else.

Show the user this list and wait for a yes before creating anything.

## 1. The watch field

```bash
clay audiences fields list --entity-type companies
clay audiences fields create --entity-type companies --name "Signals: watch"
```

Reuse the field if it already exists. Its value is a short watchlist name, such as `agencies` or `saas-50-200`. One field can then hold several watchlists, each with its own value.

## 2. The segment

Create a company segment named "Signals watchlist · <short offer name>" whose filter is: Signals: watch equals `<value>`. Read `clay audiences create --help` for the filter shape, and copy the `dataPath` pattern from an existing segment (`clay audiences get <id>`).

If the user already has a live segment that should always be watched (for example website visitors that fit the ICP), add it with an `Or` group, so new members join on their own. Ask first.

## 3. The add-to-watchlist workflow

Create a workflow named "Signals: add to watchlist" with:

- **A manual trigger** whose inputs are `domain` and `watch` (both required), plus every column the lookalike CSV has: `company_name`, `linkedin_url`, `industry`, `size`, `country`, `why_fit`, `source`.
- **"Enrich company"**: a tool node with Clay's "Enrich company" action (`cpj-enrich-company-v2`; find it with `clay workflows actions list`), company identifier = `{{domain}}`, identifier type = company domain. Its fields are under `$.result.*`: `name`, `website`, `url` (LinkedIn), `employee_count`, `founded`, `industry`, `size`, `country`, `annual_revenue`, `description`, `logo_url`, `locations`, `structured_locations`, `locality`.
- **"Pick headquarters"**: a code node with `assets/pick_headquarters.py`. It picks the HQ city, state and address from the location lists.
- **"Add company to watchlist"**: the Audiences action "Create or update Audiences record" (`upsert-audiences-record`), entity type ACCOUNT, looked up by domain, skipping empty values (`removeNullValues` true). It writes the full record:
  - **CSV first, then Enrich Company** where both exist (a `coalesce`): name (`org_name`), LinkedIn page (`linkedin_url`), industry, size (a "Company size" text field), country (`location_country`).
  - **From Enrich Company only:** website, `employee_count`, founded, `revenue`, description, `logo_url`, and from the code step `location_city`, `location_state` and the headquarters location.
  - **From the CSV only:** the watch field, plus "why fit" and "source" text fields.

  Create missing fields first with `clay audiences fields create --entity-type companies`, after a yes, and read every id from `clay audiences fields list --entity-type companies`. Custom fields such as Website, Founded and Company description have their own ids.

Record fields must be mapped from an input, not typed in as a fixed value: Clay's check rejects a fixed value there. That is why `watch` is a trigger input.

Validate it with `clay workflows graph validate`. It does not need publishing: manual test runs use the draft.

## 4. Add the companies

**Cost.** Each run spends Enrich Company's price (data and action credits, from `settings.md`; nothing when Clay finds no data), plus one workflow run. Before adding a list, say the count and the cost ("100 companies, about <data> data and <action> action credits") and wait for a yes.

Test one company first and read it back:

```bash
echo '{"domain":"acme.com","company_name":"Acme","watch":"agencies","industry":"Marketing Services","size":"11-50 employees","country":"United Kingdom","source":"lookalike: <seed name>"}' | clay workflows runs test <workflowId> --inputs -
clay workflows runs get <runId> --wait 60
```

Then check the company record shows the watch value, the website, headcount and city. After that, add the rest of the CSV, one run per company, and wait for each run. A run that fails at Enrich Company saves nothing: list the failed runs and add those companies again. For more than about 100 companies, use a CSV upload trigger instead (see the Clay `workflows` skill, `csv-triggers.md`).

Finish with `clay audiences records search-count --audience-id <segmentId> --entity-type companies` and compare it with the CSV. Clay's index lags a few seconds: if it is short, wait and count again before looking for who is missing.

Every company gets its full record when it is added: the CSV columns and Enrich Company. Clay does not fill these in later by itself. Signals only need the domain, but the buyer workflow and the copy read the industry, size and country.

## Adding and removing later

- **Add:** the user says "add acme.com to my signals watchlist". Run the workflow for each domain.
- **Remove:** clear the company's watch field in the Clay app (Companies, open the company). Sending an empty `watch` through the workflow may not clear it, because the save step skips empty values.
- **See it:** Companies, Segments, the watchlist segment. Suggested columns: watch, industry, size, the source fields, and "Signals: last added" once the workflow exists.

## Without the CLI

Create the field and the segment in the Clay app (Companies, Data hub, Fields, then Segments). Import the CSV into Companies with the watch column mapped to the field. Then run Enrich Company on the imported companies, after quoting the count and the cost, so each one has its full record.
