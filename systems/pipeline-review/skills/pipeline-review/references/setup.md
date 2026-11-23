# Setup: your CRM first

This system is only as good as its fit with the place your leads live. So the setup is a short interview in three rounds, in this order, because each round needs the answer to the one before:

1. **Where your leads live** (the CRM).
2. **What you want kept current** (the fields).
3. **Your rules** (what it may do on its own, and what it must never do).

Read what you can before each round (connected tools, the CRM itself, the GTM context), then ask only what is left, with a recommendation and an example. Each round is one short message. Write every answer into `settings.md`.

## Round 1: where your leads live

**Find it first.** Check which CRM tools are connected and look in the GTM context for where deals are kept. Then ask one question to confirm, even when you found one: "Your leads seem to live in <X>. Is that where you track deals, or somewhere else too?" People often have two places (a spreadsheet of leads and a CRM for clients, or one pipeline per offer).

**Pick the one to write to.** Exactly one place per kind of deal is written to. Any other place is read only (to match people), and says so in `settings.md`. Old or frozen tables are listed as "never write".

**Look at the real data.** Read 5 recent rows with the person. Check:
- Is it a pipeline (deals with stages) or a list of clients (statuses like "active", "past")? A client list needs a few pipeline stages added, with their OK.
- One table, or several (pipelines, databases, tabs)? What is each one for, and which offers go where?
- Is it shared with a team? Then whose deals may the run touch (an owner field, a filter)?

**How it is read and written** depends on the tool. See `crm-tools.md` for each one: how to search, create, update and check a write, and what goes wrong.

| What they have | What to do |
| --- | --- |
| A CRM with a connector (HubSpot, Attio, Pipedrive, Salesforce, Notion, Airtable, Zoho, Close, Monday) | Use the connector. Fetch the tables, fields and options now, and write the exact names into `settings.md`. |
| A CRM with no connector | Read it in a browser where they are signed in, read only, and write changes as a list they apply by hand. Or a weekly CSV export, with the changes back as a CSV they import. Say plainly that the run can't write by itself. |
| A Google Sheet or Excel file | Read and write it directly. Back it up before the first write of each run. |
| Nothing yet (email and memory) | Offer to create a simple pipeline with the fields from round 2: a Google Sheet, or a Notion database if they use Notion. Create it only on a yes. |

Fills: `{{CRM}}`, `{{CRM_HOW}}`, `{{CRM_TABLES}}`.

## Round 2: what you want kept current

Show the list of fields the run can keep up to date, and ask which ones matter to them. Most people want the first five. Nothing on the list is forced on them.

| Field | What the run writes | Recommended |
| --- | --- | --- |
| Name, Company | The person, and their company | Always |
| Email, LinkedIn | Filled when empty, never overwritten | Always |
| Stage | Moved forward when the thread proves it | Always |
| Last contact | Date of the last real message, either way | Always |
| Next step | What happens next, with a date when there is one | Always |
| Latest communication | One line: what was said, who wrote last | Yes |
| Product | Which offer they want | If you sell more than one thing |
| Value | Only as stated by them or by you, with currency | If you track revenue |
| Source | Where they came from | If you track channels |
| Notes | Durable facts added, never replaced | Yes |

Then, for each field they pick:
- **Map it** to their column name, from the 5 rows you read. Never guess a column from its name alone.
- **How it is written:** always update, fill only when empty, or never touch. Default: Email, LinkedIn, Company and Source are "fill only when empty"; the rest "always update".
- **Missing columns** they want: propose adding them. Add only on a yes. A spreadsheet is backed up first.

Also ask: **which columns must the run never touch?** Typical answers: owner, deal amount from a quote tool, forecast, anything a CRM automation or another system writes. They go under "Never touch" in `settings.md`.

Fills: `{{FIELD_MAP}}`, `{{NEVER_TOUCH}}`, `{{STAGE_MAP}}` (map their stage names to the meanings in `settings.md`).

## Round 3: your rules

Start from the defaults in `act-or-ask.md` and `settings.md`, show them in plain words, and ask what to change. Recommend starting strict. Ask about these, one line each:

1. **What counts as a deal.** Draft it from the product page: who pays you, for what. Ask what they never want logged (partners, free calls, vendors, existing clients' logistics).
2. **What the run may do on its own.** Default: create a deal for a clear buying ask, update fields, move a stage forward with evidence, Won with proof, Lost only on a written no. Anything they want as a decision instead moves to the "Otherwise" side.
3. **Won proof.** What counts in their business: a payment in their payment tool, a signed contract, a paid invoice.
4. **Follow-ups.** How many, how far apart, and whether to propose closing as lost after the last one. Default: 3 follow-ups at 3, 5, then 7 days, then propose lost.
5. **Automations.** Does changing a stage or creating a deal start anything in the CRM: an email sequence, a task, a Slack alert, an invoice? If yes, those changes always become decisions, never automatic. This is the most important question for HubSpot, Pipedrive and Salesforce users.
6. **Team rules.** In a shared CRM: only their own deals (the owner filter), and whether new deals get them as owner.
7. **Anything else they always do.** For example "every new deal gets a next step", "company deals go in the company pipeline", "never create a deal without an email". Write each one as a short rule.

Fills: `{{OPPORTUNITY_TYPES}}`, `{{BUYER_PROOF}}`, `{{CRM_RULES}}`, and any row they move in `act-or-ask.md`.

## Check before the first real run

1. Show the filled `settings.md` (CRM, fields, never touch, stages, rules) and wait for an OK.
2. Run once in **preview mode** (see `SKILL.md`): the full review of the last 7 days, with every change it would make listed, and nothing written.
3. Go through the list with the person. Each wrong change becomes a fix in the settings or a rule.
4. On their OK, apply the changes, then read every written row back and show it. From then on, runs write.

## Changing it later

New pipeline, new column, new rule: tell Claude, and it updates `settings.md` the same way (map, ask, write). A correction during a run ("don't move deals to proposal sent until I've sent the PDF") becomes a line under "Your rules".
