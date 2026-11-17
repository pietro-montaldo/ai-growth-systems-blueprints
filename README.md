# AI growth systems blueprints

> **Claude:** if someone gave you this repo's link (or a link to one system's folder) and asked for a system, follow [COPY-GUIDE.md](COPY-GUIDE.md) from the top. It says how to read this repo without them cloning or opening it.

Growth systems from the AI Growth Systems Bootcamp, written as blueprints. They are not a plugin you install. Each one is a folder you read, then ask Claude to copy into your own setup and fill in for your business: your GTM context, your tools, your channels, your limits.

You end up with your own systems, in your own folder (and your own GitHub repo, if you publish them), that you can change whenever you like. Nothing here updates itself, and nothing is shared back.

| System | What it does | Runs | Main tools |
| --- | --- | --- | --- |
| [Website visitors](systems/website-visitors/README.md) | Companies that visited your website, scored against your ICP, with any warm path you have on LinkedIn, in one short daily summary | Daily | A visitor identification tool, Slack or email |
| [Creator signals](systems/creator-signals/README.md) | Buyers found in the comments of LinkedIn creators who speak to your audience, screened, enriched and scored, then sent to LinkedIn messages or a one-off email campaign | Weekly | Apify, Clay, Google Sheets or Excel |
| [Company signals](systems/company-signals/README.md) | A watchlist of companies that look like your best customer, watched for buying signals, with one signer and their work email found when a signal fires | Runs by itself in Clay | Clay |
| [Lookalike campaigns](systems/lookalike-campaigns/README.md) | 100 companies with a work email that would recognise one of your best customers, one decision maker each, and a draft Clay A/B campaign that uses that customer as proof, expanded when it works | Per campaign | Clay |
| [Pipeline review](systems/pipeline-review/README.md) | Last week's inbound, new buyers and every open deal, with the sure CRM changes made and a numbered list of decisions for you | Weekly | Your email, your CRM, your booking tool |

## Before you copy a system

1. **Build your GTM context first.** Every system reads your product, ICP, messaging and customers from the GTM context kit in the [AI-Growth-System-Bootcamp](https://github.com/pietro-montaldo/AI-Growth-System-Bootcamp) repo. The systems never copy that context. They read it fresh on every run, so when your ICP changes, every system changes with it.
2. **Optional: a do-not-contact list** from the do-not-contact plugin in the same repo. If you have one, every system that finds people checks it too. If you don't, nothing is missing: the systems always skip your customers and open deals from your GTM context and CRM.
3. **Optional: your voice skill** from voice-miner, so drafts sound like you.

## How to copy a system

Open Claude Code in any folder (the Code tab of the Claude desktop app works), paste this repo's link and say which system you want. For example:

**"Copy the lookalike campaigns system from https://github.com/pietro-montaldo/ai-growth-systems-blueprints into my setup."**

That's all. You don't need to download this repo or open Claude Code inside it: Claude fetches it to read, and installs nothing from it.

Claude follows [COPY-GUIDE.md](COPY-GUIDE.md). It reads the system's README, finds your GTM context and checks which tools you have connected. It asks you only what it can't find, and shows you the filled-in skills. After your OK it builds them in your own folder, `~/my-growth-systems`, and runs the system once with you.

At the end it asks one simple question: **do you want to publish it on your GitHub?** On a yes, it adds the system to your own repo and marketplace and pushes it, so it's saved and installable on any computer. Last, it offers to schedule the system.

You can copy one system or all of them. Start with one.

## Clay systems need the Clay CLI

The Clay systems in `systems/` are written for the Clay CLI, and that is the version to use. Claude checks your computer and the CLI before copying a Clay system:

- **You have the Clay CLI:** you get the version in `systems/`. Nothing else applies.
- **Mac or Linux without it:** Claude tells you to install it, and can do it for you with Clay's own plugin. Then you get the version in `systems/`.
- **Windows without it:** this is the only case for the fallback in `systems-mcp/`. It works with the Clay connector in Claude plus the Clay Agent inside Clay. Claude drives the Clay Agent in the built-in browser of the Claude desktop app, and you approve each step.

| System | Windows fallback (no Clay CLI) |
| --- | --- |
| Company signals | [systems-mcp/company-signals](systems-mcp/company-signals/README.md) |
| Creator signals | [systems-mcp/creator-signals](systems-mcp/creator-signals/README.md) |
| Lookalike campaigns | [systems-mcp/lookalike-campaigns](systems-mcp/lookalike-campaigns/README.md) |

The Clay Agent is on Clay's Launch, Growth and Enterprise plans. Without it, the fallback walks you through those steps in Clay by hand.

Website visitors needs no fallback: it reads your visitor tool through a connector or a CSV export. With Clay web intent on Windows without the CLI, use a CSV export of the table.

## How each system folder is laid out

```
systems/<system>/          (systems-mcp/<system>/ has the same layout)
  README.md          what it does, how the parts fit, tools, costs, what you decide
  skills/<skill>/
    SKILL.md         the skill, with {{PLACEHOLDERS}} Claude fills in for you
    settings.md      your settings: channels, ids, limits, prices
    references/      the detail the skill reads when it needs it
```

`{{PLACEHOLDERS}}` are the parts that change from one business to the next. Every one is listed in the system's README under "What you decide", with where Claude looks for the answer.

## Rules every system keeps

- **Your context is read, never copied.** The skills fetch your GTM context on every run.
- **Nothing is sent.** Skills draft. You send messages, press Launch in Clay, and publish workflows yourself.
- **Every write waits for a yes.** Every step that spends credits shows the count and the cost first.
- **People data stays on your computer**, in `~/.growth-systems/<system>/`, never inside the skill folder. That way you can share or back up a skill without sharing anyone's name.
- **LinkedIn is read-only and capped low**, so your account stays safe.

## Changing your copy later

Your copy is yours. Tell Claude what to change, for example "in my visitor digest, skip companies under 10 people", or edit the files yourself: `settings.md` for limits, channels and prices, `SKILL.md` for how the system works. If you published it, push the change to your repo the way you push any other change there.

When a run gets something wrong, tell Claude and ask it to add the correction to your skill. That is how a blueprint becomes your system.
