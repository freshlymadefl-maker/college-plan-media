# Amazon picks: weekly list + cover + socials

Owner (Nov 2): "auto create new ones consistently: create the list, make the cover (spread the images out a little better), share on socials including Pinterest. 1 a week for now. Keep in mind the holidays too."

- Storefront: https://www.amazon.com/shop/partyvibesdiy (Amazon Influencer storefront, tracking ID laurenfreshly-20). The owner is signed in to Amazon in her Chrome; we work through Claude in Chrome.
- SmartLink (bio link) has a "Shop My College Picks" button to the storefront: https://t-sml.mtrbio.com/public/smartlink/collegeplan . All our pins/posts point there.
- Brand: College Plan (parents of 8th-12th graders + college-bound students, Florida). Amazon picks are college-related, so they can go on every network (PINTEREST-PLAN.md "WHERE THINGS GO").
- Owner approved (Nov 2) that the weekly task SUBMITS the new Idea List and Collage itself (no draft step).

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
- Pinterest: 1 checklist pin (cp_amazon_pins.py, CTA "Shop my picks: tap the link") in an open 7:00am or 10:00am College Planning slot (board 1105985689682134542), pinLink = SmartLink. A 2nd pin later in the week with a different headline (e.g. "5 gifts teens actually want") is welcome if a slot is open.
- Instagram + Facebook: one Reel (the checklist rendered 1080x1920 with CTA "Shop my picks: link in bio", 7-10s, music via audioConfiguration videoVolume 0), funny/relatable parent hook first (e.g. "Me pretending I didn't just buy my senior a desk lamp for Christmas"). Open 6:00pm slot; one Amazon Reel per week max. Caption ends with "Shop my picks: link in bio 🛒", the Associates line and #ad. The Sunday TikTok task cross-posts it.

## Queued (build these first next run, then that week's own theme)
- Nothing queued.

## Log (newest first)
- 2026-11-09: Gifts for College Students (Dorm-Friendly) (week of Nov 16): Idea List + Collage "Dorm Gift Ideas" published. 6 products: ENITYA 22" XL back pillow with armrests B0DLGGGYMN, Magicteam white noise machine B07RWRJ4XW, DuomiW bedside caddy B07MBZ72XZ, LAPGEAR Home Office lap desk (oak) B089P33W98, Waitu wearable blanket hoodie B07Z5LGZJM, BedShelfie bedside/bunk shelf B09XLWQ85B. Collage light-blue stripes, 3x2 grid. Pins Nov 16 + Nov 18 7am (cp_amz_dorm_gifts, cp_amz_dorm_gifts_2), Reel IG+FB Nov 17 6pm (dorm-gifts-reel.mp4, music Good Time). Note: the collage editor tab froze once after picking a color with products on the canvas; setting Colors + Text BEFORE adding products worked. Adding products from the new Idea List (picker > Idea Lists tab) is faster than Browse history.
- 2026-11-02: Gifts for High School Teens (week of Nov 9) built from the owner's desktop app: Idea List + Collage "Teen Gift Ideas" published. 6 products: INIU 10000mAh charger B0CB1FW5FC, LED desk lamp B08923SXXP, CamelBak Chute Mag 32 oz B07XRXFWD4, Odokee sunrise clock B0DGXD6WVW, Bedsure sherpa throw B0CPS22JVK, Soundcore Select 4 Go B0DB1753RZ. Collage light-blue stripes, 3x2 grid. Pins Nov 9 + Nov 11 7am, Reel IG+FB Nov 10 6pm.
- 2026-11-01: 6 lists + 6 collages live: SAT + ACT Test Day Bag, College Visit Bag, Senior Year Study Desk Setup, Dorm Room Must-Haves, Gifts for College-Bound Seniors, Sorority Recruitment Bag.
