# The copy

Start from your own wording and change only the facts. Keep your sentences, personalize the facts, no reactions or praise, and agree the copy before anything goes into Clay. Run every line through your voice skill if you have one.

## The template

The pattern: a short opener that names the second decision maker, what you do for companies like theirs, one line of proof, one easy ask. `[First name]`, `[Company]` and `[Opener]` below are merge fields. In the Clay Agent prompt they become `{First name}`, `{Lookalike company}` and `{Lookalike opener}`: the company display name and opener fields made in setup.

**Subject (both versions):** `<Seed> + [Company]`

**Version A, offer the proof:**

> Hey [First name],
>
> [Opener]
>
> We've been helping <buyer group> like [Company] <the result your offer gives, in one line>.
>
> {{CREDIBILITY_LINE}}
>
> If this could be interesting, I can send over what <proof person>, <role> at <Seed>, said after we worked together.
>
> {{YOUR_NAME}}

**Version B, quote the proof** (only when a quote is allowed):

> Hey [First name],
>
> [Opener]
>
> We've been helping <buyer group> like [Company] <the result>. Recently it was <Seed>, <one line with the hook>. <Proof person>, their <role>, afterwards: "<exact quote>."
>
> If this could be interesting, I can send over how we set it up for them.
>
> {{YOUR_NAME}}

**Nudge, day 3, reply in the same thread:**

> Hey [First name], nudging you on the email above.
>
> If it's easier, happy to do a 15-minute chat to see if it could fit [Company]'s team.
>
> {{YOUR_NAME}}

Replace this template with your own once you have a version that gets replies. Keep the pattern.

## What changes per seed

- `<buyer group>`: what the lookalikes are, in their words ("B2B agencies", "investment firms").
- The seed's description and hook: only from its own Clay description, website or your customer notes, and only if true and public.
- The proof: version B only with an allowed quote. Without one, test A against a version that names the seed and a result from your notes, or agree another A/B idea.
- Timing words ("recently", "last month"): the real timing.
- The credibility line: re-check it before each run.

## Opener (per person, Clay field "opener")

From settings: the "with a second person" line when there is one, the solo line otherwise.

## Merge fields

Write merge fields in the Clay Agent prompt by their field name in braces: `{First name}`, `{Lookalike opener}`, `{Lookalike company}`. The prompt tells the Clay Agent to use real merge fields, not typed braces. Check the previews: a merge field that didn't take shows up as braces or a blank. The person's linked company fields (city, industry) can be merge fields too, but only use a fact that reads true for every lead.

## Spintax

At least 2 groups per email, 2 to 5 variants each, only small phrases in your words: `{Hey|Hi}`, `{interesting|useful}`, `{nudging you on|bumping}`. The prompt tells the Clay Agent these are spintax. Never vary the facts, the proof or the ask. Clay's spam check takes points off fixed sentences; a fixed proof sentence is still worth it.

## Check before showing

Render every spintax version of A, B and the nudge for 2 real people (one with a second person, one without). Check each for spam trigger words, banned phrases, dashes, square brackets, unfilled tokens and length. Fix every "must fix". Then show A, B, the nudge, the subject and every variant, and wait for the pick.
