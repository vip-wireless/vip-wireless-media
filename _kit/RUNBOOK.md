# VIP Wireless – daily post runbook

Read this fully before making the day's post. Store facts, tone, deals and review rules
live in the Google Doc "VIP Wireless – Content Brief (read me first)" (Drive file id 19p4WsC-54k2_YgSHTAfZpzOqPbky8L1Q_3nfdT-OcQE) in the Drive folder
"VIP Wireless – Social Content" — read it every run; it overrides this file if they differ.

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

## Theme rotation (repeat)
1. 15-minute screen/battery fix
2. Google review spotlight (one approved review)
3. Phone-care tip (battery health, charging port lint, case & protector, water damage do's/don'ts)
4. Real repair / before-after (owner's photos or videos when available)
5. Current deal (free screen protector with every repair)
6. Android repairs too (Samsung/Galaxy etc.)
7. Store & neighborhood: walk-ins welcome, hours, accessories, Ria transfer, SIM activation

Brand: black background, VIP red #D71928, white; Inter font; logo in `_kit/brand`.
