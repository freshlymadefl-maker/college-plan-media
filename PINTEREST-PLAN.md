# Pinterest plan (FreshlyMadeFL Etsy shop + College Plan)

Owner (Oct 15): "share frequently to Pinterest, no one is following us so we can just spew content. College Plan and also our Etsy listings." Also: "make pop culture funny videos/trends for our Etsy listings too, to share on all socials including Pinterest. I like the ones with music."

## WHERE THINGS GO (owner rule, Oct 15)
- NON-college content (FreshlyMadeFL money, bakery, candle, small business, Etsy-seller products, cheat sheets and videos): **Pinterest ONLY.** Never on College Plan's Instagram, Facebook, TikTok, Stories, newsletter or website.
- College-related content (College Plan posts and the college Etsy products: College Application Tracker, Scholarship Tracker, Sorority Recruitment kit, and any future college listing): **can go anywhere**: Instagram, Facebook, TikTok, Stories, Pinterest, newsletter mentions and the website, still following the posting rules and spacing in CONTENT-PLAN.md.

- Owner (Oct 15): "share the Pinterest post to socials when it's college related." Every week, bundle that week's NEW college pins into ONE Instagram + Facebook Reel (render 1080x1920 versions with "link in bio" instead of "tap the link", stitch with ffmpeg, add music; example instagram/2026-10-amazon/). Use an open 6:00pm Reel slot. The Sunday TikTok task cross-posts it.

## Amazon picks (owner's Amazon Associates storefront, tracking ID laurenfreshly-20)
- The owner builds shoppable lists in her Amazon storefront with Amazon's own collage tool. We NEVER copy Amazon product photos into our own graphics (against the Associates rules). Our pins are drawn checklists in College Plan style: pinterest/tools/cp_amazon_pins.py (CTA env var: "Shop my picks: tap the link" for pins, "link in bio" for socials).
- pinLink = the SmartLink https://t-sml.mtrbio.com/public/smartlink/collegeplan (it has a "Shop my college picks" button to the storefront). Every pin/post says "As an Amazon Associate I earn from qualifying purchases." (+ #ad on Instagram/Facebook/TikTok).
- No brand names or product claims we can't check. Facts that vary (test rules, dorm banned items) point to the official source.

## Accounts
- One Pinterest account (freshlymadefl), connected in Metricool under the **College Plan brand, blogId 5183464** (timezone America/New_York). Both businesses pin from it.
- Board IDs (use the numeric id as pinterestData.boardId):
  - Money & Budget Planners: 1105985689682130289
  - Small Business Spreadsheets: 1105985689682130299
  - Pricing for Makers: 1105985689682130301
  - Etsy Seller Tips: 1105985689682130302
  - College Planning: 1105985689682134542
- FreshlyMadeFL has NO Instagram/TikTok in Metricool yet. College products may also go on College Plan's Instagram/Facebook (see CONTENT-PLAN.md "Etsy products"); TikTok copies are made by the weekly TikTok cross-post task from Instagram Reels.

