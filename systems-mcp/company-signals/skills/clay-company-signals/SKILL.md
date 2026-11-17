---
name: clay-company-signals
description: "{{YOUR_NAME}}'s company signals system in Clay, for {{OFFER_AND_CARD}}. Windows fallback for a Clay setup without the Clay CLI, using the Clay connector and the Clay Agent in the built-in browser. Builds and runs it with you: pick one of your best customers, find lookalike companies, put them on a watchlist, watch them for buying signals (job posts, new hires, news, research intent) that match the triggers in your GTM context, and when a signal fires, find one person who can sign, find their work email, and add them to a buyer list or a Clay campaign. Recommends 100 companies to start. Asks before every write and every step that spends Clay credits. Use for \"set up Clay signals\", \"monitor a list of companies for signals\", \"build a lookalike watchlist\", \"alert me when target accounts hire or post jobs\", \"signal-based outbound in Clay\", \"enrol people when a signal fires\", \"add companies to my signals watchlist\". Not when the Clay CLI works (use the CLI version), not on Mac or Linux (install the Clay CLI), not for one-off lead lists or website visitor tracking, and it never launches a campaign or sends an email itself."
metadata:
  version: "0.1.0"
---

# Clay company signals: Windows fallback (Clay connector + Clay Agent)

You end up with a system that runs by itself in your Clay workspace. A watchlist of companies that look like your best customer. Clay signals that watch them every week for the buying triggers in your ICP. A Clay workflow that, when a signal fires, checks it is real, finds one person who can sign, finds their work email and saves them to a buyer list, ready for a campaign. You launch the campaign and switch on emailing yourself, in Clay.

**This version is only for Windows without the Clay CLI.** Claude does the thinking and the data work through the Clay connector. The Clay Agent, inside Clay, builds what the connector can't: fields, segments, signals and workflows. Claude types every prompt into the Clay Agent in the built-in browser of the Claude desktop app, reads the answer, and brings you each plan to approve. Never Claude in Chrome.

## Who does what

- **Claude, through the Clay connector:** the lookalike search, Enrich Company, adding companies with your "add to watchlist" workflow, reading records back.
- **The Clay Agent, from prompts Claude types in the built-in browser:** the watch field, the segment, the "add to watchlist" workflow, the signals, the buyer workflow and its test, reading prices and run costs, the campaign copy and settings.
- **You:** sign in to Clay once in the built-in browser, approve every plan and paid step, press Publish, Launch and Resume in Clay.

## Reference files

- `references/clay-agent.md`: where the Clay Agent is, the round trip, and every prompt (setup check, watchlist, signals, buyer workflow, test, publish check, campaign). Without the Clay Agent, its last section has the same steps by hand.
- `references/connector.md`: the connector's tools and what goes wrong with them.
- `references/lookalikes.md`: from one seed company to a reviewed list of N lookalikes.
- `references/watchlist.md`: full records, the watch field, the segment, and adding companies now and later.
- `references/signals.md`: how your ICP triggers become Clay signals, their settings, and the cost.
- `references/workflow.md`: the buyer workflow, step by step, its cost per hit, and how it is tested.
- `references/campaign.md`: the email copy, the workflow-type campaign, and the order for going live.
- `references/gotchas.md`: what goes wrong. Read it before building.
- `assets/read_signal.py`, `assets/email_lines.py`: the two code steps of the buyer workflow. `assets/qualify_prompt.md`, `assets/pick_buyer_prompt.md`: its two AI steps. Fill them from your GTM context.
- `settings.md`: this watchlist's choices and the Clay ids of everything built.

## Before starting

0. **Clay CLI check:** if `clay whoami` works, stop: this is the wrong version. Use the CLI version of company signals. On a Mac or Linux computer without the CLI, stop and tell the person to install the Clay CLI.
1. **GTM context:** {{GTM_CONTEXT}}. Read the ICP, product and offer, messaging and customers pages. You need: the ICP cards (who buys, company size, industry, titles, buying triggers, disqualifiers), the offer, proof you may share, and your customers. Never copy them here.
2. **Settings:** read `settings.md`. When an id is there, that piece exists: reuse it, don't build it twice.
3. **Ask once, in one batch,** for anything still missing: who signs the deal (titles), what makes a company ready to buy now, and who you never want to contact.
4. **Do-not-contact (optional).** If `~/.claude/CLAUDE.md` has a `do-not-contact:start` block, use the check-do-not-contact skill in steps 2 and 7. If not, skip it: customers and open deals are still dropped in step 2.
5. **Voice.** Use your `<name>-voice` skill if installed. Otherwise ask for 2 or 3 cold emails you wrote that got replies.
6. **Clay:** ask the connector which workspace it is on, and say the name back. Open Clay in the built-in browser and check the person is signed in to the same workspace. Then run the setup check in `references/clay-agent.md`.

