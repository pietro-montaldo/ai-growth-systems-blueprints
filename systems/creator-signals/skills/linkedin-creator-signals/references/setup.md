# Setup and first run

## Connectors

| Connector | Used for | If missing |
| --- | --- | --- |
| Apify | posts and comments | stop and say so: nothing works without the scrape |
| GTM context (Notion or repo) | ICP, competitors, messaging | stop: scoring needs the live ICP |
| Your CRM | skip customers and open deals | say the check was skipped and mark rows "CRM unchecked" |
| Clay CLI (`clay`, signed in) | Enrich Person, and for email Work Email, Enrich Company and Campaigns, as routines | offer headline-only scoring, clearly marked |
| Google Drive and Sheets | the LinkedIn outreach file, only on the LinkedIn path | an Excel file in the run folder, sent to you |
| Slack or email | the short "review waiting" note when the scheduled run finishes | the scheduled run's own session shows the review |

## One-time setup

1. **Creators, asked first.** You pick the creators to track: this is the first question when you copy the system (`{{CREATORS}}`), and the creators mode adds more later. For each one: name, profile link, one line on why their audience is your buyer. Check each against your competitors page before saving: a creator who sells what you sell is not added, and you're told why. Recommend 8 to 15 creators to start. Save them in `settings.md` with the date of the check.
2. **Outreach folder (LinkedIn path only).** Set it up the first time you pick LinkedIn, not before. With Google Drive connected: one private folder for the outreach files and nothing else. Find a folder named as in settings, or create it after a yes, and save its id in `settings.md`. Without Google: the Excel file goes in the run folder and is sent to you.
3. **Clay prices.** Read the credit price of Enrich Person, Work Email and Enrich Company from your workspace (`clay routines list`, then `clay routines get <id>`, field `estimatedCreditCost.perRun`). The same output has `estimatedCreditCost.actionExecution`, the action credits per run, billed from a separate balance. Save both, and the routine ids, in `settings.md`. Without them, forecasts show lookups, not credits.
4. **Apify prices and caps.** Check the actor names and the price per result in Apify. Confirm `max_usd_posts` and `max_usd_month`.

## Actor inputs

- **Posts:** `targetUrls` = creator links, `maxPosts` = `max_posts_per_creator`, `postedLimit` = `posted_limit`, `scrapeComments` and `scrapeReactions` false.
- **Comments:** `posts` = kept post links, `maxItems` = `max_comments_per_post`, `postedLimit` = `posted_limit`, `scrapeReplies` false, `profileScraperMode` "short". Ask only for the fields you use: comment text, name, headline, profile link, post.
- **Comments fallback** (one run per post, paged): `{"postIds": ["<post url>"], "page_number": 1, "sortOrder": "most recent", "limit": 100}`.

Actors change. If a field comes back empty for every row, look at one raw item and find what the actor calls it now.

## First live run, together

1. Posts for **one** creator, 5 posts. Check the fields: link, text, author, comment count.
2. Comments on the kept posts, 20 each. If most profile links are long ids instead of names (`/in/ACoA...`), the CRM match will miss: switch `profileScraperMode` to "main" (it costs a little more, quote it) or use the fallback actor.
3. Enrich Person on **2** people. Look at one full result and note the field names in the run notes.
4. Compare forecast and real spend, and report both.

## Schedule

Offer a weekly scheduled task on {{RUN_DAY}} that runs this skill in posts mode and stops at Pause 1. It only scrapes posts under the cap, shows the Pause 1 review in its session and sends the short note. Comments, Clay and drafts always wait for a session you start. Show the prompt first.
