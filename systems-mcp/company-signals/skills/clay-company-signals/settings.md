# Settings: company signals (Clay connector + Clay Agent)

One watchlist per copy of this file. The skill writes each Clay id here as soon as the piece exists.

## Choices

- **GTM context:** {{GTM_CONTEXT}}
- **Offer and ICP card:** {{OFFER_AND_CARD}}
- **Watchlist name (the watch field value):** {{WATCHLIST_NAME}}
- **Seed company:** (picked in step 1)
- **Companies to monitor:** {{WATCHLIST_SIZE}}
- **Signer titles:** {{SIGNER_TITLES}}
- **Mode:** list (nobody is emailed). Changes to campaign only in step 7, on your word.
- **Skip a company for:** 90 days after someone there was added
- **Hit alerts go to:** {{NOTIFY}}
- **AI model for the two AI steps:** the intermediate model of the family
- **Clay Agent:** {{CLAY_AGENT}} (yes: Claude types the prompts into the Clay Agent in the built-in browser; no: Claude walks you through the same steps in Clay by hand)

## Prices (data credits; the connector can't read them)

- Enrich Company, per company added: (read in setup)
- Signals, per company per run: (read in Companies, Data hub, Signals after creating them paused)
- Buyer workflow, per hit that reaches the save step: (read with the Clay Agent after the test run)
- Per-hit spend agreed before publishing: (date of your yes)
- Connector spend cap per user: (Clay settings, Agent users)

## Clay ids (filled while building)

Your own ids live here and nowhere else.

| Piece | Id | Created |
| --- | --- | --- |
| Watch field on companies | | |
| "Why fit" and "source" fields on companies | | |
| Watchlist segment | | |
| "Add to watchlist" workflow (connector routine id) | | |
| Signal 1 (and its `sig_` id for the trigger) | | |
| Signal 2 | | |
| Signal 3 | | |
| Buyer workflow | | |
| Buyer list segment | | |
| Campaign (step 7 only) | | |

## Costs seen

| Date | What | Credits |
| --- | --- | --- |
