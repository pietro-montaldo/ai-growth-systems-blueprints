# The buyer workflow

One Clay workflow, run once per signal hit. The Clay Agent builds it as a draft from the prompt in `clay-agent.md`. This page is what that prompt asks for, and what to check in the Clay Agent's plan. Nobody publishes it from a prompt: the person presses Publish.

Name: "Signals: find buyer (<watchlist>)".

## The steps

```
Signal triggers → 1 Read → 2 90-day check → 3 Qualify → 4 Job post or new hire?
   job post → 5 Find signers → 6 Pick buyer → found?
   new hire → the hired person
→ 7 Chosen person → 8 Work email → found? → 9 Email lines → 10 Save buyer → [Enrol] → 11 Mark company
```

Every "stop" ends the run, with no fallback.

**Triggers.** One audience signal trigger per signal, entity type companies, bound to the signal's `sig_...` id (from the signals' read-back), not its other id. Several signal triggers can share one trigger node. Triggers stay off until the workflow is published.

**What a hit carries.** The company's Audiences record by display name (`$.fields.Domain`, `$.fields['Company name']`, `$.fields.Industry`, `$.fields.id` for the record id, and custom fields such as the watch field), plus the event in `$.signal.signalType` and `$.signal.data`. A job post event has the title, URL, company, location and posted date, but **not the job description**. New hire and news events can differ by workspace: `assets/read_signal.py` reads them defensively. Check the first real one.

1. **Read** (code step, `assets/read_signal.py`). Inputs: signal type, signal data, company id, company name, domain, company LinkedIn, and "Signals: last added". `icp_card` stays empty unless a company field names the card. `SOURCE_ORDER` stays empty (source "manual") unless the watchlist has several source fields.
2. **90-day check** (rules). Continue only if the company was not added in the last 90 days and the domain is not empty. It comes first so nothing is spent on companies that would be skipped anyway.
3. **Qualify** (AI step with web access, `assets/qualify_prompt.md`, outputs `qualified` and `reason`, the intermediate model). For a job post it opens the posting to read the description, or searches the web for it.
4. **Job post or new hire?** (rules on signal type).
5. **Find signers**: Clay's "Find contacts at company" action on the domain, with the signing seniority levels (for example founder, owner, partner, c-suite, vp, director, head), title keywords for the buyer roles from the ICP card, and a limit of 10 (the most it accepts). Avoid keywords that also match other roles, such as "President", which matches sales Vice Presidents. Clay's "Find People at Company" function returns a random handful of staff, so it is the wrong tool here.
6. **Pick buyer** (AI step without web, `assets/pick_buyer_prompt.md`, outputs `found`, `full_name`, `title`, `linkedin_url`, `reason`, the intermediate model), fed the whole result of step 5.
7. **Chosen person** (small code step): the picked buyer, or the hired person on the new-hire path, with `person_source` "picked" or "new hire".
8. **Work email**: Clay's "Work Email" function with full name, company name, domain, company LinkedIn and person LinkedIn. Stop if the email is empty.
9. **Email lines** (code step, `assets/email_lines.py`, with its CONFIG block filled). Splits first and last name, and writes the opener and proof line the copy uses.
10. **Save buyer**: create or update the person in Audiences, looked up by email and LinkedIn URL. First name (set it explicitly: Clay does not fill it from the full name), last name, name, title, email, LinkedIn, the person's own city and country when the source row has them, and people fields "Signals: signal", "Signals: detail", "Signals: source", "Signals: opener", "Signals: proof", "Signals: company". Linked to the company by the account association (the company id from step 1), not just the company name.
11. **Mark company**: create or update the company, looked up by domain: today's date in a company date field "Signals: last added". It runs after Save buyer, and after the enrol step once that exists, so a company is only stamped when someone was really added.

Then a people segment "Signals buyers · <watchlist>", filtered on "Signals: opener" not empty. That is the buyer list.

## Cost per hit

Once published, the workflow runs on every hit with no budget cap, so it spends on its own:

| Step | Spends |
|---|---|
| Qualify (AI) | yes |
| Find signers | yes |
| Pick buyer (AI) | yes |
| Work email | only when an email is found |
| Code, rules and Audiences writes | no |

A hit that reached the save step cost about 3.6 data credits on the smallest models when the CLI version was built; the intermediate model costs a little more per AI step. Many hits stop early and cost less. After the test run and the first live runs, ask the Clay Agent for the real cost per step (`clay-agent.md`) and write it in settings. Before publishing, state the per-hit cost and ask once.

## Testing

Test once before publishing, and quote the cost first (about 4 to 6 data credits for a full job-post run). Each test uses one workflow run.

A sample hit, for a company already on the watchlist:

```
{"fields": {"id": "<company record id>", "Company name": "<name>", "Domain": "<domain>", "Industry": "<industry>", "LinkedIn URL": "<company LinkedIn>"},
 "signal": {"signalType": "JobPost", "data": {"jobPostData": {"title": "<a real job title at that company>", "url": "<its posting URL>", "company_name": "<name>", "domain": "<domain>"}}}}
```

Use a real posting, so Qualify has something to read. The test prompt in `clay-agent.md` disconnects Mark company for the test, so the company isn't stamped for 90 days, and reconnects it after. Show the person, step by step, what happened and who was picked. If the pick is not someone who can sign, fix the keywords or the pick order and test again. Expect one or two rounds.

## Going live in list mode

Open the workflow in the built-in browser and ask the person to press Publish. Then the publish check in `clay-agent.md`. Hits from before publishing are not processed later.

A published version is frozen. Every later change, a model change too, lands in the draft only and goes live on the next publish. Publishing ships everything in the draft: if the draft also holds a step that must not go live yet (such as the enrol step), wait, and tell the person what publishing would turn on.
