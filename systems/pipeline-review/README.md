# Pipeline review

A weekly run that keeps your sales pipeline current and moving. It reads the last 7 days of inbound (email, LinkedIn messages, bookings), your new buyers and signed deals, and every open deal in your CRM. It makes every CRM change it is sure of, and brings every doubt to you as a numbered decision. You review one report: what was done, and what needs you. Nothing is ever sent.

One skill: `pipeline-review`.

## How it fits together

```
open deals (CRM) ─┐
email, 7 days    ─┤
LinkedIn, 7 days ─┼→ classify each person → act when sure → sweep every open deal → buyer sweep → report
bookings, 7 days ─┤                         ask when not                             (proof of payment)
new buyers       ─┘
```

The core idea is a table of **what Claude does itself and what goes to you**. Creating a deal for a clear buying ask, updating fields, moving a stage forward with evidence, Won with proof of payment, Lost on an explicit written no: done. Everything else: a numbered decision you answer in five seconds ("yes 1, 3; no 2; draft 4").

## Works best with

- Your email (Gmail or Outlook connector).
- Your CRM (Notion, HubSpot, Attio, Pipedrive, a Google Sheet).
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
| `{{CRM}}` | Your CRM and where it is (link, or tool name) | Connected tools, GTM context | |
| `{{CHANNELS}}` | The inbound channels to read, and how | Connected tools | Email and bookings |
| `{{BUYER_PROOF}}` | Where proof of payment or signature lives | Connected tools, ask | |
| `{{OWN_ADDRESSES}}` | Your own email domains, so your messages count as yours | Your email | |
| `{{RUN_DAY}}` | Day and time of the weekly run | | Monday 08:00 |
| `{{CRM_TABLES}}` | A small table: each CRM table, pipeline or spreadsheet, its link or file path, what it is for, and its product options | Your CRM | |
| `{{FIELD_MAP}}` | A small table: Name, Company, Email, LinkedIn, Stage, Product, Source, Value, Last contact, Latest communication, Next step, Notes, each next to your column name or "none". Missing ones that matter (Stage, Last contact, Next step) are proposed as new columns | Your CRM's columns | |
| `{{STAGE_MAP}}` | A small table: new interest, in conversation, call booked, proposal sent, negotiation, waiting, won, lost, each next to your stage name or "none". A client list with only statuses like "active" or "past client" needs a few pipeline stages added, with your OK | Your CRM's stage or status options | |
| `{{OPPORTUNITY_TYPES}}` | What people pay you for, one bullet per kind of sale | Product page | |
| `{{OFFER_KEYWORDS}}` | Words in an email that show a buying ask, per offer | Product and messaging pages, past buyer emails | |
| `{{OFFER_LINKS}}` | The links drafts may use (offer pages, booking link) | Product page, website | Ask. Until then drafts write [link] |

If your CRM is a spreadsheet or a client list rather than a pipeline, that's fine: the copy maps what you have and proposes the few columns the review needs.

## Adapting it

- Your stages: map them once in `settings.md`. The rules talk about stages by meaning, so they work with any names.
- Stricter or looser: move a row in the "do it yourself or ask" table in `references/act-or-ask.md`. Start strict. Loosen a row only after a few weeks of decisions you always answer the same way.
- Every time you correct a run, ask Claude to add the correction to the skill. That is the main way it gets good.
