# Claude: setting up / taking over the VIP Wireless posting system

Follow this when a user asks you to set up, install, move or take over the VIP Wireless
posting system (e.g. "Set up the VIP Wireless posting system from
vip-wireless/vip-wireless-media"). Do NOT run it during a daily-post or check-in run.

## Step 1 — check access (silently, then report in one short list)
1. GitHub: `add_repo` vip-wireless/vip-wireless-media with access "push". If pushes would be
   refused, tell the user to connect GitHub Integration in claude.ai → Customize → Connectors
   with an account that can push to the repo, and to install the Claude GitHub app on it.
2. Metricool: call getBrandSettings. The brand "VIP Wireless – Phone Repair" (blogId 7406481
   unless it changed) must be listed with Facebook, Instagram and TikTok. If the brand or
   blogId differs, update `_kit/RUNBOOK.md` and the prompts in `_kit/HANDOVER.md`.
3. Google Drive: read the Content Brief (id 19p4WsC-54k2_YgSHTAfZpzOqPbky8L1Q_3nfdT-OcQE) and
   open the folder "VIP Wireless – Social Content" (id 1YyAjIMyijKmKwrhaVM9ujd7YtU6VDUS8).
   If unreachable, ask the previous operator to share/transfer ownership (see HANDOVER.md),
   or search Drive by title and update the IDs in RUNBOOK.md and HANDOVER.md if they changed.
4. Google Sheets: get_spreadsheet on the Content Calendar
   (id 1bQR_DHjF2qcL37Y8VMgzoplbJ3a5c0vYcsRmh-uv4-A).
For anything missing, name the exact connector to connect and wait; don't create tasks until
GitHub push, Metricool and Drive all work (Sheets is optional).

## Step 2 — avoid duplicates
List the user's existing scheduled tasks. If tasks named "VIP Wireless daily post",
"VIP Wireless posting check-in" or "VIP Wireless TikTok check-in" already exist, don't
create them again — offer to update them instead. Remind the user that the previous
operator must delete their copies so posts and reminders aren't doubled.

## Step 3 — one confirmation, then create
Show the three tasks in a short table (name, schedule, what it does) and ask once:
"Create these three scheduled tasks?" On yes, create each with the exact name, schedule
(timezone America/New_York) and prompt from `_kit/HANDOVER.md` section 2:
- A. VIP Wireless daily post — `CRON_TZ=America/New_York 45 6 * * *`
- B. VIP Wireless posting check-in — `CRON_TZ=America/New_York 0 11 * * 0,2,4`
- C. VIP Wireless TikTok check-in — `CRON_TZ=America/New_York 0 11 * * 1,3,5,6`
Turn on push notifications for all three (email too for A). Copy prompts verbatim.

## Step 4 — confirm
Tell the user, in a few lines: the three tasks and their next run times, which approval
setting they got, that the first draft arrives at 7 AM, and that nothing is published
without their "approved". Add a line to LOG.md ("Setup/takeover by new operator") and push.
