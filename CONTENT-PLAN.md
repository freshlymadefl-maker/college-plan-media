# College Plan — content plan (daily posting)

Goal right now: **followers**. Instagram's strongest signals for reaching new people are **sends (DM shares)**, **saves**, and **Reel watch time**. Every post should be something a parent would send to another parent or save for later. Florida-specific, verified, original, no athletics.

## What makes College Plan different (owner, Oct 9) — every post should hit at least two
1. **Funny + relatable** (parents laugh, tag, send). 2. **Educational** (save-worthy). 3. **Florida-specific** (Bright Futures, FFAA, our schools, our counties). 4. **Time-sensitive** (what's due now). Growth = engagement + entertainment: every feed post ends with ONE easy action (vote, comment a word, tag, send, save). Lots of pages cover college planning; ours wins by being the fun, Florida, right-now one.

## DATA CHECK Oct 13 — what is actually working (read this before planning anything)
First week of numbers (Oct 7–11, Metricool): followers 10 → 23. Daily reach 1,480 (Oct 8) → 331 → 126 → 13 (Oct 11).
- **Feed photos and carousels reached 1–14 accounts each** (basically only our followers) and brought in 2 follows total across 18 posts. On TikTok, every photo post shows 0 views; videos got 13–46.
- **What reached new people = funny, relatable Reels with real people in them** (the owner's credited reposts): 1,234 reach at 77% view rate, then 130–165 each. These are 90%+ of our reach.
- **Our own Reels lost people in 2–3 seconds** (Bright Futures mistakes: 116 reach, 2.6s average watch, 12% view rate; checker: 13 reach, 8%). They opened like an ad (info first, hook faded in, 13–40s long).
So, until the account has real reach: **Reels first, funny first, hook on frame 0, short.** Feed carousels drop to 3 a week (Showdown, scholarship, one time-sensitive/local carousel). Paid-product carousels go out at most every other week (they reach nobody yet) — the Oct 13/15 roadmap carousels were moved to Metricool DRAFTS (Oct 25 + Nov 1) for later. Re-check these numbers every Sunday (Metricool IGPO14 reach, IGRE11/IGRE23/IGRE24/IGRE28 for Reels, TKPO07 TikTok views) and log them below.

## Weekly calendar (3 feed carousels + 10–11 Reels + 7 Stories) — updated Oct 13 after the data check
Owner's rule (Oct 9): feed posts go out in the MORNING at 7:00am; Reels go out in the EVENING at 6:00pm. Nothing at midday or 7:30pm anymore (decision-day posts keep their release-night times).
**Spacing rule:** max ONE feed post per day and at least 4 hours between any two Instagram posts (Stories excepted). Never batch-post several feed posts in one sitting again (the Oct 8 launch blast split reach 8 ways). A big moment gets its own day, or replaces that day's slot.
| Day | Time (ET) | Slot | Template |
|---|---|---|---|
| Mon | 7:00am | **FUNNY native Reel** (group chat / texting / POV / translation) | reel/native-reel.html |
| Mon | 6:00pm | "Due this week" native list Reel (hook on frame 0, real campus photo) | reel/native-reel.html |
| Tue | 7:00am | **FUNNY native Reel** | reel/native-reel.html |
| Tue | 6:00pm | School stat reveal native Reel (real school photo, "UF's middle 50% SAT is…") | reel/native-reel.html |
| Wed | 7:00am | CAROUSEL: Rotation A deep-dive OR county post (time-sensitive/local wins) | weekly-posts #p3 / tool-posts cy1–cy5 |
| Wed | 6:00pm | Reel (rotation R, native style) | reel/native-reel.html |
| Thu | 7:00am | **FUNNY native Reel** | reel/native-reel.html |
| Thu | 6:00pm | **Trial Reel** (test a new hook/format on non-followers) | native-reel, instagramData type TRIAL_REEL |
| Fri | 7:00am | **SCHOOL SHOWDOWN** carousel | templates/showdown-posts.html (sd1–sd6) |
| Fri | 6:00pm | VOICEOVER Reel (max 30s, hook text on frame 0, no preamble — cut "here are 3 things…") | reel/voiceover-reel.html |
| Sat | 7:00am | Scholarship of the week CAROUSEL | growth-posts #sc1 |
| Sat | 6:00pm | **FUNNY native Reel** (campus-photo POVs work: tours, dorms, college towns) | reel/native-reel.html |
| Sun | 7:00am | Relatable Reel (bingo, stress meter, this-or-that) — every other week a paid-product carousel instead | reel/native-reel.html (bingo) |
| Sun | 6:00pm | **Trial Reel** | native-reel, TRIAL_REEL |
| Daily | 8:15am | **Story** (st1 countdown / st2 did-you-know / st3 photo; product + tool mentions go here) | templates/story-posts.html |
| TikTok | 9:30am / 8:00pm | Cross-posts of the Reels + Showdown/scholarship as slideshow VIDEOS (never photo posts), max 3/day | weekly TikTok task |
Spacing rule still holds: at least 4 hours between Instagram posts (Stories excepted); never batch.

## Format mix (rewritten Oct 13 from OUR data, replaces the industry-benchmark version)
Industry roundups say carousels win on engagement, but for an account our size Instagram shows carousels almost only to followers (ours reached 1–14 each). Reels are the only thing that reaches non-followers. So: 10–11 Reels + 3 carousels a week until we pass ~1,000 followers, then re-test. Every winning carousel still gets remixed into a Reel. Instagram (per Adam Mosseri) may re-show a carousel starting on SLIDE 2, so slide 2 must work as a second cover.

## Native Reels (Oct 13) — the default Reel style now
Engine: templates/reel/native-reel.html + one config per Reel in templates/reel/native/<name>.js (see the 8 examples: gc-october = group chat, texting-deadline = texting your senior, translations = says vs. means, tour-weather = photo POV with cuts, bingo = card that stamps itself, oct-4things / bf2028 / checker = hook + list over a real photo).
Render: `python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=<name>" out-silent.mp4 <secs> 30 && python3 scripts/add_music.py out-silent.mp4 out.mp4` (~1 min). Preview frames first with Playwright (setT(ms)) and LOOK at them.
Rules (from what worked):
1. **The hook is fully on screen on frame 0** (no fade-in, no logo intro, no blank first second). It is also the cover/thumbnail.
2. **7–10 seconds total.** Something new every ~1 second (a text bubble, a sticker, a photo cut). Short Reels get rewatched, which counts.
3. **Funny or relatable first, the fact second.** Write it like a parent would text it: lowercase is fine, emoji fine, real situations (portal refreshing, "basically done", the group chat, 91° campus tours). Facts stay verified and go in the caption.
4. **Looks like a person made it, not a brand:** native caption stickers, chat bubbles, real photos that slowly zoom. No navy slide decks for Reels.
5. End with ONE ask on screen: "Send this to your group chat", "Tag your co-parent", "Save this".
6. Real school photos only from photos/commons (credit in caption). Library music via audioConfiguration with videoVolume 0, our baked track for FB/TikTok.
7. Faces win. Whenever the owner sends a 3–10 second clip of herself (reaction, eye-roll, "me reading the FAFSA instructions"), use it as the Reel background with text on top instead of a photo.

## First comment (Oct 9 — owner request)
Every feed post and Reel gets a scheduled first comment from @college.plan via Metricool's firstCommentText field. It goes up the moment the post publishes and gives people an easy place to jump in. Make it a short, playful prompt that matches the post, never a repeat of the caption: Showdowns repeat the vote words plus a bonus question ("Vote here 👇 SWAMP or DOAK? Bonus points for your best game-day memory 🏟️"); quizzes say "No peeking! Drop your score 👇"; info posts ask one easy question ("What grade is your student in? 👇"); GUIDE posts say "Comment GUIDE here and we'll DM you the cheat sheet 📩". Never invent fake replies or pretend to be a parent. (Metricool can't schedule replies to other people's comments, since those don't exist yet. The owner replies by hand.)

## Guess the Florida campus (fun quiz format — owner: keep it to ONE photo)
templates/weeks/2026-10-09-guess-the-campus-v2.html: 3 slides only: (1) cover "Guess the Florida campus" over a BLURRED version of the photo with a big "?", (2) the real Commons photo (no name, sign or logo visible) + "Which campus is this?" + 4 choices A–D, (3) "Comment your guess" with the 4 choices + "answer in our Story tomorrow" + credits. No answer slide. Next day at 12:00pm, post an answer Story (1080x1920, #ans in the same file). First comment: "Lock in your guess 👇 A, B, C or D?". Use about once a month in the Thursday or Sunday slot, or as a bonus evening post. The answer comes from the photo's Commons title/description.

## Carousel rules (the cover decides everything)
Cover slide (slide 1) must pass the "would a Florida parent stop scrolling?" test:
1. ONE big line, max ~8 words, readable at thumbnail size. Lead with the payoff or the stakes, not the topic. ("Bright Futures just got harder to get" beats "Bright Futures update".)
2. Make it specific to them: a grade/class year ("Class of 2028 parents"), a Florida name (UF, Bright Futures, FFAA, their county), or a number/$ ("100% of tuition", "3 mistakes", "Oct 15").
3. Open a loop the swipe closes: a mistake, a myth, a surprising stat, "what nobody tells you", "before [deadline]".
4. A clear swipe cue: an arrow/"Swipe →" chip, or an element running off the right edge.
5. No clutter: wordmark small, no paragraphs, high contrast; photo covers need a dark overlay behind the text.
Slide 2 = second cover (it's what re-shown carousels open on): restate the hook as a promise ("Here's exactly what changed for the Class of 2028") plus the first useful fact. Middle slides: one idea per slide, big text, numbered. Last slide: save/send ask + "Free newsletter, link in bio". Aim for 6–10 slides. Write 3 cover options for every carousel and pick the strongest; note the runner-up in the Log so a later Reel or trial Reel can test it.
Note: Instagram suggests carousels with music can reach more people, but Metricool cannot attach music to carousels, so scheduled carousels go out without it. That is fine.

## School Showdowns (Fridays, Oct 9) — built for comments
Pit two Florida schools against each other on something seniors actually care about, then ask people to vote by commenting one word. Opinion is the fun part; every FACT on the slides is verified on each school's official site (athletics site for stadium facts, admissions/housing/student-life pages for the rest) and the source is named on the slide.
- Build with `python3 scripts/build_showdown.py showdowns/<date>-<a>-<b>-<topic>.json` (see the 4 configs in showdowns/ for the format; it writes the HTML + sd1–sd6 PNGs + preview.jpg). LOOK at preview.jpg before scheduling.
- Topic bank (owner, Oct 9: "doesn't have to be game day"): Greek life (sororities/frats), pre-med / future doctors, nursing, engineering, business school, dorms, dining hall / cafeteria, clubs & extracurriculars, campus life, rec center, honors college, study abroad, college town, beach/outdoors access, prettiest campus, traditions, homecoming, cost, distance from home, internships/co-ops, campus size.
- Different angles to rotate in: "Guess the Florida campus" (one real photo, answer on slide 2 / in comments), bracket tournaments over several weeks ("Florida's best college town"), "Parent pick vs. teen pick" (two answers per side), "Underrated vs. famous" (a smaller school vs. a big name on one strength), "Big school vs. small school", "In-state vs. private" (UM, Stetson, Rollins, Eckerd), and "Would you rather" campus-life choices.
- Topics: game-day atmosphere, college town (Gainesville vs Tallahassee), dorms, dining hall, prettiest campus, beach/outdoors access, school traditions, homecoming, study spots, campus size, distance from home ("2 hours from Tampa"), cost (in-state tuition, from official sites), honors college, study abroad.
- Matchups (rotate, don't repeat a pair within 6 weeks): UF vs FSU, UCF vs USF, FIU vs FAU, UNF vs UWF, FGCU vs New College, FAMU vs FSU (same city!), UF vs UCF, USF vs FSU, plus "state school vs private" (e.g. UM, Stetson, Rollins) once in a while. Bracket weeks around big moments (e.g. "Florida's best college town" bracket over 4 Fridays).
- Layout (templates/showdown-posts.html): sd1 split-photo cover with VS + one-line question (max ~8 words); sd2 second cover; sd3/sd4 one school each with a big verified stat + 2–3 verified bullets + source; sd5 vote slide with two one-word comment answers (e.g. SWAMP / DOAK); sd6 save + follow + photo credits + "College Plan is not affiliated with these schools".
- Caption: the question as the hook line, "Comment SWAMP or DOAK 👇", one line tying it to planning (campus visits, applying), "Free newsletter, link in bio", hashtags, then a "Photo credits:" line repeating the credits.
- Follow-up: the next Monday 8:15am Story can announce the winner by comment count (count comments with Metricool analytics/the post if available; otherwise skip the result).
- Game day / school spirit is OK here as CAMPUS LIFE. Still never: recruiting, athletes, team records/rivalry trash talk, betting, or logos used as graphics.

## Real school photos (Oct 9)
For posts about a real school, use REAL photos (never AI images of real campuses). Get them with the "Find photos" GitHub Action: push photoreq/<name>.txt with lines "<slug> | <search terms> | <max>" (e.g. "ucf-campus | University of Central Florida campus | 6"), wait ~90s, git pull, then LOOK at photos/commons/<slug>/contact.jpg and pick the best (packed stadiums, sunny campus icons, people having fun). Every photo is from Wikimedia Commons under a license that allows reuse with credit (CC0/public domain/CC BY/CC BY-SA, listed in credits.json). Credit each one used on the last slide AND in the caption: "Title" by Artist (License), and note "text added". Prefer sharp, well-lit, crowd-filled photos; skip blurry, empty, or construction shots. Photos already fetched: uf-stadium, fsu-stadium, uf-campus, fsu-campus.

## Doodles on every new post (owner, Oct 12: "add cute graphics like these to all our posts")
Hand-drawn doodles (templates/doodles/: star, squiggle, burst, heart, plus, dots × gold, navy, orange, coral, mist, blue; preview templates/doodles/index.html; rules in templates/doodles/README.md). Every new carousel slide, Story and native Reel gets 2–5 of them, placed in the HTML (`<img class="dd" src="../doodles/<name>.svg" style="left/top/width/rotate">`, or the `doodles` array in a native Reel config) — ONLY in empty space: never over text, faces, numbers or the swipe chip. Vary colors (orange/coral/gold on light backgrounds, gold/mist on navy and photos). build_showdown.py adds them automatically. For an already-rendered PNG: `python3 scripts/add_doodles.py in.png out.png 3` and LOOK at the result.

## Collab posts
See COLLABS.md (who to pitch, offers, DM templates, tracker). When a partner has agreed (listed as "Agreed" in the COLLABS.md tracker with a verified @handle), build the Collab post in that week's matching feed slot and schedule it with instagramData.collaborators [{"username":"<handle>","deleted":false}]. Put "with @handle" on the cover slide. Never add a collaborator who hasn't agreed.

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

## Voiceover Reels (at least one every week — Friday 6pm)
Max 30 seconds, the hook line big on frame 0 and no spoken preamble (start at "Number one…"; Oct 13 data: 38s voiceovers averaged 2.6s watched). Faceless, AI voice (en-US-AvaNeural) + big word-by-word captions over soft Florida photos, gold section chips, end card pointing to a tool or the newsletter. Formats that work: "3 [Bright Futures/FAFSA/application] mistakes Florida parents make", "What [UF/FSU/UCF] actually looks for", "Explain [dual enrollment/STARS/the FFAA] in 30 seconds", "If your student is a junior, do these 3 things this month". Script 70–110 words, spell acronyms with spaces for the voice (F F A A), every fact verified. Caption repeats the key points in text + "sound on". isAiGenerated true. A second voiceover can replace a trial Reel when it's a strong topic.

## Trial Reels
Trial Reels are shown only to non-followers first, so use them to test new hooks/formats. Keep the two regular Reels for the strongest ideas. Instagram may move a trial Reel to the profile later if it performs.

## Rotation R — Reel topics (build them as NATIVE Reels: 7–10s, hook on frame 0 — see "Native Reels")
- "X things to do before [month] ends" · "Florida deadline this week" · "Did you know (scholarship)" · school stat reveal ("UF's middle 50% SAT is…") · myth vs fact flip · "Things I wish I knew in 9th grade" style lists (written as College Plan, no personal persona)
- Render with the native engine (see "Native Reels"); the old reel-template.html slide style is retired for new Reels (it lost viewers in 2–3s). Schedule as instagramData type REEL (showReelOnFeed true) + facebookData type REEL.

## Music (Oct 9 — owner: "add music whenever possible, never on voiceover Reels")
Two layers for every Reel/TikTok video WITHOUT a voiceover:
1. **Baked-in music (all platforms).** templates/reel/render-reel.py now mixes one of our own original tracks into the video automatically (templates/reel/music/: sunny, breeze, bright — made by scripts/make_music.py, so no licensing issues; rotates by file name; pass a track name as the 5th arg to choose, or "none" to skip). For an existing silent video: `python3 scripts/add_music.py in.mp4 out.mp4 [track]`. This is what Facebook Reels and TikTok videos play.
2. **Instagram library track (Instagram only).** Also attach instagramData.audioConfiguration {"audioId": "<numeric id>", "videoVolume": 0} — videoVolume 0 mutes our baked track on Instagram so only the library song plays (library audio links the Reel to that song's audio page = extra discovery). To find a track, send a search term as audioId (e.g. "upbeat acoustic", "happy instrumental", "chill lofi"); Metricool rejects it with candidate tracks; pick an upbeat, warm INSTRUMENTAL and retry with its numeric id. Rotate; don't reuse a track two weeks running. Used so far: 901455037857983 It's A Vibe, Giulio Cercato (Oct 14 Reel); 761736589642441 Be Happy (Instrumental), Afro Sound Machine (Oct 15 trial Reel); 989564276265815 Dancing In The Sun (Instrumental), Giulio Cercato (Oct 13 Reel); 1375070527788441 Cool Water (Instrumental), Afro Sound Machine (Oct 18 trial Reel). Added Oct 13: 622819303274042 Good Time, Alex Blue (Oct 13 7am); 1326560949104401 Check This Out, Giulio Cercato (Oct 15 7am); 4283034138460390 Splash, The K Club (Oct 17 6pm); 1386811643506297 Home, Giulio Cercato (Oct 18 7am). Search "feel good" also returned 1579921342191993 Motive (Instrumental), 1347176186322399 Do Ma Thing, 1826195528219317 Take And Bake. Other good candidates: 1274149560124013 Heros Journey (Instrumental), 209500281934992 Droplets Of Light, 948458014167219 Dandelion (Instrumental).
- Trending + clean (owner, Oct 9): songs WITH lyrics are fine, just never explicit. Use the most current-sounding, popular-style track you can find (vocal or instrumental). Checked Oct 9: the Metricool/Instagram music search only reaches Instagram's business-cleared library (a search for a chart hit like "Espresso" returns only library tracks) and shows no "trending" or explicit labels, so chart-topping songs can't be attached automatically and explicit content can't be filtered by a flag. So skip any track whose title or artist suggests explicit/adult content, profanity, drinking/partying, or "(Explicit)"/"(Dirty)" labels; when in doubt pick another. Keep it warm and family-friendly. Search terms that work: "upbeat pop", "feel good", "happy", "summer pop", "upbeat acoustic".
- TikTok photo posts: tiktokData autoAddMusic true (TikTok rejects it on videos — videos rely on the baked track).
- NEVER add music of either kind to voiceover Reels (render-fast.py with the voice mp3; never run add_music.py on them; no audioConfiguration).
- Carousels/single images on Instagram and Facebook can't get music through Metricool or the API; they go out without it.

## Scholarship of the week (Saturday)
Prefer scholarships with an upcoming deadline or that Florida families miss. Mix Florida state programs (Benacquisto, FSAG, José Martí, Rosewood, Mary McLeod Bethune, First Generation Matching Grant, Children of deceased/disabled veterans, Florida Prepaid Project STARS) and national ones with real deadlines (verify the current cycle on the official site). Always: amount, who qualifies, deadline, official source.

## Relatable / funny posts (4–5 a week, mostly as native Reels — built for shares and tags)
Templates: templates/fun-posts.html — fn1 text thread, fn2 parent "post" quote card, fn3 "what they say vs. what it means", fn4 phone-notes list.
- Thursday alternates: photo quote (ph1) one week, a fun post the next.
- Friday Rotation B includes fun formats every other week.
- Other reshare formats to rotate in: "Senior year parent bingo" card, "This or that" (comment your pick), a 1–10 "parent stress meter" scale, "Things nobody tells you about junior year" lists, POV-style Reels ("POV: it's 11:58pm and the portal is loading").
Rules: original jokes only (never copy memes, tweets or other accounts), warm not mean (laugh with teens, never at a real kid), no fake engagement numbers, tie it back to a real college-planning moment, caption ends with a tag/share ask ("Tag a senior parent", "Send this to your co-parent").

## Website tools (promote them often)
- Bright Futures Checker: collegeplan.beehiiv.com/bright-futures-checker (home page embed; tools/bright-futures-checker.js — update thresholds when FL DOE publishes new classes)
- Florida College Deadline Calendar: collegeplan.beehiiv.com/calendar (home page embed; subscribable .ics built from calendar/events.json by scripts/build_ics.py)
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

## Etsy products (sold in the FreshlyMadeFL Etsy shop, College Plan branded) — added 2026-10-14
Why Etsy too: Etsy search brings buyers who have never heard of College Plan, and every download includes a link back to the newsletter. Social posts send our own audience to the Etsy listing (sales + reviews help it rank in Etsy search).
- College Application Tracker (Excel + Google Sheets): $8.99, LIVE: https://www.etsy.com/listing/4595734726. Files + listing text: ~/college-kit (spreadsheet, College_Tracker_Guide.pdf, photos 01–07). National (not Florida-specific), so it fits any senior family. Guide tab info "checked October 2026"; re-check each August.
- Scholarship Tracker (Excel + Google Sheets): $8.99, Etsy listing URL: TBD (owner publishing). Files: ~/scholarship-kit. Guide tab: where to look, scam warning signs (FTC: reportfraud.ftc.gov), tips, words to know. Checked October 2026. Promo idea: "scholarship money adds up" Reel + pins once live.
- Brand: Etsy graphics for College Plan products use the College Plan look (navy #0B2A4A, blue #5B8DC9, sky gradient, gold #B5A21F, Poppins + Lora italic accent word, gold sparkles/arc, wordmark), NOT the FreshlyMadeFL pastel style.
- Promo assets: instagram/2026-10-tracker/ (tracker-reel.mp4 = native Reel "where my senior's college deadlines live right now", AI campus background so isAiGenerated true; story-tracker.png = Story with empty space for a LINK STICKER; tracker-scene.png = 1080x1920 tracker background for future Reels). Config: templates/reel/native/tracker.js.
- How they fit the calendar (same rules as the roadmaps, products never crowd out free value):
  1. Reels: at most ONE product Reel a week, and it must be funny/relatable first (the product is the punchline, not the hook). Ends with "link in bio".
  2. Stories: one product Story a week in the 8:15am slot. Stories with a link sticker MUST be scheduled with autoPublish false (Instagram's API can't add link stickers): Metricool notifies the owner's phone, she adds the link sticker and posts. Leave an empty area around y 1520–1620 for the sticker.
  3. Every other Sunday product slot alternates: Roadmaps (beehiiv) ↔ Etsy products.
  4. Seniors email: soft mention at most once a week, alternating with the Senior Roadmap.
  5. Pinterest (FreshlyMadeFL account, College Plan brand in Metricool): product pins + free cheat-sheet pins on college topics, 1 pin/day max per product line.
- Link in bio = Metricool SmartLink https://t-sml.mtrbio.com/public/smartlink/collegeplan (set up 2026-10-15; buttons: newsletter, Etsy, Roadmaps, Pinterest; background + logo in brand/smartlinks/). Each new Etsy product gets its own SmartLink button (owner edits it in Metricool on desktop; the API can't).
- Every new College Plan Etsy product: add it to this list with its URL, make 1 native Reel config + 1 Story in its folder, and add it to the rotation above.

## Newsletter sending (beehiiv Lite plan)
The API can't send on Lite. The Sunday routine saves the 3 weekly emails + the guide as DRAFTS and reminds the owner to click Schedule/Publish. Switch back to auto-send if the plan is upgraded (Scale or higher).

## Guides log (newest first)
- 2026-10-11: FAFSA vs. FFAA: Florida's Two Financial Aid Forms, Explained — draft, slug fafsa-vs-ffaa-florida-financial-aid-forms-2027-28 (owner to publish web-only)
- 2026-10-08: Bright Futures guide re-created as a draft (slug florida-bright-futures-requirements-2027-2028-6ad3), owner to publish web-only
- 2026-10-07: Florida Bright Futures Requirements for the Classes of 2027 and 2028 — /p/florida-bright-futures-requirements-2027-2028

## TikTok (connected 2026-10-08)
- A separate Sunday 3:23pm task cross-posts the coming week's Instagram feed posts and Reels to TikTok (2-4 hours after Instagram, max 3/day, photo posts get TikTok auto-music).
- TikTok needs a title on every post. Metricool can't add music to videos, so videos get our baked-in music (scripts/add_music.py) or a voiceover.
- **Videos only (Oct 13):** TikTok photo posts got 0 views in Metricool, videos got 13–46. Cross-post Reels as-is; turn carousels into slideshow videos with `python3 scripts/slideshow_video.py tiktok/<name>.mp4 2.4 slide1.png slide2.png ...` (blurred background, slow zoom, music). Skip single-image posts on TikTok unless they become a native Reel.

## Log (newest first — the weekly routine appends here)
- 2026-10-15: College Application Tracker LIVE on Etsy (listing 4595734726). The 3 tracker pins (Oct 17/20/23) now link to the listing.
- 2026-10-15: Bio link is now the SmartLink https://t-sml.mtrbio.com/public/smartlink/collegeplan (Instagram website field). "Link in bio" captions now lead to newsletter + Etsy + Roadmaps + Pinterest.
- 2026-10-14: Pinterest board "College Planning" (id 1105985689682134542) created. Scheduled 9 College Plan pins (pinterest/collegeplan/, script /tmp/college/cppins.py style) daily 10:00am Oct 16–24: 6 free cheat sheets linking to collegeplan.beehiiv.com + 3 tracker pins linking to the Etsy SHOP (swap to the listing URL with updateScheduledPost once live). FreshlyMadeFL pins keep 1pm + 8pm. Owner setting up Metricool SmartLinks (website + Etsy + Pinterest) as the bio link.
- 2026-10-14: NEW Etsy product line (College Application Tracker, College Plan branded, sold in the FreshlyMadeFL Etsy shop). Built tracker Reel + Story in instagram/2026-10-tracker/. SCHEDULED (owner: "auto schedule, I'll add links later"): Reel Wed Oct 21 6pm IG+FB (music Check This Out, isAiGenerated true, first comment), Story Thu Oct 22 8:15am IG+FB auto-publish with "Link in bio" (no sticker). Weekly routine: keep those two slots. Owner is setting up a multi-link bio page (website + Etsy + Pinterest) and a Pinterest board "College Planning".
- 2026-10-13 DATA CHECK + REWORK of week Oct 13–18 (owner: "we're not getting any traction" → "rework everything that makes sense based on the data"). Instagram: Oct 13 7am roadmap carousel → native Reel "senior parent group chat in October" (music 622819303274042 Good Time, Alex Blue); Oct 13 6pm October Reel re-cut native (hook on frame 0, 8.5s); Oct 14 6pm BF 2028 re-cut native; Oct 15 7am freshman roadmap carousel → native Reel "texting my senior on Oct 15" (1326560949104401 Check This Out, Giulio Cercato); Oct 15 6pm trial Reel → "what my senior says vs. what it means" (POV deadline-day version retired); Oct 16 6pm UF voiceover v2 (preamble cut, hook on frame 0); NEW Oct 17 6pm Reel "touring Florida campuses in fall" (4283034138460390 Splash, The K Club); Oct 18 7am bingo image → animated bingo Reel (1386811643506297 Home, Giulio Cercato); Oct 18 6pm checker trial Reel re-cut native. Roadmap carousels (doodled) saved as Metricool DRAFTS dated Oct 25 + Nov 1. Kept: Oct 14 Hillsborough, Oct 16 Showdown, Oct 17 Jack Kent Cooke carousels. TikTok: all photo posts replaced with videos (gc-october, bf2028 moved to 8pm, texting, translations, Showdown + JKC slideshow videos, UF v2, tour-weather Oct 17 8pm, bingo, checker moved to Oct 18 8pm); UF stats, Benacquisto-slot and group-chat-reminder photo posts set to draft. Files: instagram/2026-10-native/, tiktok/showdown-uf-fsu.mp4, tiktok/jkc-scholarship.mp4.
- 2026-10-11 TikTok cross-post (week Oct 12–18): added 6 — Oct 14 9pm BF 2028 Reel, Oct 15 8pm POV trial Reel, Oct 16 10:30am Swamp vs Doak (sd1–6 JPEG), Oct 16 8pm UF voiceover Reel, Oct 17 10:30am Jack Kent Cooke (jk1–6 JPEG), Oct 18 9:30am bingo (bg1 JPEG). Skipped as already on TikTok: Oct 11 to-do, Oct 12 deadlines, roadmaps Reel + carousels, Oct 13 October Reel (TikTok Oct 10), Oct 14 Hillsborough (TikTok Oct 10), Oct 18 checker trial Reel (same video as Oct 9 TikTok).
- 2026-10-11 routine (week Oct 12–18). Already filled, skipped: Mon 7am deadlines, Mon 6pm Reel (roadmaps voiceover took the remix slot), Tue 7am (Senior Roadmap carousel took the school-stats slot; next stats school: FSU), Tue 6pm Reel, Wed 7am Hillsborough, Thu 7am Freshman Roadmap (took the Thu photo/fun slot), Fri 7am Showdown UF vs FSU, Sun 6pm trial Reel, Stories Mon/Tue/Thu. Analytics too small to pick a remix winner (no saves/shares yet); remixed the Bright Futures 2028 carousel by judgment on Wed.
- 2026-10-18 Sun 8:15am: Story ts1 calendar, refreshed dates (instagram/2026-10-18-story-calendar/)
- 2026-10-18 Sun 7am: FUN / Rotation C seasonal — "Florida senior parent bingo: October edition" single image, comment your number (instagram/2026-10-18-bingo/)
- 2026-10-17 Sat 8:15am: Story st3 "Test day? Breakfast first" (ACT Oct 17 + Saturday PSAT)
- 2026-10-17 Sat 7am: SCHOLARSHIP carousel — Jack Kent Cooke ($55K/yr, due Nov 11), AI cover photo, comment GUIDE. Cover picked: "Up to $55,000 a year. Due Nov 11." Runner-up: "Senior with a 3.75 GPA? Read this before Nov 11" (instagram/2026-10-17-scholarship-jack-kent-cooke/)
- 2026-10-16 Fri 6pm: VOICEOVER REEL #2 — "Applying to UF? 3 things parents miss" (Common App only, STARS a week later, test scores required), no music (instagram/2026-10-16-vo-uf-3-things/)
- 2026-10-16 Fri 8:15am: Story st1 countdown Oct 22 (UF ED STARS + FSU materials)
- 2026-10-15 Thu 6pm: TRIAL REEL — POV "It's deadline day in a Florida senior's house" (fun format test). Music 761736589642441 Be Happy (Instrumental), Afro Sound Machine (instagram/2026-10-15-trial-reel-pov/)
- 2026-10-14 Wed 6pm: REEL — carousel remix "Class of 2028: Bright Futures just got harder to get" (4 score changes). Music 901455037857983 It's A Vibe, Giulio Cercato (instagram/2026-10-14-reel-bf-2028/)
- 2026-10-14 Wed 8:15am: Story st2 "UF only accepts the Common App" + STARS; 7:30am Story st4 teaser for the Hillsborough carousel
- 2026-10-08: TikTok launch batch: 17 posts Oct 8-17 (4 videos, 13 photo posts/carousels).
- 2026-10-08: Roadmaps launch scheduled: Story Oct 8 9pm; voiceover Reel Oct 12 12pm; Senior carousel Oct 13 7:30pm + Story 8:45pm; Freshman carousel Oct 15 7:30pm + Story 8:45pm.
- 2026-10-08 Thu LAUNCH BLAST 10:00–11:10am (moved forward from Oct 13–18, so those evening slots are now OPEN for the Oct 11 routine to fill): newsletter promo (pr2), scholarship Benacquisto, myth vs fact FFAA, photo quote group chat, UF stats, checker promo (tl2), FAFSA vs FFAA carousel, NEW welcome/start-here post (wl1 — owner should pin it). Oct 14 7:45pm teaser Story now shows ts2 (checker) since the FAFSA carousel already ran. Still on their original days: Oct 12 deadlines, Oct 13 Reel, Oct 14 Hillsborough, Oct 18 trial Reel.
- 2026-10-09 Fri 6pm: BONUS QUIZ — Guess the Florida campus, simplified to one photo (UF University Auditorium); answer Story Oct 10 12pm instagram/2026-10-09-guess-the-campus/. First comments added to all 5 Showdowns + this quiz.
- 2026-11-13 Fri 7am: SHOWDOWN — FSU vs UCF Greek life (NOLES/KNIGHTS) instagram/2026-11-13-showdown-fsu-ucf/
- 2026-11-06 Fri 7am: SHOWDOWN — UF vs USF future doctors (GATORS/BULLS; USF 7-year B.S./M.D.) instagram/2026-11-06-showdown-uf-usf/
- 2026-10-30 Fri 7am: SHOWDOWN — FIU vs FAU dorm life (PANTHERS/OWLS) instagram/2026-10-30-showdown-fiu-fau/
- 2026-10-23 Fri 7am: SHOWDOWN — UCF vs USF most to do on campus (KNIGHTS/BULLS) instagram/2026-10-23-showdown-ucf-usf/
- 2026-10-16 Fri 7am: SHOWDOWN #1 — UF vs FSU game day (SWAMP/DOAK) instagram/sample-showdown-uf-fsu/ (SCHEDULED Oct 9)
- Next Showdowns should avoid these pairs until mid-December; good next ones: UNF vs UWF (beach access), FGCU vs New College (campus on the water), FAMU vs FSU (homecoming, same city), UM vs UF (private vs public), "Guess the campus".
- 2026-10-09: NEW SERIES: Friday School Showdowns (sample UF vs FSU game day built in instagram/sample-showdown-uf-fsu/, not scheduled yet — owner reviewing). Real photos via Find photos action (photos/commons/). Brand pillars added.
- 2026-10-09: PLAN CHANGE: 6 Reels/week (added Mon 6pm carousel-remix Reel + Wed 6pm Reel), carousel cover rules, spacing rule (1 feed post/day), Collab outreach started (COLLABS.md).
- 2026-10-09: RESCHEDULED everything pending Oct 9–18 to the new times (feed 7:00am, Reels/trial Reels 6:00pm, roadmap teaser Stories 7:30am, Oct 14 checker Story 6pm, TikToks 9:30am/11am/8pm). Oct 9 essay joke post went at 10:00am (morning had passed). Older Log lines below still show the original times.
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
