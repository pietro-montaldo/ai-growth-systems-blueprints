# Company signals: Windows fallback (Clay connector + Clay Agent)

**Use this only on Windows without the Clay CLI.** If `clay whoami` works, on any computer, use [`systems/company-signals/`](../../systems/company-signals/README.md) and ignore this folder. On a Mac or Linux computer without the CLI, install the Clay CLI first (Claude can do it with Clay's plugin), then use `systems/`.

The same system as the company signals in `systems/`, for Windows without the Clay CLI. Claude reaches Clay through the Clay connector, and drives the Clay Agent in the built-in browser of the Claude desktop app for what the connector can't do.

A system that runs by itself in your Clay workspace. A watchlist of companies that look like your best customer. Clay signals that watch them every week for the buying triggers in your ICP: job posts, new hires in the buyer role, news, research intent. And a Clay workflow that, when a signal fires, checks it is real, finds one person who can sign, finds their work email and saves them to a buyer list. Later, only when you ask, it can also enrol them in a Clay campaign.

Best for B2B offers sold to companies, where a change at the company (a new leader, a team being built) makes it ready to buy.

One skill: `clay-company-signals`. You run it to build the system, and again to add companies or a second watchlist. After that, Clay runs it.

## Who does what

The connector can search, enrich and run your own Clay workflows, but it can't create fields, segments, signals or workflows. The Clay Agent, inside Clay, builds those. Claude opens Clay in the built-in browser of the Claude desktop app (you sign in there once), types each prompt into the Clay Agent, reads its answer, and brings you every plan to approve before it says "go ahead". It never uses Claude in Chrome. Without the desktop app's browser, Claude gives you each prompt to paste by hand.

| Step | Who | How |
| --- | --- | --- |
| The plan, the lookalike search, fit check, exclusions | Claude | Clay connector (search quota), your GTM context and CRM |
| Full company records | Claude | Clay connector, Enrich Company (credits) |
| Watch field, watchlist segment, "add to watchlist" workflow | Clay Agent | A prompt Claude types, once |
| Adding companies to the watchlist | Claude | Clay connector, running your "add to watchlist" workflow |
| Signals, created paused, then resumed on your yes | Clay Agent | A prompt Claude types |
| The buyer workflow, its test run, its cost per hit | Clay Agent | A prompt Claude types, with the code and prompts in `assets/` |
| Publish, Launch, Resume | You | In Clay |
| Emailing (only when you ask) | Clay Agent, then you | Copy and settings by prompt; you create and launch the campaign |

## How it fits together

```
one best customer → lookalike search (connector) → reviewed list → full records (Enrich Company)
→ watchlist: field, segment, workflow (Clay Agent) → companies added (connector)
                                                          ↓
           buyer list  ←  work email  ←  one signer  ←  qualify  ←  signals fire (weekly)
               ↓ (only when you ask)
           Clay campaign you launch
```

Seven pauses, each waiting for your yes: the plan, the lookalike list, the watchlist, the signals (created paused), the buyer workflow (tested on one hit), publishing in list mode (the per-hit cost agreed, then you press Publish), and emailing (only when you ask).

## Works best with

- **The Claude desktop app**, for its built-in browser. Sign in to Clay once in that browser pane.
- **The Clay connector** in Claude, signed in to the same Clay workspace.
- **The Clay Agent.** It is in beta and on Clay's Launch, Growth and Enterprise plans. In Clay, open Workflows and click New: the box that says "What should we build today?" is the Clay Agent. The box on Clay's home page can open Sculptor instead, which only builds tables.
- A Clay plan with Search, Signals, Audiences, Workflows and Campaigns, and one sender inbox for the emailing step.
- Your GTM context: ICP cards with buying triggers, the offer, shareable proof, customers.

## Different from the CLI version

- Companies get their full record from Enrich Company through the connector before they are added. The "add to watchlist" workflow then only writes them, so it has no code step.
- Fields, segments, signals and both workflows are built by the Clay Agent from prompts, and it reads them back.
- The connector can't read prices, your balance or the search quota. Prices are read once in setup and in Clay's Data hub; forecasts use them.
- Tested so far: the Clay Agent created the field, the segment and two paused signals from one prompt and read them back, and planned the full buyer workflow correctly from one long prompt. Building the buyer workflow, its test run, publishing and the emailing step follow the CLI version's tested design but haven't been run through the Clay Agent yet: check each answer closely the first time.

## Costs

Signals charge per company checked on every run, plus per result for news. A rough guide for two weekly signals: 100 companies about 170 credits a month, 250 about 430, 500 about 860. Each company added runs Enrich Company once. Each hit costs a few credits more (qualify, find contacts, work email), and once the buyer workflow is live it spends that on every hit by itself, with no budget cap: the skill states the per-hit cost and asks once before you publish. The skill reads the real prices in Clay before you turn anything on. Start with 100 companies.

Clay also sets a credit limit per connected user for the connector (Clay settings, Agent users). Enrich Company runs through it.

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{YOUR_NAME}}` | Your first name | `~/.claude/CLAUDE.md`, GTM context, or ask | |
| `{{GTM_CONTEXT}}` | Notion Hub link, or `~/gtm-context/gtm/README.md` | `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{OFFER_AND_CARD}}` | The offer and ICP card this watchlist is for. One card per watchlist keeps the copy and the buyer pick sharp | ICP page | Your highest-value company offer, best card |
| `{{WATCHLIST_NAME}}` | A short lowercase tag for this watchlist | | Made from the card ("agencies") |
| `{{WATCHLIST_SIZE}}` | How many companies to monitor | | 100 |
| `{{SIGNER_TITLES}}` | Who can sign the deal | ICP card, past won deals | |
| `{{NOTIFY}}` | Where hit alerts go: a Slack channel, your own email, or none | Connected tools | None |
| `{{CLAY_AGENT}}` | Whether your Clay plan has the Clay Agent: "yes", or "no, build by hand in Clay" | Claude opens Workflows, New in the built-in browser and looks for the box "What should we build today?" | yes |

The seed company, the signals and the copy are chosen with you inside the skill.

## Adapting it

- Different triggers: map them to signal types in `references/signals.md`.
- A stricter or looser buyer pick: edit `assets/qualify_prompt.md` and `assets/pick_buyer_prompt.md`.
- Alerts as well as a list: ask the Clay Agent to add a Slack or email step at the end of the buyer workflow.
- You get the Clay CLI later: switch to the CLI version in `systems/company-signals/` and stop using this one. Your fields, signals and workflows carry over.
