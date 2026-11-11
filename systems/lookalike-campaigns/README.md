# Lookalike campaigns

Pick one of your best customers as the seed. Find 100 companies for whom that customer's name means something: same service, same kind of buyer, similar size, the seed's home market. Check them against your CRM and customers, find the main decision maker at each, plus a second one to name in the email, look up work emails, and build a draft Clay email campaign with an A/B test whose copy uses the seed as proof. When it works, expand it with the next 100.

Best for B2B offers where a happy customer is your strongest argument, and where your buyers know each other's companies.

One skill: `lookalike-campaign`. You run it for a new campaign, to read results, and to expand.

## The bar is recognition, not firmographics

A lookalike is a company that would read the seed's name and think "that's a company like us, and they rate this". A company with the right industry and size on the other side of the world has no reason to know the seed. So every company gets a recognition score (0 to 5), and only 4 or 5 go on the list without your say.

## How it fits together

```
best customer → recognition profile → Clay people search (sample of 10, then the rest)
→ domains and headcount (Clay enrichment) → recognition score → exclusions and do-not-contact
→ second decision maker → copy A and B, agreed → work emails → people list, company list,
  draft campaign with A/B test, spam check, test send → you press Launch
→ later: read results → expand with the next 100 when the rule says so
```

Nine pauses, each waiting for your yes: the seed, the search, enrichment credits, the copy, work email credits, the Clay build, the test send, and later results and expanding.

## Works best with

- The Clay CLI signed in (`clay whoami`), on a plan with Search, Audiences, Campaigns and the enrichment functions (Enrich Person, Enrich Company, Work Email).
- At least one sender inbox connected in Clay.
- Your GTM context: ICP cards, the offer, and a customers list that records which customers you may name and quote.
- Your CRM, to keep open deals and past customers out.

## Costs (rough, check your own prices)

| Step | What it costs | For 100 companies |
| --- | --- | --- |
| People search | Search quota, not credits | about 250 people pulled (about half survive) |
| Enrich Person (domains) | per person, read from Clay | about 250 |
| Enrich Company (headcount) | per domain, read from Clay | about 150 |
| Work Email | per main contact only | about 100 |

The skill reads the real prices and your search quota in Clay, and quotes count times price before each step.

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{YOUR_NAME}}` | Your first name, for the description and signature | `~/.claude/CLAUDE.md`, GTM context, or ask | |
| `{{GTM_CONTEXT}}` | Notion Hub link, or `~/gtm-context/gtm/README.md` | `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{CUSTOMERS_SOURCE}}` | Where your customers are, with whether each one may be named or quoted | GTM context customers database or CSV | |
| `{{CRM}}` | Your CRM, to drop companies with an open deal | Connected tools, GTM context | |
| `{{OFFER}}` | The offer this campaign sells | Product page | Your highest-value company offer |
| `{{BUYER_TITLES}}` | Titles of the main decision maker | ICP card, past won deals | Founder, CEO, Managing Director, Managing Partner |
| `{{SECOND_TITLES}}` | Titles for the second person you name | ICP card | Co-founder, COO, MD, Partner |
| `{{CREDIBILITY_LINE}}` | One true, checkable line about you for version A ("I also teach this to 300 operators") | Product page, proof | Ask |
| `{{EXPAND_RULE}}` | When a campaign earns the next 100 | | 2 or more positive replies per 100 leads, counted after the nudge went to everyone |

The seed, the recognition profile, the copy, the inboxes and the sending window are chosen with you in each run. Clay field and routine ids are added during setup.

## Adapting it

- A different proof style: change the A/B pair in `references/copy.md`.
- Wider than the seed's market: allowed in the expand order in `references/results-and-expand.md`, one step at a time.
- LinkedIn instead of email: stop after step 5 and draft messages to the main decision maker by hand.
