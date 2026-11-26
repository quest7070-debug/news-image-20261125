# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/quest7070-debug/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/quest7070-debug/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the [make.fun](https://make.fun/bounty/news-image-20261125) bounty "Sum up 25 November's world news in one image".

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
The image is a one-page newspaper front page for Wednesday 25 November 2026,
drawn by `draw_poster.py` (Python + Pillow, run locally at build time): the
US tariff proposal of up to 20% on the EU, China and 12 more; the Asian chip
rout (Kospi −6.2%); Pakistan's first astronaut docking at Tiangong; and
regional stories from Ukraine, the UK, the Pacific and Egypt, plus a briefs
strip. Two runs write byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

To redraw the poster from scratch:

```sh
python3 draw_poster.py
```
