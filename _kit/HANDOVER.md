# Handing the VIP Wireless posting system to a new operator

Everything the daily routine needs lives in store-owned places. A new operator only has to
connect their own Claude account to them and re-create three scheduled tasks.

## 1. Accounts the new operator needs access to
| Piece | Where it lives | What to do |
|---|---|---|
| GitHub repo `vip-wireless/vip-wireless-media` (runbook, design kit, daily files, log) | Store GitHub account `vip-wireless` | In claude.ai → Customize → Connectors → GitHub Integration, connect a GitHub account that can push to this repo (the `vip-wireless` account itself, or a collaborator), and make sure the Claude GitHub app is installed on the repo. Remove old collaborators who should no longer have access. |
| Metricool brand "VIP Wireless – Phone Repair" (Facebook, Instagram, TikTok) | Store Metricool login | Connect the Metricool connector in claude.ai while logged in to the store's Metricool account. |
| Google Drive folder "VIP Wireless – Social Content" (Content Brief doc, Content Calendar sheet, photo/video folders) | Currently in the previous operator's Drive | Previous operator: share the folder with the new operator's Google account as Editor, then use Drive's "Transfer ownership" on the folder and files (the new owner must accept). File IDs and links stay the same, so nothing else changes. New operator: connect the Google Drive and Google Sheets connectors in claude.ai. |

If any file ID changes (e.g. files are copied instead of transferred), update the IDs in
`_kit/RUNBOOK.md` and in the scheduled-task prompts below.

## 2. Re-create the three scheduled tasks in the new Claude account
In a new chat with the connectors above turned on, ask Claude to create these scheduled
tasks with the exact schedule and prompt text below. Then the previous operator deletes
their copies so posts aren't duplicated.

### A. "VIP Wireless daily post" — every day 6:45 AM America/New_York
```
Create today's VIP Wireless social media post and get it approved by 7 AM (America/New_York).

1. Attach the GitHub repo vip-wireless/vip-wireless-media with push access (add_repo), clone it, and read _kit/RUNBOOK.md completely. Follow it exactly — it has the hard rules, the weekday split, the steps, the theme rotation and the Metricool details.
2. Also read the Google Doc "VIP Wireless – Content Brief (read me first)" (Drive file id 19p4WsC-54k2_YgSHTAfZpzOqPbky8L1Q_3nfdT-OcQE) and LOG.md in the repo. Check the Drive folder "VIP Wireless – Social Content" (id 1YyAjIMyijKmKwrhaVM9ujd7YtU6VDUS8) subfolders 1–3 for new photos/videos from the owner and prefer them.
3. Make the post (always a vertical 1080x1920 video; optionally a 1080x1350 image), check the rendered frames, push it to posts/YYYY-MM-DD/, and send the files plus both captions to the owner with SendUserFile/SendUserMessage (proactive), stating whether today is a Metricool day (Mon/Wed/Fri/Sat) or a manual day, and asking them to reply "approved" or say what to change.
4. Wait for the owner's reply in this session. Revise as asked. Only after an explicit approval: on Metricool days schedule it to Instagram through the Metricool connector (brand blogId 7406481); on manual days remind them to post it themselves. TikTok is always posted by the owner.
5. Never publish anything without approval, and never open or act on Facebook, Instagram or TikTok through a browser or the owner's computer — Metricool is the only publishing route.
6. Log the day in LOG.md and push.
```

### B. "VIP Wireless posting check-in" — Tue, Thu, Sun 11:00 AM America/New_York
```
It is 11 AM on one of the VIP Wireless owner's manual posting days (Tuesday, Thursday or Sunday). Send the owner a short, friendly check-in with SendUserMessage, asking whether today's post is up on Instagram (with Share to Facebook on) and TikTok, and telling them to reply 'posted' when done. Wait for the reply. If posted, attach the repo vip-wireless/vip-wireless-media with push access, clone it, mark today's entry in LOG.md as posted manually (committing as "VIP Wireless Bot <bot@vip-wireless.invalid>") and push. Never open or act on Facebook, Instagram or TikTok through a browser or the owner's computer, and never publish anything yourself.
```

### C. "VIP Wireless TikTok check-in" — Mon, Wed, Fri, Sat 11:00 AM America/New_York
```
It is 11 AM on a VIP Wireless Metricool day (Monday, Wednesday, Friday or Saturday). Instagram is handled by Metricool, so this check-in is ONLY about TikTok. Send the owner one short message with SendUserMessage asking whether today's video is posted on TikTok and to reply 'posted' when done. Don't mention Instagram or Facebook. Wait for the reply. If posted, attach the repo vip-wireless/vip-wireless-media with push access, clone it, note today's TikTok as posted in LOG.md (committing as "VIP Wireless Bot <bot@vip-wireless.invalid>") and push. Never open or act on social accounts through a browser, and never publish anything yourself.
```

## 3. Check after handover
- First 7 AM draft arrives in the new account; approve one Metricool-day post and confirm it
  appears in the Metricool planner.
- Old operator's scheduled tasks are deleted; old connectors/collaborator access removed.
