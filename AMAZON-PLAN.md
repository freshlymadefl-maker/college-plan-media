# Amazon picks: weekly list + cover + socials

Owner (Nov 2): "auto create new ones consistently: create the list, make the cover (spread the images out a little better), share on socials including Pinterest. 1 a week for now. Keep in mind the holidays too."

- Storefront: https://www.amazon.com/shop/partyvibesdiy (Amazon Influencer storefront, tracking ID laurenfreshly-20). The owner is signed in to Amazon in her Chrome; we work through Claude in Chrome.
- SmartLink (bio link) has a "Shop My College Picks" button to the storefront: https://t-sml.mtrbio.com/public/smartlink/collegeplan . All our pins/posts point there.
- Brand: College Plan (parents of 8th-12th graders + college-bound students, Florida). Amazon picks are college-related, so they can go on every network (PINTEREST-PLAN.md "WHERE THINGS GO").
- Owner approved (Nov 2) that the weekly task SUBMITS the new Idea List and Collage itself (no draft step).

## HOLIDAY PUSH Nov 12 - Dec 21 2026 (owner, Nov 11: "keep posting these amazon things a lot though esp with christmas coming up. we can do christmas style. college student gifts, for the college student who has everything etc.") — read this FIRST in Nov/Dec
Why: last 30 days (Oct 12-Nov 10) = 82 clicks, 4 orders (~5% conversion, good). The problem is too few clicks, so: more posts, gift-search keywords, fewer taps to the list.
**Runs:** the task runs TWICE a week (Mon + Thu) through Dec 21. Each run = 1 new gift Idea List + Collage (if Chrome is reachable) + that run's socials below. From Dec 22 it goes back to Mondays only (a Thursday run after Dec 21 stops quietly).
**Socials per week (fill only EMPTY slots; never break the 4-hours-apart Instagram rule):**
- Instagram + Facebook gift Reels: **3 a week**, 6:00pm Tue, Thu, Sun (Mon run schedules Tue + Thu, Thu run schedules Sun). These replace the Tue school-stat reveal and the Thu/Sun format-test slots during the push. Use the CONTENT-PLAN.md trend format bank + December look (red/green/gold, icy blue): e.g. notes-app gift list typing itself, lock-screen pile-up ("Amazon: your order shipped" x5), receipt printing (NO prices), tier list of gifts, "things that just make sense: gifting a college kid ___", checklist ASMR. Funny parent hook on frame 0, 7-10s, list items, end card "Shop my picks: link in bio".
- Pinterest gift pins: **1 a day** in the 10:00am slot (7:00am stays the college cheat sheet). Keyword-first titles people actually search: "Gifts for College Students", "Christmas Gifts for College Guys", "Gift Ideas for the College Student Who Has Everything", "Stocking Stuffers for College Students", "Finals Week Care Package Ideas", "Gifts for Teens Who Have Everything". Rotate across ALL live gift lists (older lists too), new headline each pin, never the same list twice in one day.
- **Pin link = the matching Idea List's own URL** (amazon.com/shop/partyvibesdiy/list/...; copy it from My content when the list is published) so a click lands on the products in one tap. Use the SmartLink only when the list URL isn't known. Save each list URL in the "Live gift lists" table below.
- Instagram Story: 2 a week (Mon + Fri 8:00pm, extra to the daily 8:15am Story): "new gift list is up: link in bio" over our drawn checklist (never Amazon photos), with a poll sticker question in the caption plan if Metricool can't add stickers.
- **REEL COVERS (owner, Nov 19: "make sure you are choosing a good cover image to use for the reels? most of them are mostly blank"):** every Instagram/Facebook Reel (and video pin that is also a Reel) gets a custom cover. Our formats build on screen, so frame 0 is nearly empty. Run `python3 scripts/make_cover.py <video.mp4> covers/<name>.jpg --t <seconds where the most content is on screen, before the end card> --hook "<on-screen hook>" [--kicker "<audience>"]`, LOOK at it with Read, push, and set info.videoThumbnailUrl to its raw.githubusercontent URL pinned to the commit on the Reel post (not on Stories or Pinterest pins). Full rule: CONTENT-PLAN.md "REEL COVERS".
- TikTok: the Sunday TikTok task cross-posts the gift Reels (videos only).
**If Chrome isn't reachable:** still do ALL the socials using the gift lists that are already live (table below) with fresh angles; queue the new list theme under "Queued". Never skip the posts just because the new list couldn't be built.
**Tracking:** if per-channel tracking IDs are listed under "Tracking IDs" below, use the Pinterest one in pin links and the Instagram/Facebook one in the SmartLink/storefront, so the Associates report splits clicks by channel.

