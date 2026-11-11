# What goes wrong

Read before step 2. Add your own after each run.

- **The seed name is wrong.** A customer's name in conversation is often not its exact name. Confirm the seed by domain.
- **Firmographic lookalikes are not enough.** An industry filter alone pulls in companies that serve a different buyer. A description filter fixes most of it. A company far from the seed's market has no reason to know it: that's why recognition is scored.
- **Only about half survive.** Plan the pull for it.
- **Search limits change with your plan.** Read the quota on the first page and the error text; never assume.
- **Search gives only the company name.** Domains need Enrich Person, headcount needs Enrich Company, and the CLI's Enrich Company accepts only a domain.
- **People hold several current jobs.** Match the role to the company the search found.
- **Clay sometimes returns the social network as the employer.** Blank it and check by hand.
- **One accented LinkedIn link can reject a whole routine batch.** Percent-encode.
- **Routine results come about 20 at a time.** Page through them, or you lose rows.
- **Names carry badges:** letters after a surname, "(HIRING)", an emoji. Clean them before they reach an email.
- **Company names read badly in subjects:** "Inc", taglines after a dash, a trailing "Co." that becomes "Co..". Clean them and show the list.
- **The customer and CRM check can return nothing because it's broken.** Test it on a known customer first.
- **Empty ICP fields look like "not a fit" in Clay.** Write the fit.
- **The second decision maker search returns noise.** Check the picks.
- **Work Email can return an address at another domain.** Fine for the company's other domain, otherwise ask.
- **A person carries one campaign tag.** Tagging moves them off another list and pauses them there.
- **The spam check marks fixed sentences.** A fixed proof sentence can be worth the points.
