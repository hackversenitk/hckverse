# hckverse
Original repo of our android work: https://github.com/harshnitk17/hackverse

PLease refer to the Google slides link below for more information about the system design.
https://docs.google.com/presentation/d/1H8tKbNPb3Y-2QHmLJWK6q26woP2Bw_qBFmcNeMtClK4/edit?usp=sharing

Please refer to the following link for problem statement and technologies used.
https://devfolio.co/submissions/findmyway-offline

Instructions to run:

Zulip Bot:

1. Refer to the following link for more information about zulip and to download the development version of zulip bots package.
   https://zulipchat.com/api/writing-bots
2. Place the maps and nearby folders under ./zulip_bots/zulip_bots/bots as mentioned in the above link.
3. Get Bing Maps API key and replace it with <BING_API_KEY> in maps.py and nearby.py
4. Run the bots using: zulip-run-bot <bot-name> --config-file ~/path/to/zuliprc
