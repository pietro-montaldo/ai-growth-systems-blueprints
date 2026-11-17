# Working with the Clay Agent

The Clay Agent is Clay's own assistant. It runs on the same engine as the Clay CLI, so it can build what the connector can't: fields, workflows, lists and campaigns. It lives inside Clay, so Claude works with it in the built-in browser of the Claude desktop app: Claude types each prompt, reads the answer, and brings every plan to the person before saying go ahead. Never use Claude in Chrome for this.

## Where it is

Claude opens Clay in the built-in browser; the person signs in there once, to the same workspace as the connector. In Clay, open **Workflows** and click **New**. The box that says "What should we build today?" is the Clay Agent, and the chat stays open on the right while it works. For the setup prompt, name the new workflow first (top left), because the Clay Agent builds into it. For the other prompts, open any workflow page and its Ask Clay chat, and start each task with "New task".

The box on Clay's home page can open **Sculptor** instead. Sculptor builds tables and searches, not workflows or campaigns. If the answer comes from Sculptor, go to Workflows.

The Clay Agent is in beta, on Clay's Launch, Growth and Enterprise plans, and its own work spends data credits. Settings say whether this person has it (`clay_agent`). Without it, use "Doing it by hand" at the end.

## The round trip (built-in browser)

1. Claude says in one line what the prompt will do in Clay, types it into the Clay Agent's box and sends it.
2. Claude waits and reads the Clay Agent's answer from the page. It takes 30 seconds to a few minutes; wait in steps rather than sending again.
3. Claude checks the plan against the prompt: right names, right fields, nothing extra (no launch, no enrolling, no runs, no test email). If something is off, Claude types the correction. If it's right, Claude shows the plan to the person in plain words and asks.
4. Only after the person's yes, Claude replies "Yes, go ahead as planned" and reads the last answer. Claude checks it and reports.

Every prompt ends by asking for the plan first and saying what not to do. Never skip that. Clay's support chat can open over the Clay Agent's box: close it and check the text went into the Clay Agent, never into support.

**Paste by hand, only without the built-in browser** (for example, Claude Code in a terminal): Claude shows each prompt in a code block, the person pastes it into the Clay Agent and pastes each answer back, and the same checks apply.

## Setup (once)

### 1. The "add people" workflow and its fields

Name the new workflow "Lookalikes: add people to list", then type:

```
Build this workflow so I can call it from Claude through the Clay MCP connector (register it as a routine when it's built). Manual trigger with these inputs: email, first_name, last_name, full_name, linkedin_url, title, campaign, opener, company, company_domain (required), company_website, company_linkedin, company_city, company_state, company_country, company_industry, company_headcount (number), company_founded (number), company_description, company_revenue, company_logo_url, seed, second_contact, second_contact_title, person_city, person_state, person_country, person_location.
Step 1: upsert the company in Audiences, matched on company_domain, writing name, website, LinkedIn, city, state, country, industry, headcount, founded, description, revenue and logo, skipping empty values.
Step 2: upsert the person in Audiences matched on email, linked to the company record from step 1 (the account link, not just the company name), writing first name, last name, full name, LinkedIn, title, city, state, country and location.
Also store campaign, opener, company, seed, second_contact and second_contact_title on the person in person fields named Lookalike campaign, Lookalike opener, Lookalike company, Lookalike seed, Lookalike second contact and Lookalike second contact title. Create the ones that don't exist yet.
Do not run it and do not publish it. Show me your plan, including any fields you will create, before you build.
```

Check the plan: the company step matches on the domain, the person step links to the company record from step 1 (not only the name), and the six fields are listed. After the go ahead, the Clay Agent builds, validates and registers it.

### 2. Check it from Claude

Ask the connector for its list of routines. "Lookalikes: add people to list" shows up straight away; the workflow doesn't need to be published for the connector to run it. Save its id in settings. Then run it once on the person's own record, after a yes: their email, their company's domain, the campaign "setup test", and their first, last and full name exactly as they want them in Clay. The workflow overwrites whatever it's given, so a first name sent as the full name replaces the real one. Read the result: the person and the company are written, and the six fields are filled. Then use the check prompt below with the campaign "setup test": 1 person, 0 unlinked. The test record can stay, or the person removes it in Clay.

### 3. Prices

The connector can't read prices. Type:

```
Without running anything: what does each of these cost per run, in data credits? Enrich Company, Find People at Company, Work Email, and Find company lookalikes (per company returned). Read them from the function and action details.
```

Save the answers in settings. The Clay Agent may not know the lookalikes price: it is 1 data credit per company returned, with no charge per call, and a call that returns nothing is refunded (check it on your first batch of 10). If the Clay Agent can't say, the person reads them on Clay's pricing page or in the credit usage page after a small run. Until then, forecasts show counts, not credits.

## Lookalikes (step 2)

Fill the angle brackets from `seed.json`. Start with `limit` 10. The limit is the credit cap: about 1 credit per company returned, agreed with the person before Claude sends the prompt. The Clay Agent can't quote the cost or enforce a credit cap, so the prompt says the limit is the cap; otherwise it stops and asks again.

