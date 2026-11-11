# CLAUDE.md

This repo is a library of growth system blueprints, not a plugin or a marketplace. People open it to read a system and ask Claude to copy it into their own setup.

## When someone asks to copy, set up or install a system

Follow [COPY-GUIDE.md](COPY-GUIDE.md) step by step. In short: read the system, read their GTM context and tools, ask only the gaps in one batch, show the filled copy, save it after an OK in `~/my-growth-systems/<system>/`, run it once together, ask simply whether to publish it on their GitHub (into their own repo and marketplace), then offer a schedule. Never save straight into `~/.claude/skills/`.

Never edit the blueprint files while copying. Never save a filled-in copy, run data or anyone's personal details inside this repo.

## When someone asks what a system does

Answer from `systems/<system>/README.md`. Don't copy anything.

## When editing the blueprints themselves

- Keep them anonymous: no real names, companies, prices, Notion, Clay, Slack or Drive ids, hardcoded `mcp__<id>` tool names, or local paths. Examples use made-up companies (Acme, Brightlane, Kito) and first names only.
- Every value that changes from one business to the next is a `{{PLACEHOLDER}}` in upper snake case, listed in that system's README "What you decide" table with where Claude finds it and a default when there is one.
- Settings a person will tune go in the skill's `settings.md`, not in `SKILL.md`.
- Students are non-technical. Plain language, short sentences, no em dashes or double dashes in prose. Frontmatter `description` is one quoted string: what it does, quoted trigger phrases, then "Not for X".
- `SKILL.md` stays under about 150 lines. Detail goes in `references/`.
- Every connector step has a fallback (paste, export, do it by hand). Every write waits for a yes. Every credit-spending step shows the count and the cost first. Skills never send.
- Before finishing, search for leaks:

```bash
grep -rniE "notlinear|maven\.com/|nforce|collection://|mcp__[0-9a-f]{6}|/Users/|wf_[0-9a-z]{6}|t_[0-9a-z]{10}|C0[A-Z0-9]{8}" --exclude-dir=.git --exclude=CLAUDE.md .
```

The only expected hits outside that list are the license line and the link to the GTM context kit repo in the README.
