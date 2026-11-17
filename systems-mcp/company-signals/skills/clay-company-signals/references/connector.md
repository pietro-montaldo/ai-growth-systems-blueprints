# The Clay connector

What Claude does through the connector, and what goes wrong. Tool names differ from one setup to the next: find them by what they do.

## What it can and can't do

| Can | Can't |
| --- | --- |
| Say which workspace it's connected to | Create fields, segments, signals, workflows or campaigns (the Clay Agent does) |
| Search companies in Clay's data | Resume, publish or launch anything |
| Run Clay's functions (Enrich Company) | Read prices, the credit balance or the search quota |
| Run your own workflows once they're registered as routines | Read signal hits or workflow run costs (the Clay Agent does) |
| Read records in your Audiences | Count past one page in a single call |

## Searches (search quota, no credits)

- A query that starts with `select from companies`, as in `lookalikes.md`. Results come 20 at a time; ask for the next page while there are more. Leaving out every company already in Audiences works: `clay.exclude_company_identifiers(@audience_segment("ALL"))`.
- The quota isn't shown. Watch for a quota or limit error and stop there. Never start extra searches to get round it.

## Functions (credits)

- Run Enrich Company on concrete domains, one input set per company, in batches of up to 100. Each input set is one paid run.
- Read the results by task id, 100 per page; read every page, and wait and read again until the task says it's complete.
- **Use the function id exactly as the routines list shows it.** If an id with a prefix (such as `function:`) is refused as not found, try it without the prefix.

## Your "add to watchlist" workflow (no data credits)

After setup it shows in the connector's list of routines, with a `workflow:` id. It runs straight away; it doesn't need publishing. One input set per company, batches of up to 100. Required: `domain`, `watch`. Send `headcount` and `founded` as numbers, and leave out empty values rather than sending blanks.

## Big runs

Everything the connector returns lands in the chat, not in a file. One search page is about 12,000 tokens, and every workflow result repeats all its inputs.

- Give batches of search pages and big function results to a helper agent with the connector: it writes the rows to `$STATE` and sends back short rows.
- Follow a running function or workflow by reading one record's progress, not the whole result. Confirm writes by asking the Clay Agent to count the segment.
- When the chat gets long, or a run stops, start a new chat from the files in `$STATE`. Never search or pay again for a company already done.

## Prices and spend

No prices and no balance through the connector. Forecasts use the prices in settings. Clay also caps how much each connected user can spend through the connector (Clay settings, Agent users): Enrich Company for a big list can hit that cap before the balance. Signals and the buyer workflow spend inside Clay, not through the connector.
