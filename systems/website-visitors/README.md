# Website visitors

A short daily summary of the companies that visited your website: which offer and ICP card they fit, how engaged they were, whether they came back, and whether you already have a warm path in on LinkedIn. You decide who to contact. The system never contacts anyone and never mentions the visit.

One skill: `website-visitor-digest`.

## How it fits together

```
visitor tool  →  companies and sessions  →  ICP fit (from your live ICP)  →  engagement score
                                                                              ↓
              summary to Slack, email or chat  ←  warm paths on LinkedIn (read-only, capped)
```

1. **A visitor identification tool** turns website sessions into companies. Examples: Clay web intent, RB2B, Dealfront (Leadfeeder), Warmly, Apollo website visitors, HubSpot. The digest reads it through a connector or CLI, or from a CSV export you drop in a folder.
2. **ICP fit.** A visit identifies a company, not a person. So the digest checks only the company-level parts of each ICP card (size, industry, country, company type, description) against your live ICP, and picks the best card and offer.
3. **Engagement.** Sessions, different days, time engaged, high-intent pages (pricing, contact, booking) and where they came from add up to Hot, Warm or Light.
4. **Three layers.** Came back (good fit and visited on 2 or more days in 30 days) first, then first-time visitors who fit your focus offer, then everyone else in one line each.
5. **Warm paths (optional).** For the top companies only, a read-only LinkedIn check: your 1st-degree connections and people who engaged with your recent posts who work there. Capped low and paced, so your account stays safe.
6. **Summary** to one Slack channel, your own email or the chat. Then the digest remembers the time, so the next run starts from there.

## Works best with

- A visitor identification tool with a connector or CLI (or exports).
- Your GTM context (ICP and product pages).
- Slack, or your email, for the daily summary.
- Optional: a LinkedIn tool connected to your own account that can read connections and post engagers (LeadShark or similar). Without one, the digest gives you a LinkedIn search link per company to check by hand.

## Costs

The digest itself spends nothing: it reads what your visitor tool already collected. Your visitor tool and any enrichment inside it cost what they cost there. LinkedIn reads are free but capped (see `settings.md`).

## What you decide

| Placeholder | What it is | Where Claude looks | Default |
| --- | --- | --- | --- |
| `{{YOUR_NAME}}` | Your first name, for the skill description | `~/.claude/CLAUDE.md`, GTM context, or ask | |
| `{{WEBSITE}}` | The website being tracked | GTM context, product page | |
| `{{GTM_CONTEXT}}` | How to find your context: the Notion Hub link, or `~/gtm-context/gtm/README.md` | The `gtm-context` block in `~/.claude/CLAUDE.md` | |
| `{{VISITOR_TOOL}}` | Your visitor identification tool | Connected tools, or ask | |
| `{{VISITOR_SOURCE}}` | How to read it: table or list id, connector call, or export folder | The tool itself | `~/.growth-systems/website-visitors/exports/` |
| `{{FOCUS_OFFER}}` | The offer that gets its own layer in the digest | GTM context, product page (your highest-value offer) | Your highest-value offer |
| `{{DESTINATION}}` | Where the summary goes: a Slack channel name and id, your own email, or chat only | Connected tools, or ask | Chat only |
| `{{HIGH_INTENT_PAGES}}` | Words in page paths that show buying intent | Your site's pages | pricing, contact, book, demo, services |
| `{{LINKEDIN_TOOL}}` | Your read-only LinkedIn tool, or `none` | Connected tools | `none` |
| `{{LOOKBACK_HOURS}}` | Window of the first run | | 24 |

## Adapting it

- Different layers (for example one per offer): change "Three layers" in `SKILL.md` and the layout in `references/digest-format.md`.
- Score inside your visitor tool instead (a Clay formula or AI column, for example): keep `references/scoring.md` as the rules and point step 2 at the column.
- Weekly instead of daily: change the schedule and set `lookback_hours` to 168.
