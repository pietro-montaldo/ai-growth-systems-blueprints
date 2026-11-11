# Scoring a visiting company

Score from the **live ICP page** in your GTM context, read at the start of every run. Never copy the cards into this skill. When the page changes, the scoring changes with it.

## 1. Company fit

A visit tells you the company, not the person. Use only what company data can show:

| Check | From |
| --- | --- |
| Headcount | the visitor tool's company data |
| Industry | same |
| Country | the company's country, not the visit's |
| Company type (agency, SaaS, school, public body...) | industry plus description |
| Description | the company's own description |

For each offer's cards:

1. Count how many of the five checks the card's "who" and "find them" lines support. Missing data counts as no.
2. Tier: **A** = 5 of 5, **B** = 4, **C** = 3, **D** = 2, below that **no fit**.
3. Check the card's "not them" lines. One clear match means no fit for that card.
4. Pick the best card across all offers. On a tie, prefer {{FOCUS_OFFER}}, then the higher-value offer.
5. Geography is a score, never a filter, unless your ICP says otherwise: +2 in your main markets, +1 in other high-income countries.

Write the result as: best offer, card, tier, score, and one short reason ("50-person agency, UK, card 1").

Person-level signals on the cards (titles, what someone posts) can't be judged from a visit. The LinkedIn step may add them as context, never as a score.

## 2. Low-confidence match

When the visit came from a country where the company has no presence, the match may be a wrong IP lookup or a remote employee. Flag it ("low-confidence match: visit from <city, country>"). Don't drop it.

## 3. Engagement

Add points per company:

| Signal | Points |
| --- | --- |
| 2 or more sessions in 30 days | 2 |
| 4 or more sessions in 30 days | 2 more |
| Visited on 2 or more different days | 1 |
| Time engaged this window: 180 s or more / 60 s or more / 20 s or more | 3 / 2 / 1 |
| Each high-intent page, up to 2 | 2 |
| Came from a known source (UTM, referrer, campaign) | 1 |

**Hot** = 7 or more, **Warm** = 4 to 6, **Light** = under 4.

Tune these points to your site. A pricing page visit matters more on some sites than a long read of a blog post.

## 4. Doing it in your visitor tool instead

If your tool can run code or AI columns (Clay can), you can move the fit check there so every company is scored once when it first visits. Keep this file as the rules, and write the date of the ICP version you scored against next to the score, so you know when to re-score.
