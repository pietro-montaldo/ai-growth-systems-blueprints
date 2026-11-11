# Building it in Clay

Names: campaign = people list = tag: `<Seed> lookalikes <YYYY-MM-DD> <offer short name>`. Company list: `<Seed> lookalikes <YYYY-MM-DD> <buyer group>`. No personal names. List everything below first and build after one yes. One change per command, and report each one.

## 0. One-time setup

Skip what settings already has an id for. Ask before creating each piece.

- **People fields** (text): campaign tag, company display name, opener. If creator signals' email setup already made a campaign tag and company field, reuse them.
- **"Add to campaign list" workflow and routine:** manual trigger with email, first name, last name, full name, LinkedIn link, title, company, campaign, opener; one step that adds or updates a people record by email and LinkedIn link and writes those fields. Test once on your own record, publish after a yes, create the routine. Shared with creator signals when it exists: never change its inputs without saying so.
- **Company fields** (text): list tag, ICP fit, seed, main contact, second contact.
- **"Add to company list" workflow and routine:** the same shape for companies, matching by domain, skipping empty values.
- Read the credit prices of Enrich Person, Enrich Company and Work Email (`clay routines get <id>`, `estimatedCreditCost.perRun`) into settings.

## 1. People list

Run the people routine with one item per main contact (the campaign name as the tag, plus company display name and opener). A person carries one campaign tag, so tagging moves them off any older list and pauses them there: the exclusion step should have kept those people out. Then create the list (people filtered on tag = campaign name) and check its count. The search index lags about 10 seconds: wait and recount before looking for who is missing.

## 2. Company list, ICP scored

Companies only show a fit in Clay once the ICP field is filled; empty looks like "not a fit". Score each company against the live ICP card in one line (card and tier), then run the company routine with tag, ICP fit, seed, main and second contact. Create the company list, check the count, and read 2 records back. Say how many companies already existed.

## 3. The campaign

1. `clay campaigns create --name "<campaign name>"`. It makes a list-fed campaign: right here, the list is fixed.
2. Attach the people list, then set the goal in one sentence.
3. `clay campaigns audience <cam>` for the field ids; swap them into the copy tokens.
4. Add two steps to the first variant: the first email (new thread, day 0, subject and body) and the nudge (reply in thread, day 3, body only).
5. Start the A/B test: Clay copies the sequence into variant B, 50/50.
6. Give B its own first email body, unlinked from A. Subject and nudge stay shared.
7. Name the variants, one at a time: "A: <what A tests>", "B: <what B tests>".

## 4. Checks

Spam check and previews for A and B are free. Report the scores and each issue; change wording only with the person's OK. Show the rendered previews for one lead with a second person and one without.

## 5. Inboxes, window, test

- Inboxes: list the connected ones by address and ask.
- Window: Clay's default is Mon to Fri, 9:00 to 17:00 New York. For a seed in another market, offer that market's time zone. Schedule settings are replaced whole: read, change, send all back.
- Test: ask "Send a test of A and B to <your address>?" and confirm the address in this session. One test per variant. Never retry a send automatically.

## 6. Hand-off

Campaign link, counts, who had no email, credits used (balance before and after), and: "It's a draft. Press Launch in Clay when you're happy." Then add the campaign and the company list to settings.
