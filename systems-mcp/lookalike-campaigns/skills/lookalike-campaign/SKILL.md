---
name: lookalike-campaign
description: "{{YOUR_NAME}}'s lookalike campaign for {{OFFER}}, Windows fallback for a Clay setup without the Clay CLI, using the Clay connector and the Clay Agent in the built-in browser: picks one best customer as the seed, finds companies that would recognise that customer until {{TARGET_COMPANIES}} have a work email (same service, same kind of buyer, similar size, the seed's home market), checks them against the CRM and customers, finds the main decision maker plus a second one to name, looks up work emails through the connector, writes the people to Clay, and types the prompts the Clay Agent uses to build the list and a draft A/B campaign whose copy uses the seed as proof. Also reviews a running campaign and expands it when it works. Use for \"lookalike campaign\", \"lookalikes of <customer>\", \"find companies like <customer> and email them\", \"campaign using <customer> as proof\", \"how is the lookalike campaign doing\", \"expand the lookalike campaign\". Not when the Clay CLI works (use the CLI version), not on Mac or Linux (install the Clay CLI), not for signal-based outreach or creator comment lists, and it never launches or sends a campaign."
metadata:
  version: "0.2.1"
---

# Lookalike campaign: Windows fallback (Clay connector + Clay Agent)

One seed customer, {{TARGET_COMPANIES}} companies for whom that customer means something, one draft Clay campaign that uses the seed as proof. You launch it in Clay yourself.

**This version is only for Windows without the Clay CLI.** Claude does the thinking and the data work through the Clay connector. The Clay Agent, inside Clay, builds what the connector can't: the workflow that writes people to Clay, the lookalike search, the list and the campaign. Claude types every prompt into the Clay Agent in the built-in browser of the Claude desktop app, reads the answer, and brings you each plan to approve. Never Claude in Chrome.

**The target is {{TARGET_COMPANIES}} companies with a Clay-found work email**, not that many candidates. About 1 in 4 search results passes with a narrow search, and as few as 1 in 20 with a strict bar in a small market; some kept companies have no leader in Clay or no email. Keep searching until the target is reached. Credits are worth spending for quality: forecast each paid step (count times price) and ask once per batch. Every new batch after going back to the search is a new forecast and a new yes.

**The bar is recognition, not firmographics.** A lookalike would read the seed's name and think "that's a company like us, and they rate this". Same service, same kind of buyer, similar size, and the seed's home market (or a public reason to know the seed there).

Settings are in `settings.md`. Run data lives in `~/.growth-systems/lookalike-campaigns/runs/<date>-<seed>/`, called `$RUN`. `companies.json` holds every candidate company: its decision and reason, its `stage` (found, cleared, enriched, emailed, written, dropped), the full company record, main and second contact, and the email. Update the stage after every step, so a new chat can resume. `people.json` is built from it once companies have their contacts. Both hold people's names and never go in a repo.

**Work in batches and save as you go.** Every connector result passes through the chat, so a 100-company run fills it. Work about 50 companies at a time, give search pages and big results to helper agents that write them to `$RUN` and send back short rows, and keep only short rows in the chat (`references/connector.md`, "Big runs"). If the chat gets long or a run stops, start again from `companies.json`: never search or pay twice for a company already in it.

## Who does what

- **Claude, through the Clay connector:** companies and people searches, Enrich Company, Find People at Company, Work Email, writing people to Clay with your "add people" workflow, reading records back.
- **The Clay Agent, from prompts Claude types in the built-in browser:** one-time setup, Find company lookalikes, the people list, the draft campaign, the spam check, previews, the link check, results.
- **You:** sign in to Clay once in the built-in browser, approve every plan and paid step, connect inboxes, send the test email, press Launch.

## Reference files

