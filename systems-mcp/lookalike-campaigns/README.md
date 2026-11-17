# Lookalike campaigns: Windows fallback (Clay connector + Clay Agent)

Copying this system? Claude follows [COPY-GUIDE.md](../../COPY-GUIDE.md) at the root of this repo. A link to this folder is enough to start.

**Use this only on Windows without the Clay CLI.** If `clay whoami` works, on any computer, use [`systems/lookalike-campaigns/`](../../systems/lookalike-campaigns/README.md) and ignore this folder. On a Mac or Linux computer without the CLI, install the Clay CLI first (Claude can do it with Clay's plugin), then use `systems/`.

The same system as the lookalike campaigns in `systems/`, for Windows without the Clay CLI. Claude reaches Clay through the Clay connector, and drives the Clay Agent in the built-in browser of the Claude desktop app for what the connector can't do.

Pick one of your best customers as the seed. Find companies for whom that customer's name means something (same service, same kind of buyer, similar size, the seed's home market) until 100 of them have a work email. Check them against your CRM and customers, find the main decision maker at each, plus a second one to name in the email, look up work emails, and build a draft Clay email campaign with an A/B test whose copy uses the seed as proof. When it works, expand it with the next 100.

Best for B2B offers where a happy customer is your strongest argument, and where your buyers know each other's companies.

One skill: `lookalike-campaign`. You run it for a new campaign, to read results, and to expand.

## The bar is recognition, not firmographics

A lookalike is a company that would read the seed's name and think "that's a company like us, and they rate this". A company with the right industry and size on the other side of the world has no reason to know the seed. So every company gets a recognition score (0 to 5), and only 4 or 5 go on the list without your say.

## Who does what

The connector can search, enrich and run your own Clay workflows, but it can't build anything in Clay. The Clay Agent, inside Clay, builds those pieces. Claude opens Clay in the built-in browser of the Claude desktop app (you sign in there once), types each prompt into the Clay Agent, reads its answer, and brings you every plan to approve before it says "go ahead". It never uses Claude in Chrome. Without the desktop app's browser, Claude gives you each prompt to paste by hand.

| Step | Who | How |
| --- | --- | --- |
| Seed, recognition profile, keep or drop, CRM and customer checks, copy | Claude | Your GTM context and CRM |
| Companies and people searches | Claude | Clay connector (search quota, no credits) |
| Find company lookalikes | Clay Agent | A prompt Claude types in the built-in browser |
| Enrich Company, Find People at Company, Work Email | Claude | Clay connector (credits) |
| Writing people and their companies to Clay | Claude | Clay connector, running your "add people" workflow |
| One-time setup: fields and the "add people" workflow | Clay Agent | A prompt Claude types, once |
| People list, draft A/B campaign, spam check, previews | Clay Agent | A prompt Claude types |
| Inboxes, test email, Launch | You | In Clay |
| Results | Clay Agent, or the campaign's Analytics tab | Claude reads them in the built-in browser |

## How it fits together

```
best customer → recognition profile → Find company lookalikes (Clay Agent), then companies searches,
competitor names and a named list (connector) to fill the gaps
→ read every description: keep, check or drop → exclusions (customers, open deals, companies already in Clay, free)
→ full company records (Enrich Company) → decision makers (people search, then Find People)
→ copy A and B, agreed → work emails → enough companies with an email? if not, change the strategy
→ people written to Clay, each linked to their company (connector)
→ people list and draft campaign with A/B test, spam check, previews (Clay Agent) → you press Launch
→ later: read results → expand with the next 100 when the rule says so
```

Ten pauses, each waiting for your yes: the seed, the search, company record credits, Find People credits, the copy, work email credits, writing to Clay, the Clay build, the test send, and later results and expanding.

## Works best with

- **The Claude desktop app**, for its built-in browser. Sign in to Clay once in that browser pane.
- **The Clay connector** in Claude, signed in to your Clay workspace.
- **The Clay Agent.** It is in beta and on Clay's Launch, Growth and Enterprise plans. In Clay, open Workflows and click New: the box that says "What should we build today?" is the Clay Agent. The box on Clay's home page can open Sculptor instead, which only builds tables. Without the Clay Agent, Claude gives you the same steps to click through in Clay yourself. It is slower, and the campaign editor needs care.
- At least one sender inbox connected in Clay.
- Your GTM context: ICP cards, the offer, and a customers list that records which customers you may name and quote.
- Your CRM, to keep open deals and past customers out.

