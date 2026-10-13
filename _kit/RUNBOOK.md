# VIP Wireless – daily post runbook

Read this fully before making the day's post. Store facts, tone, deals and review rules
live in the Google Doc "VIP Wireless – Content Brief (read me first)" (Drive file id 19p4WsC-54k2_YgSHTAfZpzOqPbky8L1Q_3nfdT-OcQE) in the Drive folder
"VIP Wireless – Social Content" — read it every run; it overrides this file if they differ.

## Services to promote
Repairs (main focus), unlocked phones for sale, buying phones for cash, accessories,
Ria money transfer, SIM activation.

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
| Day | Instagram (+Facebook auto-share) | TikTok |
|---|---|---|
| Mon, Wed, Fri, Sat | Metricool schedules it after approval | Owner posts manually |
| Tue, Thu, Sun | Owner posts manually | Owner posts manually |
Metricool Free = 20 published posts/month per brand; 4 days/week stays under it.
Before scheduling, count this month's Metricool posts (getScheduledPosts + LOG.md); if 20
would be exceeded, treat the day as manual and say so.

## Steps each morning
1. Read the brief doc, `LOG.md` (what's been posted — don't repeat a topic within 7 days or
   a review within 21 days), and check Drive folders 1–3 for new photos/videos the owner
   added (prefer new real media when present).
2. Pick today's theme from the rotation below.
3. Make the content:
   - ALWAYS a vertical video, 1080x1920, 8–15s, built from `_kit/templates/video_template.html`
     (copy to `posts/YYYY-MM-DD/`, edit text/scenes/photos, render with `_kit/render.py video`).
     Keep key text inside the middle area (TikTok/Reels UI covers the bottom ~350px and right edge).
   - Optional still 1080x1350 from `_kit/templates/image_post_template.html` when a photo post fits better.
   - Captions: Instagram/Facebook caption and TikTok caption (shorter, 3–5 hashtags), local & friendly.
   - Look at a few rendered frames before sending; fix anything clipped or off-brand.
4. Save `posts/YYYY-MM-DD/` (video, optional image, captions.txt), commit as
   "VIP Wireless Bot <bot@vip-wireless.invalid>", push to main.
5. Send the owner (proactive, so it reaches the phone): the video + image files and a short
   message with both captions and "Reply 'approved' or tell me what to change."
   Open the message with the day's posting plan, in bold, on its own line:
   - Manual day (Tue/Thu/Sun): "📣 TODAY IS YOUR DAY TO POST — Instagram (with Share to
     Facebook on) and TikTok. I'll check in at 11 AM."
   - Metricool day (Mon/Wed/Fri/Sat): "✅ Metricool posts this to Instagram at 11 AM after you
     approve (15 min after approval if you approve later). You post TikTok."
6. Wait for the reply. Apply changes, re-render, re-push, re-send until approved.
7. After approval:
   - Metricool day: createScheduledPost for brand blogId 7406481, network instagram,
     type REEL with the raw.githubusercontent.com link to the mp4 (or POST with the image),
     autoPublish true, timezone America/New_York, time = 11:00 AM, or 15 minutes after
     approval if later. Confirm with the plannerUrl.
   - Manual day: remind the owner to post to Instagram from the IG app (Share to Facebook
     on) and to TikTok (add a trending sound / TikTok text-to-speech if they like).
   - Every day: TikTok is manual — remind the owner.
8. Append a line to `LOG.md` (date, theme, review used if any, Metricool or manual) and push.

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
- TikTok: suggest the owner add a trending sound at low volume; Instagram Reels via
  Metricool: add an Instagram-library track when available.
- Run series ("Phone Myth Monday", "15-Minute Fix") so people come back.
- Honest claims only: no fake urgency, no invented customers or numbers, reviews quoted as
  written, 15-minute fine print kept.
- Every morning message: one line on why this post should perform (hook/format), so the owner
  learns what works. Monthly, use Metricool analytics to see which formats won and do more of those.

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

Brand: black background, VIP red #D71928, white; Inter font; logo in `_kit/brand`.
