# Setup, first run and schedule

## 1. Connect the visitor tool

| Tool | How the digest reads it |
| --- | --- |
| Clay web intent | The web intent table, through the Clay CLI or connector. Note the table id and the column ids for session, company, domain, pages and time in `settings.md`. |
| RB2B, Dealfront, Warmly, Apollo, HubSpot | Their connector if you have one. Otherwise a daily or weekly CSV export into the exports folder. |
| Anything else | A CSV export with at least: company name, domain, visit time, pages. Time on page and source are a bonus. |

Read a sample of 5 sessions with the person and check every field the steps use is there. Write what each field is called in `settings.md` under "How to read it".

## 2. The destination

- **Slack:** one channel, by name and id. Send a one-line test only after a yes.
- **Email:** the person's own address only, as a draft or a note to self.
- **Chat only:** no setup.

## 3. LinkedIn tool (optional)

If one is connected, map its call names to the five allowed reads in `linkedin.md`, and write them in `settings.md`. Show the caps and say what they protect. If none is connected, set `linkedin.tool` to `none`.

## 4. First run, together

Run Look mode for the last 7 days. Check with the person: are the companies real, are the fits right, is the next step useful? Fix `scoring.md` or the settings with what you learn. Then run Daily digest once.

## 5. Schedule

Offer a daily scheduled task (morning, before the person starts work) that runs this skill in Daily digest mode. Show the prompt first. For Notion users, put the GTM Hub link in the prompt.
