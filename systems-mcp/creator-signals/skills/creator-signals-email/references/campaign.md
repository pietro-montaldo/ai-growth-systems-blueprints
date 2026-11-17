# Building the campaign

## Name and tag

Campaign name = list name = tag value: `Creator signals YYYY-MM-DD <short campaign name>`, for example "Creator signals 2026-11-02 reporting guide". Never a person's name, company or email.

## Adding people to the list

Build the input sets by this rule, never by hand. One input set per person on the list, from three sources: the person (people.json), their Work Email result, and the Enrich Company result for their company. One workflow run per person, all in one connector call (up to 100; above that, split into calls of 100 and run one at a time). Each input set looks like this:

```json
{
  "email": "", "first_name": "", "last_name": "", "full_name": "", "linkedin_url": "",
  "title": "", "company": "", "campaign": "<campaign name>", "post": "Sam's post on reporting",
  "cta": "a session on automating client reports", "cta_date": "Nov 10",
  "cta_link": "https://...",
  "company_domain": "acme.example", "company_linkedin": "https://www.linkedin.com/company/acme",
  "company_website": "https://www.acme.example", "company_city": "Leeds", "company_state": "England",
  "company_country": "United Kingdom", "company_industry": "Marketing Services",
  "company_headcount": 12, "company_founded": 2015, "company_description": "<up to 600 characters>",
  "company_revenue": "1M-5M", "company_logo_url": "https://...",
  "person_city": "Leeds", "person_state": "England", "person_country": "United Kingdom", "person_location": "Leeds, England, United Kingdom"}
```

- `company_domain` is required. It is the company domain sent to Work Email, kept only when the email is at that domain. People with an email at another business go on the decide list instead.
- `company_linkedin` comes from the person's current role, else from Enrich Company.
- The `company_*` record comes from Enrich Company (SKILL.md step 2b). City and state come from the location marked headquarters, else the first one. Write the country as a full name ("United Kingdom", not "GB"). Headcount and founded are numbers.
- The person's own city, state, country and location come from the Enrich Person result part 1 already paid for. A country only when Clay gave one.
- Leave out empty values. The workflow skips blanks, so running it again never wipes a field.
- Before running, list anyone with no company record or no CTA fields, and any company where Enrich Company answered with another company. Fix those first.

The workflow first adds or updates that company by domain with the full record, then links the person to it, so the person's Company column in Clay is filled. Someone with no company domain has no work email either, so they never reach this step.

Follow progress on one record, and when the task is complete, read the results for failures only. Report any run that failed; don't retry it blindly. Then the Clay Agent check prompt (`../linkedin-creator-signals/references/clay-agent.md`): the count equals the people sent, no one has no linked company (it must be 0), and who has no country of their own (list them; don't pay to fill them unless you'll use it). Clay's counts lag a few seconds behind the workflow: if the count is short, wait and ask again. In email the CTA link is the full `https://` link so it is clickable everywhere. The workflow updates by email and LinkedIn link, so running it again updates the same record.

## The one-off list

A people segment filtered on the campaign field equal to the campaign name, created by the Clay Agent in the same prompt as the campaign. Check its count equals the people sent. When the campaign is finished, part 1 offers to archive the list.

## Campaign settings

The list and campaign prompt sets them all at once: the list, the sender inboxes you picked, the sending window, and the goal in one sentence ("Invite each person to the session that fits them best"). Check each in the Clay Agent's plan.

## Copy

- In the prompt, name the merge fields in braces: {First name}, {Creator signals post}, {Creator signals CTA}, {Creator signals CTA date}, {Creator signals CTA link}. The Clay Agent turns them into real merge fields. Personal facts come from these fields only, never from AI snippets.
- The first email is a new thread with a subject. Follow-ups reply in the same thread with no subject, 3 then 7 days later, unless you say otherwise.
- Plain text paragraphs with a blank line between them, no square brackets except in links, your first name as the signature.
- Show readable placeholders ("[First name]"), never raw tokens or ids.
- A subject that starts with a lowercase field starts lowercase. Offer a subject that opens with fixed words instead ("Session on <topic>, <date>").

## Spintax

Fixed wording sent to a whole list is a fingerprint, so every email varies a few phrases, written `{Hey|Hi}` in the prompt; the Clay Agent turns them into spintax.
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

- Spam check and previews are free. A test sends one real email, through the Clay Agent's test email prompt: only to the person's confirmed address, from a connected inbox, after a clear yes. Never retry it automatically.
- The campaign stays a draft. Give the link and say to press Launch in Clay.
- Add `campaign, list, run date, people, status` to the past campaigns table in settings.
