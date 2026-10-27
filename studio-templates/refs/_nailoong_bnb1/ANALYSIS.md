# User template analysis — `ui.html` (BNB Pack #1)

**Source:** saved page from `https://nailoongbnb.com/` (local `E:/pack/template/bnb/1/ui.html`)  
**Offline tree:** `/workspace/user-templates/ui.html` + `ui_files/` (~174 assets, ~13 MB)  
**Shots:** `/workspace/user-templates/shots/` (desktop/mobile full, hero, section crops, `scroll.gif`)  
**Compare:** `/workspace/user-templates/shots/compare/` (original vs recreated `bnb-1` + Bonkle)

## 1. Overall vibe

Premium **illustrated character site**, not a generic CSS-meme landing. Cream paper (`#fbf7ef`) + deep navy ink (`#1b1f4b`) + punch yellow (`#ffd21f`) / orange / pink. Display type **Lilita One** (+ **ZCOOL KuaiLe** for CN), body **Plus Jakarta Sans**. Soft “riso” print texture, floating character cutouts, dense real artwork, and a long scroll that feels like a brand campaign for `$奶龙` on BNB during TOKEN2049 week.

What makes it feel *much* better than our previous 50 templates:

| Ours (typical) | This page |
|---|---|
| CSS shapes, emoji, thin SVG | Dozens of painted/sticker character webps |
| Sparse sections, lots of empty air | High density: stats bar, lore, timeline, event chapter, chart, TV, meme rail, join |
| One logo reused everywhere | Distinct poses (sit, head, body, bite props, posters) |
| Flat cards | Layered ghosts, blobs, candle backdrop, sticky header, topbar ticker |
| Generic “how to buy” | Same steps but framed inside a full market stage |

## 2. Section order

1. **Topbar** — rotating promo messages (airport / TOKEN2049 / follower count)  
2. **Sticky header** — logo wordmark + `$ticker` badge, section nav, CA pill, X/TG icons, Buy, burger  
3. **Hero** — left copy (eyebrow chain, giant title, badge+tagline, lead, CTAs, 3 stats); right media stage (poster / muted YouTube); floating X/DEX “bite” characters + large body cutout  
4. **Token ticker bar** — logo, live price/mcap/vol/liq (JS), short CA, chart CTA  
5. **Divider** — big typographic statement + CTAs  
6. **Lore** — art + story + fact grid; **Numbers** growth timeline (6 beats with sources)  
7. **TOKEN2049 / Spotlight** — dark/yellow chapter, quote card, KPI grid, 4 event shots  
8. **Market** — candle/glow backdrop, chart window (GeckoTerminal iframe), CA card with character, **How to buy** 4 steps  
9. **Watch** — TV player + episode playlist (YouTube), then **Memes** horizontal rail + lightbox  
10. **Join** — community CTAs + social tiles  
11. **Footer** — brand, columns, long legal/privacy  
12. Chrome: lightbox, language toggle, toast

## 3. Layout & typography

- Wide wrap (`~1600px` content with large gutter), generous `clamp` section padding.  
- Split layouts (copy | art) with large radii (`--radius: 28px`) and deep soft shadows.  
- Display headlines with italic `<em>` accents; eyebrow labels above titles.  
- Badges for `$ticker` in multiple sizes; mono CA chips.  
- Mobile: burger collapses menu; hero stacks; rail becomes swipeable.

## 4. Color palette (CSS variables)

- Ink `#1b1f4b`, mute `#8b8da6`, paper `#fbf7ef`  
- Navy `#062867` / `#0b1f5c`  
- Yellow `#ffd21f` / `#ffe46a`, orange `#ff7a2c`, pink `#ff2d95`, blue `#2c3fd8`  
- Buttons: ink / light / yellow / dark / line variants

## 5. Imagery system

- **Brand:** `logo.webp`  
- **Character kit:** `head`, `body`, `love`, `sit`, `x` / `x-bite`, `dex` / `dex-bite` — used as floating “ghosts” and section mascots  
- **Hero poster / Season art:** `season2.webp` (+ YouTube embed)  
- **Event / meme posters:** numbered `1.webp`…`20.webp` (+ `(1)` variants) — horizontal rail + lightbox  
- **Partner marks:** Dexscreener, BNB icon  
- Missing offline wall textures (`../imagery/wall/*`) — CSS still holds without them

## 6. Motion & interaction

- Keyframes: `float`, `rock`, `bob`, `sweep`, `morph`, `breathe`  
- Scroll **reveal** via IntersectionObserver  
- Topbar message rotation  
- Sticky header scroll state  
- Meme rail scroll + progress bar + lightbox  
- Burger menu; CA copy toasts  
- Live market numbers / chart iframe / YouTube hero+playlist (network)  
- Optional EN↔ZH i18n (`data-i18n`)

## 7. Components checklist

- Buy CTAs → PancakeSwap  
- CA copy (short + full)  
- Dexscreener / BscScan / chart embed  
- Tokenomics-as-timeline (not just 3 tiles)  
- How-to-buy 4 steps with icons  
- Video stage + episode list  
- Meme gallery rail  
- Social join strip  
- Partner/event storytelling (TOKEN2049, Changi)

## 8. Recreation notes (`bnb-1`)

**Kept:** CSS system (fonts, colors, layout, float/ghost/blob/riso), section skeleton, sticky header, topbar, lore+numbers, spotlight chapter, market+howto, watch stage, meme rail+lightbox, join, footer, character art kit inlined as data-URIs.

**Mapped to Studio fields:** `NAME`, `TICKER`, `LOGO`, `BANNER`, `TAGLINE`, `ABOUT`, `CA`, `CHAIN_NAME`, `DEX`, `BUY_URL`, `DEXS_URL`, `CHART_URL`, `X_URL`, `TG_URL`, `SUPPLY`/`TAX`/`LP`, `NATIVE`, `WALLET`; gallery slots use `gimg` + `{{LOGO}}` so uploaded/auto memes cycle in.

**Stripped / limited:** Next.js chunks & trackers; live Dexscreener price polling; YouTube embeds/playlist/sound toggle; CN i18n; TOKEN2049-specific copy → generic Spotlight; wall background images (absent in save).

**Lessons for upgrading the other 50:** ship real illustrated kits (even small webp packs), raise section density, add a sticky CA/Buy chrome, a horizontal meme rail, and one “campaign chapter” between lore and chart—not more flat CSS themes alone.