### MORE ON AMAZON ITSELF (owner, Nov 12: "we can put as much as we can")
Amazon's storefront takes 4 kinds of content: Idea Lists, Photo posts (Collages count), Videos, Livestreams. Every run with Chrome reachable now does, after the new list + collage:
1. **1 extra holiday Collage of an OLDER live list** (rotate through the "Live gift lists" table, then the 6 Nov 1 lists): December red/green colors, a new gift-style title (<=16 chars, e.g. "Teen Gift Ideas" -> "Teen Xmas Gifts"), same spread-out grid rule, description ending "From College Plan." Submit. Log which list was re-collaged so we don't repeat it within 2 weeks.
2. **Fill missing list URLs** in the table (pins then link straight to the list).
3. **Video test (once):** try uploading ONE gift Reel as a storefront video tied to the list's products. Amazon reviews videos and usually wants the real product on screen; ours show only a drawn checklist, so if it's rejected, log the reason and stop trying. If it's accepted, upload each new gift Reel there too.
- Real product photos/videos (the owner holding or using a product) are what Amazon likes best and can show on product pages. If the owner drops clips or photos in the repo (photos/amazon/), post them as storefront Photos/Videos tagged to that product. Never use Amazon's own product images outside Amazon's tools.
- Livestreams: owner only (needs her live).

### Holiday theme calendar (2 lists a week; if a row is done, take the next unused one)
| Run | Theme (list title) | Collage title (<=16 chars) |
|---|---|---|
| Mon Nov 16 | Home for Thanksgiving: College Kid Travel Kit (queued, see below) | Thanksgiving Trip |
| Thu Nov 19 | Gifts for the College Student Who Has Everything | Has Everything |
| Mon Nov 23 | Stocking Stuffers for Teens + College Kids (Black Friday weekend shoppers; no deal claims) | Stocking Stuffers |
| Thu Nov 26 | Small Gifts College Kids Actually Use (no prices/"under $X") | Small Gifts |
| Mon Nov 30 | Finals Week Care Package | Finals Care Pack |
| Thu Dec 3 | Gifts for College Guys | College Guy Gifts |
| Mon Dec 7 | Gifts for College Girls | College Girl Gift |
| Thu Dec 10 | Gifts for the College Freshman Home for Winter Break | Freshman Gifts |
| Mon Dec 14 | Last-Minute Gifts They'll Actually Use (no delivery promises) | Last-Minute Gifts |
| Thu Dec 17 | Cozy Winter Break Gifts for Teens | Cozy Break Gifts |
| Mon Dec 21 | Winter Break Room Reset for Teens | Room Reset |
Collage color: red/green or a December color if Amazon offers one; otherwise light blue. Reel/pin hook ideas: "the college kid who has everything still doesn't have ___", "what my college kid actually used vs. what I bought", "gifts that survive a dorm room", "stocking stuffers that won't end up in the junk drawer", "POV: your freshman comes home and sleeps for 3 days".

