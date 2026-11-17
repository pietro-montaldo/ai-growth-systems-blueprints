# Working with the Clay Agent

The Clay Agent is Clay's own assistant. It runs on the same engine as the Clay CLI, so it can build what the connector can't: fields, segments, signals, workflows and campaigns. It lives inside Clay, so Claude works with it in the built-in browser of the Claude desktop app: Claude types each prompt, reads the answer, and brings every plan to the person before saying go ahead. Never use Claude in Chrome for this.

## Where it is

Claude opens Clay in the built-in browser; the person signs in there once, to the same workspace as the connector. In Clay, open **Workflows** and click **New**. The box that says "What should we build today?" is the Clay Agent, and the chat stays open on the right while it works. To build a workflow, name the new workflow first (top left), because the Clay Agent builds into it. For other prompts, open any workflow page and its Ask Clay chat, and start each task with "New task".

The box on Clay's home page can open **Sculptor** instead. Sculptor builds tables and searches, not workflows or signals. If the answer comes from Sculptor, go to Workflows.

The Clay Agent is in beta, on Clay's Launch, Growth and Enterprise plans, and its own work spends data credits. Settings say whether this person has it (`clay_agent`). Without it, use "Doing it by hand" at the end.

## The round trip (built-in browser)

1. Claude says in one line what the prompt will do in Clay, puts it in the Clay Agent's box and sends it.
2. Claude waits and reads the Clay Agent's answer from the page. It takes 30 seconds to a few minutes; wait in steps rather than sending again.
3. Claude checks the plan against the prompt: right names, right fields, right ids, nothing extra (no publishing, no running, no resuming unless the step says so). If something is off, Claude types the correction. If it's right, Claude shows the plan to the person in plain words and asks.
4. Only after the person's yes, Claude replies "Yes, go ahead as planned" and reads the last answer. Claude checks it and reports.

**Long prompts** (the buyer workflow, about 14,000 characters with its code): put the whole prompt in the box as one paste, not typed line by line. Typed line breaks can send the message half-written. Check the box holds the whole text, start to end, before sending.

Every prompt ends by asking for the plan first and saying what not to do. Never skip that. Clay's support chat can open over the Clay Agent's box: close it and check the text went into the Clay Agent, never into support.

**Paste by hand, only without the built-in browser** (for example, Claude Code in a terminal): Claude shows each prompt in a code block, the person pastes it into the Clay Agent and pastes each answer back, and the same checks apply.

## Setup check (before step 1)

```
Without changing anything: tell me whether this workspace can use Signals, company segments in Audiences, Workflows and Campaigns. List any existing signals, company segments and workflows whose names start with "Signals". List the connected sender inboxes by address, and the data credit balance.
```

If Signals is missing, the system can't run: stop and say so. Without Campaigns, list mode still works. With no inbox, list mode works and emailing waits until one is connected. If there are signals or segments with similar names, ask before creating new ones: two signals watching the same companies are charged twice.

Prices: Enrich Company's price per company (data credits) comes from this prompt, or from the credit usage page after the first few:

```
Without running anything: what does Clay's Enrich Company function cost per run, in data credits?
```

## The watchlist (step 3)

Name a new workflow "Signals: add to watchlist", then send:

```
Build these. Do not run or publish anything, and show me your plan first, including every field you will create.
1) Company text fields "Signals: watch", "Signals: why fit" and "Signals: source". Reuse any that already exist.
2) A company segment named "Signals watchlist · <short offer name>" whose filter is: Signals: watch equals "<watchlist name>".
3) In this canvas, a workflow I can call from Claude through the Clay MCP connector (register it as a routine when it's built). Manual trigger with these inputs: domain (required), watch (required), company_name, website, linkedin_url, industry, size, headcount (number), founded (number), revenue, description, logo_url, city, state, country, why_fit, source.
One step: create or update the company in Audiences, matched on domain, skipping empty values, writing name, website, LinkedIn, industry, a "Company size" text field, headcount, founded, revenue, description, logo, city, state, country, and the three Signals fields. Every value comes from a trigger input, never a fixed value.
```

Check the plan: the match is on the domain, every field is mapped from an input, nothing runs. After the go ahead, the connector lists the new routine: save its id in settings. Then add one company and check its record (`watchlist.md`).

## Signals (step 4)

```
Create these in Signals. Do not resume any signal and do not build, run or publish any workflow. Show me your plan first.
<For each signal:> A <JobPost | NewHire | News | CompanyTopicIntent> signal named "Signals: <what it watches> (<watchlist>)", watching the company segment "<segment name>" by its id, entity type companies, created paused, schedule weekly: <its settings in plain words, from signals.md>.
After creating them, read each signal back and show me: the segment id it watches, its filters, its status (it must be paused), and its signal.id (sig_...), which a workflow trigger will need.
```