## Different from the CLI version

- Find company lookalikes runs through the Clay Agent. Claude reads its result list in the built-in browser. In a small market it can return nothing; an empty call is refunded.
- There is no separate company list. The "add people" workflow writes each company with its full record, and the searches skip every company already in your Clay Audiences.
- The connector can't read prices or your credit balance. You read the prices once in setup; forecasts use them.
- The connector counts one page at a time, and can't see whether a person is linked to their company. Claude pages through to count, and the Clay Agent checks the links.
- Everything the connector returns lands in the chat. Claude works in batches of about 50, hands the heavy reading to helper agents and saves to the run folder as it goes. A 100-company campaign uses a lot of Claude usage: on a smaller Claude plan, run it over a few sessions.

## Costs (rough, check your own prices)

| Step | What it costs | For 100 companies |
| --- | --- | --- |
| Find company lookalikes | per company returned (about 1 credit each), nothing per call, refunded when empty | the first source, batches of 10 then up to 50 |
| Companies and people searches | Search quota, not credits | 400 to 2,000 companies read: 1 in 4 pass with a narrow search, 1 in 20 with a strict bar in a small market |
| Enrich Company (full record) | per keep and check company | about 120 to 150 |
| Find People at Company | per kept company with no leader after the people search | about 1 in 5 kept companies |
| Work Email | per main contact only | about 110 |
| "Add people" workflow | no data credits | one run per main contact |
| The Clay Agent's own work | data credits, at Clay's current agent pricing | a few prompts per campaign |

Clay also sets a credit limit per connected user for the connector (in Clay's settings, under Agent users), 1,000 credits by default. A 100-company campaign spends about 300 through the connector; raise the limit before a bigger run.

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{YOUR_NAME}}` | Your first name, for the description and signature | `~/.claude/CLAUDE.md`, GTM context, or ask | |
| `{{GTM_CONTEXT}}` | Notion Hub link, or `~/gtm-context/gtm/README.md` | `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{CUSTOMERS_SOURCE}}` | Where your customers are, with whether each one may be named or quoted | GTM context customers database or CSV | |
| `{{CRM}}` | Your CRM, to drop companies with an open deal: its name, where it is, and which stages count as open | Connected tools, GTM context | |
| `{{OFFER}}` | The offer this campaign sells | Product page | Your highest-value company offer |
| `{{BUYER_TITLES}}` | Titles of the main decision maker | ICP card, past won deals | CEO, Founder, Managing Director, President, Executive Director, COO |
| `{{SECOND_TITLES}}` | Titles for the second person you name | ICP card | Co-founder, COO, MD, Partner |
| `{{CREDIBILITY_LINE}}` | One true, checkable line about you for version A. Examples: "I also teach this to 300 operators", "We've run this for 40 agencies since 2021", "I ran growth at a 50-person agency for six years" | Product page, proof, customers list | Ask, with these examples and 2 options drafted from your GTM context |
| `{{TARGET_COMPANIES}}` | How many companies with a Clay-found work email the campaign needs. The search keeps going until it is reached | | 100 |
| `{{MIN_STAFF}}` | Smallest company worth emailing, by exact headcount from Enrich Company | ICP card | 10 |
| `{{EXPAND_RULE}}` | When a campaign earns the next 100 | | 2 or more positive replies per 100 leads, counted after the nudge went to everyone |
| `{{CLAY_AGENT}}` | Whether your Clay plan has the Clay Agent: "yes", or "no, build by hand in Clay" | Claude opens Workflows, New in the built-in browser and looks for the box "What should we build today?" | yes |

The seed, the recognition profile, the copy, the inboxes and the sending window are chosen with you in each run. The workflow id and the prices are added during setup.

## Adapting it

- A different proof style: change the A/B pair in `references/copy.md`.
- Wider than the seed's market: allowed in the expand order in `references/results-and-expand.md`, one step at a time.
- LinkedIn instead of email: stop after step 5 and draft messages to the main decision maker by hand.
- You get the Clay CLI later: switch to the CLI version in `systems/lookalike-campaigns/` and stop using this one. Your fields and workflow carry over.
