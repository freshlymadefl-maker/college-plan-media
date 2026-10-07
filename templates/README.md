# College Plan design templates

- `carousel-example.html`: 7-slide Instagram carousel (1080x1350, 4:5). Each slide is a `<div class="s" id="sN">`.
  Render each slide with Playwright: open the file, `page.locator('#sN').screenshot(...)` at viewport 1080x1350.
  Reuse the CSS as-is; only change slide text/content. Fonts: Poppins (headings), Inter (body), Lora italic (accent).
- Colors: navy #0B2A4A, blue #5B8DC9, sky #EAF3FB, gold #B5A21F.
- `wordmark_navy.png` / `wordmark_white.png`: logo (must sit next to the HTML when rendering).
- `cheatsheet.html`: Bright Futures cheat sheet PDF source.
- `weekly-posts.html`: the 5 weekly post types (#p1 Mon deadlines, #p2 Tue school stats, #p3 Wed carousel cover, #p4 Thu reframe quote, #p5 Fri myth vs. fact). Same render method.