Files this skill saves (watchlist CSVs, company records) go in `~/.growth-systems/company-signals/`, called `$STATE`.

## Steps

### 1. Pause: agree the plan

Ask in one message:

- **Which offer and ICP card** this watchlist is for.
- **The seed company.** Suggest 2 or 3 from your best customers (the ones who came back for more), with one line each on why. You pick one.
- **How many companies to monitor.** Recommend **100** to start. Show the monthly signal cost for 100, 250 and 500 from `references/signals.md`.
- **Which signals.** Map the ICP's buying triggers to Clay signal types with `references/signals.md` and show the 2 or 3 that fit best.
- **Mode.** Start in **list mode**: the workflow saves buyers to a list and nobody is emailed. Emailing comes in step 7, once you trust the list.

### 2. Pause: build and review the lookalike list

Follow `references/lookalikes.md`. Draft the search from the seed company and the ICP card, read the first page, show 10, and adjust until you say it looks right. Then pull N plus a buffer, drop customers, open deals, competitors and, if you have the list, do-not-contact companies, and save `$STATE/<date>-signals-watchlist.csv`. Show the counts and wait for an OK.

### 3. Pause: create the watchlist in Clay

Follow `references/watchlist.md`. List what will be created (the company fields, one segment, one small workflow) and the Enrich Company cost (count times the price in settings). After a yes, have the Clay Agent build the field, segment and workflow, run Enrich Company through the connector, add the companies with their full record, and check the segment count against the CSV.

### 4. Pause: create the signals

Follow `references/signals.md`. Show each signal's settings in plain words, the schedule, and the cost forecast. The Clay Agent creates them **paused** and reads them back. Read their cost in Companies, Data hub, Signals. Resume only after a clear yes.

### 5. Pause: build and test the buyer workflow

Follow `references/workflow.md`. Fill `assets/qualify_prompt.md` and `assets/pick_buyer_prompt.md` from the ICP card and show both. The Clay Agent builds the workflow as a draft in list mode from one prompt with the code and both prompts. Check its plan against `references/workflow.md` before the go ahead. Then test it once on a sample hit: quote the cost first. Show what each step did and who was picked. Fix and retest until the pick is a real signer.

### 6. Pause: you publish it in list mode

Once live, the workflow spends credits on every hit, on its own, with no budget cap (`references/workflow.md`, "Cost per hit"). First say that per-hit cost and the expected hits a month, and ask once. Record your yes in `settings.md`. Then open the workflow in the built-in browser and ask you to press **Publish**. Check with the Clay Agent that a version is live and show where the buyer list lives. A published version is frozen: later edits wait in the draft until you publish again, and publishing ships everything in the draft.

### 7. Pause: emailing, only when you ask

Follow `references/campaign.md`. Write the copy from your own wording, show 2 versions filled in for a real person on the list, and agree one. You create the workflow-type campaign in Clay. The Clay Agent adds the copy and settings and runs the spam check. If you have a do-not-contact list, you upload its blocklist. You press Launch. The Clay Agent then adds the enrol step to the draft workflow. **You press Publish in Clay yourself.** That is the moment emails start.

## Rules

- Never send, launch, resume or publish. You press Publish, Launch and Resume in Clay yourself, and a signal is resumed only after your yes.
- Every Clay write is listed first and waits for a yes. Every credit-spending step quotes the count and the cost first.
- Every Clay Agent prompt asks for the plan first and says what not to do (no publishing, no running, no resuming unless the step says so). Claude types it in the built-in browser, never in Claude in Chrome, and says go ahead only after your yes.
- Every company written to Clay carries its full record (Enrich Company). Every person is linked to their company record and carries their own location and country from the row that found them (free).
- AI steps use the intermediate model, not the cheapest: quality first.
- Signals are created paused and read back before they run.
- One person per company, and a company is skipped for 90 days after someone there was added.
- Pick only people who can sign. If nobody fits, add nobody. Never invent a role, email or company detail.
- Proof in emails comes only from customers who gave permission, as recorded in your GTM context.
- No names, emails or company details in segment, field, campaign or workflow names.
- After each build step, write the new Clay ids into `settings.md`.
- The Clay CLI works? This skill doesn't apply: use the CLI version.
- Write in plain language, short sentences, no em dashes.

## Adapting this skill

A second watchlist (another offer or card) is a second copy of this skill with its own `settings.md`, or a second section in it. Change signal choices in `references/signals.md` and the buyer rules in the two prompts in `assets/`. When a Clay Agent prompt needs changing or a gotcha bites, add it to `references/clay-agent.md` or `references/gotchas.md`.
