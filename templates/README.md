# College Plan design templates

- `carousel-example.html`: 7-slide Instagram carousel (1080x1350, 4:5). Each slide is a `<div class="s" id="sN">`.
  Render each slide with Playwright: open the file, `page.locator('#sN').screenshot(...)` at viewport 1080x1350.
  Reuse the CSS as-is; only change slide text/content. Fonts: Poppins (headings), Inter (body), Lora italic (accent).
- Colors: navy #0B2A4A, blue #5B8DC9, sky #EAF3FB, gold #B5A21F.
- `wordmark_navy.png` / `wordmark_white.png`: logo (must sit next to the HTML when rendering).
- `cheatsheet.html`: Bright Futures cheat sheet PDF source.
- `weekly-posts.html`: the 5 weekly post types (#p1 Mon deadlines, #p2 Tue school stats, #p3 Wed carousel cover, #p4 Thu reframe quote, #p5 Fri myth vs. fact). Same render method.

## Photo posts (templates/photo-posts.html)
- Generate a background with beehiiv `generate_image` (pub_851868ac-cd7b-4156-a1a0-dfac96c6e363, aspect 3:4, style photorealistic, preset pro). Generic Florida scenery / campus-style scenes only: no real school names, logos, mascots, signs or recognizable landmarks, no text in the image.
- The workspace can't download from beehiiv directly. Write `fetch/<name>.txt` with a line `photos/<name>.jpg <asset url>`, commit + push; the GitHub Action (.github/workflows/fetch-images.yml) downloads it into /photos and commits (~40s). Then `git pull`.
- Set the photo with style="--img:url(../photos/<name>.jpg)" on #ph1 (photo + quote) or #ph2 (photo + white card). Check readability after rendering.
- When scheduling in Metricool, set instagramData.isAiGenerated = true for posts that use an AI photo.

## Promo posts (templates/promo-posts.html)
- pr1 = free Bright Futures cheat sheet (uses cheatsheet-page-1/2.png mockups; regenerate those with pdftoppm if the PDF changes). pr2 = newsletter "what you get, by grade".
- Posted on Saturdays, alternating pr1 / pr2, 10:30am ET. Write a fresh caption each time; refresh the design every ~6 weeks (new headline, color variant or AI photo background) so it doesn't look repetitive.

## Newsletter auto-send (beehiiv API via GitHub Actions)
- Write `newsletter/drafts/<date>-<grade>.html` (body HTML, same structure as previous emails) and `<date>-<grade>.meta.json`
  (name, title, subtitle, subject, preview, segment_id, scheduled_at in UTC, seo_title, seo_description, tags),
  then `python3 scripts/make_queue_item.py <meta> <html>` -> `newsletter/queue/<name>.json`. Commit + push.
- `.github/workflows/send-newsletter.yml` posts each queued file to the beehiiv Create Post API (status confirmed, scheduled)
  using the repo secret BEEHIIV_API_KEY, then moves it to newsletter/sent/ (with beehiiv's response) or newsletter/failed/ (with the error).
  It also retries hourly. Check the result after ~1–2 min with `git pull`.
- Segments: Seniors seg_ec20379a-5aff-4412-81da-eaf22a6a390a · Juniors seg_4696667f-dbfa-42a6-a0b5-2f4a0b9ae687 · 8th–10th seg_b407009e-e7b1-415f-953d-51cd3b15791f
- Template with brand email theme: post_template_92da00b7-d6e0-447a-aded-93f586f22255
- The API stores the body as one raw-HTML block, so make_queue_item.py converts the draft into inline-styled email HTML
  (banner <img>, colored boxes, brand fonts). Don't use merge tags in the body (they aren't filled in there); the personal
  referral link lives in the publication email footer. Use a unique "slug" in meta. To unschedule a post, queue
  {"_action": "delete", "post_id": "post_..."} (file name starting with 0- so it runs first).
