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
