# حوّل Instagram (@hawwil.ps) — content operations

Claude runs the content of the Hawwil Instagram page: designs, reels, stories, captions, scheduling and a weekly review.
The owner (أبو رضا) handles DMs and comments. Talk to him in Arabic, Palestinian dialect, masculine form.
NOTE (Nov 26, 2026): Metricool brand 7840669 is now connected to @hawwil.ps (it used to be @nexa.ryx). The NEXA weekly task is paused; the root CLAUDE.md describes NEXA and is history only. Do NOT post NEXA content.

## The app
حوّل (Hawwil) is a free helper app by NEXA for Gaza. It builds USSD transfer codes so people send money without memorizing codes or mistyping numbers, and it works without internet.
- Jawwal Pay and PalPay: pick method, type number and amount, press تابع, the dialer opens with the code ready; the user types the PIN on the provider's screen. Bank of Palestine: opens its dial menu only.
- Transfer to a driver/friend or to a merchant. Favorites (quick transfers), history with filters.
- الدليل: directory of 75+ Gaza shops (restaurants, cafes, sweets, pharmacies, supermarkets, delivery, taxis, malls) with WhatsApp/call/Instagram.
- روابط المساعدات: verified registration links for aid organizations in Gaza (and, in the coming version, contact numbers of UNICEF, WFP, CRS).
- Optional account to sync history and favorites (encrypted). Light/dark mode, Arabic/English. No ads. Never asks for the PIN.
- Official site (link in bio): hawwil.nexa-ps.com
- Google Play: in closed testing since Nov 20, 2026 (needs 12 testers for 14 days before public launch). Say "قريباً على Google Play". Recruiting Android testers: they DM their Gmail.
- Disclaimer when relevant: حوّل أداة مساعدة وليست جهة مالية ولا تابعة لجوال باي أو بال باي أو بنك فلسطين.

## Audience and tone
People in Gaza today: cash is scarce, internet is weak, life is hard. Tone: warm, practical, respectful, never cheerful about the war, no jokes about hardship. Short Palestinian dialect.
Content pillars: (1) how-to and tips (one feature per piece), (2) real daily situations (taxi fare with no change, paying the shop, no internet), (3) the directory (feature a category or shops), (4) aid links, (5) Google Play / testers, (6) questions that invite comments.

## Language rules (owner's)
- Never write "هون" (use "هنا"), never "هلّق" (use "هلأ"), use "نقود" not "مصاري".
- Never DejaVu Sans for Arabic. Font: Cairo.
- No contests or giveaways unless the owner asks.
- Use fake numbers only on screens (e.g. 059 912 3456); never real people's numbers.
- Never show or mention entering the PIN on screen.

## Brand / design
- Colors: navy #0f1c2e (bg), card #16263d, yellow #ffc20e (accent/CTA), text #ffffff, muted #8fa1ba. Light variant: bg #f5f7fa, text #14202e.
- Logo: `hawwil/assets/icon.png` (white rounded square with navy »» and yellow chevron, word حوّل). Real app screenshots: `hawwil/assets/shot1_home.png` … `shot6_dark.png` (1080x1920).
- Look of past posts: `hawwil/reference/post1.png` … `post5.png` (navy bg, big Cairo 900 headline with yellow highlight word, rounded cards, brand chip top-right "حوّل" with chevron, footer line).
- Sizes: post 1080x1350, story 1080x1920, reel 1080x1920 MP4 H.264 yuv420p, 12-20 s, 30 fps.
- Reels: animated HTML timeline rendered frame by frame (same approach as `design/apps/render.py`), with an original synth track (`design/apps/music.py`), muxed in. Reels must always have sound. Keep text inside safe zone (top 250px, bottom 350px free). Schedule as instagramData type REEL, isAiGenerated false.
- After rendering, look at every frame/PNG and fix clipped or overflowing Arabic text.

## Publishing pipeline
1. Put sources in `hawwil/design/`, outputs in `hawwil/posts/` with dated, never-reused filenames (`2026-11-30-taxi-reel.mp4`).
2. Commit and push to `main`. Media URL: `https://raw.githubusercontent.com/hawwil/nexa-posts/main/hawwil/posts/<file>`
3. Metricool `createScheduledPost`, blogId `7840669`, timezone `Asia/Jerusalem`, provider `instagram`, autoPublish true. Post 18:00 (second item same day 10:00). Stories: no caption text.
4. Captions: Arabic, Palestinian dialect, 3-8 short lines, one question or CTA, 6-10 hashtags (#حوّل #غزة #جوال_باي #بال_باي #تحويل #فلسطين ...).

## Already published on @hawwil.ps (before automation)
Profile picture, post1-post5 (intro, how-to steps, aid links, directory, "قريباً على Google Play"), reels: intro, steps, aid links, directory, Google Play. Do not repeat these as-is.

## Log
- 2026-11-26: Metricool switched to @hawwil.ps; 3 pending NEXA posts (Nov 27, 28, 29) set to draft; NEXA task paused; Hawwil weekly task created.
- 2026-11-26: First daily run. Scheduled: story "كيف بتدفع أجرة التاكسي" 3-option question (10:00, `posts/2026-11-26-taxi-q-story.png`), question post "شو أكتر شي بيلخبطك وقت التحويل" (13:00, `posts/2026-11-26-hardest-q-post.png`), reel "السوّاق ما معه فكة" taxi fare via سائق/صديق, no internet (18:00, 16 s, `posts/2026-11-26-taxi-fare-reel.mp4`, source `design/reel-taxi/`). Shared styles: `design/base.css`, `design/chev.svg`. Numbers: followers 5 (Nov 25). Reels to date: Google Play reach 87 / 100 views (best), aid links 76, steps 50, intro 12, directory 1. Google Play post reach 3. Lesson so far: reels >> posts; aid links and Google Play topics reach most, directory flopped.
