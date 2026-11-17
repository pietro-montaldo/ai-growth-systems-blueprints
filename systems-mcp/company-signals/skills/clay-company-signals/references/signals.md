# Signals

The Clay Agent creates, reads back and resumes the signals from the prompts in `clay-agent.md`. Never guess a fixed value (a seniority level, a news topic): a misspelt one matches nothing and the signal looks broken. When unsure, ask the Clay Agent for the allowed values first.

## From ICP triggers to signal types

Read the ICP card's buying triggers and map each one:

| A trigger like | Clay signal type | Watches |
|---|---|---|
| "they are hiring for X", "the job post mentions the tool", "a team is being built" | JobPost | companies |
| "a new Head of X just joined", "new leader in the buyer role" | NewHire | companies |
| "just raised", "new leader announced", "launched a new initiative", "acquired" | News (topics such as Fundraising, Executive Appointment, New Initiatives and Programs) | companies |
| "they are researching our category" | CompanyTopicIntent | companies |
| "our champion changed jobs" | JobChange | people, not this watchlist |

Pick the 2 or 3 strongest. Name them for the person in plain words, for example "a job post at a watched company mentions <tool>" or "a watched company hires a Head of <function>".

**Topic intent** tells you a company is researching a topic. Use it to rank or alert, not as the opening line of an email: "I saw you were researching X" reads as creepy. It is also turned on separately in Clay, so creating it can fail on plans where other signals work. Its topics come from Clay's own list: ask the Clay Agent to search topics for your plain words, and never copy topic ids from another signal.

## Settings to put in the prompt

All signals watch the watchlist segment by its id, entity type companies. Never put a segment's name where its id goes.

- **JobPost:** job description keywords or job title keywords from the trigger, posted in the last 30 days, at most 3 per company, starting from the companies in the segment.
- **NewHire:** job title keywords for the buyer roles, seniority (for example c-suite, vp, director, head), started in the last 3 months, and a one-time look back of 3 months on the first run.
- **News:** topics from Clay's fixed list, and read only new articles on each run.
- **CompanyTopicIntent:** topic ids from Clay's topic search.

Name each signal "Signals: <what it watches> (<watchlist>)". Weekly is a good start.

## Cost, before resuming

Two ways Clay charges:

- **Per company checked**, on every run, whether or not anything happened: JobPost, NewHire, topic intent (times each topic). Cost per month is about companies × runs per month × the per-check price.
- **Per result**: News. A tight topic list is the cost lever.

The Clay Agent can't price a signal. After creating them paused, open **Companies, Data hub, Signals** in the built-in browser and read each one's credit spend and per-run cost. When the CLI version was built, Clay showed about 0.2 credits per company per run for JobPost and NewHire. So for two weekly signals:

| Companies | Credits a month, about |
|---|---|
| 100 | 170 |
| 250 | 430 |
| 500 | 860 |

Treat these as a rough guide. Say the real number before resuming.

**The workflow spends too.** Each hit starts one run of the buyer workflow once it is published, and that run spends on its own, with no budget cap (`workflow.md`, "Cost per hit"). Quote both together: signal checks per month, plus the expected hits times the per-hit cost.

## Create, read back, resume

1. The setup check lists existing signals. If one of the same type already watches the same companies, reuse it.
2. The signals prompt creates them **paused**, and the Clay Agent reads each back. Check the segment id, the filters word for word, the status and the `sig_` id. Save the ids in settings: the workflow trigger needs the `sig_` id.
3. Show the settings and the cost. Only after a clear yes, the resume prompt.

To change a signal's filters later, ask the Clay Agent to read the current filters first, then send the whole new set: a partial change can replace the rest.

## Where to see them

In Clay: **Companies, Data hub, Signals**. Signals that watch segments are listed there, with cadence, segments, credit spend and hits. The sidebar Signals page may show only table-based signals, such as website visitors. Hits are saved on each company, not in a table, and can take a while to show up after a run.

## What to expect

Signals only see changes after they start. NewHire looks back once, on the first run. A new watchlist mostly pays off in the weeks after setup.