### Live gift lists (pin these; add each new one with its URL)
| List | URL |
|---|---|
| Gifts for the College Student Who Has Everything (Nov 23) | https://www.amazon.com/shop/partyvibesdiy/list/2YE61IOUBQINZ |
| Home for Thanksgiving: College Kid Travel Kit (Nov 16) | https://www.amazon.com/shop/partyvibesdiy/list/34I789TQ21CJ2 |
| Gifts for College Students (Dorm-Friendly) (Nov 9) | https://www.amazon.com/shop/partyvibesdiy/list/3HNNCYKBNVAQK |
| Gifts for High School Teens (Nov 2) | https://www.amazon.com/shop/partyvibesdiy/list/360B153S4QRM2 |
| Gifts for College-Bound Seniors (Nov 1) | https://www.amazon.com/shop/partyvibesdiy/list/2HVODW0VD7QUJ |
| SAT + ACT Test Day Bag (Nov 1) | https://www.amazon.com/shop/partyvibesdiy/list/WLJSDTGV7DWW |
| College Visit Bag (Nov 1) | https://www.amazon.com/shop/partyvibesdiy/list/2B9K39DWF05OF |
| Dorm Room Must-Haves (Nov 1) | https://www.amazon.com/shop/partyvibesdiy/list/95PN5EH1KE7T |
(Senior Year Study Desk Setup and Sorority Recruitment Bag URLs not found on the storefront page Nov 23.)

### Tracking IDs
(none yet: owner to decide on one per channel: Pinterest, Instagram/Facebook, Idea Lists)

## Rules
- Never copy Amazon product photos into OUR graphics (pins, Reels). Amazon images live only inside Amazon's own Idea List and Collage tools. Our pins = drawn checklists (pinterest/tools/cp_amazon_pins.py).
- Disclosure on every pin/post: "As an Amazon Associate I earn from qualifying purchases." Instagram/Facebook/TikTok captions also get #ad.
- No prices, deal or discount claims, "best seller" claims, or delivery-by-date promises (they change). No medical/safety claims.
- Products: top non-sponsored search results rated 4.4+ with lots of reviews (prefer 1,000+), family friendly, no weapons/alcohol/vapes/supplements/medicines, no adult items. Generic, useful items; avoid sizes that confuse (pick a variant title that matches, e.g. "Twin XL").
- Facts that vary (test-day rules, dorm banned items, airline rules) point to the official source in the list description and the pin.
- Don't repeat a theme or a product set already in the Log below.

## Theme calendar (pick the row for the coming week; if done already, pick the next unused idea that fits the season)
| Week of | Theme (list title) |
|---|---|
| Nov 9 2026 | Gifts for High School Teens |
| Nov 16 2026 | Gifts for College Students (dorm-friendly) |
| Nov 23 2026 | Home for Thanksgiving: College Kid Travel Kit |
| Nov 30 2026 | Stocking Stuffers for Teens + College Kids |
| Dec 7 2026 | Finals Week Care Package |
| Dec 14 2026 | Last-Minute Gifts They'll Actually Use (no delivery promises) |
| Dec 21 2026 | Winter Break Room Reset for Teens |
| Dec 28 2026 | New Semester Desk Reset |
| Jan 2027 | FAFSA + Paperwork Organizer Kit; Spring SAT/ACT Prep Supplies; Cozy Dorm Winter Must-Haves; Study Snacks + Focus Kit |
| Feb 2027 | Valentine's Care Package for College Kids; Spring Break College Visit Bag; Senior Year Organization (decisions coming) |
| Mar 2027 | AP Exam Kit; Road Trip College Tour Essentials; Gifts for the Admitted Student |
| Apr 2027 | Decision Day Gift Ideas (May 1); Prom + Senior Events Emergency Kit; Teacher Thank-You Gifts |
| May 2027 | Graduation Gifts for Seniors; Dorm Shopping Starter List; Summer Job + Internship Essentials |
| Jun-Jul 2027 | Dorm series: Bedding, Bathroom, Desk + Tech, Laundry, Mini Kitchen + Snacks, First Aid + Wellness, Storage |
| Aug 2027 | Move-In Day Kit; Back to School for High Schoolers; Sorority Recruitment Bag (refresh) |
| Sep-Oct 2027 | Application Season Desk; Fall College Visit Bag; Homecoming Emergency Kit |
Holidays to weave in: Thanksgiving, Black Friday/Cyber Monday (no deal claims), Christmas/holiday gifting (Nov-Dec heavy), New Year, Valentine's Day, spring break, Decision Day (May 1), graduation, move-in, Halloween/homecoming.

