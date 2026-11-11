# Results and expanding

## Reading a campaign

Pick it from settings "Campaigns". `clay campaigns get <cam>` shows the status (draft means never launched: ask before reading results). `clay campaigns analytics <cam>` gives sent, replies and bounces by step.

Report per variant: leads, first email sent, nudge sent, replies, positive replies, bounces, unsubscribes. A reply is positive only when it asks for the proof, the setup, a call or a price, or says yes. When unsure, ask the person to look at the thread: never read their inbox for this without asking.

With about 50 leads per variant, only a big gap means anything. Say so.

## The expand rule

{{EXPAND_RULE}}

- Not reached: say how far off, and offer one change for the next test (a different seed, the other proof style, a different buyer group). Don't expand.
- Reached: propose the next batch.

## The next batch

1. Same seed and `seed.json`. Re-check the proof and its permission first.
2. Search again with the strategy that worked, and try what didn't get tried. Companies already in Clay Audiences stay out, and every past company list from "Already targeted" is excluded. The target is again companies with a work email.
3. Widen in this order, one step at a time and only with a yes: the seed's wider market, then the next size bucket, then a neighbouring service. Each step lowers recognition: say so.
4. Copy: the winning version as A, one new idea as B.
5. Name: `<Seed> lookalikes <date> <offer> batch 2`. New people list, new company list, new campaign. Never add leads to a launched campaign's list: tagging moves people between lists.
