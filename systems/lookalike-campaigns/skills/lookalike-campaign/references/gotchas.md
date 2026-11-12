# What goes wrong

Read before step 2. Add your own after each run.

- **The seed name is wrong.** A customer's name in conversation is often not its exact name. Confirm the seed by domain.
- **Firmographic lookalikes are not enough.** An industry filter alone pulls in companies that serve a different buyer. A description filter fixes most of it. A company far from the seed's market has no reason to know it: that's why recognition is scored.
- **Only about 1 in 4 searched companies passes the bar.** Plan about 4 candidates per company wanted, and set the target on companies with a work email, not on candidates.
- **Search limits change with your plan.** Read the quota on the first page and the error text; never assume.
- **A people search gives only the company name.** That's why the search starts from companies. In the people-first flow, domains need Enrich Person, and the CLI's Enrich Company accepts only a domain.
- **People hold several current jobs.** Match the role to the company the search found.
- **Clay sometimes returns the social network as the employer.** Blank it and check by hand.
- **One accented LinkedIn link can reject a whole routine batch.** Percent-encode.
- **Routine results come about 20 at a time.** Page through them, or you lose rows.
- **Names carry badges:** letters after a surname, "(HIRING)", an emoji. Clean them before they reach an email.
- **Company names read badly in subjects:** "Inc", taglines after a dash, a trailing "Co." that becomes "Co..". Clean them and show the list.
- **The customer and CRM check can return nothing because it's broken.** Test it on a known customer first.
- **Empty ICP fields look like "not a fit" in Clay.** Write the fit.
- **The decision maker search returns noise:** chapter volunteers, board members, members, assistants, a membership tier written as a job. Filter those titles and check every pick.
- **Titles carry extras.** "CEO | Speaker" is a CEO; judge only the first part. "Head of Partnerships" and "Chief of Staff" look like leaders and aren't.
- **Short employer names match everything.** A blank or 2 to 3 letter name never matches a company.
- **Re-running a step can undo your work.** Re-running the people search keeps the contacts already found, and a dropped company stays dropped when the list is rebuilt.
- **Employer names on profiles differ from Clay's company names.** Map the unmatched ones to their domain by hand.
- **Work Email can return an address at another domain.** Fine for the company's own other domain. An address at another business (the founder's other company) drops the company.
- **A person carries one campaign tag.** Tagging moves them off another list and pauses them there.
- **The spam check marks fixed sentences.** A fixed proof sentence can be worth the points.
- **People are not linked to their companies unless the routine links them.** The Company column in Clay stays empty even with the company name written on the person. Upsert the company first, link the person to it, and check that no one on the list is unlinked.
- **The company's location is not the person's.** Writing the company's city on the person leaves the person's own City, State and Country empty. Map the person's location from the search or Find People result onto the person's fields, in the same routine.
- **Records are thin without Enrich Company.** The search gives a size bucket and a location string; website, city, exact headcount and founding year come from Enrich Company on every company.
- **Broad searches bury the best fits.** A second round of narrower searches, split the way the seed's world divides, can find many more. Pick the split that fits the seed.
- **Find company lookalikes follows Clay's industry.** It charges per result and matches on industry, topic and size, so a seed filed under the wrong industry gets the wrong kind of company back. It is still step one: read a batch of 10, then fix the seed set and keywords. Competitor lookups mostly confirm names you have.
- **Communities and networks count members as staff** in Clay. Exact headcount over the max can't be a hard rule for them.
- **Find People at Company finds a leader at only a few companies** and doesn't skip people already on campaign lists.
- **Enrich Company can resolve to a sister company.** Check the returned name.
- **The seed's own group looks like perfect lookalikes.** Exclude its parent and sister brands.
- **A build can start from another session.** Read the run folder and the draft campaigns in Clay before building, and update a draft rather than create a second.
