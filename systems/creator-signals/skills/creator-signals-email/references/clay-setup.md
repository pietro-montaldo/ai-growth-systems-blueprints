# One-time Clay setup

Run once, before the first email campaign. Each item creates something in your Clay workspace: say what you will create and ask first. Save every id in `../linkedin-creator-signals/settings.md` under "Email". Check the workspace with `clay whoami`.

## 1. People fields

Clay people records have name, title, email and LinkedIn link, but no company field and nothing to tag a campaign with. Create these text fields on people:

| Name | Holds |
| --- | --- |
| Creator signals campaign | the campaign name: the tag the one-off list filters on |
| Creator signals company | current company |
| Creator signals post | creator and post subject ("Sam's post on reporting") |
| Creator signals CTA | short CTA topic, lowercase ("a session on automating client reports") |
| Creator signals CTA date | "Nov 10" |
| Creator signals CTA link | the CTA link |

Clay renames a taken name ("Name (2)"): read the returned id and name. Reuse a field that already exists.

## 2. The "add to campaign list" workflow

- Name: "Creator signals: add to campaign list".
- Trigger: manual, with inputs email, first_name, last_name, full_name, linkedin_url, title, company, company_domain, company_linkedin, campaign, post, cta, cta_date, cta_link. Required: email, campaign, company_domain.
- Step 1, "Upsert company": adds or updates a company record, matching on domain (`company_domain`). Write domain, company name (`company`) and LinkedIn page (`company_linkedin`). Skip empty values.
- Step 2, "Add to campaign list", after step 1: adds or updates a people record. Match on email and LinkedIn link, write name, first name, last name, title, email, LinkedIn link and the six fields above, skip empty values. **Link the person to the company from step 1:** add a step input that reads step 1's result record id (`$.result.entityId`) and map it to the person's company association (`associations|accountId`).

Without that link the person's Company column in Clay stays empty, even when the company name is written on the person. A matching email domain or name never creates the link.

A trigger can have only one outgoing step: create step 1 first, wire step 2 after step 1, and step 1 after the trigger. `clay workflows graph validate` should show no warnings.

Already set up without the company step? Add it the same way, then run the routine again for the people already tagged, so they are linked too.

Test it once on your own record only (your name, email and LinkedIn link, campaign "setup test"). Read the record back. Ask before publishing. Then publish it and create a routine from it. Save the routine id.

## 3. Check

The routine shows the inputs above, a list filtered on campaign "setup test" counts 1, and your test record shows its company in the Company column. Tell the person what was created, and that the test record can stay or be removed by hand.

## Doing it by hand in Clay

Same three pieces in the Clay app: Audiences, People, Fields for step 1; Workflows, New, manual trigger, then two "Upsert record" steps for step 2 (company first, then the person with the company set as its association); then Publish and "Create routine".
