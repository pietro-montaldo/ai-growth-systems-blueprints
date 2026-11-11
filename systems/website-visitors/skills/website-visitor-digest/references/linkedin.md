# Warm paths on LinkedIn (read-only)

Goal: for the best-fit companies only, find people you already know there. Your 1st-degree connections, and people who engaged with your recent posts. They are a way in, nothing more. Never treat one of them as the visitor.

## Allowed calls

Only reads, through a tool connected to your own LinkedIn account. With LeadShark these are: activity limits (read only), people search, lead activity, your recent posts, and post engagers. Never call anything that sends a message, sends or accepts a connection, comments, reacts, enriches, or starts an automation. If your tool names the calls differently, map them here once, during setup, and list the names.

## Every call is counted first

Keep a counter file at `$STATE/linkedin-YYYY-MM-DD.json`: `{"limits": 0, "search": 0, ..., "total": 0, "last_call": "<time>", "stopped": null}`.

Before every call:
1. Read the counter. If `stopped` is set, or this kind is at its cap, or `total` is at `daily_total`: skip this call and every later call of this kind today. Don't retry, don't work around it.
2. Wait until `min_seconds_between_calls` plus a random 0 to 8 seconds have passed since `last_call`.
3. Add one to the kind and to `total`, set `last_call`, save, then make the call.

One call at a time, never in parallel. If any response shows a cooldown, or fewer remaining calls than `stop_if_remaining_below`, set `stopped` to the reason and make no more LinkedIn calls today. The digest still goes out without the LinkedIn part.

## Steps

1. **Safety check:** one activity limits read. Apply the stop rule.
2. **Engagers, once a day, shared by every company.** If `$STATE/engagers-YYYY-MM-DD.json` exists, use it. Otherwise read your 10 most recent posts, then the engagers (comments and reactions) of each post from the last 30 days, most comments first, until the cap. Keep only name, headline, profile link and which post. Save the file.
3. **Per company,** from the first two layers, in report order, up to `max_companies_per_run`:
   - Cache first: `$STATE/company-<domain>.json` younger than `company_cache_days` means no calls.
   - Otherwise one people search: the company name in double quotes (drop Inc, Ltd, GmbH and the like), 1st-degree only, 10 results.
   - **Only people whose headline names the company count.** LinkedIn also matches schools and past roles, so a result without the company in the headline is not staff.
   - Add today's engagers whose headline names the company.
   - For up to `max_people_per_company` of them, engagers first: one lead activity read. Note whether they engaged with your content, are connected, and whether you messaged before. Drop anyone your tool flags as "do not engage", and anyone on your do-not-contact list if you have one.
   - Save `{connections, engagers, activity, note}` to the cache file.
4. Companies over the limit, or blocked by a cap, show "LinkedIn check skipped (daily cap)".

## Without a LinkedIn tool

Give each company in the first two layers a people search link filtered to 1st-degree connections at that company, so you can check in a few seconds. That is often enough.
