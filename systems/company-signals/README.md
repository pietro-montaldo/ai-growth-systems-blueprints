# Company signals

A system that runs by itself in your Clay workspace. A watchlist of companies that look like your best customer. Clay signals that watch them every week for the buying triggers in your ICP: job posts, new hires in the buyer role, news, research intent. And a Clay workflow that, when a signal fires, checks it is real, finds one person who can sign, finds their work email and saves them to a buyer list. Later, only when you ask, it can also enrol them in a Clay campaign.

Best for B2B offers sold to companies, where a change at the company (a new leader, a team being built) makes it ready to buy.

One skill: `clay-company-signals`. You run it to build the system, and again to add companies or a second watchlist. After that, Clay runs it.

## How it fits together

```
one best customer → lookalike search (Clay) → reviewed list → watchlist segment
                                                                  ↓
             buyer list  ←  work email  ←  one signer  ←  qualify  ←  signals fire (weekly)
                 ↓ (only when you ask)
             Clay campaign you launch
```

Seven pauses, each waiting for your yes: the plan, the lookalike list, the watchlist, the signals (created paused), the buyer workflow (tested on one hit), publishing in list mode (you press Publish), and emailing (only when you ask).

## Works best with

- The Clay CLI signed in (`clay whoami`), on a plan with Search, Signals, Audiences, Workflows and Campaigns.
- At least one sender inbox connected in Clay, for the campaign step.
- Your GTM context: ICP cards with buying triggers, the offer, shareable proof, customers.
- Without the CLI, every step has a "do it in Clay" version in the reference files.

## Costs

Signals charge per company checked on every run, plus per result for news. A rough guide for two weekly signals: 100 companies about 170 credits a month, 250 about 430, 500 about 860. Each buyer found costs a few credits more (qualify, find contacts, work email). The skill reads the real prices in Clay before you turn anything on. Start with 100 companies.

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

The seed company, the signals and the copy are chosen with you inside the skill.

## Adapting it

- Different triggers: map them to signal types in `references/signals.md`.
- A stricter or looser buyer pick: edit `assets/qualify_prompt.md` and `assets/pick_buyer_prompt.md`.
- Alerts as well as a list: add a Slack or email step at the end of the buyer workflow (see `references/workflow.md` for how steps are added).
