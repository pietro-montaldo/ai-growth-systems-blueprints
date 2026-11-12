---
name: lookalike-campaign
description: "{{YOUR_NAME}}'s lookalike campaign for {{OFFER}}: picks one best customer as the seed, finds companies that would recognise that customer until 100 have a work email (same service, same kind of buyer, similar size, the seed's home market), checks them against the CRM and customers, finds the main decision maker plus a second one to name, looks up work emails, and builds a draft Clay campaign with an A/B test whose copy uses the seed as proof. Also reviews a running campaign and expands it with the next 100 when it works. Use for \"lookalike campaign\", \"lookalikes of <customer>\", \"find companies like <customer> and email them\", \"campaign using <customer> as proof\", \"how is the lookalike campaign doing\", \"expand the lookalike campaign\". Not for signal-based outreach (clay-company-signals) or creator comment lists (linkedin-creator-signals), and it never launches or sends a campaign."
metadata:
  version: "0.2.1"
---

# Lookalike campaign

One seed customer, 100 companies for whom that customer means something, one draft Clay campaign that uses the seed as proof. You launch it in Clay yourself.

**The target is {{TARGET_COMPANIES}} companies with a Clay-found work email**, not that many candidates. Only about 1 in 4 search results passes the bar, and some kept companies have no leader in Clay or no email. Keep searching until the target is reached. Credits are worth spending for quality: forecast each paid step (count times price, plus the action credits Clay also bills) and ask once per batch. Every new batch after going back to the search is a new forecast and a new yes.

**The bar is recognition, not firmographics.** A lookalike would read the seed's name and think "that's a company like us, and they rate this". Same service, same kind of buyer, similar size, and the seed's home market (or a public reason to know the seed there).

Settings are in `settings.md`. Run data lives in `~/.growth-systems/lookalike-campaigns/runs/<date>-<seed>/`, called `$RUN`. `companies.json` holds every candidate company (its decision and reason, the full company record, main and second contact). `people.json` is built from it once companies have their contacts. Both hold people's names and never go in a repo.

## Reference files

- `references/seed-and-search.md`: confirm the seed, the recognition profile, the Clay companies searches, the named list
- `references/enrich-and-check.md`: full company records, fit, exclusions, customers and open deals, decision makers (search, then Find People), work emails, the target check
- `references/copy.md`: the template, adapting it to a seed, the A/B pair, opener, nudge, tokens
- `references/clay-build.md`: one-time setup, people list, company list, draft campaign, checks, test send
- `references/results-and-expand.md`: reading results and the expand rule
- `references/gotchas.md`: what goes wrong. Read it before step 2.

If Clay's own skills are installed, follow them for the mechanics (`clay:searches`, `clay:routines`, `clay:audiences`, `clay:campaigns`). Read each command's `--help` before its first use.

## Before starting

1. **GTM context:** {{GTM_CONTEXT}}. Read the ICP, product and offer, and messaging pages. Query {{CUSTOMERS_SOURCE}} and {{CRM}} with filters only. Never copy their content here.
2. **Voice:** your `<name>-voice` skill if installed.
3. `clay whoami` and the credit balance. The search quota shows on the first search page: check it before promising 100.
4. Settings have no Clay ids yet: do the one-time setup in `references/clay-build.md` first.
5. Asked to review or expand a campaign? Go to `references/results-and-expand.md`.

## Steps

### 1. Pause: the seed

Suggest 2 or 3 seeds from your best customers whose logo you may show, with one line each, unless you named one. **Confirm the seed by domain** in the customers list: similar names are different companies. Read its Clay profile and write `$RUN/seed.json` per `references/seed-and-search.md`. Check what proof is allowed: the name only, or a quote. Show the profile and the proof line, and wait for a yes.

### 2. Pause: the search strategy

Start with Clay's **Find company lookalikes**, seeded with the seed (and, once found, its best confirmed fits) and steered with countries, sizes and description keywords, per `references/seed-and-search.md`. It charges per company returned: forecast it, show a batch of 10 with a one-line fit read each, and ask. Then fill the gaps with what fits this seed: companies searches, narrower searches when a broad one buries the fits, competitor lookups, a named list of the seed's best-known peers, Enrich Company to judge the unsure ones. Spend credits where they buy quality: show the plan with a credit forecast and adjust until you say it looks right. Then pull, give each company its recognition points from `seed.json`, read every description, and mark each company keep, check or drop with a reason. Expect to drop most results: plan about 4 candidates per company wanted. Watch the quota and the per-search cap. Never start extra searches to get round a cap: report it.