- `references/clay-agent.md`: where the Clay Agent is, how a prompt goes back and forth, and every prompt (setup, lookalikes, build, checks, results). Without the Clay Agent, its last section has the same steps by hand.
- `references/connector.md`: the connector's tools and what goes wrong with them. Read it before step 2.
- `references/seed-and-search.md`: confirm the seed, the recognition profile, the lookalike and companies searches, the named list
- `references/enrich-and-check.md`: full company records, fit, exclusions, customers and open deals, decision makers, work emails, the target check
- `references/copy.md`: the template, adapting it to a seed, the A/B pair, opener, nudge, merge fields
- `references/results-and-expand.md`: reading results and the expand rule
- `references/gotchas.md`: what goes wrong. Read it before step 2.

## Before starting

0. **Clay CLI check:** if `clay whoami` works, stop: this is the wrong version. Use the CLI version of the lookalike campaigns. On a Mac or Linux computer without the CLI, stop and tell the person to install the Clay CLI.
1. **GTM context:** {{GTM_CONTEXT}}. Read the ICP, product and offer, and messaging pages. Query the customers list and the CRM named in `settings.md` with filters only. Never copy their content here.
2. **Voice:** your `<name>-voice` skill if installed.
3. **Clay connector:** ask it which workspace it is connected to, and say the name back. If the connector isn't connected, stop and say so.
4. **Built-in browser:** open Clay in it and check the person is signed in to the same workspace. If the desktop app's browser isn't available, use the paste-by-hand round trip in `references/clay-agent.md`.
5. **Setup:** settings have no "add people" workflow id yet? Do the setup in `references/clay-agent.md` first.
6. **Prices:** settings have none? Forecasts show counts until they're added (setup, step 3).
7. Asked to review or expand a campaign? Go to `references/results-and-expand.md`.

## Steps

### 1. Pause: the seed

Suggest 2 or 3 seeds from your best customers whose logo you may show, with one line each, unless you named one. **Confirm the seed by domain** in the customers list: similar names are different companies. Read its Clay profile through the connector and write `$RUN/seed.json` per `references/seed-and-search.md`. Check what proof is allowed: the name only, or a quote. Show the profile and the proof line, and wait for a yes.

### 2. Pause: the search strategy

Start with Clay's **Find company lookalikes**, through the Clay Agent: Claude writes the prompt with the seed (and, once found, its best confirmed fits), countries, sizes and description keywords, per `references/seed-and-search.md`. It charges per company returned: forecast it, ask, and put the agreed credit cap in the prompt so the Clay Agent runs without a second round trip. Start with a batch of 10, read it with a one-line fit read each, and ask. Then fill the gaps through the connector with what fits this seed: companies searches, narrower searches when a broad one buries the fits, the seed's competitors, a named list of the seed's best-known peers, Enrich Company to judge the unsure ones. Spend credits where they buy quality: show the plan with a credit forecast and adjust until you say it looks right. Then pull, give each company its recognition points from `seed.json`, read every description, and mark each company keep, check or drop with a reason. Expect to drop most results: plan about 4 candidates per company wanted. Never start extra searches to get round a Search limit: report it.

### 3. Exclusions (free, before any credits)

Run these on every keep and check company before Enrich Company, so no credits go on companies that would drop anyway. The connector searches skip every company already in your Clay Audiences. Companies from the lookalike search and the named list are checked against Audiences too (`references/enrich-and-check.md`). Then check the CRM and the customers list (both in `settings.md`), on companies now and on people once they are found. Test each check on one known match first, so an empty result means clear, not broken. If you have a do-not-contact list, run check-do-not-contact too. Report what dropped and why.

### 4. Pause: credits for full company records

Forecast Enrich Company for every keep and check company left after the exclusions, from the price in settings, say the total, and ask once. Test 2 first. It fills website, LinkedIn page, exact headcount, founded, HQ city, state and country, industry, revenue, description and logo. Drop companies under `min_staff`, unless you say to keep one. A company with no headcount goes to check. Warn when Clay answered with a different company. Show keep and check with a reason each and the recognition points, and wait for your keep or drop on every check one: only kept companies go on to step 5.

