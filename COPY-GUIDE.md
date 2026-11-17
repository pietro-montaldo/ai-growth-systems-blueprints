# Copy guide

Claude follows this guide when someone asks to copy a system from this repo into their own setup. The blueprint stays untouched. The copy is theirs.

## Start: usually from a link

The normal way in: the person opens Claude Code in any folder, pastes this repo's link (or a link to one system's folder) and names the system or skill they want. They don't clone this repo or open Claude Code inside it, so its `CLAUDE.md` isn't loaded. This guide holds every rule you need. Don't ask them to do any setup for the blueprint itself.

1. **Which system.** Take it from their words: a system name, a skill name (`lookalike-campaign` is the lookalike campaigns system) or the folder in the link. If it isn't clear, show the table from the README and ask which one.
2. **Get the files, read-only.** If the repo isn't already on their computer, download it to a temporary folder (the session's scratchpad if there is one): `git clone --depth 1 <repo link>`. Without git, download `<repo link>/archive/refs/heads/main.zip` and unzip it. Never put it inside their project or one of their repos. Say it in one line: "I've downloaded the blueprint to read it. Nothing from it is installed."
3. Every path in this guide (`systems/<system>/`, `systems-mcp/<system>/`) is inside that download. Go on with step 0.

## 0. Clay systems: the Clay CLI decides the version

Do this first for any system that uses Clay, before reading anything else. Find out yourself, and ask only when you can't tell:

- **Their computer:** Windows, Mac or Linux (from the session's environment).
- **The Clay CLI:** does `clay whoami` run and show a workspace?

Then:

| Their setup | Version | What to do |
| --- | --- | --- |
| The Clay CLI works (any computer) | `systems/<system>/` | Use only this. Ignore `systems-mcp/` completely: don't read it, mention it or borrow from it. |
| Mac or Linux, no Clay CLI | `systems/<system>/` | Tell them the system needs the Clay CLI and offer to install it with Clay's own plugin (its `setup` skill installs it and opens the sign-in). Go on once `clay whoami` works. Never offer the connector version. |
| Windows, no Clay CLI | `systems-mcp/<system>/`, if it exists | The only case for the connector version. If the folder doesn't exist, say the system needs the Clay CLI. Check the Clay connector is connected (ask it which workspace it's on); without it, stop and say what's needed. |

Say in one line which version you are copying and why. A copy of the connector version made earlier is replaced by the CLI version as soon as the person has the Clay CLI.

## 1. Read before asking

1. **The system's README.** Read `systems/<system>/README.md` in full, then every `SKILL.md`, `settings.md` and reference file of that system. Only in the Windows case from step 0, read `systems-mcp/<system>/` instead, and use that folder everywhere this guide says `systems/<system>/`.
2. **GTM context.** Look in `~/.claude/CLAUDE.md` for a block between `gtm-context:start` and `gtm-context:end`.
   - A Notion Hub link: fetch the Hub, then only the pages this system needs (the README says which).
   - A repo and `~/gtm-context`: read `~/gtm-context/gtm/README.md`, then the pages it links.
   - Neither: say once that the system works much better with the GTM context kit, and recommend building it first. If they want to go on anyway, use their own source files as the context: a `COMPANY-PROFILE.md`, their website pages, their notes. `{{GTM_CONTEXT}}` then points at those file paths, and the skill reads them at run time like the context. Without ICP cards, fit is a one-line judgment against who buys, marked "no ICP cards". If there are no files either, ask the 3 or 4 questions the system needs (what you sell, who buys, who signs) and offer to save the answers to `COMPANY-PROFILE.md` next to the copy.