Check each read-back against what you meant, word for word: a misspelt fixed value matches nothing. Save the ids and the `sig_` ids in settings. The Clay Agent can't show a signal's price: read it in **Companies, Data hub, Signals** (credit spend and per-run cost), then quote it.

Resume, only after the person's yes:

```
New task: resume only the signals named "<name>" and "<name>". Change nothing else, and read their status back.
```

## The buyer workflow (step 5)

Name a new workflow "Signals: find buyer (<watchlist>)". Fill this from settings, the two prompts in `assets/` (filled) and the two code files in `assets/`, and send it as one paste:

```
Build the buyer workflow in this canvas as a draft. Do not publish it, do not run or test it, and do not resume any signal. Show me your plan first, including every field and segment you will create. Use the intermediate model (the "mini" tier) for both AI steps.

TRIGGERS: one audience signal trigger per signal, entity type companies, bound to signal.id <sig_...> (<type>) and <sig_...> (<type>). They can share one trigger node.

STEPS (each "stop" ends the run, with no fallback):
<steps 1 to 11 from workflow.md, with the field names "Signals: ...">
Then create a people segment "Signals buyers · <watchlist>" filtered on Signals: opener is not empty. Validate the graph.

PROMPT 1 (Qualify):
<assets/qualify_prompt.md, filled>

PROMPT 2 (Pick buyer):
<assets/pick_buyer_prompt.md, filled>

CODE 1 (Read), Python, use exactly:
<assets/read_signal.py from "from datetime import" to the end>

CODE 2 (Email lines), Python, use exactly:
<assets/email_lines.py, with its CONFIG block filled>
```

Check the plan: both triggers on the right `sig_` ids, every step in order, both AI steps on the intermediate model, Save buyer linked to the company by the account association, Mark company only after Save buyer, nothing run or published. Two things the Clay Agent will point out, and the answers:

- **icp_card:** CODE 1 reads an ICP card input. Without a company field that names the card, tell it to leave the input empty.
- **source:** with `SOURCE_ORDER` empty, the source is always "manual". Fill it only if the watchlist has more than one source field.

## The test run (step 5)

Quote the cost first (`workflow.md`, "Testing"). Then:

```
New task: test the draft "Signals: find buyer (<watchlist>)" once with the input below. Before the test, disconnect "Mark company" so the test doesn't stamp the company, and reconnect it after. Do not publish. Then show me, step by step, what each step did, who was picked and why, the email found, and the data credits each step used.
<a sample hit, as in workflow.md>
```

If the pick is not someone who can sign, fix the keywords or the pick order with a new prompt and test again.

## Publish check and cost per hit (step 6)

The person presses **Publish**. Then:

```
New task, without changing anything: is a version of "Signals: find buyer (<watchlist>)" published, and are its signal triggers on that version? From its runs so far, what does a run that reaches Save buyer cost per step, in data credits?
```

## Campaign (step 7)

The person creates the workflow-type campaign in Clay (`campaign.md`). Then:

```
New task: in the draft campaign "<name>", set the agreed copy below: email 1 as a new thread with the subject <subject>, and a reply in the same thread <3> days later. Use the people fields Signals: opener, Signals: proof and Signals: company and the first name as real merge fields, and words in {a|b} as spintax. Set the sender inboxes <addresses>, weekdays in office hours in <time zone>, pause everyone at a company when anyone there replies, and open and click tracking off. Run the spam check and show me a preview for one person on the buyer list. Do not launch and do not enrol anyone. Show me your plan first.
<copy>
```

After the person launches it:

```
New task: in the draft of "Signals: find buyer (<watchlist>)", add an "Enroll in campaign" step for the campaign "<name>" between Save buyer and Mark company, using the person saved by Save buyer. Validate. Do not publish. Show me your plan first.
```

## Doing it by hand (no Clay Agent)

Claude walks the person through each piece in the built-in browser, one at a time, and checks each one through the connector where it can.

- **Fields and segment:** Companies, Data hub, Fields, then Segments. Filter: Signals: watch equals the watchlist name.
- **Adding companies:** import the CSV with the full records (from Enrich Company through the connector) into Companies, with the watch column mapped to the field.
- **Signals:** Companies, Data hub, Signals. Create each on the segment, paused, with the settings from `signals.md`.
- **Buyer workflow:** Workflows, New, Build manually, step by step from `workflow.md`, pasting the code and prompts from `assets/`. Slow, but every step is visible.
- **Campaign:** Campaigns, New sequence, Workflow tab.