### 5. Decision makers (search quota, then credits)

People searches limited to the kept companies not searched yet pick a main contact ({{BUYER_TITLES}}) and a second decision maker ({{SECOND_TITLES}}) per company, per `references/enrich-and-check.md`. Running them again keeps the contacts already found. Only the first part of a title counts ("CEO | Speaker" is a CEO). Member, board, chapter, advisor, volunteer, assistant, vice, chief of staff and partnership titles never count: check the picks. For kept companies with no leader, forecast Find People at Company from settings and ask. Report who has a second person (they get the "you or <second>" opener) and who has none.

### 6. Pause: the copy

Adapt the template in `references/copy.md` to this seed, keeping your wording. Show version A and B filled in for 2 real people, plus the nudge, every spintax variant and the subject. Check every version for spam words, banned phrases, dashes and length, and fix every "must fix" first. Wait for your pick or edits.

### 7. Pause: work emails

Forecast Work Email (main contacts only) and ask. Only people with a Clay-found email go on the list. An email at the company's own other domain is fine; one at another business drops the company. Then count companies with an email against the target. Below it, go back to step 2 and change the strategy before building. Companies dropped so far stay dropped.

### 8. Pause: write to Clay, then build

1. **Write the people.** It spends no data credits. Say how many people and companies will be written, and ask. Then run it through the connector (`references/connector.md`): each run adds the company by domain with its full record, then the person, linked to that company, with the campaign name as the tag.
2. **Check.** Follow the workflow runs by reading one record's progress, not every result: each result repeats all its inputs. When they're done, type the check prompt into the Clay Agent: count the people with the tag, no one may be unlinked, and list who has no country.
3. **Build.** Type the build prompt from `references/clay-agent.md` into the Clay Agent: the people list and the draft campaign with the agreed copy, A/B test, nudge, spam check and previews. Show the person the Clay Agent's plan, and say "go ahead" only after their yes. Report the spam scores and every issue; change wording only with their OK.
4. **A draft that already exists** (more people found after going back to the search) needs no new build: the list follows the tag, so the new people join the draft by themselves. Ask the Clay Agent for the list count, the draft's lead count and two previews instead. Never create a second list or campaign.

### 9. Hand-off

Inboxes, the sending window and the test email are yours, in Clay (`references/clay-agent.md`). Give the campaign name, list count, who had no email, credits used, and the expand rule. Add the campaign to settings ("Campaigns"). Say it is a draft: you press Launch in Clay.

## Rules

- Never launch, resume or send a campaign. Test emails only to your own address, confirmed in this session, after a clear yes.
- Every Clay write is listed first and waits for a yes. Every credit step quotes count times price first.
- Every Clay Agent prompt asks for the plan first and says what not to do (no launch, no enrolling, no test email, no runs unless the step says so). Claude types it in the built-in browser, never in Claude in Chrome, and says go ahead only after the person approves the plan.
- The Clay CLI works? This skill doesn't apply: use the CLI version.
- One email per company. The second decision maker is only named, never emailed.
- Every person written to Clay is linked to their company record. Every company carries the full record from Enrich Company. Every person also carries their own city, state, country and location, taken from the search and Find People results already in hand (free); a country only when it's certain, never guessed.
- Never guess an email address or invent a fact about a company, a person or the seed.
- Proof only within the permission recorded for the seed. A quote needs your confirmation that the person agreed to those exact words.
- Never contact a customer, a company with an open deal, or anyone already on another of your lists.
- No names or emails in list, field or campaign names. Plain language, short sentences, no em dashes.

## Adapting this skill

Prices, caps, the target and the expand rule live in `settings.md`. When a run teaches you something (a bad filter, a seed name mix-up, a Clay Agent prompt that needed changing), ask Claude to add it to `references/gotchas.md` or `references/clay-agent.md`.
