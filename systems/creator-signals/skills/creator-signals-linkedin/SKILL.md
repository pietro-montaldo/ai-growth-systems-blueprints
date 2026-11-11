---
name: creator-signals-linkedin
description: "{{YOUR_NAME}}'s LinkedIn creator signals, part 2 (LinkedIn): turns this week's shortlist from linkedin-creator-signals into personal LinkedIn messages in the weekly Google Sheet. Starts from your own template, offers 2 or 3 versions close to your wording filled in for real people, drafts the batch with the one you pick, matches each person to the best CTA, and checks length and banned phrases. Use when you pick LinkedIn for a creator signals list, or say \"draft the LinkedIn messages\", \"LinkedIn DMs for this week's list\", \"redo the LinkedIn drafts\". Not for email (use creator-signals-email), not for finding people (use linkedin-creator-signals), and it never sends or connects."
metadata:
  version: "0.1.0"
---

# LinkedIn creator signals (part 2: LinkedIn messages)

Writes one short personal message per shortlisted person into this week's sheet. You send them by hand from your own profile, as a connection note or a DM.

Settings, run files and copy rules live in the sibling skill folder `../linkedin-creator-signals/` (call it `$FIND`): `$FIND/settings.md`, `$FIND/references/run-files.md`, `$FIND/references/copy.md`. Run data is in `~/.growth-systems/creator-signals/`, and `$RUN` is the current run.

## Before starting

- The run is at stage `scored` and its channel is `linkedin`. If the channel is empty, ask "LinkedIn or email for this list?" and record it. If it is `email`, stop and point to `creator-signals-email`: one list goes to one channel.
- Read the People tab. The list is every row with Status "shortlist" or "send": you may have changed Status by hand. Apply your edits to `$RUN/people.json`.
- Load your voice skill if installed. Follow `$FIND/references/copy.md` for every copy rule.

## Steps

**1. Template.** Read "Saved campaigns" in settings. If one fits, show its agreed version filled in for 2 people from this list and ask "Same as last time?". Otherwise ask the gaps in `copy.md` section 2 and agree a version per section 3. Save it.

**2. CTA per person.** If the CTA has options, list the live ones and pick one per person per `copy.md` section 4. Write it to the CTA column.

**3. Draft.** Fill the agreed version per person. At most `linkedin_max_chars` (200) characters, so it works as a connection note and as a DM. Check every draft per the copy rules and fix every flag. Set Channel to "linkedin".

**4. Sheet.** Write Draft, CTA and Channel into the People tab of the same file. Read it back to check. Set the run's stage to `drafted`.

## Rules

- Never send messages, connection requests, comments or reactions. Never use a tool that acts through your LinkedIn account.
- Never draft for people outside the list. Never react to or quote their comment.
- The skill doesn't check connection status: you see on the profile whether to connect or message.

## Done means

Every row on the list has a draft of 200 characters or fewer in this week's sheet, the agreed version is saved for next week, and the chat says how many drafts there are, which CTAs they point to, and that nothing was sent.

## Adapting this skill

A different limit or channel (for example voice notes or InMail): change `linkedin_max_chars` in settings and the shape in step 3.
