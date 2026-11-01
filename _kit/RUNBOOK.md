# VIP Wireless – daily post runbook

Read this fully before making the day's post. Store facts, tone, deals and review rules
live in the Google Doc "VIP Wireless – Content Brief (read me first)" (Drive file id 19p4WsC-54k2_YgSHTAfZpzOqPbky8L1Q_3nfdT-OcQE) in the Drive folder
"VIP Wireless – Social Content" — read it every run; it overrides this file if they differ.

## Services to promote
Repairs (main focus), unlocked phones for sale, buying phones for cash, accessories,
Ria money transfer, SIM activation, and phone financing / lease-to-own through Acima (owner, 2026-10-21).

## Hard rules
- Nothing is published without the owner's explicit approval in chat that day.
- Never open, log into, or act on Facebook, Instagram or TikTok through any browser or the
  owner's computer. The ONLY publishing route is the Metricool connector.
- Never use a review that mentions the owner by name. Never claim "genuine Apple parts".
  Never show prices quoted in reviews.
- Any use of the 15-minute promise must carry the fine print: most iPhone screens and
  batteries; back glass and other repairs may take longer and depend on parts availability.
- Prefer the store's own photos/videos (Drive folders 1–3, `_kit/photos`) over stock.

## Weekly split (America/New_York)
Owner's instruction (2026-11-01): posts are made Mon–Fri (Mon, Tue, Wed, Thu, Fri).
Sat and Sun are the owner's own days — make nothing, send nothing, and skip them in the rotation.
| Day | Instagram (+Facebook auto-share) | TikTok |
|---|---|---|
| Mon–Fri | Metricool schedules it after approval (unless the monthly limit is reached, see below) | Owner posts manually |
| Sat, Sun | No post from us (owner's day) | No post from us |
If a run starts on Sat/Sun, stop without making or sending anything.
(History: Mon/Wed/Fri/Sat from 2026-10-16; every day Oct 22–31, 2026; Mon–Fri from 2026-11-01.)

## Metricool monthly limit (owner, 2026-11-01)
Metricool Free = 20 published posts per calendar month per brand. Mon–Fri is ~21–23 posts a
month, so the limit is usually reached near the end of the month.
Before sending the draft, count this month's Metricool posts (getScheduledPosts + LOG.md).
If 20 are already used: STILL make the post and send it to the owner as usual, but open the
message with, in bold on its own line: "⚠️ Metricool has reached its 20-post limit for this
month — please post this one to Instagram yourself (and TikTok as usual)." Do not schedule it
in Metricool, even after approval. Log it as "Metricool limit reached — owner posts IG + TikTok".

## Format rotation: video one day, image the next (owner, 2026-11-01)
Alternate strictly: check the last post in LOG.md — if it was a video, today is an IMAGE post
(1080x1350); if it was an image, today is a VIDEO (1080x1920). Log the format in each LOG.md
entry ("Format: VIDEO" or "Format: IMAGE"). On image days send only the image (the owner can
post it to TikTok as a photo post).

## Steps each morning
1. Read the brief doc, `LOG.md` (what's been posted — don't repeat a topic within 7 days or
   a review within 21 days), and check Drive folders 1–3 for new photos/videos the owner
   added (prefer new real media when present).
2. Pick today's theme from the rotation below.
3. Make the content:
   - Video or image per the Format rotation above (image posts: 1080x1350, bold
     text + a real photo). Make posts interesting (strong hook, stickers, cards), not templated.
     `photo_07_repair_in_progress.jpg` shows the BACK of a screen part — never use it as a
     "broken screen"/repair hero shot; use `photo_03_before_after_cracked_iphone.jpg` or owner photos.
   - Video posts: vertical video, 1080x1920, 8–15s, built from `_kit/templates/video_template.html`
     (DARK), `_kit/templates/video_template_light.html` (LIGHT) or
     `_kit/templates/video_template_seasonal.html` (AUTUMN / HALLOWEEN via body class)
     (copy to `posts/YYYY-MM-DD/`, fix the logo path to `../../_kit/brand/logo_wide.jpg`,
     edit text/scenes/photos, render with `_kit/render.py video`).
   - Mix DARK and LIGHT (owner, 2026-10-16: "too much dark doesn't look good all the time").
     Check the Look column in LOG.md: never more than 2 posts in a row in the same look, and aim
     for roughly half light; in season, rotate AUTUMN/HALLOWEEN in too (see Design variety). Image posts have the same pair (`image_post_template_light.html`).
     Keep key text inside the middle area (TikTok/Reels UI covers the bottom ~350px and right edge).
   - Image posts: 1080x1350 from `_kit/templates/image_post_template.html` (DARK) or `image_post_template_light.html` (LIGHT).
   - Captions: Instagram/Facebook caption and TikTok caption (shorter, 3–5 hashtags), local & friendly.
   - Look at a few rendered frames before sending; fix anything clipped or off-brand.
4. Save `posts/YYYY-MM-DD/` (today's video or image, captions.txt), commit as
   "VIP Wireless Bot <bot@vip-wireless.invalid>", push to main.
5. Send the owner (proactive, so it reaches the phone): today's video or image file and a short
   message with both captions and "Reply 'approved' or tell me what to change."
   Open the message with the day's posting plan, in bold, on its own line:
   "✅ Metricool posts this to Instagram at 11 AM after you approve (15 min after approval if
   you approve later). You post TikTok."
6. Wait for the reply. Apply changes, re-render, re-push, re-send until approved.
7. After approval:
   - Metricool day: createScheduledPost for brand blogId 7406481, network instagram,
     type REEL with the raw.githubusercontent.com link to the mp4 (or POST with the image),
     autoPublish true, timezone America/New_York, time = 11:00 AM, or 15 minutes after
     approval if later. Confirm with the plannerUrl.
   - TikTok is always manual — remind the owner (add a sound / TikTok text-to-speech).
8. Update the Google Sheet "VIP Wireless – Content Calendar" (id
   1bQR_DHjF2qcL37Y8VMgzoplbJ3a5c0vYcsRmh-uv4-A) in place with the Google Sheets connector:
   today's row → Planned content (what was made), Post type, Status (Draft sent / Approved /
   Scheduled in Metricool / Posted), Notes. Add planned future items (approved deals,
   countdowns, deal ideas awaiting a decision) to their rows. Never recreate the sheet; if
   the Sheets connector isn't available, skip this and tell the owner once.
