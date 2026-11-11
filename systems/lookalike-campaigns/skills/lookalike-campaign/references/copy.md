# The copy

Start from your own wording and change only the facts. Keep your sentences, personalize the facts, no reactions or praise, and agree the copy before anything goes into Clay. Run every line through your voice skill if you have one.

## The template

The pattern: a short opener that names the second decision maker, what you do for companies like theirs, one line of proof, one easy ask. In Clay tokens, `[First name]`, `[Company]` and `[Opener]` below are lead fields.

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

## Clay tokens

Take the exact field ids and labels from `clay campaigns audience <campaign id>` after the list is attached. Tokens look like `{{lead:first_name|First name}}` and `{{lead:<field id>|Opener}}`. The company record fields on each person (city, industry, founded, description) can be tokens too, but only use a fact that reads true for every lead. The signature can use `{{sender.senderFirstName}}`: previews show it raw, the test email fills it.

## Spintax

At least 2 groups per email, 2 to 5 variants each, only small phrases in your words: `{{spintax:Hey|Hi}}`, `{{spintax:interesting|useful}}`, `{{spintax:nudging you on|bumping}}`. Never vary the facts, the proof or the ask. Clay's spam check takes points off fixed sentences; a fixed proof sentence is still worth it.

## Check before showing

Render every spintax version of A, B and the nudge for 2 real people (one with a second person, one without). Check each for spam trigger words, banned phrases, dashes, square brackets, unfilled tokens and length. Fix every "must fix". Then show A, B, the nudge, the subject and every variant, and wait for the pick.