### 3. Pause: credits for full company records

Forecast Enrich Company for every keep and check company, from the price in settings, say the total, and ask once. Test 2 first. It fills website, LinkedIn page, exact headcount, founded, HQ city, state and country, industry, revenue, description and logo. Drop companies under `min_staff`, unless you say to keep one. A company with no headcount goes to check. Warn when Clay answered with a different company. Show keep and check with a reason each and the recognition points, and wait for your keep or drop on every check one: only kept companies go on to step 5.

### 4. Exclusions (free)

The search already skips every company in your Clay Audiences. Companies added another way (the named list, by hand) are checked against "Already targeted" in settings. Then check {{CRM}} and the customers list, on companies now and on people once they are found. Test the check on one known customer first, so an empty result means clear, not broken. If you have a do-not-contact list, run check-do-not-contact too. Report what dropped and why.

### 5. Decision makers (search quota, then credits)

One people search limited to the kept companies not searched yet picks a main contact ({{BUYER_TITLES}}) and a second decision maker ({{SECOND_TITLES}}) per company, per `references/enrich-and-check.md`. Running it again keeps the contacts already found. Only the first part of a title counts ("CEO | Speaker" is a CEO). Member, board, chapter, advisor, volunteer, assistant, vice, chief of staff and partnership titles never count: check the picks. For kept companies with no leader, forecast Find People at Company from settings and ask. Report who has a second person (they get the "you or <second>" opener) and who has none.

### 6. Pause: the copy

Adapt the template in `references/copy.md` to this seed, keeping your wording. Show version A and B filled in for 2 real people, plus the nudge, every spintax variant and the subject. Check every version for spam words, banned phrases, dashes and length, and fix every "must fix" first. Wait for your pick or edits.

### 7. Pause: work emails

Forecast Work Email (main contacts only) and ask. Only people with a Clay-found email go on the list. An email at the company's own other domain is fine; one at another business drops the company. Then count companies with an email against the target. Below it, go back to step 2 and change the strategy before building. Companies dropped so far stay dropped.

### 8. Pause: build in Clay

First read `$RUN` and the drafts already in Clay (`clay campaigns list`): if a draft for this run exists, update it rather than create a second. List what will be created (people list, company list, campaign, variants) and ask once. Then follow `references/clay-build.md`: tag people (the routine adds each person's company and links the person to it, so the Company column in Clay is filled) and companies, create both lists and check counts, check that no person is unlinked, create the draft campaign, add A, start the test, give B its own first email, name the variants, spam check, previews for 2 leads. Ask which inboxes and sending window. Ask before the test send, then send one test per variant to the address you confirm.

### 9. Hand-off

Give the campaign link, list counts, who had no email, credits used, and the expand rule. Add the campaign to settings ("Campaigns") and its company list to "Already targeted". Say it is a draft: you press Launch in Clay.

## Rules

- Never launch, resume or send a campaign. Test emails only to your own address, confirmed in this session, after a clear yes.
- Every Clay write is listed first and waits for a yes. Every credit step quotes count times price first.
- One email per company. The second decision maker is only named, never emailed.
- Every person written to Clay is linked to their company record. Every company carries the full record from Enrich Company. Every person also carries their own city, state, country and location, taken from the search and Find People results already in hand (free); a country only when it's certain, never guessed.
- Never guess an email address or invent a fact about a company, a person or the seed.
- Proof only within the permission recorded for the seed. A quote needs your confirmation that the person agreed to those exact words.
- Never contact a customer, a company with an open deal, or anyone already on another of your lists.
- No names or emails in list, field or campaign names. Plain language, short sentences, no em dashes.

## Adapting this skill

Prices, caps, the target and the expand rule live in `settings.md`. When a run teaches you something (a bad filter, a seed name mix-up), ask Claude to add it to `references/gotchas.md`.
