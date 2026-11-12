# Creator signals

Every week, find real buyers in the comments of LinkedIn creators you pick, who speak to your audience but don't sell what you sell. The system keeps only posts about something you sell, drops empty, keyword and AI-written comments, enriches the people left and scores them against your live ICP. You review every step in chat: each post and person with its link and why it was picked, and you confirm or change it by number. Then you pick one channel for the confirmed list: personal LinkedIn messages you send by hand from an outreach file (a Google Sheet, or Excel), or a one-off email campaign in Clay that you launch yourself.

Best for offers sold to individuals or small teams (courses, coaching, productized services, tools for solo experts), where the buyer is the person commenting.

Three skills, used in order:

| Skill | Part | What it does |
| --- | --- | --- |
| `linkedin-creator-signals` | 1. Find and qualify | Posts, comments, screening, enrichment, scoring, shortlist, each reviewed with you in chat, then asks: LinkedIn or email? |
| `creator-signals-linkedin` | 2a. LinkedIn | One short personal message per shortlisted person, from your own template, agreed with you first, then the outreach file with everything you need to reach out. You send them. |
| `creator-signals-email` | 2b. Email | Work emails, a one-off Clay list, a Clay campaign with your agreed copy, spam check, a test email to you. You press Launch. |

One list goes to one channel, never both.

## How it fits together

```
your creators → this week's posts (Apify) → keep on-topic posts → PAUSE 1 in chat: approve comment scrape
→ comments (Apify) → screen people → PAUSE 2 in chat: approve enrichment
→ enrich (Clay) → score against live ICP → shortlist → PAUSE 3 in chat: confirm the list, LinkedIn or email?
→ LinkedIn: drafts agreed in chat → outreach file (Google Sheet or Excel)
→ email: one-off Clay list and campaign → you press Launch
```

Nothing is created until the last stage: the outreach file on the LinkedIn path. Every paid step is forecast and waits for your yes. The only exception: the weekly posts scrape runs by itself when it costs less than your posts cap (USD 0.50 by default).

## Works best with

- **Apify** for posts and comments (required: nothing works without the scrape).
- **Clay**, through the Clay CLI, for "Enrich Person", and for email, "Work Email", "Enrich Company" and Campaigns. Without Clay, scoring falls back to the headline and comment, clearly marked.
- **Google Drive and Sheets** for the LinkedIn outreach file. Without them, an Excel file.
- **Your GTM context** (ICP, competitors, messaging, customers) and your **CRM**, to skip customers and open deals.
- Slack or email for the "ready for review" note. Optional.

Never uses a tool that reads or acts through your own LinkedIn account. LinkedIn data comes from Apify only.

## Costs (rough, check your own prices)

| Step | Price the system uses as a default | Typical week |
| --- | --- | --- |
| Posts (Apify) | about USD 0.002 per post | 10 creators × 7 posts: about USD 0.15 |
| Comments (Apify) | about USD 0.002 per comment | 8 posts × 150 comments: about USD 2.40 |
| Enrich Person (Clay) | read from your Clay workspace during setup | 40 people |
| Work Email (Clay), email only | read from Clay during setup | the shortlist |
| Enrich Company (Clay), email only | read from Clay during setup | one per company on the email list, so every company in Clay has its full record |

Clay also bills action credits, from a separate balance, on every routine run. Every Clay forecast shows both.

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{CREATORS}}` | **Asked first.** The LinkedIn creators to track: name, profile link, one line on why their audience is your buyer. You pick them; each is checked against your competitors before saving | Ask. Recommend 8 to 15 | |
| `{{YOUR_NAME}}` | Your first name | `~/.claude/CLAUDE.md`, GTM context, or ask | |
| `{{GTM_CONTEXT}}` | Notion Hub link, or `~/gtm-context/gtm/README.md` | `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{OFFERS_IN_SCOPE}}` | The offers this system finds buyers for | Product and ICP pages | Offers sold to individuals |
| `{{AUDIENCE}}` | Who you hope to find in the comments, in one line | ICP page | |
| `{{KEEP_TOPICS}}` | Post topics that speak to what you sell, 3 to 6 bullets | Product, ICP and messaging pages | |
| `{{DROP_TOPICS}}` | Extra topics to drop for your business, on top of the standard ones | Competitors page, or ask | |
| `{{COMPETITOR_SERVICES}}` | What a competitor sells, so their people are dropped | Competitors page | |
| `{{KNOWN_PEOPLE_SOURCES}}` | Where customers and open deals live, to skip them | CRM and Customers in GTM context | |
| `{{OUTREACH_FILE}}` | Where the LinkedIn outreach file goes: a Google Sheet or an Excel file | Connected tools: Google Drive means a Sheet | Google Sheet if Drive is connected, else Excel |
| `{{DRIVE_FOLDER}}` | Folder and file name for the outreach files | | "LinkedIn outreach" |
| `{{NOTIFY}}` | Where the scheduled run's short "review waiting" note goes: a Slack channel, your own email, or chat only. The review itself is always in chat | Connected tools | Chat only |
| `{{RUN_DAY}}` | Day and time of the weekly run | | Monday 07:30 |

Creators live in `settings.md`, and you can add more any time ("add a creator"). Campaigns, Clay prices and Clay ids are added during setup and live there too.

## Adapting it

- Different buyers: change `{{KEEP_TOPICS}}` and `{{DROP_TOPICS}}`, and the competitor rule in `references/screening.md`.
- Team sales instead of individuals: this system is weaker there. Use company signals or website visitors for companies.
- Your own channel: add a part 2c skill next to the two here (for example a CRM import) and add it to Pause 3.