3. **Do-not-contact (optional).** Look for a block between `do-not-contact:start` and `do-not-contact:end` in `~/.claude/CLAUDE.md`. If there is none, carry on without it: don't warn, don't mark rows, don't ask them to build one, and leave the copy's "if you have a do-not-contact list" lines as they are. If there is one, read what it gives:
   - **It names a check skill that is installed** (for example check-do-not-contact): the copy runs that skill where the blueprint says so.
   - **It only gives rules** (where the list lives, who is off-limits): write those rules into the copy's `settings.md` under a "Do-not-contact" heading, and change every "run check-do-not-contact" in the copy to "check the do-not-contact rules in `settings.md`". A step that needs a file only the skill makes (company signals' blocklist upload) is built from those rules when they point at a list you can read; otherwise leave that step out and say so.

   Customers and open deals are always checked from the GTM context and CRM either way.
4. **Voice.** Look for an installed `<name>-voice` skill.
5. **Tools and sources.** Check which connectors and CLIs the README lists are connected (for Clay: `clay whoami`). Note what is missing and what the fallback is (an export, a pasted thread, a CSV). Look at the real data the system will read, not just its name: a client spreadsheet is not a pipeline, and an export has an end date.
   - **Clay** is settled in step 0. In the Windows case only: the connector version drives the Clay Agent in the built-in browser of the Claude desktop app, never in Claude in Chrome. Open Clay there and ask them to sign in once in that browser pane. Then open Workflows, New: if the Clay Agent's box ("What should we build today?") is there, `{{CLAY_AGENT}}` is yes. Without the desktop app's browser, the skill gives them each prompt to paste by hand.
