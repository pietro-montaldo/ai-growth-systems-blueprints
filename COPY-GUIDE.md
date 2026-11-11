# Copy guide

Claude follows this guide when someone asks to copy a system from this repo into their own setup. The blueprint stays untouched. The copy is theirs.

## 1. Read before asking

1. **The system's README.** Read `systems/<system>/README.md` in full, then every `SKILL.md`, `settings.md` and reference file of that system.
2. **GTM context.** Look in `~/.claude/CLAUDE.md` for a block between `gtm-context:start` and `gtm-context:end`.
   - A Notion Hub link: fetch the Hub, then only the pages this system needs (the README says which).
   - A repo and `~/gtm-context`: read `~/gtm-context/gtm/README.md`, then the pages it links.
   - Neither: say once that the system works much better with the GTM context kit, and recommend building it first. If they want to go on anyway, use their own source files as the context: a `COMPANY-PROFILE.md`, their website pages, their notes. `{{GTM_CONTEXT}}` then points at those file paths, and the skill reads them at run time like the context. Without ICP cards, fit is a one-line judgment against who buys, marked "no ICP cards". If there are no files either, ask the 3 or 4 questions the system needs (what you sell, who buys, who signs) and offer to save the answers to `COMPANY-PROFILE.md` next to the copy.
3. **Do-not-contact (optional).** Look for a block between `do-not-contact:start` and `do-not-contact:end` in `~/.claude/CLAUDE.md`. If it is there, the copy uses it. If not, carry on without it: don't warn, don't mark rows, don't ask them to build one. Customers and open deals are always checked from the GTM context and CRM either way.
4. **Voice.** Look for an installed `<name>-voice` skill.
5. **Tools and sources.** Check which connectors and CLIs the README lists are connected (for Clay: `clay whoami`). Note what is missing and what the fallback is (an export, a pasted thread, a CSV). Look at the real data the system will read, not just its name: a client spreadsheet is not a pipeline, and an export has an end date.

Never copy the GTM context into the skill. The skill reads it at run time. What the copy holds is only how to find it (the Hub link or the repo path) and the settings.

## 2. Fill the gaps in one batch

Go through the README's "What you decide" table. Some placeholders are maps (stage names, field names, tables): fill every row, don't leave a default that was never checked. For each placeholder:

- Fill it from what you read in step 1 when you can, and say where it came from.
- Use the default when the table gives one and nothing better exists.
- Otherwise add it to one list of questions.
- When their tool is missing something the system needs (a column, a stage, a field), propose adding it as part of the questions. Add it only on a yes, and back up a file before changing it.

Ask the questions once, in one message, in plain words. Recommend an answer for each when you can. Never ask where to save the copy: see step 4.

## 3. Show the copy before saving

Fill every `{{PLACEHOLDER}}` in the files under `skills/`. Copy the system README too, but replace its "What you decide" table with a short "My answers" list (each placeholder, the value, and where it came from), so the README itself has no placeholders left. Then:

1. Search the filled files for placeholders: `grep -rnE "\{\{[A-Z_]+\}\}"`. None may be left. Clay tokens such as `{{lead:...}}` and `{{spintax:...}}` are part of the skill and stay. If a placeholder can't be filled, ask.
2. Remove the "Adapting this skill" section only if the person says so. It helps later edits.
3. Show the person, per skill: the filled frontmatter `description`, the settings, and any rule you changed. Keep it short. Offer the full files on request.
4. Wait for an OK. Change what they ask and show it again.

## 4. Save it in a folder

Save the filled system in `~/my-growth-systems/<system>/`, with the same layout as the blueprint (`README.md`, `skills/<skill>/`). Never straight into `~/.claude/skills/`, and never inside this blueprint repo.

- **If that folder already exists:** stop and ask. Offer to compare first. Never overwrite.
- **State folder:** create `~/.growth-systems/<system>/` for run data. It holds real people's names, so it never goes next to the skills and never into a repo.
- Tell the person where the files are.

## 5. First run, together

Run the system once with the person watching, by reading and following the skill files in `~/my-growth-systems/<system>/skills/` in this session, as its SKILL.md says for a first run. Use small numbers (a few people, one company, one week). Ask before every paid step, even inside the caps. Fix the settings with what you learn, and show each change.

## 6. Offer to publish it on GitHub

Ask one simple question: **"Do you want to publish this system on your GitHub?"**

On a yes, you do the work and they approve:
1. Find their repo yourself: run `claude plugin marketplace list` and pick the marketplace that is theirs, or use the repo they name. If they don't have one yet, say the course shows how to set one up, and keep the folder local for now.
2. Add the system the way their repo already does it: read its README or CLAUDE.md and follow it. In a marketplace that usually means a plugin folder for the system and an entry in its marketplace file, with the version bumped in both.
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
