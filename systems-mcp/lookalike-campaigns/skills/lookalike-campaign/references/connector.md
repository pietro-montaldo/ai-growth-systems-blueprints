# The Clay connector

What Claude does through the connector, and what goes wrong. Tool names differ from one setup to the next: find them by what they do.

## What it can and can't do

| Can | Can't |
| --- | --- |
| Say which workspace it's connected to | Build fields, workflows, lists or campaigns (the Clay Agent does) |
| Search companies and people in Clay's data | Run Find company lookalikes (the Clay Agent does) |
| Run Clay's functions (Enrich Company, Find People at Company, Work Email) | Read prices or the credit balance |
| Run your own workflows once they're registered as routines | See whether a person is linked to their company |
| Read records in your Audiences | Count past one page in a single call |

## Searches (search quota, no credits)

- **Companies:** a query that starts with `select from companies`, as in `seed-and-search.md`. Results come 20 at a time. Ask for the next page while there are more; each page has its own task id. Leaving out every company already in Audiences works here: `clay.exclude_company_identifiers(@audience_segment("ALL"))`.
- **People at companies:** up to 10 company domains per call, a query that starts with `select from people`, and `limit 4 by clay_company_id` to cap people per company.
- **The quota isn't shown.** Watch for a quota or limit error and stop there. Never start extra searches to get round it.

## Functions (credits)

- Run a function on concrete values (domains, names): one input set per company or person, in batches of up to 100. Each input set is one paid run.
- Read the results by task id. They come 100 per page; read every page, and wait and read again until the task says it's complete. Never write "not found" for a row that hasn't finished.
- **Big results:** Find People at Company returns whole profiles. Save the result to a file in `$RUN` and read the fields you need from it, rather than reading it in the chat.
- **Use the function id exactly as the routines list shows it.** If an id with a prefix (such as `function:`) is refused as not found, try it without the prefix.
- **The listed inputs aren't exact.** The connector's list of inputs can name fields that aren't required and miss ones that are. Work Email needs the full name, the company domain and the company name. When a run fails, the error names the real required inputs: fix and run again.
- **Numbers as numbers.** Inputs typed as numbers (headcount, founded) must be sent as numbers, not text.

## Your "add people" workflow (no data credits)

After setup it shows in the connector's list of routines, with a `workflow:` id. It runs straight away; it doesn't need publishing. One input set per main contact, batches of up to 100. Required: `company_domain`, `email`, `campaign`. Send `company_headcount` and `company_founded` as numbers, and leave out empty values rather than sending blanks. Read the results: each one says which fields it wrote.

## Big runs

Everything the connector returns lands in the chat, not in a file. A 100-company run reads about 400 search results and 150 full company records, which is more than one chat holds comfortably.

- Work in batches of about 50 companies: search, judge and save one batch before the next.
- Write each search page and each function result to `$RUN` as soon as it comes back: the domain, name, country, size and a short description for searches, and only the fields the skill uses for functions. Don't repeat whole results in the chat.
- Show the person short rows (company, country, size, decision, reason), never whole records.
- Claude gives each batch of search pages, and each big function result, to a helper agent with the connector: it reads them, writes the rows to `$RUN`, and sends back only short rows. One search page is about 12,000 tokens, so this keeps the main chat usable. The helpers still use a lot of Claude usage: on a smaller Claude plan, spread a 100-company campaign over a few sessions.
- Follow a running function or workflow by reading one record's progress (ask for one entity), not the whole result: every result repeats all its inputs, and 17 workflow results take about 20,000 tokens. Confirm writes with the Clay Agent's count instead.
- When the chat gets long, or a run stops, start a new chat from `companies.json`, using each company's `stage`. Never search again or pay again for a company already in it.

## Reading Audiences

Ask in plain words ("people whose Lookalike campaign is exactly <name>"). Two traps:

- The total it reports is the size of the page, not the real total. Count by reading pages of 100 (offset 0, 100, 200...) until a page comes back short.
- It doesn't show the company link. The Clay Agent check in `clay-agent.md` does, or the Company column in the list in Clay.

## Prices and spend

No prices and no balance through the connector. Forecasts use the prices in settings. To report what a run cost, ask the person to read the balance in Clay before and after, or report the count of runs. Clay also caps how much each connected user can spend through the connector (Clay settings, Agent users): a large run can hit that cap before the balance.