## How to build it in the owner's Chrome (learned Nov 1)
1. tabs_context_mcp (createIfEmpty), work in a new tab. Storefront pages: https://www.amazon.com/create/collection?affiliateId=partyvibesdiy (Idea List), https://www.amazon.com/create/collage?affiliateId=partyvibesdiy (Collage), https://www.amazon.com/manage-content?affiliateId=partyvibesdiy (My content).
2. Pick products: on any amazon.com page run JS that fetch()es /s?k=<query> and parses [data-component-type="s-search-result"] (skip ones with .puis-sponsored-label-text), rating from .a-icon-alt. Long loops time out: start the loop as a background async and poll a window variable.
3. The "Add products" picker only offers Idea Lists / Your orders / Browse history (+ a search box). Easiest: navigate to each chosen /dp/<ASIN> page first, then in the picker open "Browse history" (newest first) and tick the checkboxes. Check the product count after "Done".
4. Idea List: title, description ("... From College Plan." + official-source note when needed), add 5-8 products, an "AI description" suggestion pops up: dismiss it with its X (keep our text). Save menu (yellow Save ▾): Submit / Save draft / Schedule. Use Submit.
5. Collage: add the same products, then Text tab = short title (max ~16 characters, it overflows otherwise), Colors tab = light-blue stripes (College Plan look; purple stripes for sorority/girly themes, others when a holiday fits, e.g. red/green in December if offered), description. Items on the canvas can be dragged (and resized from corner handles).
   SPREAD THE IMAGES OUT (owner, Nov 1): fill the whole canvas evenly, roughly a 2-3 column grid, little to no overlap, nothing covering or touching the title, every product visible, no big empty corners. Zoom-screenshot the canvas and fix it before saving. Then Preview, then Save ▾ > Submit.
6. Both post types show "submitted ... when approved it will be published". Check My content: the new items say Published/In review.
7. Close the tabs you opened.

## Socials (same week)
- **REEL COVERS (owner, Nov 19: "make sure you are choosing a good cover image to use for the reels? most of them are mostly blank"):** every Instagram/Facebook Reel (and video pin that is also a Reel) gets a custom cover. Our formats build on screen, so frame 0 is nearly empty. Run `python3 scripts/make_cover.py <video.mp4> covers/<name>.jpg --t <seconds where the most content is on screen, before the end card> --hook "<on-screen hook>" [--kicker "<audience>"]`, LOOK at it with Read, push, and set info.videoThumbnailUrl to its raw.githubusercontent URL pinned to the commit on the Reel post (not on Stories or Pinterest pins). Full rule: CONTENT-PLAN.md "REEL COVERS".
- Pinterest: 1 checklist pin (cp_amazon_pins.py, CTA "Shop my picks: tap the link") in an open 7:00am or 10:00am College Planning slot (board 1105985689682134542), pinLink = SmartLink. A 2nd pin later in the week with a different headline (e.g. "5 gifts teens actually want") is welcome if a slot is open.
- Instagram + Facebook: one Reel (the checklist rendered 1080x1920 with CTA "Shop my picks: link in bio", 7-10s, music via audioConfiguration videoVolume 0), funny/relatable parent hook first (e.g. "Me pretending I didn't just buy my senior a desk lamp for Christmas"). Open 6:00pm slot; one Amazon Reel per week max. Caption ends with "Shop my picks: link in bio 🛒", the Associates line and #ad. The Sunday TikTok task cross-posts it.

## Queued (build these first next run, then that week's own theme)
- (none) Next holiday row: Thu Nov 26 Small Gifts College Kids Actually Use, then Mon Nov 30 Finals Week Care Package. Stocking Stuffers (Mon Nov 23 row) was not built this run (one list per run); fold it into a later run if a slot frees up.

