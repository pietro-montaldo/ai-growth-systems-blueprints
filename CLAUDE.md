# CLAUDE.md

This repo is a library of growth system blueprints, not a plugin or a marketplace. People open it to read a system and ask Claude to copy it into their own setup.

## When someone asks to copy, set up or install a system

Follow [COPY-GUIDE.md](COPY-GUIDE.md) step by step. Most people never open this repo: they paste its link in Claude Code anywhere, so this file isn't loaded and COPY-GUIDE.md must hold every rule a copy needs. In short: read the system, read their GTM context and tools, ask only the gaps in one batch, show the filled copy, save it after an OK in `~/my-growth-systems/<system>/`, run it once together, ask simply whether to publish it on their GitHub (into their own repo and marketplace), then offer a schedule. Never save straight into `~/.claude/skills/`.

Never edit the blueprint files while copying. Never save a filled-in copy, run data or anyone's personal details inside this repo.

### Clay systems: CLI first, no exceptions

Before copying or running any Clay system, check the person's computer and whether `clay whoami` works (ask only if you can't tell). COPY-GUIDE.md step 0 has the table.

- **The Clay CLI works:** use `systems/<system>/` only. `systems-mcp/` plays no role: don't read it, mention it or borrow from it.
- **Mac or Linux without the CLI:** tell them they need the Clay CLI and offer to install it with Clay's plugin. Never the connector version.
- **Windows without the CLI, and only then:** `systems-mcp/<system>/`, the fallback. It drives the Clay Agent in the built-in browser of the Claude desktop app, never in Claude in Chrome.

## When someone asks what a system does

Answer from `systems/<system>/README.md`. Don't copy anything. Mention `systems-mcp/<system>/` only to someone on Windows without the Clay CLI.

## When editing the blueprints themselves

- `systems-mcp/<system>/` is the Windows fallback of a Clay system, for people with no Clay CLI: the Clay connector does the searches, enrichment and workflow runs, and the Clay Agent builds what the connector can't, from prompts the skill types in the built-in browser. Keep it in step with its twin in `systems/`: a change to one system's logic goes into both, unless it is about the CLI, the connector or the browser itself. Each fallback README and SKILL.md opens with the CLI check and stops when the CLI works.
- Keep them anonymous: no real names, companies, prices, Notion, Clay, Slack or Drive ids, hardcoded `mcp__<id>` tool names, or local paths. Examples use made-up companies (Acme, Brightlane, Kito) and first names only.
- Any step that writes people or companies to Clay keeps the records complete: the company upserted by domain with its full Enrich Company record, each person linked to it (the account link, not just the company name) and carrying their own city, state, country and location from data the system already has. After the write, check no one is unlinked and list who has no country. Never pay to fill fields nothing will use.
- Every value that changes from one business to the next is a `{{PLACEHOLDER}}` in upper snake case, listed in that system's README "What you decide" table with where Claude finds it and a default when there is one. A placeholder that holds a description (a CRM, a source, a list of rules) lives in `settings.md` only; sentences say "the CRM in `settings.md`". Only short names go inside sentences. A placeholder that is asked gets an example in its table row.
- A step that uses a past list (already targeted, past campaigns, known people) reads a table in `settings.md`. COPY-GUIDE.md step 1.6 fills it at copy time when the student has past outreach, so name the table there if you add a new one.
- Settings a person will tune go in the skill's `settings.md`, not in `SKILL.md`.
- Students are non-technical. Plain language, short sentences, no em dashes or double dashes in prose. Frontmatter `description` is one quoted string: what it does, quoted trigger phrases, then "Not for X".
- `SKILL.md` stays under about 150 lines. Detail goes in `references/`.
- A do-not-contact list is always optional. Use it when the student has one; never require it, warn about it, or mark rows without it. Customers and open deals are always checked from the GTM context and CRM.
- Every connector step has a fallback (paste, export, do it by hand). Every write waits for a yes. Every credit-spending step shows the count and the cost first. Skills never send.
- Before finishing, search for leaks:

```bash
grep -rniE "notlinear|maven\.com/|nforce|collection://|mcp__[0-9a-f]{6}|/Users/|wf_[0-9a-z]{6}|t_[0-9a-z]{10}|C0[A-Z0-9]{8}" --exclude-dir=.git --exclude=CLAUDE.md .
```

The only expected hits outside that list are the license line and the link to the GTM context kit repo in the README.