9. Append a line to `LOG.md` (date, theme, look DARK/LIGHT, review used if any, channel) and push.

## Trends, events and deal ideas (every run)
- Before picking the theme, do a quick web search for what's trending right now that a local
  phone shop can ride: TikTok/Instagram trend formats and memes, new iPhone/Samsung/iOS
  releases or bugs, viral phone moments, weather (snow, rain, heat = phone tips), local
  Columbus news. Use a trend when it fits naturally; otherwise follow the rotation.
- Event calendar: Halloween, Thanksgiving, Black Friday / Cyber Monday, Christmas, New Year,
  Valentine's Day, Super Bowl, Mother's/Father's Day, back-to-school, July 4th, new iPhone
  launch (September), tax-refund season, and Columbus game days (search the current Ohio
  State football schedule). For game days use generic "game day" wording and colors —
  no team names, logos or trademarks in boost-ready posts.
- Deal ideas: when an event or game day is 10–21 days away, add a "💡 Deal idea" section to
  that morning's message with 2–3 concrete promotion options (what, dates, rough cost to the
  store, sample hook) and ask whether to run one. Suggest each event once (note it in
  LOG.md); remind once more ~5 days before if no answer.
- Countdown series for big-sale events (Black Friday, Christmas, approved deals, iPhone
  launch): when the owner approves a deal, plan a countdown — e.g. 7 days, 3 days, 1 day,
  "today's the day", "last chance" — in the normal daily slots (they replace the rotation on
  those days). Countdown visuals can show the number big ("3 DAYS"); they are time-bound, so
  tag them Organic. Lay out the countdown dates in the morning message when the deal is
  approved.
- Never announce, imply or advertise a deal the owner hasn't approved in chat. Approved deals
  go into the brief/LOG.md with start and end dates.

