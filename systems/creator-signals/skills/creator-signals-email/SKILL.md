---
name: creator-signals-email
description: "{{YOUR_NAME}}'s LinkedIn creator signals, part 3 (email): turns this week's shortlist from linkedin-creator-signals into a one-off Clay email campaign, a single email or a sequence. Forecasts and asks before the Clay Work Email lookups, puts the people with an email on a Clay list for this campaign only, creates the campaign on it with the inboxes you pick, writes the copy from your template and agrees it with you, spam-checks it, previews it, sends you a test email on a yes, then hands over for you to press Launch in Clay. Use when you pick email for a creator signals list, or say \"set up the email campaign for this week's list\", \"Clay campaign for the creator leads\", \"sequence for the shortlist\". Not for LinkedIn messages (use creator-signals-linkedin), not for long-running campaigns, and it never launches or sends the campaign."
metadata:
  version: "0.3.0"
---

# LinkedIn creator signals (part 3: Clay email campaign)

Builds one Clay campaign for one list: the shortlist of one run. The list is used once, for this campaign only. The skill prepares everything and sends you a test. The campaign starts only when you press Launch in Clay.

Settings, run files and copy rules live in the sibling folder `../linkedin-creator-signals/` (`$FIND`). Run data is in `~/.growth-systems/creator-signals/`, and `$RUN` is the current run.

## Reference files

- `references/clay-setup.md`: one-time Clay setup (people fields, the "add to campaign list" workflow and routine), with your OK
- `references/campaign.md`: naming, the one-off list, campaign settings, tokens, spintax, spam words, test and hand-off
- `$FIND/references/copy.md`: the copy rules

If Clay's own skills are installed, follow them for the mechanics (`clay:campaigns`, `clay:audiences`, `clay:workflows`, `clay:routines`). Read each command's `--help` before its first use.

## Before starting

- The run is at stage `scored` with channel `email`. If the channel is empty, ask and record it. If it is `linkedin`, stop: one list goes to one channel.
- The list is every person in `$RUN/people.json` with Status "shortlist" or "send", as you confirmed it at Pause 3. This path creates no file: the Clay list and campaign are the record.
- If settings have no routine id or field ids under "Email", do `references/clay-setup.md` first.
- Load your voice skill if installed.

## Steps

**1. Company websites.** Work Email needs the company's website. Take it from the person's current role in the Enrich Person data (free, already there), with the company's LinkedIn page when the role has one. Never use a platform, marketplace or university domain. Sort the list: ready, needs a company lookup (company page but no website), no company.

**2. Pause E1: work emails.** Forecast Enrich Company for the middle group and Work Email for ready plus middle, from the prices in settings (data credits and action credits), and ask once. After a yes, run them through the Clay CLI routines, at most 100 items per file. Work Email is a waterfall: wait until complete, a few minutes, and read every page of results. Map results by LinkedIn slug. When an email's domain differs from the company you sent, Clay found the person at another business: put them on a "decide" list, never on this list with the original company. Show each one ("email at <domain>, sent <company>") and let you decide. Report how many have an email. The others stay off the list: say who, and that they could go to LinkedIn in a separate run.

**2b. Pause E2: company records.** Every company on the list gets its full Clay record first. One Enrich Company item per company domain of the people with an email at that domain; reuse any company already enriched in step 2. Forecast it (count, data and action credits) and ask. After a yes, run it, split over 100 items.

**3. Already in a campaign?** For each past campaign in settings that is not finished, compare its list with this one by email. Anyone already on an active or draft list stays off this one. Say so.

**4. Basics, in one batch.** Single email or a sequence (how many follow-ups), which inboxes to send from (list the connected ones by address), and the sending window. Name the campaign per `references/campaign.md`.

**5. One-off list.** Build the routine items by the rule in `references/campaign.md`, from the people, their Work Email results and the Enrich Company results. Never type items by hand. Fix every person with no company record or missing CTA fields first, and check every company Clay answered with a different name or domain. Run the "add to campaign list" routine on the items, tagged with the campaign name. The routine adds the company with its full record first and links the person to it. Then create the list filtered on that tag. Check its count matches, and that no one on it is missing their company (`references/campaign.md`).

**6. Campaign.** Create it as a draft, then one change per command: the list, the inboxes, the goal. Say each change in plain words.

**7. Copy.** Per `copy.md`: start from the saved campaign's agreed version, adapt it to email (a subject line, same sentence and facts), and add spintax per `references/campaign.md`. Check every spintax version for spam words, banned phrases, dashes and length, and fix every "must fix" before you see it. Show 2 or 3 versions filled in for 2 real people, with every variant listed, and wait for your pick. Same for follow-ups. Write the picked copy into the campaign.

**8. Check.** Run Clay's spam check on the copy. Report the score and each issue, and offer a fix for each, but change your wording only with your OK. Preview the rendered emails for 2 people.

**9. Test email.** Ask: "Send a test of the first email to <your address>?" Only after a clear yes, send one test. Ask you to check your inbox.

**10. Hand-off.** Give the campaign link and say: review it in Clay and press Launch when ready. Update `$RUN/people.json` (Channel "email", Email, Campaign, Status "in campaign"), add the campaign and list to settings, and set the run's stage to `campaign-ready`.

## Rules

- Never launch, resume or send the campaign, and never work around that through workflows, enrolment steps or other tools.
- Test emails only to your own address, confirmed in this session, one at a time.
- Only people with a Work Email from Clay go on the list. Never guess an address or a domain.
- Every person written to Clay is linked to their company record, and every company carries its full record from Enrich Company. Every person also carries their own location and country from the Enrich Person results the find stage already paid for (free); a country only when Clay gave one.
- Someone whose work email is at another business is never linked to the original company.
- No personal data in a campaign, list or field name.
- Do-not-contact (optional): if you have the list, run check-do-not-contact on the people before step 5.

## Done means

A draft Clay campaign on a one-off list of this run's shortlist, every person linked to a company with its full record, with agreed copy, a clean spam check, previews and (if asked) a test in your inbox. The chat gives the link, the people on the list, who had no email, who is waiting on the decide list, the credits used (data and action credits), and says the campaign has not started.
