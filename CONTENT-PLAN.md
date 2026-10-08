# College Plan — content plan (daily posting)

Goal right now: **followers**. Instagram's strongest signals for reaching new people are **sends (DM shares)**, **saves**, and **Reel watch time**. Every post should be something a parent would send to another parent or save for later. Florida-specific, verified, original, no athletics.

## Weekly calendar (7 feed posts + 4 Reels + 7 Stories)
| Day | Time (ET) | Slot | Template |
|---|---|---|---|
| Mon | 7:30pm | "Don't miss" deadlines | weekly-posts #p1 |
| Tue | 12:00pm | **Reel** (rotation R) | reel/reel-template.html |
| Tue | 7:30pm | Florida school stats (GPA / SAT / ACT / acceptance) | weekly-posts #p2 |
| Wed | 7:30pm | Deep-dive carousel (rotation A) | #p3 + inner slides / ph2 cover |
| Thu | 7:30pm | Photo quote / reframe | photo-posts #ph1 |
| Fri | 12:00pm | **VOICEOVER Reel** (at least 1/week, owner loves these: AI voice + word-by-word captions, 25–40s) | reel/voiceover-reel.html (see templates/README.md "Voiceover Reels") |
| Fri | 7:30pm | Engagement / list post (rotation B) | #p5, growth-posts #rk1, ph2 |
| Sat | 10:30am | Scholarship of the week | growth-posts #sc1 |
| Sun | 7:30pm | Rotation C | ck1 / pr1 / pr2 |
| Thu | 12:00pm | **Trial Reel** (rotation R; shown to non-followers first) | reel template, instagramData type TRIAL_REEL |
| Sun | 12:00pm | **Trial Reel** (rotation R) | reel template, instagramData type TRIAL_REEL |
| Daily | 8:15am | **Story** (rotate st1 deadline countdown / st2 did-you-know / st3 photo reminder; on Wed add an st4 'New post' teaser at 7:45pm) | templates/story-posts.html |

## Rotation A — Wednesday carousels (cycle in order, then repeat with new angles)
1. What admissions looks for now ("It's not 2002 anymore": holistic review, essays, rigor, self-reported grades like UF STARS, test policies — verify each school)
2. Financial aid explainers (FAFSA, FFAA, SAI, net price calculators, CSS Profile)
3. Bright Futures deep-dives (hours, GPA calc, Gold Seal, using it out of state = no)
4. Testing strategy (SAT vs ACT vs CLT, superscoring, dates)
5. Dual enrollment / AP / IB / AICE in Florida
6. Application pieces (essay, recs, activities list, résumé)
7. Campus visits (questions to ask, what to look for)
8. Grade-by-grade roadmaps (8th, 9th, 10th, 11th, 12th)

## Rotation B — Friday engagement / lists
1. Highest-paying college degrees (source: Florida Board of Governors / FL DOE wage outcomes, NACE salary survey — name the dataset + year)
2. Florida schools with the best campus life (cite the ranking source + year, e.g. Niche / Princeton Review; say "according to")
3. Myth vs. fact
4. This or that / which would you pick (comment driver)
5. Florida school superlatives (oldest, biggest, smallest class sizes, most majors — from official data)
6. Quick quiz (answer in caption/comments)

## Rotation C — Sundays
1. Monthly to-do list by grade (first Sunday of each month — ck1)
2. Free cheat sheet promo (pr1)
3. Newsletter promo (pr2)
4. "Week ahead" or seasonal photo post (ph2)

## Voiceover Reels (at least one every week — Friday 12pm)
Faceless, AI voice (en-US-AvaNeural) + big word-by-word captions over soft Florida photos, gold section chips, end card pointing to a tool or the newsletter. Formats that work: "3 [Bright Futures/FAFSA/application] mistakes Florida parents make", "What [UF/FSU/UCF] actually looks for", "Explain [dual enrollment/STARS/the FFAA] in 30 seconds", "If your student is a junior, do these 3 things this month". Script 70–110 words, spell acronyms with spaces for the voice (F F A A), every fact verified. Caption repeats the key points in text + "sound on". isAiGenerated true. A second voiceover can replace a trial Reel when it's a strong topic.

## Trial Reels
Trial Reels are shown only to non-followers first, so use them to test new hooks/formats. Keep the two regular Reels for the strongest ideas. Instagram may move a trial Reel to the profile later if it performs.

## Rotation R — Reels (10–15s, hook in first 2s, big text, end with "Save this + follow")
- "X things to do before [month] ends" · "Florida deadline this week" · "Did you know (scholarship)" · school stat reveal ("UF's middle 50% SAT is…") · myth vs fact flip · "Things I wish I knew in 9th grade" style lists (written as College Plan, no personal persona)
- Render: `python3 templates/reel/render-reel.py file.html out.mp4 13 30` (~1.5 min). Schedule as instagramData type REEL (showReelOnFeed true) + facebookData type REEL.

