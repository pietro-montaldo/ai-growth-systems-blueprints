# Building the campaign

## Name and tag

Campaign name = list name = tag value: `Creator signals YYYY-MM-DD <short campaign name>`, for example "Creator signals 2026-11-02 reporting guide". Never a person's name, company or email.

## Adding people to the list

One routine run per person, all in one call (up to 100 items):

```json
{"items": [{"id": "<linkedin slug>", "inputs": {
  "email": "", "first_name": "", "last_name": "", "full_name": "", "linkedin_url": "",
  "title": "", "company": "", "company_domain": "", "company_linkedin": "",
  "campaign": "<campaign name>", "post": "Sam's post on reporting",
  "cta": "a session on automating client reports", "cta_date": "Nov 10",
  "cta_link": "https://..."}}]}
```

`company_domain` is required. Take it from the person's Work Email result (the company domain it used), and `company_linkedin` from their current role. The routine first adds or updates that company by domain, then links the person to it, so the person's Company column in Clay is filled. Someone with no company domain has no work email either, so they never reach this step.

Poll the run until it is complete. Report any item that failed; don't retry it blindly. Then check the link: count the people whose campaign field equals the campaign name and who have no company (`count from people where <campaign field> = "<campaign name>" and not company.exists()`). It must be 0. The count lags about 10 seconds behind the routine. In email the CTA link is the full `https://` link so it is clickable everywhere. The routine updates by email and LinkedIn link, so running it again updates the same record.

## The one-off list

A people audience filtered on the campaign field equal to the campaign name. Check its count equals the people sent. Clay's search lags a few seconds behind the routine: if the count is short, wait 10 seconds and count again. When the campaign is finished, part 1 offers to archive the list.

## Campaign settings

After creating the draft, read a fresh copy, then one change per command: the list, the sender inboxes you picked, and the goal in one sentence ("Invite each person to the session that fits them best").

## Copy

- Use the exact field tokens the campaign's audience shows: first name, plus post, cta, cta_date and cta_link from setup. Personal facts come from these fields only, never from AI snippets.
- The first email is a new thread with a subject. Follow-ups reply in the same thread with no subject, 3 then 7 days later, unless you say otherwise.
- Plain text paragraphs with a blank line between them, no square brackets except in links, your first name as the signature.
- Show readable placeholders ("[First name]"), never raw tokens or ids.
- A subject that starts with a lowercase field starts lowercase. Offer a subject that opens with fixed words instead ("Session on <topic>, <date>").

## Spintax

Fixed wording sent to a whole list is a fingerprint, so every email varies a few phrases: `{{spintax:Hey|Hi}}`.
- At least 2 groups per email, 2 to 5 variants each.
- Vary small phrases only: the greeting, a connector, the closing line, a verb. Never the facts (name, post, CTA, date, link) and never the ask itself.
- Every variant is something you would write: from your template, your past messages and your voice skill, or a near-identical rewording of your own phrase.
- Show every variant, not just the first.

## Spam trigger words

Check every spintax version. Words to change (start list, add your own):

free, 100%, act now, apply now, bonus, buy, cash, cheap, click here, congratulations, deal, discount, don't hesitate, double your, earn, exclusive deal, guarantee, limited time, no cost, offer expires, once in a lifetime, risk-free, special promotion, urgent, winner

- "Free" is the one most likely to appear. Say what it is instead ("a live session", "open to everyone") or let the linked page say it.
- Never fix a trigger word by changing the meaning or adding a claim. Offer a plain alternative and let the person choose.
- Words alone don't decide delivery. Warmed inboxes, verified emails and low volume per inbox matter more.

## Test and hand-off

- Spam check and previews are free. A test sends one real email: only to the person's confirmed address, from a connected inbox, after a clear yes. Never retry it automatically.
- The campaign stays a draft. Give the link and say to press Launch in Clay.
- Add `campaign, list, run date, people, status` to the past campaigns table in settings.
