# Pipeline review

Copying this system? Claude follows [COPY-GUIDE.md](../../COPY-GUIDE.md) at the root of this repo. A link to this folder is enough to start.

A weekly run that keeps your sales pipeline current and moving. It reads the last 7 days of inbound (email, LinkedIn messages, bookings), your new buyers and signed deals, and every open deal in your CRM. It makes every CRM change it is sure of, and brings every doubt to you as a numbered decision. You review one report: what was done, and what needs you. Nothing is ever sent.

One skill: `pipeline-review`. It is built around **your** CRM: where your leads live, the fields you want kept current, and your rules.

## How it fits together

```
open deals (CRM) ─┐
email, 7 days    ─┤
LinkedIn, 7 days ─┼→ classify each person → act when sure → sweep every open deal → buyer sweep → report
bookings, 7 days ─┤                         ask when not                             (proof of payment)
new buyers       ─┘
```

## Setup: your CRM first

The copy fits the system to the place your leads live, in three short rounds (`skills/pipeline-review/references/setup.md`). Each round needs the answer to the one before, so they come one after the other:

1. **Where your leads live.** Claude finds the CRM you have connected (HubSpot, Pipedrive, Attio, Salesforce, Notion, Airtable, a Google Sheet, an Excel file), confirms it with you, and reads 5 real rows. Several places? One is written to per kind of deal, the rest are only read. No CRM yet? It offers to create a simple one.
2. **What you want kept current.** You pick the fields from a short list (stage, last contact, next step, latest communication, value...), Claude maps each to your column, and you name the columns it must never touch.
3. **Your rules.** What counts as a deal, what it may change on its own, what proves a win, follow-ups, team rules, and the big one: does a stage change start an automation in your CRM? If yes, that change always waits for you.

The first run is a **preview**: the full review, every change it would make listed, nothing written. You correct it, then it writes.

## What it does each week

The core idea is a table of **what Claude does itself and what goes to you**. Creating a deal for a clear buying ask, updating fields, moving a stage forward with evidence, Won with proof of payment, Lost on an explicit written no: done. Everything else: a numbered decision you answer in five seconds ("yes 1, 3; no 2; draft 4").

## Works best with

- Your email (Gmail or Outlook connector).
- Your CRM, connected: HubSpot, Pipedrive, Attio, Salesforce, Notion, Airtable, or a Google Sheet or Excel file. Without a connector it can read a CSV export and give you the changes to apply by hand. `skills/pipeline-review/references/crm-tools.md` has how each one is read and written.
- Your booking tool (cal.com, Calendly, HubSpot meetings).
- Where buyers prove themselves: a payment platform (Stripe, a course platform), signed contracts in Drive or a signature tool, paid invoices.
- Optional: a LinkedIn tool that can read your messages. Without one, paste the week's important threads, or skip LinkedIn and say so in the report.

## Costs

None beyond your connectors. It reads; it doesn't enrich.

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{YOUR_NAME}}` | Your first name | `~/.claude/CLAUDE.md`, or ask | |
| `{{BUSINESS}}` | Your business name | GTM context | |
| `{{GTM_CONTEXT}}` | Notion Hub link, or `~/gtm-context/gtm/README.md` | `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{CRM}}` | Your CRM, as a short name ("the HubSpot deals pipeline"). Round 1, confirmed with you even when found | Connected tools, GTM context, then ask | |
| `{{CRM_HOW}}` | How the run reads and writes it: the connector, a file path, or "CSV export, changes applied by hand" | Connected tools, round 1 | |
| `{{CHANNELS}}` | The inbound channels to read, and how | Connected tools | Email and bookings |
| `{{BUYER_PROOF}}` | Where proof of payment or signature lives | Connected tools, ask | |
| `{{OWN_ADDRESSES}}` | Your own email domains, so your messages count as yours | Your email | |
| `{{RUN_DAY}}` | Day and time of the weekly run | | Monday 08:00 |
| `{{CRM_TABLES}}` | A small table: each CRM table, pipeline or spreadsheet, its link or file path, what it is for, which offers go there, and "write" or "read only". Example: "Deals pipeline, write, all company deals; Leads sheet, read only" | Your CRM, round 1 | |
| `{{FIELD_MAP}}` | A small table of the fields you picked in round 2, each next to your column name and how it is written (always update, fill only when empty). Example: "Last contact → Last touch, always update" | Your CRM's columns, round 2 | Name, Email, Stage, Last contact, Next step |
| `{{NEVER_TOUCH}}` | Columns the run never writes. Example: "Owner, Amount, Forecast category" | Round 2 | None |
| `{{STAGE_MAP}}` | A small table: new interest, in conversation, call booked, proposal sent, negotiation, waiting, won, lost, each next to your stage name or "none". A client list with only statuses like "active" or "past client" needs a few pipeline stages added, with your OK | Your CRM's stage or status options | |
| `{{OPPORTUNITY_TYPES}}` | What people pay you for, one bullet per kind of sale | Product page, round 3 | |
| `{{CRM_RULES}}` | Your own rules, one line each: which changes start an automation (and so always wait for you), team and owner rules, anything you always do. Example: "Moving a deal to Proposal sent starts a HubSpot sequence: always ask" | Round 3, then every correction | None |
| `{{OFFER_KEYWORDS}}` | Words in an email that show a buying ask, per offer | Product and messaging pages, past buyer emails | |
| `{{OFFER_LINKS}}` | The links drafts may use (offer pages, booking link) | Product page, website | Ask. Until then drafts write [link] |

If your CRM is a spreadsheet or a client list rather than a pipeline, that's fine: the copy maps what you have and proposes the few columns the review needs. Nothing is added without your yes.

## Adapting it

- Your stages: map them once in `settings.md`. The rules talk about stages by meaning, so they work with any names.
- A new pipeline, a new column, or a new CRM: ask Claude to redo that round of the setup.
- Stricter or looser: move a row in the "do it yourself or ask" table in `references/act-or-ask.md`. Start strict. Loosen a row only after a few weeks of decisions you always answer the same way.
- Every time you correct a run, ask Claude to add the correction to the skill. That is the main way it gets good.
