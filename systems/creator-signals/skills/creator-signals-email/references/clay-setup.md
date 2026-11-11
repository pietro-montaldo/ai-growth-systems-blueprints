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
- Trigger: manual, with inputs email, first_name, last_name, full_name, linkedin_url, title, company, campaign, post, cta, cta_date, cta_link.
- One step that adds or updates a people record: match on email and LinkedIn link, write name, first name, last name, title, email, LinkedIn link and the six fields above, skip empty values.

Test it once on your own record only (your name, email and LinkedIn link, campaign "setup test"). Read the record back. Ask before publishing. Then publish it and create a routine from it. Save the routine id.

## 3. Check

The routine shows the inputs above, and a list filtered on campaign "setup test" counts 1. Tell the person what was created, and that the test record can stay or be removed by hand.

## Doing it by hand in Clay

Same three pieces in the Clay app: Audiences, People, Fields for step 1; Workflows, New, manual trigger, "Upsert record" step for step 2; then Publish and "Create routine".