6. **Past outreach (optional).** Some people have already reached out to people, others haven't. A fresh copy starts with empty past-list tables (for example lookalike campaigns' "Already targeted" and "Campaigns"), and some lookups (Clay's Find People at Company) don't skip people already on a campaign list. So look for what exists: other systems in `~/my-growth-systems/` (their campaign and list tables in `settings.md`), and for Clay systems, past campaigns and lists in Clay (`clay campaigns list` and the Audiences lists; on Windows, ask them to name them). Found nothing? Skip this and say nothing. Found some? In step 2, offer to fill the copy's past-list tables with them, so nobody gets a second first email. Fill them only on a yes.

Never copy the GTM context into the skill. The skill reads it at run time. What the copy holds is only how to find it (the Hub link or the repo path) and the settings.

## 2. Fill the gaps in one batch

Go through the README's "What you decide" table. Some placeholders are maps (stage names, field names, tables): fill every row, don't leave a default that was never checked. For each placeholder:

- Fill it from what you read in step 1 when you can, and say where it came from.
- Use the default when the table gives one and nothing better exists.
- Otherwise add it to one list of questions.
- When their tool is missing something the system needs (a column, a stage, a field), propose adding it as part of the questions. Add it only on a yes, and back up a file before changing it.

Two rules for the values:

- **Values inside sentences stay short.** When a placeholder sits inside a sentence of `SKILL.md` or a reference, fill it with a short name that reads well there ("the Notion Sales CRM"). Links, ids, filters and how to read it go in `settings.md`. Read every filled sentence once: if one reads badly, shorten the value.
- **Every question comes with an example.** Give the example from the README table, and when the GTM context has the facts (customer counts, years, results, what they teach), draft 2 options from them to pick from. Never invent a fact for them.

Ask the questions once, in one message, in plain words. A placeholder the table marks **Asked first** opens the message, and is never filled from your own guess. Recommend an answer for each when you can. Never ask where to save the copy: see step 4.

## 3. Show the copy before saving

Fill every `{{PLACEHOLDER}}` in the files under `skills/`. Copy the system README too, but replace its "What you decide" table with a short "My answers" list (each placeholder, the value, and where it came from), so the README itself has no placeholders left. Then:

1. Search the filled files for placeholders: `grep -rnE "\{\{[A-Z_]+\}\}"`. None may be left. Clay tokens such as `{{lead:...}}` and `{{spintax:...}}` are part of the skill and stay. If a placeholder can't be filled, ask.
2. Remove the "Adapting this skill" section only if the person says so. It helps later edits.
3. Show the person, per skill: the filled frontmatter `description`, the settings, and any rule you changed. Keep it short. Offer the full files on request.
4. Wait for an OK. Change what they ask and show it again.

## 4. Save it in a folder

Save the filled system in `~/my-growth-systems/<system>/`, with the same layout as the blueprint (`README.md`, `skills/<skill>/`). The Windows connector version goes in the same place, under the same system name. Never straight into `~/.claude/skills/`, and never inside this blueprint repo.

- **If that folder already exists:** stop and ask. Offer to compare first. Never overwrite.
- **Check the skill names.** Look for a skill with the same name as each skill in the copy: in `~/.claude/skills/`, the current project's `.claude/skills/`, and the plugins they have installed (`claude plugin list`). The usual cause is their own earlier copy of this system, published or not: then this is an update, so compare and ask, never install a second one. If a different skill has the name, suggest a new one (for example `my-lookalike-campaign`). On a yes, rename the skill folder, the `name:` in its frontmatter and every mention of it in the copy.
- **State folder:** create `~/.growth-systems/<system>/` for run data. It holds real people's names, so it never goes next to the skills and never into a repo.
- Tell the person where the files are.

## 5. First run, together

Run the system once with the person watching, by reading and following the skill files in `~/my-growth-systems/<system>/skills/` in this session, as its SKILL.md says for a first run. Use small numbers (a few people, one company, one week). Ask before every paid step, even inside the caps. Fix the settings with what you learn, and show each change.

## 6. Offer to publish it on GitHub

Ask one simple question: **"Do you want to publish this system on your GitHub?"**

On a yes, you do the work and they approve:
1. Find their repo yourself: run `claude plugin marketplace list` and pick the marketplace that is theirs, or use the repo they name. If they don't have one yet, say the course shows how to set one up, and keep the folder local for now.
2. Add the system the way their repo already does it: read its README or CLAUDE.md and follow it. In a marketplace that usually means a plugin folder for the system and an entry in its marketplace file, with the version bumped in both. If the system is already there, it's an update: change that plugin and bump its version, never add a second one.
3. Show what will be added in plain words (which files, which system), then commit and push after a yes. Keep the repo private: the settings hold their channel names, ids and links.
4. Install or update it from their marketplace, so the skills show up in every session as `<system>:<skill>`.

If GitHub isn't connected (`gh auth status` fails), they sign in themselves, the way the course showed them. If they say no, the folder stays local. It still works: any session can run it by its path ("run the skill in `~/my-growth-systems/<system>/skills/<skill>`"). They can publish later by saying "publish my <system> system on GitHub".

## 7. Schedule it, only on a yes

Offer a schedule only if the README says the system runs on one, and only when the sources it reads are connected. A run that depends on exports or pasted text can't do anything on its own: offer a weekly reminder instead, to drop fresh exports in a folder and run it by hand.

When it fits, offer a scheduled task (the Claude desktop app's scheduled tasks, or a cloud routine where the system allows it). Show the prompt, the day and the time first. The prompt names the skill as installed (`<system>:<skill>`), or by its path if they kept it local, plus the mode. For Notion users it includes the GTM Hub link, so the run finds the context without local memory.

## 8. After the copy

Tell the person in two or three lines:
- what they now have and where (the folder, and the repo if they published),
- what still needs them (a tool to connect, a Clay setup step, a scheduled task they declined),
- how to change it later: "tell me what to change". If it is published, the change goes into their repo and is pushed with a version bump, or the installed copy won't see it. If it is local, the folder is edited directly.

## Rules for the copy

- Plain language, short sentences, no em dashes in anything you write into the skill.
- Keep every safety rule of the blueprint: never send, approval before writes, cost before credits, read-only LinkedIn, caps. The person can loosen a cap in `settings.md`; tell them what it protects first.
- Ids, channel names and links are fine in the copy: it is private to them. Never put them back into this blueprint repo.
- Never write a filled-in copy, run data or anyone's personal details into this blueprint repo.
