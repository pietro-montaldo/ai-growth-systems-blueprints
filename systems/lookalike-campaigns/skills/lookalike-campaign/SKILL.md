---
name: lookalike-campaign
description: "{{YOUR_NAME}}'s lookalike campaign for {{OFFER}}: picks one best customer as the seed, finds 100 companies that would recognise that customer (same service, same kind of buyer, similar size, the seed's home market), checks them against the CRM and customers, finds the main decision maker plus a second one to name, looks up work emails, and builds a draft Clay campaign with an A/B test whose copy uses the seed as proof. Also reviews a running campaign and expands it with the next 100 when it works. Use for \"lookalike campaign\", \"lookalikes of <customer>\", \"find companies like <customer> and email them\", \"campaign using <customer> as proof\", \"how is the lookalike campaign doing\", \"expand the lookalike campaign\". Not for signal-based outreach (clay-company-signals) or creator comment lists (linkedin-creator-signals), and it never launches or sends a campaign."
metadata:
  version: "0.1.0"
---

# Lookalike campaign

One seed customer, 100 companies for whom that customer means something, one draft Clay campaign that uses the seed as proof. You launch it in Clay yourself.

**The bar is recognition, not firmographics.** A lookalike would read the seed's name and think "that's a company like us, and they rate this". Same service, same kind of buyer, similar size, and the seed's home market (or a public reason to know the seed there).

Settings are in `settings.md`. Run data lives in `~/.growth-systems/lookalike-campaigns/runs/<date>-<seed>/`, called `$RUN`, with one `people.json` that every step updates. It holds people's names and never goes in a repo.

## Reference files

- `references/seed-and-search.md`: confirm the seed, the recognition profile, the Clay search
- `references/enrich-and-check.md`: domains, headcount, recognition score, exclusions, customers and open deals, second decision maker, work emails
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

### 2. Pause: the search

Draft the search from `seed.json` and the ICP card. Show the filters in plain words. Pull a sample of 10, show it with a one-line fit read each, and adjust until you say it looks right. Then pull enough for 100 companies (about 2.5 people per company wanted), watching the quota and the per-search cap. Never start extra searches to get round a cap: report it.

### 3. Pause: credits for domains and headcount

Forecast Enrich Person, then Enrich Company, from the prices in settings, say the total, and ask once. Test on 2 people first. Then score per `references/enrich-and-check.md`. Show keep, check and drop with reasons and the recognition score of each company, and let you decide the borderline ones.

### 4. Exclusions (free)

Drop companies already on another of your lists (`settings.md`, "Already targeted"), then check {{CRM}} and the customers list. Test the check on one known customer first, so an empty result means clear, not broken. If you have a do-not-contact list, run check-do-not-contact too. Report what dropped and why.

### 5. Second decision maker (search quota only)

One search limited to the kept companies for {{SECOND_TITLES}}. Pick one per company per `references/enrich-and-check.md`. Report how many have a second person; the rest get the solo opener.

### 6. Pause: the copy

Adapt the template in `references/copy.md` to this seed, keeping your wording. Show version A and B filled in for 2 real people, plus the nudge, every spintax variant and the subject. Check every version for spam words, banned phrases, dashes and length, and fix every "must fix" first. Wait for your pick or edits.

### 7. Pause: work emails

Forecast Work Email (main contacts only) and ask. Only people with a Clay-found email go on the list. Flag emails at another domain.

### 8. Pause: build in Clay

List what will be created (people list, company list, campaign, variants) and ask once. Then follow `references/clay-build.md`: tag people and companies, create both lists and check counts, create the draft campaign, add A, start the test, give B its own first email, name the variants, spam check, previews for 2 leads. Ask which inboxes and sending window. Ask before the test send, then send one test per variant to the address you confirm.

### 9. Hand-off

Give the campaign link, list counts, who had no email, credits used, and the expand rule. Add the campaign to settings ("Campaigns") and its company list to "Already targeted". Say it is a draft: you press Launch in Clay.

## Rules

- Never launch, resume or send a campaign. Test emails only to your own address, confirmed in this session, after a clear yes.
- Every Clay write is listed first and waits for a yes. Every credit step quotes count times price first.
- One email per company. The second decision maker is only named, never emailed.
- Never guess an email address or invent a fact about a company, a person or the seed.
- Proof only within the permission recorded for the seed. A quote needs your confirmation that the person agreed to those exact words.
- Never contact a customer, a company with an open deal, or anyone already on another of your lists.
- No names or emails in list, field or campaign names. Plain language, short sentences, no em dashes.

## Adapting this skill

Prices, caps and the expand rule live in `settings.md`. When a run teaches you something (a bad filter, a seed name mix-up), ask Claude to add it to `references/gotchas.md`.