## Links (pinLink)
- Etsy shop: https://www.etsy.com/shop/FreshlyMadeFL
- FSA Spend-Down Tracker: https://www.etsy.com/listing/4594157049 (board Money & Budget Planners)
- Sinking Funds / Paycheck Savings Planner: https://www.etsy.com/listing/4594168525 (Money & Budget Planners)
- Cake Pricing Calculator: https://www.etsy.com/listing/4594192409 (Pricing for Makers / Etsy Seller Tips)
- Order Tracker: https://www.etsy.com/listing/4594198661 (Small Business Spreadsheets / Etsy Seller Tips)
- Profit & Loss Spreadsheet: https://www.etsy.com/listing/4594773827 (Small Business Spreadsheets)
- Candle Pricing Calculator: https://www.etsy.com/listing/4594778387 (Pricing for Makers / Etsy Seller Tips)
- College Application Tracker: https://www.etsy.com/listing/4595734726 (College Planning)
- Scholarship Tracker: NOT LIVE YET (check CONTENT-PLAN.md "Etsy products" for a URL; until then don't pin it)
- Sorority Recruitment Resume + Prep Kit: NOT LIVE YET (same rule). When live, it gets its own new board only if the owner creates one; otherwise use College Planning.
- College Plan newsletter (free cheat-sheet pins): https://collegeplan.beehiiv.com/
Owner adds new listings over time: before each run, check CONTENT-PLAN.md "Etsy products" and this file for new URLs.

## Daily slots (America/New_York), 5 pins a day
| Time | What | Link |
|---|---|---|
| 7:00am | College Plan free cheat sheet (college topics) | newsletter |
| 10:00am | College Plan pin: college Etsy product pin OR another cheat sheet | listing / newsletter |
| 1:00pm | FreshlyMadeFL free cheat sheet (money, pricing, small business topics) | the matching listing |
| 4:00pm | FreshlyMadeFL product pin (new headline + screenshot) or a VIDEO pin | listing |
| 8:00pm | FreshlyMadeFL product pin | listing |
Fill only EMPTY slots (check getScheduledPosts first). Some slots are already filled through late Oct / mid Nov.

## Rules
- Every pin is a NEW image: new headline, new screenshot or new topic. Never re-schedule an image that was already pinned (check pinterest/ folders + the Log). Same listing max once a day.
- Facts: cheat-sheet content must be evergreen and verified (official sources: studentaid.gov, College Board, ACT, FTC, IRS, state agencies). If not sure, leave it out. Say "check with your plan / each college" where rules vary.
- Product pin sticker numbers must be real values visible in the screenshot (pinterest/assets/win/). Never invent features, reviews, "bestseller" or sales numbers.
- Proof points (owner, Oct 15): product pins/thumbnails show what it does for the buyer + a TRUE badge (math tested, info checked Oct 2026, scam guide included, no Canva needed).
- Pop culture / trends: use trend FORMATS (POV, "nobody: / me:", "tell me you're a ___ without telling me", "things that just make sense", "the girls who get it", "rating ___ as a baker") with ORIGINAL words. Never song lyrics, movie/TV quotes, celebrity names or likenesses, copyrighted characters, brand names or logos. Nothing mean.
- Titles under 100 characters, keyword first ("Cake Pricing Calculator: ..."). Description 2-4 sentences with natural keywords. Alt text on every pin.

## Tools (run from the repo root; Playwright + Chromium are preinstalled)
- pinterest/tools/fm_product_pins.py: FreshlyMadeFL product pins (palette per product from pinterest/tools/themes.py: fsa blush, sinking sage, cake peach, order lavender, pl sky, candle honey). Pass a JSON list or edit PINS.
- pinterest/tools/fm_cheatsheets.py: FreshlyMadeFL cheat-sheet pins (checklist / steps / table / formula / example blocks).
- pinterest/tools/cp_pins.py: College Plan look (navy, sky, gold, Lora italic) cheat sheets + college product pins.
- Screenshots of every spreadsheet tab: pinterest/assets/win/ (fsa_, psp_ = sinking funds, bake_, ord_, pl_, candle_, college_, scholar_). Sorority kit pages: pinterest/assets/rush/.
- Copy a tool to /tmp, replace its content lists with NEW content, set OUT to the right folder (pinterest/freshlymadefl or pinterest/collegeplan), run, then LOOK at every PNG/JPG with the Read tool (no overlaps, text inside the frame, readable at phone size).
- Media URL: push, then https://raw.githubusercontent.com/freshlymadefl-maker/college-plan-media/<commit sha>/<path>.

## Videos (2 per week for Etsy listings, music on). PREFER the stock meme format (see "Stock meme videos" below); the native-reel engine is the backup.
- Engine: templates/reel/native-reel.html + a config in templates/reel/native/<name>.js (see CONTENT-PLAN.md "Native Reels": hook on frame 0, 7-10 seconds, something new every second, funny first, one ask at the end).
- FreshlyMadeFL products: set logo:false, logoText:'FRESHLYMADEFL' in the config (hides the College Plan wordmark). Use a plain bg ('sky' or 'navy') or a background image made from pinterest/assets/win screenshots (1080x1920). No AI photos of food or products (owner dislikes the AI look).
- Render: python3 templates/reel/render-fast.py "templates/reel/native-reel.html?cfg=<name>" /tmp/<name>-silent.mp4 <secs> 30 && python3 scripts/add_music.py /tmp/<name>-silent.mp4 pinterest/videos/<name>.mp4 (music is baked in, works on every network).
- Schedule as a Pinterest pin with the mp4 as media (providers pinterest, pinterestData with board + title + link). If Metricool rejects video pins, keep the video, skip it on Pinterest and say so in the report.
- College products (College App Tracker, Scholarship Tracker, Sorority kit): the same video may ALSO go out as an Instagram + Facebook Reel in an open 6:00pm slot, but only if no other Etsy product Reel is scheduled that week (CONTENT-PLAN.md rule: max one product Reel a week), with instagramData audioConfiguration {audioId, videoVolume 0} for library music.

## Stock meme videos (owner, Oct 15): the closest thing to the reposts that get our reach
Real people on screen win. We can't repost, and we don't use AI people, so we use REAL free stock footage in the classic relatable meme layout: big caption on top, the clip as a big square, a yellow punchline that pops in, one ask at the end, music.
- Tool: `python3 scripts/stock_meme.py <config.json>` then `python3 scripts/add_music.py <out>-silent.mp4 <out>.mp4` (configs: clip, start, dur 7-8, top, punch + punch_t, end + end_t, brand collegeplan|freshlymadefl, crop_x to keep the face in the square). LOOK at frames at 1s, 4s and 7s before scheduling.
- Clip library: clips/stock/ (Mixkit). Get more by finding clips on mixkit.co search pages (e.g. mixkit.co/free-stock-video/<word>/), CHECKING each clip's page says "Mixkit Stock Video Free License" (skip "Restricted"), then pushing fetch/<name>.txt with lines "clips/stock/<name>.mp4 https://assets.mixkit.co/videos/<id>/<id>-720.mp4" (the Fetch images GitHub Action downloads them; wait ~75s, git pull). The free license allows social media marketing, no credit needed; never post a clip on its own, never resell it, never show the person in a way that mocks them or implies something sensitive about them (the joke is always on "me", the narrator).
- Writing: first person ("me at 11pm...", "when the cute custom order..."), a real, specific moment, the punchline is the twist, the end card is the product or the ask. Original words only (no lyrics, quotes, celebrities, brands).
- Use it for College Plan funny Reels too, not only Etsy videos. First ones: pinterest/videos/meme-deadline-screenshot.mp4 (also an IG/FB Reel Wed Oct 28 6pm), meme-cake-saturday.mp4, meme-custom-order.mp4.

## Log (newest first)
- 2026-10-15: Amazon picks: 7 checklist pins 7am Oct 19-25 (College Planning, link SmartLink) + Reel shopping-lists-reel.mp4 IG+FB Tue Oct 20 6pm (music Good Time 622819303274042).
- 2026-10-15: Stock meme video pins scheduled 4pm: Oct 23 meme-deadline-screenshot (College Planning -> College App Tracker), Oct 24 meme-cake-saturday (Pricing for Makers -> Cake Pricing), Oct 25 meme-custom-order (Etsy Seller Tips -> Order Tracker). Pinterest accepts video pins through Metricool.
- 2026-10-15: Plan created. Already scheduled: FreshlyMadeFL product pins 8pm Oct 14 - Nov 12; FreshlyMadeFL cheat sheets 1pm Oct 15-26; College Plan pins 10am Oct 16-24. Weekly Pinterest task created.