```
Use Find company lookalikes (find-company-lookalikes-v2), seeded with <seed domain><, plus confirmed fits: domains>. Countries: <seed market countries>. Headquarters only. Sizes: <size buckets>. Description keywords: <model words and service words>. Excluded keywords: <words for businesses to leave out>. Limit: <10>.
The cost isn't shown in advance, and I accept that: the limit of <10> results is my cap, at about 1 data credit per company returned. Run it once now without asking again. When it has run, list every result as: company name, domain, HQ country, size, one-line description. Don't add anything to Audiences.
```

The action has no setting to leave out companies already in Audiences: Claude checks the results (`enrich-and-check.md`, step 1). Keyword filters that are too tight return nothing: loosen them in the next prompt. In a small market it can return nothing at all, even with one seed and no keywords. After two empty calls, stop and fill the list through the connector's searches.

## Checks after writing the people (step 8)

```
Without changing anything: in Audiences, count the people whose Lookalike campaign is exactly "<campaign name>", tell me how many of them have no linked company, and list the ones with no country.
```

Unlinked must be 0. If not, run the "add people" workflow again for those people, and check again.

## The build (step 8)

Fill the copy exactly as agreed. In the copy, `{First name}`, `{Lookalike opener}` and `{Lookalike company}` are merge fields, and `{a|b}` is spintax.

```
Two things in Audiences and Sequencer.
1) Create a people segment named "<campaign name>" with everyone whose Lookalike campaign is exactly "<campaign name>".
2) Create a draft campaign named "<campaign name>" on that segment, with an A/B test on email 1 and a nudge. Name the versions "A: <what A tests>" and "B: <what B tests>".
Subject for both versions: <subject>
Version A, email 1: "<version A>"
Version B, email 1: "<version B>"
Email 2 for both, <3> days later, sent as a reply in the same thread: "<nudge>"
{First name}, {Lookalike opener} and {Lookalike company} are merge fields. Words in {a|b} are spintax. Use real merge fields, not typed braces.
Leave sender accounts empty. Run the spam check and show me previews for one lead with a second contact and one without. Do not launch, do not enroll anyone, and do not send a test email. Show me your plan first.
```

Check the plan: one segment, one draft campaign on it, a 50/50 split, both versions, the nudge as a reply after the right number of days, sender accounts empty, and nothing launched or enrolled. Then check the answer: the previews read right (names, opener, company, no braces), and the spam scores. A fixed proof sentence loses a few points; that's expected.

**The draft already exists** (more people written after going back to the search): don't build again. The list follows the tag, so new people join the draft by themselves. Type instead:

```
New task, without changing anything: the people segment and the draft campaign named "<campaign name>" already exist. Tell me how many people the segment has now and how many leads the draft will send to. Show me the email 1 preview of both versions for <email of a lead with a second contact> and <email of a lead without one>, and the spam check scores. Do not launch, do not enroll anyone, do not send a test email, and do not create a second segment or campaign.
```

## Hand-off (step 9)

The person does these in the campaign in Clay:

- **Inboxes:** Sender accounts tab. List the connected inboxes by address and let the person pick.
- **Sending window:** Clay's default is Mon to Fri, 9:00 to 17:00 New York. For a seed in another market, suggest that market's time zone.
- **Test email:** after "Send a test of A and B to <your address>?" and a yes, either the person sends it from the campaign, or this prompt: `Send one test email of each version of "<campaign name>" to <their address>. Nothing else.`
- **Launch:** only the person, when they're happy.

## Results (results-and-expand.md)

```
Without changing anything: read the campaign "<campaign name>". Tell me its status, and for each version: leads, first emails sent, nudges sent, replies, bounces and unsubscribes.
```

Or Claude opens the campaign's **Analytics** tab in the built-in browser, sets Variant to each version, and reads the numbers.

## Doing it by hand (no Clay Agent)

Claude walks the person through each piece in the built-in browser, one at a time, and checks each one through the connector where it can.

- **Fields:** Audiences, People, Fields. Add the six text fields from setup.
- **Workflow:** Workflows, New, Build manually. A manual trigger with the inputs from setup, then two "Write to Audiences" steps: the company (match on domain), then the person (match on email), with the person's company set from the company step's result. Publish, then create a routine from it. Check it in the connector's list of routines.
- **Lookalikes:** Find leads, Company lookalikes. The preview of 50 is free; Continue charges for every result. This panel has no country or size filters, so lean on the connector's companies searches instead.
- **List:** Audiences, People, Segments, the plus sign. Filter Lookalike campaign is exactly the campaign name, then Save filters.
- **Campaign:** Sequencer, New sequence, pick the list. In the editor, type "/" and wait for the menu to insert a merge field; filter it with one word ("First", "opener", "Lookalike"). Turn on the A/B test, add the nudge with Add message and keep "Send as reply" on, then Save. Spintax comes from the same "/" menu.
- **Results:** the Analytics tab.