## Scholarship of the week (Saturday)
Prefer scholarships with an upcoming deadline or that Florida families miss. Mix Florida state programs (Benacquisto, FSAG, José Martí, Rosewood, Mary McLeod Bethune, First Generation Matching Grant, Children of deceased/disabled veterans, Florida Prepaid Project STARS) and national ones with real deadlines (verify the current cycle on the official site). Always: amount, who qualifies, deadline, official source.

## Relatable / funny posts (2 a week — built for shares and tags)
Templates: templates/fun-posts.html — fn1 text thread, fn2 parent "post" quote card, fn3 "what they say vs. what it means", fn4 phone-notes list.
- Thursday alternates: photo quote (ph1) one week, a fun post the next.
- Friday Rotation B includes fun formats every other week.
- Other reshare formats to rotate in: "Senior year parent bingo" card, "This or that" (comment your pick), a 1–10 "parent stress meter" scale, "Things nobody tells you about junior year" lists, POV-style Reels ("POV: it's 11:58pm and the portal is loading").
Rules: original jokes only (never copy memes, tweets or other accounts), warm not mean (laugh with teens, never at a real kid), no fake engagement numbers, tie it back to a real college-planning moment, caption ends with a tag/share ask ("Tag a senior parent", "Send this to your co-parent").

## Website tools (promote them often)
- Bright Futures Checker: collegeplan.beehiiv.com/#bright-futures-checker (home page embed; tools/bright-futures-checker.js — update thresholds when FL DOE publishes new classes)
- Florida College Deadline Calendar: collegeplan.beehiiv.com/#calendar (home page embed; subscribable .ics built from calendar/events.json by scripts/build_ics.py)
- Saturday promo rotation now cycles: cheat sheet (pr1) → newsletter (pr2) → deadline calendar → Bright Futures checker. Build the tool promos in the pr1/pr2 style ("Add every Florida college deadline to your phone" / "Is your student on track for Bright Futures? Check in 30 seconds"). Captions: "Link in bio" (the bio link is the website home page).
- Mention the calendar in the Monday deadlines caption at least every other week, and the checker in Bright Futures posts.

