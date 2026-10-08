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
| Fri | 12:00pm | **Reel** (rotation R) | reel template |
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

## Trial Reels
Trial Reels are shown only to non-followers first, so use them to test new hooks/formats. Keep the two regular Reels for the strongest ideas. Instagram may move a trial Reel to the profile later if it performs.

## Rotation R — Reels (10–15s, hook in first 2s, big text, end with "Save this + follow")
- "X things to do before [month] ends" · "Florida deadline this week" · "Did you know (scholarship)" · school stat reveal ("UF's middle 50% SAT is…") · myth vs fact flip · "Things I wish I knew in 9th grade" style lists (written as College Plan, no personal persona)
- Render: `python3 templates/reel/render-reel.py file.html out.mp4 13 30` (~1.5 min). Schedule as instagramData type REEL (showReelOnFeed true) + facebookData type REEL.

## Scholarship of the week (Saturday)
Prefer scholarships with an upcoming deadline or that Florida families miss. Mix Florida state programs (Benacquisto, FSAG, José Martí, Rosewood, Mary McLeod Bethune, First Generation Matching Grant, Children of deceased/disabled veterans, Florida Prepaid Project STARS) and national ones with real deadlines (verify the current cycle on the official site). Always: amount, who qualifies, deadline, official source.

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

## Guides log (newest first)
- 2026-10-07: Florida Bright Futures Requirements for the Classes of 2027 and 2028 — /p/florida-bright-futures-requirements-2027-2028

## Log (newest first — the weekly routine appends here)
- 2026-10-18 Sun: promo newsletter (pr2)
- 2026-10-17 Sat: scholarship — Benacquisto
- 2026-10-16 Fri: myth vs fact — Bright Futures FFAA
- 2026-10-15 Thu: photo quote — group chat
- 2026-10-14 Wed: carousel — FAFSA vs FFAA (Rotation A #2)
- 2026-10-13 Tue: UF stats; Reel — 4 things before October ends
- 2026-10-12 Mon: deadlines Oct 15–23
- 2026-10-11 Sun: October to-do list (ck1)
- 2026-10-10 Sat: promo cheat sheet (pr1)
- 2026-10-08 Thu: Bright Futures carousel
