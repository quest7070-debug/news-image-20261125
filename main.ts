// News-image entry for make.fun's "Sum up 25 November's world news in one image"
// bounty (news-image-20261125). Node 22, standard library only.
// The image is drawn by draw_poster.py (run locally at build time) and held in
// this repository as entry.png; the program copies it to /output/entry.png.
// The copy is byte-for-byte, so two runs always write the same bytes.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, statSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
if (!existsSync(source) || statSync(source).size === 0) {
  throw new Error('entry.png is missing or empty');
}
copyFileSync(source, join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
