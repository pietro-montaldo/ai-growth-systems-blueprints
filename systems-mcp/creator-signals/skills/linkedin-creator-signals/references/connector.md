# The Clay connector

What Claude does through the connector, and what goes wrong. Tool names differ from one setup to the next: find them by what they do.

## What it can and can't do

| Can | Can't |
| --- | --- |
| Say which workspace it's connected to | Create fields, workflows, lists or campaigns (the Clay Agent does) |
| Run Clay's functions: Enrich Person, Work Email, Enrich Company | Read prices or the credit balance |
| Run your own workflows once they're registered as routines | See whether a person is linked to their company (the Clay Agent can) |
| Read records in your Audiences | Count past one page in a single call |

## Functions (credits)

- Run a function on concrete values, one input set per person or company, in batches of up to 100. Each input set is one paid run.
- **Enrich Person:** the LinkedIn profile link. **Work Email:** full name, company name and company domain are all required, plus the profile link and the company LinkedIn page when you have them. **Enrich Company:** the company domain.
- The connector's list of inputs isn't exact: when a run fails, the error names the real required inputs. Fix and run again.
- Use the function id exactly as the routines list shows it. If an id with a prefix (such as `function:`) is refused as not found, try it without the prefix.
- Read the results by task id, 100 per page; read every page, and wait and read again until the task says it's complete. Work Email is a waterfall and can take a few minutes. Never write "not found" for a row that hasn't finished.
- Map every result by the input it carries (the profile link, the domain), never by position.

## Your "add to campaign list" workflow (no data credits)

After the email setup it shows in the connector's list of routines, with a `workflow:` id. It runs straight away; it doesn't need publishing. One input set per person, batches of up to 100, built by the rule in `creator-signals-email/references/campaign.md`. Send headcount and founded as numbers, and leave out empty values rather than sending blanks.

## Big results

Everything the connector returns lands in the chat. Enrich Person returns whole profiles, and every function or workflow result repeats all its inputs.

- Give each batch's results to a helper agent with the connector: it reads every page, writes only the fields the skill uses to `$RUN`, and sends back short rows (name, company, title, country, status).
- Follow a running function or workflow by reading one record's progress, not the whole result. Confirm writes with the Clay Agent's count (`clay-agent.md`).
- When the chat gets long, or a run stops, start again from the run files. Never pay twice for a person already in `seen.csv` or a result already saved.

## Prices and spend

No prices and no balance through the connector. Forecasts use the prices in settings. To report what a run cost, ask the Clay Agent for the balance before and after, or report the count of runs. Clay also caps how much each connected user can spend through the connector (Clay settings, Agent users): a large week can hit that cap before the balance.
