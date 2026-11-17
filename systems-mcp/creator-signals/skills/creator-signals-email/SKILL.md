---
name: creator-signals-email
description: "{{YOUR_NAME}}'s LinkedIn creator signals, part 3 (email): turns this week's shortlist from linkedin-creator-signals into a one-off Clay email campaign (Windows fallback without the Clay CLI: the Clay connector plus the Clay Agent in the built-in browser), a single email or a sequence. Forecasts and asks before the Clay Work Email lookups, puts the people with an email on a Clay list for this campaign only, creates the campaign on it with the inboxes you pick, writes the copy from your template and agrees it with you, spam-checks it, previews it, sends you a test email on a yes, then hands over for you to press Launch in Clay. Use when you pick email for a creator signals list, or say \"set up the email campaign for this week's list\", \"Clay campaign for the creator leads\", \"sequence for the shortlist\". Not when the Clay CLI works (use the CLI version), not for LinkedIn messages (use creator-signals-linkedin), not for long-running campaigns, and it never launches or sends the campaign."
metadata:
  version: "0.1.0"
---

# LinkedIn creator signals (part 3: Clay email campaign), Windows fallback

Builds one Clay campaign for one list: the shortlist of one run. The list is used once, for this campaign only. The skill prepares everything and sends you a test. The campaign starts only when you press Launch in Clay.

**This version is only for Windows without the Clay CLI.** Work Email and Enrich Company run through the Clay connector. The Clay Agent, in the built-in browser of the Claude desktop app (never Claude in Chrome), builds the one-time setup, the list and the campaign from the prompts in `$FIND/references/clay-agent.md`. If `clay whoami` works, stop and use the CLI version.

Settings, run files and copy rules live in the sibling folder `../linkedin-creator-signals/` (`$FIND`). Run data is in `~/.growth-systems/creator-signals/`, and `$RUN` is the current run.

## Reference files

- `references/clay-setup.md`: one-time Clay setup (people fields and the "add to campaign list" workflow, built by the Clay Agent), with your OK
- `references/campaign.md`: naming, the one-off list, campaign settings, tokens, spintax, spam words, test and hand-off
- `$FIND/references/copy.md`: the copy rules
- `$FIND/references/connector.md`: Clay's functions and your workflow through the connector
- `$FIND/references/clay-agent.md`: the round trip in the built-in browser and every Clay Agent prompt

## Before starting

- The run is at stage `scored` with channel `email`. If the channel is empty, ask and record it. If it is `linkedin`, stop: one list goes to one channel.
- The list is every person in `$RUN/people.json` with Status "shortlist" or "send", as you confirmed it at Pause 3. This path creates no file: the Clay list and campaign are the record.
- If settings have no workflow id under "Email", do `references/clay-setup.md` first.
- Open Clay in the built-in browser and check the person is signed in to the same workspace as the connector.
- Load your voice skill if installed.

## Steps

**1. Company websites.** Work Email needs the company's website. Take it from the person's current role in the Enrich Person data (free, already there), with the company's LinkedIn page when the role has one. Never use a platform, marketplace or university domain. Sort the list: ready, needs a company lookup (company page but no website), no company.

**2. Pause E1: work emails.** Forecast Enrich Company for the middle group and Work Email for ready plus middle, from the prices in settings, and ask once. After a yes, run them through the Clay connector, at most 100 per call (`$FIND/references/connector.md`). Work Email is a waterfall: wait until complete, a few minutes, and read every page of results. Map results by LinkedIn slug. When an email's domain differs from the company you sent, Clay found the person at another business: put them on a "decide" list, never on this list with the original company. Show each one ("email at <domain>, sent <company>") and let you decide. Report how many have an email. The others stay off the list: say who, and that they could go to LinkedIn in a separate run.

**2b. Pause E2: company records.** Every company on the list gets its full Clay record first. One Enrich Company item per company domain of the people with an email at that domain; reuse any company already enriched in step 2. Forecast it (count times price) and ask. After a yes, run it through the connector, split over 100 per call.

**3. Already in a campaign?** For each past campaign in settings that is not finished, compare its list with this one by email. Anyone already on an active or draft list stays off this one. Say so.

**4. Basics, in one batch.** Single email or a sequence (how many follow-ups), which inboxes to send from (list the connected ones by address), and the sending window. Name the campaign per `references/campaign.md`.

**5. One-off list.** Build the workflow's input sets by the rule in `references/campaign.md`, from the people, their Work Email results and the Enrich Company results. Never type them by hand. Fix every person with no company record or missing CTA fields first, and check every company Clay answered with a different name or domain. Say how many people and companies will be written, and ask. Then run the "add to campaign list" workflow through the connector, tagged with the campaign name. It adds the company with its full record first and links the person to it. Then the Clay Agent check: the count matches, no one is missing their company, and who has no country (`references/campaign.md`).

**6. Campaign.** After the copy is agreed (step 7), one Clay Agent prompt creates the list and the draft campaign with the inboxes, window, goal, copy, spam check and previews (`$FIND/references/clay-agent.md`). Show the person the Clay Agent's plan and say go ahead only after their yes.

**7. Copy.** Per `copy.md`: start from the saved campaign's agreed version, adapt it to email (a subject line, same sentence and facts), and add spintax per `references/campaign.md`. Check every spintax version for spam words, banned phrases, dashes and length, and fix every "must fix" before you see it. Show 2 or 3 versions filled in for 2 real people, with every variant listed, and wait for your pick. Same for follow-ups. The picked copy goes into the step 6 prompt.

**8. Check.** Read the Clay Agent's spam check and previews for 2 people. Report the score and each issue, and offer a fix for each, but change your wording only with your OK. A fix is a new prompt to the Clay Agent.

**9. Test email.** Ask: "Send a test of the first email to <your address>?" Only after a clear yes, the test email prompt to the Clay Agent sends one. Ask you to check your inbox.

**10. Hand-off.** Give the campaign link and say: review it in Clay and press Launch when ready. Update `$RUN/people.json` (Channel "email", Email, Campaign, Status "in campaign"), add the campaign and list to settings, and set the run's stage to `campaign-ready`.

## Rules

- Never launch, resume or send the campaign, and never work around that through workflows, enrolment steps or other tools. Every Clay Agent prompt says so.
- Use the built-in browser for the Clay Agent, never Claude in Chrome. The Clay CLI works? Use the CLI version.
- Test emails only to your own address, confirmed in this session, one at a time.
- Only people with a Work Email from Clay go on the list. Never guess an address or a domain.
- Every person written to Clay is linked to their company record, and every company carries its full record from Enrich Company. Every person also carries their own location and country from the Enrich Person results the find stage already paid for (free); a country only when Clay gave one.
- Someone whose work email is at another business is never linked to the original company.
- No personal data in a campaign, list or field name.
- Do-not-contact (optional): if you have the list, run check-do-not-contact on the people before step 5.

## Done means

A draft Clay campaign on a one-off list of this run's shortlist, every person linked to a company with its full record, with agreed copy, a clean spam check, previews and (if asked) a test in your inbox. The chat gives the link, the people on the list, who had no email, who is waiting on the decide list, the data credits used, and says the campaign has not started.
