# Things Clay does that are easy to get wrong

Each of these cost a real build an hour or more. Check them before building.

## The Clay Agent and the built-in browser

- **Use the built-in browser, never Claude in Chrome**, to work with the Clay Agent. Sign in there once, to the same workspace as the connector.
- **The home page box in Clay can be Sculptor, not the Clay Agent.** Sculptor builds tables and searches only. Use Workflows, New.
- **Long prompts sent line by line can go out half-written.** Put the buyer workflow prompt in the box as one paste, and check it holds the whole text before sending.
- **The Clay Agent can't price a signal.** Read the cost in Companies, Data hub, Signals.
- **The Clay Agent reads the code you give it.** It flagged that the read step expects an ICP card field and that the source is always "manual" with no source list. Answer both in the plan rather than letting it guess.
- **Clay's support chat can open over the Clay Agent.** Close it and type into the box that answers as the Clay Agent, never into support.
- **Not tested through the Clay Agent yet:** building the buyer workflow, its test run, the publish check and the campaign steps. They follow the CLI version's tested design. Read each answer closely the first time, and add what you learn here.

## Segments and the watchlist

- **A segment holds only what its filter says.** When a list looks bigger than expected, ask the Clay Agent for the segment's filter.
- **Keep one tag for "watched".** Don't reuse a source field (lookalike campaign, visit date) to decide who is watched.

## Signals

- **Signals that watch segments are under Companies, Data hub, Signals** in Clay, not on the sidebar Signals page.
- **A created signal is paused** until resumed. A signal with a typo in a fixed value, such as a seniority or a news topic, runs and finds nothing.
- **A signal has two ids.** Workflow triggers want the `sig_...` one from the read-back.
- **Hits from before a workflow is published are never processed by it.**

## Workflows

- **Record fields need an input, not a fixed value.** To write a fixed value such as the watch name, make it a trigger input or a code output.
- **Code steps:** standard library only, no network, about 1 second.
- **Find contacts at company** accepts a limit of 1 to 10, and returns a different 10 each call. Steer it with title keywords so the 10 are likely buyers.
- **The AI pick settles for the closest match** unless told not to. The prompt says "if nobody fits, return found = false" and gives a strict order.
- **first_name is not filled from the full name.** The workflow writes it.
- **Free and trial plans may allow 100 runs per workflow, ever.** Tests count. Failed runs don't.
- **A published version is frozen.** Every change lands in the draft only. If the draft also holds a step that must not go live yet (such as an enrol step), wait, and tell the person what publishing would turn on.
- **A live workflow spends on every hit, with no budget cap.** State the per-hit cost and ask once before publishing.
- **Workflow and function results repeat every input.** Follow progress on one record; confirm writes with the Clay Agent's count.

## Campaigns

- **A workflow-fed campaign must be made in Clay** (New sequence, Workflow tab), and the type can't be changed.
- **The enrol step only finds live campaigns.** Launch first, then add the step.
- **A paused campaign rejects enrolments.** Don't leave the workflow live with the campaign paused.