## Calendar upkeep (every Sunday)
Add any newly verified Florida deadlines to calendar/events.json (official source URL required; Florida public universities' EA/RD/materials/decision dates, SAT/ACT/CLT dates and registration deadlines from College Board/ACT, FAFSA/FFAA, Bright Futures, Florida scholarship deadlines). Remove nothing that's still upcoming. Run python3 scripts/build_ics.py, commit, push.

## Big moments (celebration / community posts — schedule the evening of)
- Dec 4: UCF Early Action decisions · Dec 9: USF Early Action decisions · Dec 11: UF Early Decision decisions · Dec 17: FSU ED/EA decisions → "Drop your senior's good news below 🎉" (warm, celebrate every outcome; add a kind line for deferrals/denials)
- May 1: College Decision Day → "Where is your senior headed? 🎓" · Late May/June: graduation congrats post
- Re-verify each date the week before. Add new moments as they're announced.

## County and school-specific posts (1 every other week; local posts get shared in local group chats)
Template: templates/tool-posts.html #cy1–#cy5 (swap county, college, facts). Note: Hillsborough's college is now "Hillsborough College" (hcfl.edu), not HCC.
Rotate counties: Hillsborough (start here), Pasco, Pinellas, Polk, Orange, Miami-Dade, Broward, Palm Beach, Duval, Seminole, Lee, Brevard. Topics: dual enrollment partner college and how to sign up, district college/career fair dates, magnet/AICE/IB program deadlines, district scholarship programs. Verify on the district or college website; name the county in the headline ("Hillsborough parents: ...").

## "Comment a word" posts (manual DMs for now)
- 1–2 posts a week end with "Comment GUIDE and we'll DM you the free cheat sheet" (or another word that fits: LIST, CHECKLIST, DATES). Use it on the Saturday post and at most one other post.
- The owner replies by hand using an Instagram saved reply, so keep the keyword set small: GUIDE (cheat sheet + newsletter link) is the default.
- Mention in the Sunday report which posts use a comment word, so the owner knows to watch those comments.

## Google guides (web-only articles on collegeplan.beehiiv.com, 1 per week, published Wednesday)
Built with scripts/make_guide.py (no email is sent). Evergreen, search-style titles. Update an existing guide instead of repeating a topic.
Queue (in order, skip ones already in the Guides log):
1. FAFSA vs. FFAA: Florida's two financial aid forms explained
2. Florida public university application deadlines 2026–27 (all 12 schools: EA/ED/regular, self-report dates)
3. University of Florida admission stats (Class of 2030) — then one per school: FSU, UCF, USF, FIU, FAU, UNF, UWF, FGCU, New College, FAMU, FPU
4. Florida dual enrollment explained (who qualifies, cost, how credits transfer)
5. Bright Futures service hours: what counts and how to log them
6. The Benacquisto Scholarship explained
7. SAT vs. ACT vs. CLT for Florida students
8. AP vs. IB vs. AICE vs. dual enrollment in Florida
9. Self-reported grades in Florida (UF STARS, SSAR): what they are and when they're due
10. Florida state scholarships and grants list (FSAG, First Generation Matching Grant, José Martí, Rosewood, Mary McLeod Bethune ...)

## Paid products (beehiiv Digital Products, file download)
Status: LIVE since 2026-10-08 (Stripe connected).
- Florida Senior Year Roadmap, Class of 2027: $15, https://collegeplan.beehiiv.com/products/florida-senior-year-roadmap (product f11db4ac-7fa9-493e-b584-ca483fb9c7cf). PDF products/Florida-Senior-Year-Roadmap-Class-of-2027.pdf, card products/senior.png
- Freshman Roadmap: Plan Now, Don't Cram Later: $12, https://collegeplan.beehiiv.com/products/freshman-roadmap (product d98d8883-f0fe-4b35-b864-47118ecd7dac). PDF products/Freshman-Roadmap-Plan-Now-Dont-Cram-Later.pdf, card products/freshman.png
- If a PDF is rebuilt, update the product with save_product(file_url = jsDelivr link pinned to the new commit).
- Rebuild with: python3 templates/products/build.py (check every date against official sources first; refresh the Senior Roadmap each August for the new class).
- Website: home page section "Printable Roadmaps" (anchor /#roadmaps) + a "New: printable roadmaps" link under the hero signup.
- Promo assets: templates/product-posts.html (sr1-5, fr1-5 carousels; rs1-3 Stories), templates/reel/roadmaps-reel.html (voiceover). Renders in instagram/2026-10-roadmaps/.
- Once live: soft-mention in emails at most once a week (seniors email → Senior Roadmap; early email → Freshman Roadmap), one promo post every other week, never pushy. Free resources stay free.

## Newsletter sending (beehiiv Lite plan)
The API can't send on Lite. The Sunday routine saves the 3 weekly emails + the guide as DRAFTS and reminds the owner to click Schedule/Publish. Switch back to auto-send if the plan is upgraded (Scale or higher).

## Guides log (newest first)
- 2026-10-08: Bright Futures guide re-created as a draft (slug florida-bright-futures-requirements-2027-2028-6ad3), owner to publish web-only
- 2026-10-07: Florida Bright Futures Requirements for the Classes of 2027 and 2028 — /p/florida-bright-futures-requirements-2027-2028

## Log (newest first — the weekly routine appends here)
- 2026-10-08: Roadmaps launch scheduled: Story Oct 8 9pm; voiceover Reel Oct 12 12pm; Senior carousel Oct 13 7:30pm + Story 8:45pm; Freshman carousel Oct 15 7:30pm + Story 8:45pm.
- 2026-10-08 Thu LAUNCH BLAST 10:00–11:10am (moved forward from Oct 13–18, so those evening slots are now OPEN for the Oct 11 routine to fill): newsletter promo (pr2), scholarship Benacquisto, myth vs fact FFAA, photo quote group chat, UF stats, checker promo (tl2), FAFSA vs FFAA carousel, NEW welcome/start-here post (wl1 — owner should pin it). Oct 14 7:45pm teaser Story now shows ts2 (checker) since the FAFSA carousel already ran. Still on their original days: Oct 12 deadlines, Oct 13 Reel, Oct 14 Hillsborough, Oct 18 trial Reel.
- 2026-12-04/09/11/17 8:30pm: decision-day posts already scheduled (UCF, USF, UF ED, FSU) — instagram/2026-12-decisions/. Re-verify each release date the week before; if a date moves, update the post in Metricool.
- 2026-10-10 Sat 4pm: VOICEOVER REEL #1 — 3 Bright Futures mistakes (instagram/2026-10-tools/vo-bf-mistakes.mp4)
- 2026-10-18 Sun 12pm: TRIAL REEL — Bright Futures checker demo (instagram/2026-10-tools/checker-reel.mp4)
- 2026-10-15 Thu: 8:15am Story ts3 (Hillsborough info session tonight)
- 2026-10-14 Wed 12pm: COUNTY #1 — Hillsborough dual enrollment carousel (cy1–cy5). Next county post ~Oct 28: Pasco (Pasco-Hernando State College).
- 2026-10-12 Mon 8:15am: Story ts2 (checker)
- 2026-10-11 Sun 12pm: tool promo — deadline calendar (tl1)
- 2026-10-10 Sat 8:15am: Story ts1 (calendar)
- 2026-10-09 Fri 12pm: REEL — Bright Futures checker demo
- 2026-10-09 Fri: fun — text thread (college essay 'the title')
- 2026-10-13 Tue: Reel — 4 things before October ends (UF stats moved to Oct 8 blast)
- 2026-10-12 Mon: deadlines Oct 15–23
- 2026-10-11 Sun: October to-do list (ck1)
- 2026-10-10 Sat: promo cheat sheet (pr1)
- 2026-10-08 Thu: Bright Futures carousel
