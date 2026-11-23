# Reading and writing each CRM

The steps in `SKILL.md` talk about deals, fields and stages by meaning. This file is how that works in each tool. Each run reads "Every CRM" and the section for the CRM in `settings.md`. During setup, add what you learn about their CRM to its section.

## Every CRM

- **Fetch the schema once per run** before writing: tables, field names, stage and picklist options. Write only values that exist in those options. A missing option is a decision, never a new option made on the fly.
- **Search before every create**, in every table the settings list: email, then LinkedIn, then name, then company.
- **Query with filters** (open stages, changed in the window). Never read a whole table through a connector. A spreadsheet is read whole.
- **Read back every write** at the end of the run with one query, and say in the report if anything didn't land.
- **Never touch** the columns under "Never touch" in `settings.md`, and never delete, archive or merge records.
- **More than about 20 writes:** hand them to a subagent with exact values, then check with a query.
- **Dates** as ISO dates. **LinkedIn links** clean, without tracking parameters.
- **No connector, or it fails:** the changes go in the report as a list ready to apply by hand, and the first line says "CRM not written: <reason>".

## HubSpot

- A deal is three linked records: the **contact**, the **company** and the **deal**. Create or find the contact and company first, then the deal, and associate the deal with both. A deal with no contact is invisible to most HubSpot views.
- Stages belong to a **pipeline**. Use the internal stage ids from the schema, not the labels. Moving a deal to another pipeline is always a decision.
- Last contact and latest communication usually live on the deal as custom properties, or as a **note** on the deal. Ask in setup which one they want. Never log fake emails or calls as activities.
- Owner: in a team portal, filter on the person's owner id and set it on new deals only if the rules say so.
- Stage changes often start **workflows** (sequences, tasks, notifications). Check round 3, question 5.

## Pipedrive

- Deals link to a **person** and an **organization**. Find or create both first.
- Stages belong to a pipeline; use the stage ids from the schema. Won and lost are deal statuses, not stages: set the status, with a lost reason when you set lost.
- Latest communication goes in a **note** on the deal unless they have a custom field. Next step is often an **activity** with a due date: ask in setup.
- Automations on stage changes are common. Check round 3, question 5.

## Salesforce

- Usually **Lead** (not yet qualified) and **Opportunity** (linked to an Account and a Contact). Converting a lead is always a decision.
- Stages are the opportunity's StageName picklist; won and lost are stages with a closed flag. Required fields (close date, amount) may block a create: ask in setup what to put.
- Flows and validation rules may fire. Check round 3, question 5.

## Attio

- People and companies are records; deals are a list or an object linked to them. Find or create the person and company first.
- Stage is a status attribute on the deal or list entry. Use the option ids from the schema.

## Notion

- Each pipeline is a database. Use its data source, fetched once per run for the property names and options.
- Create pages with the database as parent, update pages by id. Dates go in the date property's start.
- Several databases (one per offer) are common: the settings say which offers go where.

## Airtable, Zoho, Close, Monday and others

- Same pattern: find the tables and fields in the schema, match before create, use option values that exist, read back.
- Write their quirks here during setup (required fields, linked records, automations).

## Google Sheets and Excel

- One row per deal. The header row holds the column names from the field map.
- **Back up first,** once per run before the first write: a copy of the tab or file named `<name> backup YYYY-MM-DD`.
- Match on the email column first. Update the row in place. A new deal is a new row at the bottom.
- Stage is a text value from the stage map. Keep their spelling exactly, or a filter they use breaks.
- Never sort, filter, reformat or delete rows. Never touch formulas.
- CSV files: same rules, and the backup is `<name>.backup-YYYY-MM-DD.csv` next to it.
