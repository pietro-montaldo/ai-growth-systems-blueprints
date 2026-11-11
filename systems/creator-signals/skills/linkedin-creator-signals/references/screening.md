# Screening commenters

A person counts once, however many comments they left. Their best comment decides. Read every comment yourself: no keyword list catches pod and AI comments well. On a big week, split the comments across subagents by post and ask each for back a table of `slug, verdict, reason`.

## Drop straight away

| Reason | Rule |
| --- | --- |
| no person | a company, showcase or school page, or no `/in/` profile link |
| already known | customer, open deal or CRM lead (see settings) |
| seen | enriched in the last 90 days (`seen.csv`) |
| empty | under 5 words once links, hashtags and emoji are gone, or filler only ("great post", "thanks for sharing", "following", "100%", "congrats") |
| lead magnet keyword | three words or fewer on a lead magnet post, or a one or two word reply in capitals |
| competitor | sells {{COMPETITOR_SERVICES}} |
| non-buyer | developer, engineer, student, recruiter or "open to work", unless the headline also says founder, owner, consultant or similar |

The creator replying on their own post is skipped, not dropped.

## AI-written comments

Add points. One signal proves nothing; several together usually mean a tool wrote it.

| Signal | Points |
| --- | --- |
| stock phrases ("this resonates", "couldn't agree more", "game changer", "invaluable", "navigating the landscape") | 2 each, max 4 |
| stock closing question ("What are your thoughts?", "Curious how others approach this") | 2 |
| "It's not just X, it's Y" | 2 |
| praise opener ("Great breakdown", "Love this") | 1 |
| names the author ("Great insights, Sarah!") | 1 |
| em dash | 1 |
| bullet or numbered list | 1 |
| three-part list ("clarity, focus, and execution") | 1 |
| restates the post | 1 |
| 12 or more words with no I, we or my and no question | 1 |
| their own concrete detail (I, we, my plus a number, a client, a team, last week) | minus 2 |

3 or 4 points: review it. 5 or more: drop.

## The judgment pass

For every person left, ask one question: **does the comment add something only this person could have said?**

Keep when it has:
- their own experience, with a detail (a tool, a number, a client type, what went wrong),
- a real question about how to do the thing,
- a disagreement or caveat with a reason,
- a clear sign they have the problem you solve ("we're 6 people and still copy-paste every proposal").

Drop when it is:
- praise plus a summary of the post,
- a generic question that fits any post,
- a polished paragraph that could sit under any post unchanged,
- a pod pattern: an aphorism that restates the post as a rule, the creator's name tagged with nothing specific, a stock engagement question.

When in doubt, keep. Enrichment and scoring catch weak fits later, and a lost real buyer costs more than one lookup.

Use these reasons so the counts group well: "AI-written or pod comment", "generic praise", "competitor: <what>", "wrong layer: <role>", "real point in own voice".

## Who is a competitor

Only people who sell what you sell: {{COMPETITOR_SERVICES}}. People who sell something next to it are often your buyers, not competitors. Decide this once with the competitors page, and write the edge cases here.

## Examples

| Comment | Call |
| --- | --- |
| "Great post!" | drop, empty |
| "GUIDE" (on "comment GUIDE for the guide") | drop, lead magnet keyword |
| "This resonates deeply, Mark. In today's fast-paced landscape, it isn't just about efficiency, it's about transformation. What are your thoughts?" | drop, AI-written |
| "Love this. Clarity, consistency and execution are what make it stick." | drop, praise plus summary |
| "We tried this with our proposal template last month and cut drafting from 2 hours to 20 minutes, but the formatting still breaks. Did you hit that?" | keep: own detail and a real question |
| "I'm a solo consultant and still do all of this by hand. Where do I even start?" | keep: has the problem you solve |
