# Buyer sweep: who actually bought

Goal: everyone who bought in the window, matched to the CRM and moved to won. Read only what is new in the window, never whole customer lists.

## Proof, by kind of sale

| Kind | Proof of won | Not proof |
| --- | --- | --- |
| Online purchase (course, product, subscription) | A new paid order, enrollment or charge in the platform, above 0, in the window | A "just signed up" message with no order behind it; a free or 100% discount seat |
| Services and company deals | A signed contract, a paid invoice, or the client confirming payment in writing | A contract or invoice only sent: that moves the stage forward, it isn't won |

## Reading the platforms

- **With a connector** (Stripe, your payment or course platform): list orders or charges created in the window, newest first, and stop paging at the first one older.
- **Notification emails** ("new order", "new enrollment", "payment received"): use them to know which products had new buyers, and to count. The number of new buyers should match the number of notices. If not, say how many are unaccounted for.
- **No connector:** if the platform is open in a browser where the person is signed in, read it there, read only. Never click anything that changes it. If it doesn't open, say "<platform> not checked: <reason>" on the first line of the report, set no online buyer to won this run, and list people who wrote that they bought as decisions.
- **Contracts and invoices:** files created in the window with "agreement", "contract", "SOW" or "invoice" in the name, and signature tool notices in email.

People telling you they bought are context to match names and second emails. The platform is the proof.

## Match and act

Match every buyer by email, then name, then company. A different purchase email still matches by name: note the second email.
- Matched open or lost row with proof: set won, product, last contact, latest communication (what, when, amount), next step if they asked for anything.
- Paying buyer with no row: create one at won, with product, source if known, email, value and latest communication.
- Recurring payment from a row already at won: no change except last contact (see `act-or-ask.md`).
- Likely but unconfirmed: a decision, never won.
