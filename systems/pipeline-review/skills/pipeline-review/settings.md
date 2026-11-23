# Settings: pipeline review

## Where things are

- **GTM context:** {{GTM_CONTEXT}}
- **CRM:** {{CRM}}
- **How it is read and written:** {{CRM_HOW}}
- **Channels:** {{CHANNELS}}
- **Proof of payment or signature:** {{BUYER_PROOF}}
- **Your own addresses:** {{OWN_ADDRESSES}}
- **Weekly run:** {{RUN_DAY}}

## CRM tables

One row per table, pipeline or spreadsheet: its link or file, what it is for, which offers go there, and whether the run writes to it or only reads it. Most small businesses have one.

{{CRM_TABLES}}

## Fields

The fields you want kept current, next to what they are called in your CRM, and how each is written: always update, fill only when empty, or never. A field you didn't pick is not in this table, and the run doesn't write it.

{{FIELD_MAP}}

## Never touch

Columns the run never writes, even when it has a value for them:

{{NEVER_TOUCH}}

## Stages

The skill's rules use these meanings. Next to each, your stage or status name, or "none".

{{STAGE_MAP}}

## What counts as an opportunity

Someone who would pay you for:

{{OPPORTUNITY_TYPES}}

Never logged (flag the meaningful ones, ignore the rest):
- partnerships, collaborations, co-selling, referral or affiliate deals, revenue shares
- paid work where you supply another business in your field, if that is not what you sell
- free advice calls and catch-ups with no buying ask
- existing won clients sorting contract, scheduling or delivery logistics
- people asking for feedback, favors or homework
- vendors selling to you, recruiters, newsletters, automated notices, "great post"

## Email search words

Words that show a buying ask for each offer, used in the inbox searches:

{{OFFER_KEYWORDS}}

## Your rules

Your own rules for this CRM, set up with you and added to after each correction. They win over the defaults in this skill.

{{CRM_RULES}}

## Follow-ups

- At most 3 follow-ups after your first reply, spaced 3, 5, then 7 days.
- After the last one, propose closing as lost. Never set it without a written no.

## Links for drafts

{{OFFER_LINKS}}
