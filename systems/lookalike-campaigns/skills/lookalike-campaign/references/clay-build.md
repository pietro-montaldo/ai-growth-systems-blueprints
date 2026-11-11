# Building it in Clay

Names: campaign = people list = tag: `<Seed> lookalikes <YYYY-MM-DD> <offer short name>`. Company list: `<Seed> lookalikes <YYYY-MM-DD> <buyer group>`. No personal names. List everything below first and build after one yes. One change per command, and report each one.

Before building, read `$RUN` and `clay campaigns list`. A build can already have started from another session: if a draft campaign or list for this run exists, update it rather than create a second one.

## 0. One-time setup

Skip what settings already has an id for. Ask before creating each piece.

- **People fields** (text): campaign tag, company display name, opener, seed, second contact, second contact title, and the company record: domain, website, LinkedIn page, city, state, country, industry, headcount, founded, description, revenue, logo. If creator signals' email setup already made a campaign tag field, reuse it, so one campaign tag per person holds across systems.
- **"Lookalikes: add people to list" workflow and routine:** a manual trigger with email, first name, last name, full name, LinkedIn link, title, campaign, opener, company, company_domain, the other company record fields, seed, second contact and second contact title. Required: email, campaign, company_domain. Two steps:
  1. **Upsert company:** add or update a company record, matching on `company_domain`, with the full record: name, LinkedIn page, website, city, state, country, industry, headcount, founded, revenue, description and logo. Skip empty values. Then the company is complete even before the company routine runs.
  2. **Upsert person**, after step 1: add or update a people record by email and LinkedIn link, write the fields above, and **link the person to the company from step 1**: add a step input that reads step 1's result record id (`$.result.entityId`) and map it to the person's company association (`associations|accountId`).

  A trigger can have only one outgoing step: wire step 1 after the trigger and step 2 after step 1. `clay workflows graph validate` should show no warnings. Test once on your own record, publish after a yes, create the routine.
- **Company fields** (text): list tag, ICP fit, seed, main contact, second contact, website, description, founded.
- **"Lookalikes: add companies to list" workflow and routine:** the same shape for companies in one step, matching by domain, skipping empty values, with the full company record.
- Read the credit prices of Enrich Company, Find People at Company, Work Email and Enrich Person (`clay routines get <id>`, `estimatedCreditCost.perRun`) into settings.

## 1. People list

Run the people routine with one item per main contact (files of up to 100 items; split above that and run one at a time): the campaign name as the tag, company display name, opener, seed, second contact, and the full company record from Enrich Company. `company_domain` is required; enrich any company with no website or city first.

The link is what fills the person's **Company** column in Clay. Writing the company name on the person does not: a matching email domain or name never creates the link.

A person carries one campaign tag, so tagging moves them off any older list and pauses them there: the search and exclusion steps should have kept those people out. Then create the list (people filtered on tag = campaign name) and check its count. The search index lags about 10 seconds: wait and recount before looking for who is missing.

Then check the link. This must return 0:

```
count from people where <campaign tag field> = "<campaign name>" and not company.exists()
```

## 2. Company list, ICP scored

Companies only show a fit in Clay once the ICP field is filled; empty looks like "not a fit". Score each company against the live ICP card in one line (card and tier), then run the company routine with tag, ICP fit, seed, main and second contact, and the full record: website, description, founded, city, state, country, logo, headcount, revenue. Create the company list, check the count, and read 2 records back. Say how many companies already existed.

## 3. The campaign

1. `clay campaigns create --name "<campaign name>"`. It makes a list-fed campaign: right here, the list is fixed.
2. Attach the people list, then set the goal in one sentence.
3. `clay campaigns audience <cam>` for the field ids; swap them into the copy tokens. Every company record field on the person (website, city, industry, headcount, founded, description), the seed and the second contact can be tokens too.
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
