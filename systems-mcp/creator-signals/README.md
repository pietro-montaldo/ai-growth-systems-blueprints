# Creator signals: Windows fallback (Clay connector + Clay Agent)

Copying this system? Claude follows [COPY-GUIDE.md](../../COPY-GUIDE.md) at the root of this repo. A link to this folder is enough to start.

**Use this only on Windows without the Clay CLI.** If `clay whoami` works, on any computer, use [`systems/creator-signals/`](../../systems/creator-signals/README.md) and ignore this folder. On a Mac or Linux computer without the CLI, install the Clay CLI first (Claude can do it with Clay's plugin), then use `systems/`.

The same system as the creator signals in `systems/`, for Windows without the Clay CLI. Claude runs Clay's Enrich Person, Work Email and Enrich Company through the Clay connector, and drives the Clay Agent in the built-in browser of the Claude desktop app (never Claude in Chrome) for the one-time email setup, the list and the campaign. The LinkedIn path doesn't use Clay at all.

Every week, find real buyers in the comments of LinkedIn creators you pick, who speak to your audience but don't sell what you sell. The system keeps only posts about something you sell, drops empty, keyword and AI-written comments, enriches the people left and scores them against your live ICP. You review every step in chat: each post and person with its link and why it was picked, and you confirm or change it by number. Then you pick one channel for the confirmed list: personal LinkedIn messages you send by hand from an outreach file (a Google Sheet, or Excel), or a one-off email campaign in Clay that you launch yourself.

Best for offers sold to individuals or small teams (courses, coaching, productized services, tools for solo experts), where the buyer is the person commenting.

Three skills, used in order:

| Skill | Part | What it does |
| --- | --- | --- |
| `linkedin-creator-signals` | 1. Find and qualify | Posts, comments, screening, enrichment, scoring, shortlist, each reviewed with you in chat, then asks: LinkedIn or email? |
| `creator-signals-linkedin` | 2a. LinkedIn | One short personal message per shortlisted person, from your own template, agreed with you first, then the outreach file with everything you need to reach out. You send them. |
| `creator-signals-email` | 2b. Email | Work emails through the connector, a one-off Clay list and a Clay campaign with your agreed copy built by the Clay Agent, spam check, a test email to you. You press Launch. |

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
- **The Clay connector** in Claude, for "Enrich Person", and for email, "Work Email" and "Enrich Company". Without Clay, scoring falls back to the headline and comment, clearly marked.
- **The Clay Agent and the Claude desktop app's built-in browser**, for the email path only: the one-time setup, the one-off list, the campaign, the spam check and the test email. Sign in to Clay once in that browser pane. The Clay Agent is in beta and on Clay's Launch, Growth and Enterprise plans; without it, Claude walks you through those steps in Clay by hand.
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

Clay also caps how much each connected user can spend through the connector (Clay settings, Agent users). The connector can't read prices: they are read once in setup with the Clay Agent.

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
| `{{CLAY_AGENT}}` | Whether your Clay plan has the Clay Agent: "yes", or "no, build by hand in Clay". Only the email path needs it | Claude opens Workflows, New in the built-in browser and looks for the box "What should we build today?" | yes |

Creators live in `settings.md`, and you can add more any time ("add a creator"). Campaigns, Clay prices and Clay ids are added during setup and live there too.

## Adapting it

- Different buyers: change `{{KEEP_TOPICS}}` and `{{DROP_TOPICS}}`, and the competitor rule in `references/screening.md`.
- Team sales instead of individuals: this system is weaker there. Use company signals or website visitors for companies.
- Your own channel: add a part 2c skill next to the two here (for example a CRM import) and add it to Pause 3.
- You get the Clay CLI later: switch to the CLI version in `systems/creator-signals/` and stop using this one. Your fields, workflow and settings carry over.

## Different from the CLI version

- Enrich Person, Work Email and Enrich Company run through the Clay connector, in batches of up to 100. Big results go to a helper agent that writes the fields to the run folder (`linkedin-creator-signals/references/connector.md`).
- The email path's one-time setup, list, campaign, spam check, previews and test email are built by the Clay Agent from prompts in `linkedin-creator-signals/references/clay-agent.md`. The "add to campaign list" workflow runs through the connector.
- Prices are read once in setup with the Clay Agent; the connector can't read prices or your balance.
- Tested in the other fallbacks: the connector functions, the Clay Agent building an "add people" workflow, and a draft campaign on a list with merge fields, spintax, spam check and previews. This system's own prompts follow the same pattern and haven't been run end to end yet.
