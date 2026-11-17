# One-time Clay setup

Run once, before the first email campaign. Each item creates something in your Clay workspace: say what will be created and ask first. Save every id in `../linkedin-creator-signals/settings.md` under "Email". Ask the connector which workspace it is on, and check the built-in browser is signed in to the same one.

## 1. What gets built

Clay people records have name, title, email and LinkedIn link, but no company field and nothing to tag a campaign with. The Clay Agent creates these text fields on people (reusing any that exist):

| Name | Holds |
| --- | --- |
| Creator signals campaign | the campaign name: the tag the one-off list filters on |
| Creator signals company | current company |
| Creator signals post | creator and post subject ("Sam's post on reporting") |
| Creator signals CTA | short CTA topic, lowercase ("a session on automating client reports") |
| Creator signals CTA date | "Nov 10" |
| Creator signals CTA link | the CTA link |

And the workflow "Creator signals: add to campaign list": a manual trigger with every input of the list, then step 1 adds or updates the company by domain with its full record, and step 2 adds or updates the person, **linked to the company from step 1**, with their own city, state, country, location and seniority and the six fields. Without that link the person's Company column in Clay stays empty, even when the company name is written on the person.

## 2. Build it with the Clay Agent

Use the email setup prompt in `../linkedin-creator-signals/references/clay-agent.md`. Check the Clay Agent's plan: the company is matched on the domain, the person is linked to the company record from step 1 (not only the name), the six fields are listed, and nothing runs or is published. Show the plan to the person and say go ahead only after their yes. The workflow doesn't need publishing for the connector to run it: save its id from the connector's list of routines.

## 3. Test it on your own record

After a yes, run the workflow once through the connector on your own record: your email, your LinkedIn link, your company's domain, the campaign "setup test", and your first, last and full name exactly as they should read in Clay. The workflow overwrites whatever it's given, so a first name sent as the full name replaces the real one. Read the result: the person and the company are written and the six fields are filled. Then the Clay Agent check prompt with the campaign "setup test": 1 person, 0 unlinked. The test record can stay, or you remove it in Clay.

## Doing it by hand in Clay

Without the Clay Agent, see "Doing it by hand" in `../linkedin-creator-signals/references/clay-agent.md`.
