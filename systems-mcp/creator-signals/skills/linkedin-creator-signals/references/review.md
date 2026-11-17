# Reviews in chat

Every pause is a review in chat. Nothing is created until the LinkedIn path makes its outreach file at the very end. The goal of each review: you can decide in one reply, without opening anything else.

## Shape of every review

1. **One line on where we are:** what ran, what it cost against the forecast, what the next paid step costs.
2. **The table.** Every row has a number, a link (the post or the profile) and the reason it was kept or picked. Keep each cell to one line. Show every row: you decide on all of them.
3. **What stands out,** at most 3 bullets: borderline calls, flags (company fixed from the profile, commented on several posts), anything the numbers hide. Skip it when there is nothing.
4. **The question,** last, in one line, with the reply that approves it and how to change things by number ("Reply 'approve the comment scrape', or tell me which numbers to switch").

Then stop and wait.

## The three reviews

| Pause | Each row shows | You confirm |
| --- | --- | --- |
| 1. Posts | number, creator, post first line linked to the post, why kept or dropped, comment count, cost. Grouped keep, unsure, drop | the posts to scrape comments on |
| 2. People to enrich | number, name linked to the profile, headline, their comment linked to the post, why kept | who gets Clay credits |
| 3. Shortlist | number, fit, name linked to the profile, role and company, why picked, their comment linked to the post. Fit 3 listed after as "on hold", the rest as a count | the final list and the channel |

Example row at Pause 3:

| # | Fit | Name | Role | Why picked | Their comment |
| --- | --- | --- | --- | --- | --- |
| 1 | 5 | [Ana](https://www.linkedin.com/in/example/) | Founder, Brightlane | Runs a 6-person agency, wants repeatable client reporting | [We still copy-paste every report by hand…](https://www.linkedin.com/posts/example) |

## Applying your answer

- Save the numbers with the run (`$RUN/review-posts.json` or `$RUN/review-people.json`: number to post link or profile slug) when the table is shown. Apply changes by number, never by guessing a name.
- Short answers work: "switch 3 and 7", "skip 12, 14", "move 24 up", "drop 3", "all good".
- Confirm each change in one line before the paid call ("Switched 3 to keep and 7 to drop. New forecast: USD 0.61.").
- A name that is not in the table: say so and ask. Never add people from outside the run.

## When the run was scheduled

A scheduled run can't wait for an answer. It shows the Pause 1 review in its own session and sends a short note to {{NOTIFY}}. You open that session, or start one and say "creator signals review", and the review is shown again from `$RUN`.
