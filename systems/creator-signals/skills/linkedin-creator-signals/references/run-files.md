# Run files

Everything lives in `~/.growth-systems/creator-signals/` (`$STATE`). It holds people's names: keep it out of any repo and any shared folder.

| File | Holds |
| --- | --- |
| `runs/YYYY-MM-DD/run.json` | `stage` (new, pause-1, pause-2, scored, drafted, campaign-ready), `channel` (linkedin or email), `sheet` (file id and name), `notes` |
| `runs/YYYY-MM-DD/posts.json` | every post scraped, with your keep, drop or unsure and the reason |
| `runs/YYYY-MM-DD/comments.json` | the raw comments of kept posts |
| `runs/YYYY-MM-DD/people.json` | one row per person: slug, name, headline, best comment, post, verdict, Clay fields, card, fit, why, interests, status, draft, email |
| `posts-done.csv` | `post_url,run` for every post already comment-scraped. Later runs skip them. |
| `seen.csv` | `slug,date,why` for everyone enriched. Skipped for 90 days, so nobody costs Clay credits twice. |
| `spend-YYYY-MM.json` | `{"apify_usd": 0, "clay_credits": 0, "runs": [...]}`: forecast and actual per paid step |

`$RUN` is the newest run folder whose stage is not finished. "Slug" is the part after `linkedin.com/in/` in a profile link, lowercase.

## The weekly sheet

One Google Sheet per run, in the Drive folder, two tabs:

- **Posts:** creator, date, post link, first line, comments, decision, reason. The forecast on top.
- **People:** Status, Fit, Name, Headline, Company, Title, Size, Location, Card, Why, Interests, Best comment, Post, Flags, then Draft, CTA, Channel, Email, Campaign (filled later).

Dark header row, frozen header plus Status and Fit, wrapped text, a Status dropdown (shortlist, hold, skip, send, sent, replied) and a filter. Reuse the file if one exists for the same date. CSV in `$RUN` only when Sheets is not connected, and say so.
