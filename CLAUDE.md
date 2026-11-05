# NEXA Instagram (@nexa.ryx) — content operations

Claude runs the content of the NEXA Instagram page: designs, captions, scheduling and weekly analytics review.
The owner (أبو رضا) handles DMs, comments and customer orders. Talk to him in Arabic, Palestinian dialect, masculine form.

## Business
NEXA is a digital-services store: official subscriptions with full warranty at best prices (Canva Pro, Adobe, Gemini, Claude, others),
and buying any digital product for customers who lack a card. Payment: Visa, PayPal, USDT. Orders via Instagram DM.

## Goal
Grow from 61 followers (Nov 3, 2026) to 300 in 30 days, plus first real orders from the page.
Content plan doc: https://claude.ai/artifact/DyqThzD4uM3YuyzWbqWnNG

## Publishing pipeline
1. Design PNGs (see Design system), commit to `posts/` in this repo, push to `main`.
2. Media URL: `https://raw.githubusercontent.com/hawwil/nexa-posts/main/posts/<file>`
3. Schedule with Metricool `createScheduledPost`, blogId `7840669`, timezone `Asia/Jerusalem`, provider `instagram`.
4. Best times from Metricool: 10:00 and 18:00 local. Default to 18:00.
5. Never commit with a filename that already exists: use a new name (e.g. `-v2`) so URLs stay stable.

## Design system (files in `design/`)
- Fonts: Cairo (headings 800-900, body 500-700). Never DejaVu Sans for Arabic. The sandbox has no Arabic fonts:
  `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --sparse https://github.com/google/fonts ~/google/fonts && cd ~/google/fonts && git sparse-checkout set ofl/cairo`
  then copy the .ttf to `~/.fonts` and run `fc-cache -f`.
- Render: HTML/CSS at exact size, `google-chrome --headless=new --no-sandbox --hide-scrollbars --allow-file-access-from-files --screenshot=out.png --window-size=1080,1350 file://...`
- Sizes: post 1080x1350, story 1080x1920.
- Colors: background #06040c, text #f5f0ff, purple #7c3aed → #a855f7, accent #c084fc, muted #a99bc7.
- Layout: right-aligned RTL, 80px side margins, logo band at top (`logo.png`, faded with mask), pill tag, big headline,
  one supporting line, content in rounded translucent purple cards, footer line with CTA/info left and @nexa.ryx.
- `base2.css` is the shared stylesheet; `gen.py` builds a numbered carousel; `p1.html`, `p2.html`, `story.html` are references.
- After rendering, look at every PNG and fix clipped text (gradient-clipped headlines need padding-bottom) before publishing.

## Owner's tasks (remind him when relevant)
- Reels that need screen recordings: write him a short script; he films.
- Reply to comments within the first hour and DMs the same day.
- Contest 1 (Canva Pro month) draw on Monday Nov 9, 2026: he picks the winner and sends the handle; Claude designs the winner post.

## Log
- 2026-11-03: Scheduled week 1: intro (Nov 4 10:00), contest (Nov 5 18:00), AI tools carousel (Nov 7 18:00), last-chance story (Nov 8 18:00).
- 2026-11-05: Weekly review: 61 followers (0 gained/lost in 7d). Only intro post live (Nov 4): reach 7, views 17, 2 likes, 0 follows. Account reach 7d ~12. Too early to rank post types; contest goes live tonight.
  Scheduled week 2: draw-day story (Nov 9 10:00), Canva free vs Pro carousel (Nov 10 18:00), how to order in 3 steps (Nov 12 18:00), "we pay for you" (Nov 14 18:00), ask-which-subscription story (Nov 15 18:00).
  Owner to film: Gemini CV reel (Nov 11) and Claude 3-things reel (Nov 13). Winner post pending his handle on Nov 9. Week-2 designs: `design/week2.py`.