## Reach playbook (apply to every post)
Goal: stop the scroll, get watched to the end, get saved/shared/commented. Engagement and
watch time drive reach on all three platforms.
- HOOK in the first 1–2 seconds: big on-screen text that creates curiosity or calls out the
  viewer ("Your iPhone battery is lying to you", "Don't pay $300 for this", "POV: you dropped
  your phone at 9 AM and need it by lunch"). No logo intro — logo stays small in the corner.
- Keep videos 7–15s, one idea, a visual change every 1–2s (cuts, zooms, text pops). End on a
  loopable frame or a payoff so people rewatch.
- Real footage beats graphics: when the owner has clips/photos (screen swaps, timers, cracked
  phones, the shop), build around them; text-only templates are the fallback.
- Give value people save/share: quick tips, myths vs facts, "3 signs your battery needs
  replacing", "don't do this if your phone gets wet".
- Formats to rotate: POV, before → after, timer/race ("15:00 on the clock"), myth vs fact,
  "things phone shops won't tell you", guess-the-damage, review reaction, day-in-the-shop,
  customer question answered.
- Copy: short punchy lines, conversational, one emoji per line max, no corporate words.
  First caption line = the hook again (it shows before "more"). End with ONE clear CTA
  (walk in today / save this / send to the friend with the cracked screen) or a question
  that invites comments ("What's the worst crack you've ever had? 👇").
- Local SEO: say "Columbus" / "Whitehall" / "iPhone screen repair" in on-screen text and
  caption (TikTok and Instagram search read them). 3–5 targeted hashtags, not 30.
- Sound: see the Music section below.
- Run series ("Phone Myth Monday", "15-Minute Fix") so people come back.
- Honest claims only: no fake urgency, no invented customers or numbers, reviews quoted as
  written, 15-minute fine print kept.
- Every morning message: one line on why this post should perform (hook/format), so the owner
  learns what works. Monthly, use Metricool analytics to see which formats won and do more of those.

## Two kinds of posts: boost-ready and organic
Tag every post in the morning message and LOG.md as **Boost-ready** or **Organic**.
Aim for roughly half boost-ready (at least 3 a week); the owner may test-boost any of them.
- Boost-ready posts: phone number on the end card/caption (not every scene); short legible
  text; evergreen (no "today"/dates burned into the video; timing goes in the caption);
  no "best/cheapest/guaranteed"; commercial-safe music only (TikTok Commercial Music Library,
  Instagram library tracks added via Metricool); no customer faces/names/personal screens.
- Organic posts: free to chase reach — trending sounds (even popular songs), "today"/timely
  hooks, memes, bolder humor, trends, stitches/duets ideas for the owner.
- Both kinds: still images are fine too (a clean graphic with the phone number works well
  for Instagram/Facebook). Always truthful — no fake reviews, invented customers, made-up
  numbers or stock, and keep the 15-minute fine print. Call-first rule still applies.

## Music
- Metricool days (Instagram Reel): add a track from Instagram's library through Metricool's
  audioConfiguration (pass a song/artist search term as audioId; set videoVolume 100,
  audioVolume ~25–40 so on-screen text/voice stays clear). If Metricool rejects the audio
  (e.g., account not eligible), schedule without it and tell the owner.
- TikTok: name 1–2 specific sound suggestions in the morning message
  (commercial-library ones for boost-ready posts; trending ones allowed for organic posts).

## Voiceover (owner wants a natural AI voice on every video, from 2026-10-14)
- Write a ~12–15s voiceover script timed to the scenes (hook in the first 2s, ends with the
  phone number). Spoken lines may say "about 15 minutes"; the fine print stays on screen.
- If a text-to-speech connector is available (owner plans to connect Speko), generate a
  natural-sounding voice (friendly, conversational; not robotic), get the audio file into the
  workspace, and mix it into the mp4 with ffmpeg (voice ~100%, leave room for music).
  Check timing against the rendered scenes; re-time scenes if a line runs long.
  On Metricool days keep any Instagram library track low (audioVolume ~15–20) under the voice.
- If no TTS connector works (not connected, or its audio can't be downloaded here), send the
  video without voice, include the script in the morning message, and tell the owner once in
  that message why (and that TikTok's built-in Text-to-speech can voice it). Never use a
  robotic fallback like espeak.

## Theme rotation (repeat)
1. 15-minute screen/battery fix
2. Google review spotlight (one approved review)
3. Phone-care tip (battery health, charging port lint, case & protector, water damage do's/don'ts)
4. Real repair / before-after (owner's photos or videos when available)
5. Current deal (free screen protector with every repair)
6. Android repairs too (Samsung/Galaxy etc.)
7. Store & neighborhood: walk-ins welcome, hours, accessories, Ria transfer, SIM activation
8. Unlocked phones for sale (show real in-store phones/boxes when available, e.g. `_kit/photos/photo_06_new_iphones_in_box.jpg`)
9. We buy phones: sell your old phone for cash at the store (bring it in for a quote)
10. FREE PHONE offer (see below)

Free phone offer (owner, 2026-11-01, ongoing until the owner says it ends): customers who
start a NEW ACTIVATION and pay 3 MONTHS of their bill in advance get a FREE PHONE.
Feature it regularly (about once a week, Boost-ready) and mention it in SIM-activation and
phones-for-sale posts. Wording: "Get a FREE phone when you pay 3 months in advance on a new
activation" / "New activation + 3 months paid = FREE phone". Say only what the owner gave.
Owner (2026-11-01): NEVER name the carrier or the phone models (they change week to week) —
no plan prices, dollar values or end date either. The goal is PHONE CALLS: make it Boost-ready,
big "FREE PHONE" hook, phone number large on screen and in the first line of the caption,
CTA "Call 380-271-8085 to claim yours" / "Call or walk in today". Don't combine it with
Acima wording in the same headline (the free phone isn't financed).
Visuals: show THREE budget Android phones together (the kind usually on the offer — Galaxy
A16-style, Moto G 5G / Moto G Play-style) so no single model is the focus. Never write model
names on screen or in captions. Owner (2026-11-01): use the ready-made hero image EVERY time —
`_kit/photos/offer_phones/free_phone_hero.png` (1080x1350; three budget Androids on a white
podium, light-blue background, empty top third for the headline). Backup/variety:
`free_phone_hero_alt.png`. For 1080x1920 videos, place it centered and extend the background
above/below. Transparent cutouts (owner OK'd removing the background and using any
background that fits the post): `free_phone_cutout.png` (three phones, no podium),
`free_phone_cutout_alt.png`, `free_phone_cutout_podium.png` (with the white podium) — put them
on any brand/LIGHT/DARK/seasonal background, add glow, shadow, confetti, a "FREE" badge, etc.
Don't regenerate or download other phone photos unless the owner asks; if the
owner adds real photos of the offer phones to Drive folders 1–3, those may be used too.

Financing (owner, 2026-10-21): customers can finance / lease-to-own a phone through Acima.
Mention it in EVERY post or video about buying a phone from us (phones for sale, unlocked
phones, new iPhones/Androids) — on screen and in the caption, e.g. "Financing available
through Acima" / "Lease-to-own options with Acima". Keep it generic: no payment amounts,
rates, "$0 down", "no credit check/needed" or approval promises, and no Acima logo — just
the name in text. "Ask us about Acima" / "call 380-271-8085" is the CTA for details.

Sales & buying posts: we sell new and used iPhones and Android phones (mostly Apple, Samsung,
Motorola) and we buy unlocked phones. In posts say "iPhones & Androids" and always send
people to call for current stock ("Call 380-271-8085 to check what's in stock today"). Never invent prices, stock, models or conditions; only name specific
models/prices/offers the owner has given. For buying: "call or walk in for a quote", no
promised amounts.

Call-first rule (all posts): the goal is to get people to CALL 380-271-8085 or walk in.
- Never mention what we don't repair, buy or sell, or any conditions/limits on repairs or
  phones we buy. Keep it open: "Not sure what's wrong? Call us and we'll take a look."
- But don't over-promise either: no "we fix anything", "any phone, any problem" or
  "we buy every phone". Invite the question instead.
- Every post's CTA leads with the phone number (call / text-friendly wording) plus "or walk in".

## Design variety (owner, 2026-10-21)
The owner likes the designs but plain black/white with red every day "feels all the same".
- Use seasonal colors regularly: `_kit/templates/video_template_seasonal.html` has two looks
  set by the body class — `autumn` (orange/amber/brown with falling leaves) and `halloween`
  (purple night, glowing moon, flying bats, orange accents). Use HALLOWEEN for all Halloween
  deal/countdown posts Oct 24–31 and often in late October; AUTUMN through November
  (Thanksgiving). Later: winter/holiday colors in December, etc. — add a new body-class
  palette to the seasonal template when a new season starts.
- Log the look as DARK, LIGHT, AUTUMN or HALLOWEEN. Never 3 posts in a row with the same
  look; in season, roughly every other post should be seasonal.
- Vary the animation too: the seasonal template has pop-in / slide-in / drop-in scene entries
  and a pulsing phone number; mix entries, zooms on photos, counters, text pops so videos
  don't feel templated. Keep text legible (big, high contrast) and inside the safe area.
- Keep the VIP logo (black pill) and a touch of VIP red on every post so it's still on-brand.

### HALLOWEEN STORY POSTS (owner, 2026-10-23) — every post Oct 24–31, 2026
- Look HALLOWEEN on all of them (video or image): genuinely SCARY/spooky — deep purple/black night,
  orange glow, fog, moon, bats, flicker, shadows. Spooky-fun, not gore. Keep VIP red + logo pill small.
- Tell a tiny STORY. The first 1 second must grab attention with motion and NO talk about repairs or
  services: start mid-scene (e.g. "3:07 AM…" on screen, phone glowing on a nightstand, lights flicker,
  a ghost swoops in and SMASHES the screen — crack draws in + screen shake). Only after the twist
  (~3–5s) reveal the punchline and the deal/service, then the phone-number end card.
- Story ideas (one per day, don't repeat): ghost cracks the screen; zombie hand grabs the phone from
  under the bed and drops it; vampire's phone at 1% at midnight ("battery's dying… like me");
  haunted mirror cracks = phone cracks; witch's cauldron drops the phone in (water-damage tip);
  three candles blown out one by one = "3 DAYS LEFT"; jack-o'-lantern carved face reveals "TODAY".
- Image posts: tell the story as a 2–3 panel comic strip (setup → spooky twist → deal/CTA).
- Deals (approved, see LOG.md 2026-10-13): Scary Screen = UP TO $50 off screen repairs Oct 24–31,
  amount depends on model — always "up to" + "call for your model". Costume deal Oct 31 ONLY: come in
  costume → case + screen protector for $25 (normally $40). Countdown: Sat 24 launch, Wed 28 "3 days",
  Fri 30 "tomorrow", Sat 31 "today". Other days Oct 25–29: Halloween stories that still mention
  Scary Screen. Keep the 15-minute fine print whenever 15 min is used.
- SOUND (owner, 2026-10-23): Halloween posts must use SPOOKY / ghostly background sound — NOT the
  usual 'Make It' track. Instagram via Metricool audioConfiguration: search terms like "Halloween",
  "spooky", "horror", "haunted", "creepy" (if several match, pick a clearly spooky instrumental from the
  candidates and use its numeric id). Also bake spooky sound effects into the mp4 itself with ffmpeg
  (low eerie drone/wind, whoosh when the ghost flies in, glass-crack hit when the screen breaks) so the
  scare lands even without a library track. TikTok: suggest a spooky/trending Halloween sound.
- SCENE-SYNCED SFX (owner, 2026-10-23): don't just lay one smooth spooky bed — change the sound with
  the scene, several effects per video, each timed to what's on screen: lights flicker → flicker buzz;
  phone vibrates → phone_buzz; ghost flies in → whoosh; screen breaks → crack + sting; tension → heartbeat;
  storm/lightning → thunder; door/floor → creak; reveal/deal → ding; drone/wind low underneath.
  Kit: `_kit/sfx/` (wavs synthesized by `make_sfx.py`; re-run it if missing). After rendering:
  `python3 _kit/sfx/mix.py silent.mp4 final.mp4 drone@0:0.35 flicker@0.6 whoosh@1.4 crack@2.2:1 ...`
  (name@seconds[:volume]). Read the scene timings from the HTML animation delays. On Instagram keep any
  library track low (audioVolume ~15–20) so the effects stay audible; add new effects to make_sfx.py as needed.

Brand: VIP red #D71928 with either a black (DARK) or warm off-white #F7F5F2 (LIGHT) background, or a seasonal palette (see Design variety);
Inter font; logo in `_kit/brand` (on LIGHT it sits in a black pill, as in the light templates).
