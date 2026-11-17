# Working with the Clay Agent

The Clay Agent is Clay's own assistant. It runs on the same engine as the Clay CLI, so it can build what the connector can't: fields, workflows, lists and campaigns. It lives inside Clay, so Claude works with it in the built-in browser of the Claude desktop app: Claude types each prompt, reads the answer, and brings every plan to the person before saying go ahead. Never use Claude in Chrome for this. Part 1 only uses it for prices; everything else here is for the email path (`creator-signals-email`).

## Where it is

Claude opens Clay in the built-in browser; the person signs in there once, to the same workspace as the connector. In Clay, open **Workflows** and click **New**. The box that says "What should we build today?" is the Clay Agent, and the chat stays open on the right while it works. To build a workflow, name the new workflow first (top left), because the Clay Agent builds into it. For other prompts, open any workflow page and its Ask Clay chat, and start each task with "New task".

The box on Clay's home page can open **Sculptor** instead, which only builds tables and searches. If the answer comes from Sculptor, go to Workflows.

The Clay Agent is in beta, on Clay's Launch, Growth and Enterprise plans, and its own work spends data credits. Settings say whether this person has it (`clay_agent`). Without it, use "Doing it by hand" at the end.

## The round trip (built-in browser)

1. Claude says in one line what the prompt will do in Clay, puts it in the Clay Agent's box and sends it. A long prompt goes in as one paste, not typed line by line, so it can't go out half-written.
2. Claude waits and reads the answer from the page. It takes 30 seconds to a few minutes; wait in steps rather than sending again.
3. Claude checks the plan against the prompt: right names, right fields, nothing extra (no launch, no enrolling, no test email, no runs unless the step says so). If something is off, Claude types the correction. If it's right, Claude shows the plan to the person in plain words and asks.
4. Only after the person's yes, Claude replies "Yes, go ahead as planned" and reads the last answer. Claude checks it and reports.

Every prompt ends by asking for the plan first and saying what not to do. Never skip that. Clay's support chat can open over the Clay Agent's box: close it and check the text went into the Clay Agent, never into support.

**Paste by hand, only without the built-in browser** (for example, Claude Code in a terminal): Claude shows each prompt in a code block, the person pastes it into the Clay Agent and pastes each answer back, and the same checks apply.

## Prices (part 1 setup)

```
Without running anything: what does each of these cost per run, in data credits? Enrich Person, Work Email and Enrich Company. Read them from the function details.
```

Save the answers in settings. If the Clay Agent can't say, read them in the credit usage page after the first small run.

## Email setup (once, `creator-signals-email/references/clay-setup.md`)

Name a new workflow "Creator signals: add to campaign list", then send:

```
Build this workflow so I can call it from Claude through the Clay MCP connector (register it as a routine when it's built). Manual trigger with these inputs: email, first_name, last_name, full_name, linkedin_url, title, company, company_domain, company_linkedin, campaign, post, cta, cta_date, cta_link, company_website, company_city, company_state, company_country, company_industry, company_headcount (number), company_founded (number), company_description, company_revenue, company_logo_url, person_city, person_state, person_country, person_location, person_seniority. Required: email, campaign, company_domain.
Step 1: create or update the company in Audiences, matched on company_domain, skipping empty values, writing name, LinkedIn page, website, founded, description, city, state, country, industry, employee count, revenue and logo.
Step 2: create or update the person in Audiences, matched on email and LinkedIn URL, skipping empty values, linked to the company record from step 1 (the account association, not just the company name), writing first name, last name, full name, title, email, LinkedIn, the person's own city, state, country, location and seniority, and these people text fields: Creator signals campaign, Creator signals company, Creator signals post, Creator signals CTA, Creator signals CTA date, Creator signals CTA link. Create the fields that don't exist yet.
Do not run it and do not publish it. Show me your plan first, including every field you will create.
```

Check the plan: the company is matched on the domain, the person is linked to the company record from step 1 (not only the name), the six fields are listed, nothing runs. After the go ahead, the connector lists the new routine: save its id in settings. Then the setup test in `clay-setup.md`.

## The list and the campaign (email steps 5 and 6)

After the people are written:

```
New task, without changing anything: in Audiences, count the people whose Creator signals campaign is exactly "<campaign name>", tell me how many of them have no linked company, and list the ones with no country.
```

Unlinked must be 0. Then:

```
Two things in Audiences and Campaigns.
1) Create a people segment named "<campaign name>" with everyone whose Creator signals campaign is exactly "<campaign name>".
2) Create a draft campaign named "<campaign name>" on that segment, with the sender inboxes <addresses>, sending <window and time zone>, and this goal: "<goal in one sentence>".
Email 1, a new thread, subject: <subject>
"<email 1>"
<For each follow-up:> Email <n>, <days> days later, sent as a reply in the same thread: "<follow-up>"
{First name}, {Creator signals post}, {Creator signals CTA}, {Creator signals CTA date} and {Creator signals CTA link} are merge fields. Words in {a|b} are spintax. Use real merge fields, not typed braces.
Run the spam check and show me previews for two people on the list. Do not launch, do not enroll anyone beyond the segment, and do not send a test email. Show me your plan first.
```

Check the plan: one segment, one draft campaign on it, the right inboxes and window, every email in order with the follow-ups as replies, nothing launched. Then check the answer: the previews read right (names, post, CTA, date, a clickable link, no braces) and the spam scores. Report every issue; change wording only with the person's OK.

## Test email (email step 9)

Only after the person's clear yes to "Send a test of the first email to <their address>?":

```
New task: send one test email of the first email of "<campaign name>" to <their address>. Nothing else.
```

## Archiving a finished campaign's list (part 1, step 1)

With the person's yes:

```
New task: archive the people segment "<campaign name>". Change nothing else.
```

## Doing it by hand (no Clay Agent)

Claude walks the person through each piece in the built-in browser, one at a time, and checks each one through the connector where it can.

- **Fields:** Audiences, People, Fields. Add the six text fields.
- **Workflow:** Workflows, New, Build manually. A manual trigger with the inputs above, then two "Write to Audiences" steps: the company (match on domain), then the person (match on email), with the person's company set from the company step's result. Publish, then create a routine from it.
- **List:** Audiences, People, Segments, the plus sign. Filter Creator signals campaign is exactly the campaign name.
- **Campaign:** Campaigns, New sequence, pick the list. In the editor, type "/" and wait for the menu to insert a merge field; filter it with one word. Add follow-ups with Add message and keep "Send as reply" on. Spintax comes from the same "/" menu.
