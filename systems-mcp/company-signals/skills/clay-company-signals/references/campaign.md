# Emailing the buyers

Only when the person asks to switch on emailing. Until then the workflow stays in list mode.

## 1. The copy

Start from the person's own words: a cold email they sent that got replies, a template they use, or their voice skill. Keep their sentences. Only fill in the facts. No praise, no reactions, no clever lines: that reads as automated.

The shape that worked:

1. **Opener**: the signal, as a plain fact. From the "Signals: opener" field, for example "Saw your <job title> job post mentions <tool>." or "Saw you recently joined <company> as <title>." Never mention topic intent or website visits.
2. **What you do**, in one sentence in the buyer's words from the GTM messaging page.
3. **One line of credibility**, such as a rating or a number you may share.
4. **The ask**: offer to send a short case. "If this could be useful, I can send over <proof>." The "Signals: proof" field holds the case. Use only customers who gave permission in the GTM context.
5. **Follow-up** 3 days later, as a reply in the same thread: a two-line bump that offers a short call.

Subject: short and plain, for example "<company> + <topic>".

Show 2 versions, each filled in for a real person from the buyer list, and recommend one. Wait for the pick.

**Spintax.** Vary 2 or 3 small phrases so every email isn't identical, written `{Hey|Hi}` in the copy the Clay Agent gets. Never vary the facts or the ask. Every variant must be something you would write.

## 2. The campaign: a workflow type, made in Clay

Clay campaigns come in two types, and the type can't be changed later:

- **People**: leads come from a segment. This is the type the Clay Agent makes by default.
- **Workflow**: leads are added by a workflow's "Enroll in campaign" step. This system needs this type.

So the person creates it in Clay: **Campaigns, New sequence, Workflow tab, Create workflow sequence**. Then the campaign prompt in `clay-agent.md` sets it up: the name "Signals · <watchlist>", the copy as a new thread plus a reply 3 days later, the inboxes the person picks, weekdays in office hours in the buyers' main time zone, everyone at a company paused when anyone there replies, and open and click tracking off. Then the spam check and a preview. Fix anything it flags with the person.

## 3. Do-not-contact blocklist (optional)

If the person has the do-not-contact list, run check-do-not-contact's "make a blocklist" and ask them to upload the file in Clay: **Campaigns, Blocklist**. If there is no list, skip this step. The watchlist already left out customers and open deals. Say in one line that a company that becomes a customer or an open deal later should be taken off the watchlist.

## 4. The order for going live

1. **The person launches the campaign** in Clay. With no leads, nothing sends.
2. **The enrol step prompt** in `clay-agent.md` adds "Enroll in campaign" to the draft workflow, between Save buyer and Mark company. The step only accepts a campaign that is live and of the workflow type: if the Clay Agent can't find the campaign, it isn't live yet.
3. **The person presses Publish** in Clay. From then on, every qualified hit is emailed.

**Keep the campaign running while the workflow is live.** A paused campaign rejects every enrolment, so each hit would spend credits on the lookups and then fail at the last step. To recover those runs, with the person's OK: open the workflow's Runs view in the built-in browser, select the failed runs and choose **Re-run, Resume from failed node**. That restarts each run at the enrol step without paying for the lookups again.

If an enrolment fails as "indeterminate" or "persistence unavailable", the person may already be enrolled. Never retry those: ask the person to check the campaign.

## 5. Moving people already on the list

People added in list mode are not enrolled by switching on emailing, and their companies are stamped for 90 days. If the person wants them emailed too, ask the Clay Agent to enrol them from the buyer list, with their OK, one batch, after the campaign is live.