## Log (newest first)
- 2026-11-23 (Mon, holiday push, owner's desktop app + Chrome): **Gifts for the College Student Who Has Everything** Idea List + Collage "Has Everything" SUBMITTED and showing Published in My content (https://www.amazon.com/shop/partyvibesdiy/list/2YE61IOUBQINZ). 6 products: VENTIMI heated throw B09838MXBJ (4.4, 4,922), YGSKK mini projector B0F7RR3YC6 (4.5, 5,760), YFONG weighted sleep mask B09C5PD9VD (4.6, 8,152), no-drill under-desk cable tray B0BZ3GHM8N (4.7, 3,556), OGHom travel steamer B0FT7NWBBK (4.5, 2,255), Elite Gourmet 1L glass kettle B08FVFYB8Y (4.5, 18,072). Description has the housing-rules appliance note. Collage light-blue stripes (no December color offered), 3x2 grid (steamer/kettle/mask top, projector/blanket/tray bottom), title clear. FOUND: the Thanksgiving Travel Kit list + collage were already published Nov 16 (an earlier run built them but never logged it), so it's cleared from Queued; filled 8 list URLs in the Live gift lists table (fetched from the storefront page). Socials (pin links = list URLs): pins 10am Tue Nov 24 cp_amz_has_everything ("Gifts for College Students Who Have Everything: 6 Useful Dorm Ideas"), Wed Nov 25 cp_amz_dont_need_anything ("Christmas Gifts for College Students Who Say They Don't Need Anything"), Thu Nov 26 cp_amz_winter_break_travel ("Travel Gifts for College Students: Winter Break Travel Kit Checklist", Thanksgiving list). Reel IG+FB Tue Nov 24 6pm has-everything-reel.mp4 (hook card + checklist, icy blue/December red, cover has-everything-reel-cover.jpg, music Good Time 622819303274042). Story IG+FB Mon Nov 23 8pm story-has-everything.png. A 2nd Reel dont-need-anything-reel.mp4 (cream/green, "idk, money?" hook) + cover were made for Thu Nov 26 6pm but NOT scheduled: the scheduler blocked a 2nd Amazon Reel this week (task rule = 1 Amazon Reel/week); it's in instagram/2026-11-amazon/ if the owner wants it. Media hosted from GitHub raw URLs (commits 6b4711a pins, 2d59846 Reels/covers/Story) instead of Metricool drafts. Note: GitHub upload commits only stick if you scroll the Commit button into view and click it by coordinate, then wait for the redirect; a ref click + navigate lost 3 commits.
- 2026-11-19 (Thu, holiday push): NO BUILD for the 3rd run in a row: no Claude in Chrome tools in this cloud run (searched twice; the task runs in the cloud, not on the owner's computer), so the Thanksgiving Travel Kit stays queued and "Has Everything" is queued too; no collage, no list URLs filled; skipped the 2-hour send_later retry because a cloud session can't reach her Chrome either. Socials from live lists (SmartLink, list URLs still unknown): pins 10am Fri Nov 20 cp_amz_cozy_college ("Cozy Christmas Gifts for College Students: Dorm Gift Ideas They'll Use", dorm list), Sat Nov 21 cp_amz_teen_junk_drawer ("Christmas Gifts for Teens: Useful Ideas That Skip the Junk Drawer", teen list), Sun Nov 22 cp_amz_senior_first_dorm ("Gifts for High School Seniors Going to College: First Dorm Ideas", Nov 1 seniors list), Mon Nov 23 cp_amz_winter_break ("Winter Break Gifts for College Students: Sleep, Study + Cozy Ideas", dorm list) (tool pinterest/tools/cp_amz_gifts_1119.py). Reel IG+FB Sun Nov 22 6pm small-christmas-lock-reel.mp4 (format LOCK-SCREEN PILE-UP, look 'xmas'; "me: we're doing a SMALL Christmas this year / my lock screen by Thanksgiving"; config trend/amz-lock-small-xmas.js; cover covers/small-christmas-lock-reel.jpg; IG music 393903371411311 The Nerve). Story IG Fri Nov 20 8pm instagram/2026-11-20-story-gift-lists/story.png ("Their first dorm list", seniors, green). Media commit 2ccffd0968da0ad269c2f0f380f9e5a358ac03ed.
- 2026-11-16 (Mon, holiday push): NO BUILD again: no Claude in Chrome tools in this cloud run (searched twice), so the Thanksgiving Travel Kit list stays queued; no collage, no list URLs filled. Socials from live lists (SmartLink, list URLs still unknown): pins 10am Tue Nov 17 cp_amz_senior_xmas ("Christmas Gifts for High School Seniors Going to College", Nov 1 seniors list), Wed Nov 18 cp_amz_teen_practical ("Practical Christmas Gifts for Teens They'll Actually Use", teen list), Thu Nov 19 cp_amz_college_everything ("Gifts for College Students Who Have Everything (Cozy Dorm Ideas)", dorm list) (tool pinterest/tools/cp_amz_gifts_1116.py). Reel IG+FB Thu Nov 19 6pm college-gifts-tier-reel.mp4 (format TIER LIST, new December look 'xmas' in trend-reel.html, config trend/amz-tier-college-gifts.js; IG music 631409104021154 Too Fast). Tue Nov 17 6pm was already the dorm-gifts Reel and Wed 6pm is taken, so only 1 new Reel this run. Story IG Mon Nov 16 8pm instagram/2026-11-16-story-gift-lists/story.png ("The cozy dorm list", icy blue, "Gift lists: link in bio"). Media commit 4ae8d152c8267dace455c1b64e476704005ae5ce.
- 2026-11-12 (Thu, holiday push): NO BUILD: Claude in Chrome tools weren't available in this cloud run, so the queued Thanksgiving Travel Kit list stays queued (build it next run). Socials from live lists: pin cp_amz_teen_everything Mon Nov 16 10am ("Gifts for Teens Who Have Everything", teen list, SmartLink since list URLs are unknown); Reel teen-has-everything-receipt-reel.mp4 IG+FB Mon Nov 16 6pm (format: RECEIPT PRINTING, December green/red look; new template templates/reel/receipt-reel.html + receipt/teen-has-everything.js; IG music 801712745786459 Best Life) because Sun Nov 15 6pm was already taken; Story instagram/2026-11-13-story-gift-lists/story.png IG Fri Nov 13 8pm. Fri-Sun 10am pin slots were already full (older College Plan pins), so only Mon got a gift pin.
- 2026-11-09: Gifts for College Students (Dorm-Friendly) (week of Nov 16): Idea List + Collage "Dorm Gift Ideas" published. 6 products: ENITYA 22" XL back pillow with armrests B0DLGGGYMN, Magicteam white noise machine B07RWRJ4XW, DuomiW bedside caddy B07MBZ72XZ, LAPGEAR Home Office lap desk (oak) B089P33W98, Waitu wearable blanket hoodie B07Z5LGZJM, BedShelfie bedside/bunk shelf B09XLWQ85B. Collage light-blue stripes, 3x2 grid. Pins Nov 16 + Nov 18 7am (cp_amz_dorm_gifts, cp_amz_dorm_gifts_2), Reel IG+FB Nov 17 6pm (dorm-gifts-reel.mp4, music Good Time). Note: the collage editor tab froze once after picking a color with products on the canvas; setting Colors + Text BEFORE adding products worked. Adding products from the new Idea List (picker > Idea Lists tab) is faster than Browse history.
- 2026-11-02: Gifts for High School Teens (week of Nov 9) built from the owner's desktop app: Idea List + Collage "Teen Gift Ideas" published. 6 products: INIU 10000mAh charger B0CB1FW5FC, LED desk lamp B08923SXXP, CamelBak Chute Mag 32 oz B07XRXFWD4, Odokee sunrise clock B0DGXD6WVW, Bedsure sherpa throw B0CPS22JVK, Soundcore Select 4 Go B0DB1753RZ. Collage light-blue stripes, 3x2 grid. Pins Nov 9 + Nov 11 7am, Reel IG+FB Nov 10 6pm.
- 2026-11-01: 6 lists + 6 collages live: SAT + ACT Test Day Bag, College Visit Bag, Senior Year Study Desk Setup, Dorm Room Must-Haves, Gifts for College-Bound Seniors, Sorority Recruitment Bag.
