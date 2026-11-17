# Run files

Everything lives in `~/.growth-systems/creator-signals/` (`$STATE`). It holds people's names: keep it out of any repo and any shared folder.

| File | Holds |
| --- | --- |
| `runs/YYYY-MM-DD/run.json` | `stage` (new, pause-1, pause-2, scored, drafted, campaign-ready), `channel` (linkedin or email), `outreach_file` (LinkedIn path: file id and name, or the Excel path), `notes` |
| `runs/YYYY-MM-DD/posts.json` | every post scraped, with your keep, drop or unsure and the reason |
| `runs/YYYY-MM-DD/comments.json` | the raw comments of kept posts |
| `runs/YYYY-MM-DD/review-posts.json`, `review-people.json` | the numbers shown in the last review: number to post link or profile slug |
| `runs/YYYY-MM-DD/people.json` | one row per person: slug, name, headline, best comment, post, verdict, Clay fields, card, fit, why, interests, status, draft, email |
| `posts-done.csv` | `post_url,run` for every post already comment-scraped. Later runs skip them. |
| `seen.csv` | `slug,date,why` for everyone enriched. Skipped for 90 days, so nobody costs Clay credits twice. |
| `spend-YYYY-MM.json` | `{"apify_usd": 0, "clay_credits": 0, "runs": [...]}`: forecast and actual per paid step |

`$RUN` is the newest run folder whose stage is not finished. "Slug" is the part after `linkedin.com/in/` in a profile link, lowercase.

## The outreach file (LinkedIn path only)

The only file the system creates, made after you agree the drafts. One per run: a Google Sheet in the outreach folder when Google Drive is connected, otherwise an Excel file in `$RUN` sent to you. Named "{{DRIVE_FOLDER}} YYYY-MM-DD". One tab, "Outreach", one row per person on the confirmed list:

#, Status, Name, LinkedIn link, Message, Characters, Why picked, Fit, Role, Company, Location, Their comment, Creator, Post link, CTA, CTA link, Sent as (connection note or DM), Sent on, Notes.

Dark header row, frozen header plus #, Status and Name, wrapped text, a wide Message column, a Status dropdown (to send, sent, replied, no reply, skip) and a filter. Reuse the file if one exists for the same date. The email path creates no file: the Clay list and campaign are the record.
