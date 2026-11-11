# Collecting the last 7 days

## Exports and pasted text

When a source is an export or a paste, not a connector:
- The window ends at the newest item in it, not today. Say that date in the report ("Stripe export ends 10-18").
- If the export is older than the window, ask for a fresh one first. Only if there isn't one, offer to widen the window, at most 6 weeks, and say so in the report.
- Never read a file twice in one run as if it were new. Note the newest item date in `~/.growth-systems/pipeline-review/last-run.json`, and next time start after it.

## Email

Search the inbox for the window, page until empty, and dedupe by thread:
- one search per offer with its buying words from settings, excluding promotions,
- replies to you: subject starting "Re" not from you,
- what you sent: proposals, quotes, pricing, contracts, invoices,
- for every open deal with an email: anything from or to that address in the window.

Open every candidate thread in full. Read the latest message in full for anything you will act on. Your own addresses (settings) count as you.

No email connector: ask the person to paste the threads that matter, or to forward them to a folder you can read. Say in the report that email was pasted, not searched.

## LinkedIn messages

With a tool that reads your own inbox: list threads with a message in the window, page until older, skip threads where your own automated message is the only one, and open the candidates. Never look anyone up or enrich them. If the tool refuses, report LinkedIn as "not checked". Never estimate.

Without one: the person pastes the threads that matter, or LinkedIn is "not checked".

## Bookings

Bookings created in the window, past and upcoming. Read the title, notes and booking answers. A booking with a buying ask is an opportunity at "call booked". Catch-ups without one are flagged or ignored.

## Anything else

Forms, chat widgets, community messages: add them here with how to read them, during setup or later.
