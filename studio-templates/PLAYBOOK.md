# Meme-Coin One-Page Site Playbook

Built from real data on 2026-10-26.

Sources:
- Dexscreener API: token-profiles/latest, token-boosts latest+top, and `latest/dex/search` across about 130 meme terms. This gave 770 tokens with websites and 769 unique domains.
- 420 top-scored domains were fetched; **298 were alive** (`sites.csv`).
- 297 were rendered in headless Chrome, with 271 hero shots and 28 full-page shots in `shots/`.
- GMGN (gmgn.ai and its API) returned **HTTP 403** to every request, so the dataset is Dexscreener only.

## 0. Fast path (daily workflow)
```bash
cd /workspace/meme-research
python3 build.py --list                              # 50 archetypes
python3 build.py token.json neon-degen --out out/    # one site
python3 build.py token.json random                   # surprise style
python3 build.py token.json all                      # all 50 variants
python3 build.py token.json comic-book,casino-jackpot,anime-tokyo
```
Each run outputs `OUT/<slug>-<archetype>/index.html` plus `assets/logo.*` (and `assets/meme*.*`). It is a single self-contained HTML file: Google Fonts is the only external dependency, with no build step, and it is ready for Netlify, Vercel or GitHub Pages.

## 1. Inputs (token.json)
| key | req | notes |
|---|---|---|
| name, ticker, logo, ca, chain | ✔ | logo = local path or URL (copied to assets/). chain ∈ solana, ethereum, base, bsc, arbitrum, sui, ton, tron |
| x_url, tg_url | – | the social button is hidden automatically when the value is empty |
| buy_url | – | default: Jupiter (SOL), Uniswap (ETH/Base/Arb), PancakeSwap (BSC), etc. |
| chart_url / dexs_url | – | default: Dexscreener embed / page for the CA (verified with real PONKE CA, it renders a live chart) |
| tagline, about | – | strongly recommended; there is a generic fallback |
| supply, tax, lp | – | defaults 1,000,000,000 / 0/0 / Burned |
| dex, native, wallet | – | defaults from the chain |
| images | – | list of meme images; these fill the gallery slots (`.gimg`) in turn. Without it, the logo is reused with CSS filters |

Placeholders inside the templates are `{{NAME}} {{TICKER}} {{LOGO}} {{CA}} {{CHAIN}} {{CHAIN_NAME}} {{X_URL}} {{TG_URL}} {{BUY_URL}} {{CHART_URL}} {{DEXS_URL}} {{TAGLINE}} {{ABOUT}} {{SUPPLY}} {{TAX}} {{LP}} {{DEX}} {{NATIVE}} {{WALLET}}`. build.py warns about any placeholder left unfilled.

## 2. What real sites contain (counts across 297 rendered live sites)
- **Sections:**
  - contract/CA 170
  - about/lore 148
  - community/socials 143
  - supply 87
  - memes/gallery 82
  - chart 65
  - tokenomics 54
  - how-to-buy 45
  - roadmap 44
  - disclaimer 43
  - FAQ 26
- **Outbound links:**
  - x.com 762
  - t.me 368
  - dexscreener 229
  - pump.fun 113
  - uniswap 75
  - jup.ag 64
  - CMC 59
  - CoinGecko 49
  - dextools 45
  - raydium 25
- **Stacks:**
  - Next.js 88, Vite/React 46, jQuery 28, Bootstrap 25
  - GSAP 18, Lottie 15, Swiper 14, WordPress 13, Hostinger 10, particles 10
  - Tailwind 8, Three.js 7, Lenis 7, Wix 6, Framer 6, Spline 5, Webflow 5
  - 109 load Google Fonts
- **Effects:** pulse 38, marquee/ticker 47 (24 as named keyframes), float 18, blink 15, ping 14, fadeIn 13, spin 13, bounce 10, then wiggle, glow and twinkle. 35 sites use background or hero video.
- **Iframes:** Dexscreener 14, YouTube 13, Twitter 11.
- **Fonts seen most:** Inter, Anton, Oswald, JetBrains Mono, Space Grotesk, Orbitron, Press Start 2P, Bangers, Luckiest Guy, VT323, Fraunces, Cinzel, Bebas Neue, Archivo Black.

**Key patterns**
1. The mascot IS the brand. The best sites put the character huge in the hero, then reuse it everywhere: stickers, gallery, cursor, loaders.
2. One committed aesthetic beats generic "crypto dark mode". The winners are pure cartoon (Moo Deng, Pnut), pure comic (Andy, MEW), pure retro (Retardio) or pure editorial (Bobo).
3. A copy-CA bar sits in or just under the hero (more than half of all sites have it), with Buy + Chart + X + TG one click away.
4. A ticker marquee divides sections. Its copy is self-aware and degen ("no team, no roadmap, just vibes").
5. Order of sections: Hero → marquee → About/lore → Tokenomics → How to buy (4 steps) → Chart → Roadmap/phases → Memes → Community CTA → disclaimer footer.
6. Tokenomics is usually tiny (supply, 0 tax, LP burned, renounced), so it gets styled as a playful object: cards, chips or bars.
7. Detail comes from micro-interactions: hover tilt, bobbing logo, confetti, click SFX, typed text, scroll reveals.
8. The disclaimer "no intrinsic value or expectation of financial return" is near-universal on the larger tokens.

## 3. Section blueprint (all templates implement it, each in its own visual language)
1. **Nav**: logo + name/ticker, 3–5 anchor links (hidden on mobile), social icons.
2. **Hero**: giant name/ticker, tagline, mascot treatment, Buy (primary) + Chart (secondary), CA copy bar.
3. **Marquee**: ticker repeated with slogans (one or two rows, opposite directions).
4. **About/Lore**: `{{ABOUT}}` + a second in-character paragraph.
5. **Tokenomics**: Supply / Tax / LP / Chain.
6. **How to buy**: four steps (wallet → native coin → DEX + paste CA → swap) + **Dexscreener embed**.
7. **Roadmap**: three or four phases, named in the archetype's voice (Issues, Levels, Chapters, Arcs, Jackpots...).
8. **Memes gallery**: `.gimg` slots.
9. **Community CTA**: TG + X.
10. **Footer**: disclaimer + year.

## 4. The 20 archetypes
| # | archetype | layout / hero | palette & fonts | motion & interaction | tone | inspired by |
|---|---|---|---|---|---|---|
| 1 | sticker-cartoon | sky + clouds, big bobbing mascot on wavy ground | sky blue/yellow/pink; Luckiest Guy + Nunito | bob, wiggle, confetti on click | wholesome cute | moodengsol.com, pnutsol.com, pepe.vip, worthless-coin-community-hub.lovable.app |
| 2 | comic-book | asymmetric panel grid, POW burst, trading-card stats | CMYK red/yellow/blue, halftone; Bangers + Comic Neue | panel pop-in, click SFX | "BAM! issue #1" | boysclubandy.com, mew.xyz |
| 3 | retro-pixel | CRT arcade, PRESS START, HP bars, world map | black/neon; Press Start 2P + VT323 | scanlines, blink, typed dialog | 8-bit game | retardio.xyz, godthedog, nochillio |
| 4 | terminal-hacker | stacked terminal windows, ASCII tokenomics, git-log roadmap | black/green; JetBrains Mono | matrix rain canvas, typing | dev/edgy | fartcoinsol.wtf, fartcoin.meme, infinitebackrooms |
| 5 | win95-desktop | teal desktop, icons, draggable windows, taskbar + clock | Win95 grey/teal; Pixelify Sans + VT323 | drag, Setup Wizard, popups | nostalgic absurd | retardio.xyz, unicorn.meme |
| 6 | neon-degen | grid + orbs, glitch h1, conic ring logo, bento | black/acid lime/magenta; Orbitron + Space Grotesk | glitch, mouse spotlight | hype degen | hidranet, kekpepe.xyz, troll.run |
| 7 | luxury-editorial | framed plate, rotating stamp, drop cap, asymmetric gallery | cream/gold/black; Fraunces + Inter + Plex Mono | slow reveals, stamp spin | high-fashion ironic | bobothebear.io, mooncat, ownthedoge.com |
| 8 | brutalist-bold | giant clipped H1, bordered grid with side labels | B&W + red; Anton + Archivo | hard cuts, marquee | alpha/sigma | gigachadsolana.com, sigmasolana, mogcoin |
| 9 | y2k-vaporwave | striped sun, moving perspective grid, chrome text | purple/pink/cyan; Monoton + Audiowide + VT323 | grid scroll, glass cards | aesthetic ｖａｐｏｒ | vapor/giga-style sites, rizz |
| 10 | doodle-notebook | ruled paper, red margin, sticky notes, polaroids, to-do | paper/ink/highlighter; Permanent Marker + Patrick Hand + Caveat | sketchy wobble | handmade lowfi | wojak.art, rageguy.meme, boden4pres |
| 11 | storybook-quest | parchment book, crest + ribbon, chapters, locked quest | parchment/burgundy/gold; Cinzel + Libre Caslon | page reveals | epic fable | cattleaxe.lol, thefoxbox.org |
| 12 | corporate-parody | SaaS landing, fake swap widget, logo marquee, pricing-as-roadmap, FAQ | white/indigo; Inter Tight | product-UI polish | deadpan startup | deliveryguy.fun, theinu.fun, toshithecat.com, asteroidonlong.com |
| 13 | casino-jackpot | marquee sign with chasing bulbs, working 3-reel slot (lands on logo), poker chips, playing-card steps | red/gold/felt green; Bungee Shade + Bungee + Rubik | blinking lights, reel spin, chip flip | Vegas high-roller | rizzmas.org, cartoon-money sites |
| 14 | tabloid-newspaper | broadsheet: blackletter masthead, EXTRA ticker, 3 columns, clip-out CA coupon, funny pages | newsprint/ink/red; UnifrakturMaguntia + Old Standard TT + Oswald | live dateline | satirical press | newspaper-style meme sites (boden-era political memes) |
| 15 | cosmic-space | starfield canvas + nebula, logo as planet with orbiting moons + Saturn ring, countdown | deep space/orange/cyan; Exo 2 + Major Mono Display | parallax stars, orbits, live countdown | mission control | asteroidonlong.com, dogelonmars, moon-themed tokens |
| 16 | acid-pop | pill nav, morphing blob mascot, tilted double marquee, bento numbers | acid lime/black/pink/blue; Bricolage Grotesque | blob morph, emoji/logo rain "party mode" | Gen-Z playful | asteroidonlong.com (lime), lolcoin/bull-style sites |
| 17 | clay-bubbly | floating 3D clay blobs, squishy mascot on pedestal, bubble tokenomics | pastel pink/blue/mint; Baloo 2 + Fredoka | squash-and-stretch, float, click squish | soft & cute | itsafwog.com, suicarabbit |
| 18 | museum-gallery | gilded frame + spotlight + brass plaque, roped gallery, catalogue, provenance timeline | gallery wall beige/gold/burgundy; Playfair Display + Cormorant + Jost | 3D frame tilt on hover | museum-serious ironic | ownthedoge.com, mooncat |
| 19 | political-campaign | campaign hero "X FOR PRESIDENT", rosette badge, flag stripes, letter from candidate, ballot steps | red/white/navy/gold; Alfa Slab One + Roboto Condensed + Libre Baskerville | badge pulse, chant marquee | rally parody | trump/maga/boden-style political memes |
| 20 | anime-tokyo | rotating speed lines, rising sun, vertical kanji, manga panels + SFX, gacha cards | black/hot pink/cyan/yellow; Dela Gothic One + Noto Sans JP + Zen Dots | skewed text, power-level meters | shonen episode | kabosu/shiba-style JP sites, LMAO-style anime memes |

**How to pick an archetype:**
- animal mascot → 1, 17 or 16
- frog/pepe → 2, 6 or 10
- cat → 1 or 18
- dog → 18 or 20
- political figure → 19 or 14
- AI/dev/fart humour → 4 or 5
- luxury/"rich" → 7 or 13
- space/rocket → 15
- fantasy → 11
- "serious" parody → 12
- gaming → 3

To produce 10 or more sites a day, rotate archetypes so no two consecutive tokens share one.

## 5. Copy templates
- **Tagline:** "The {adjective}est {animal} on {chain}." / "{name}: not a coin, a lifestyle." / "Born on {chain}. Raised by memes."
- **About:** "{name} (${T}) is a community-driven meme coin on {chain}. No team allocation, no presale, no promises, just {mascot trait} and a community that refuses to sell."
- **Marquee:** "${T} ✦ NO TEAM ✦ NO PRESALE ✦ LP BURNED ✦ JUST VIBES" / "BUY ${T} ✦ HOLD ${T} ✦ MEME ${T}"
- **Steps:** "Get {wallet} → Buy {native} → Go to {dex} & paste the CA → Swap for ${T}"
- **Roadmap:** Phase 1 launch/socials/1k holders → Phase 2 listings (CG/CMC)/trending/collabs → Phase 3 CEX/merch/moon. Always rename the phases in the archetype's voice.
- **Disclaimer:** "${T} is a meme coin with no intrinsic value or expectation of financial return. Not financial advice."

## 6. "Beautiful & detailed" checklist
- [ ] One committed aesthetic: fonts, palette, borders, shadows and copy voice all agree
- [ ] Mascot is huge in the hero and reused 4+ times (nav, about, gallery, footer or marquee)
- [ ] Contract address visible above the fold, with a copy button and toast
- [ ] Buy and Chart buttons in the hero; X and TG in nav and in the closing CTA; empty links are hidden
- [ ] At least one marquee; at least one idle animation (bob, float, spin); scroll reveals; hover states on every card and button
- [ ] At least one signature interaction (slot machine, confetti, drag windows, typing, glitch, countdown, tilt)
- [ ] Live Dexscreener embed in a themed frame
- [ ] Section labels in the archetype's voice, not "Tokenomics" everywhere
- [ ] Mobile at 390px: no horizontal scroll, nav collapses, grids go to 1–2 columns, tap targets ≥ 40px
- [ ] `prefers-reduced-motion` respected; images have alt text; OG/Twitter meta set from name/ticker/logo
- [ ] Disclaimer in the footer

## 7. Technical recipe (shared core in `templates_src/_core.css|js`)
- **Copy CA:** any `[data-copy]` copies `{{CA}}` via `navigator.clipboard`, with a textarea fallback and a toast.
- **Dexscreener embed:** `https://dexscreener.com/{chain}/{CA}?embed=1&loadChartSettings=0&trades=0&tabs=0&info=0&chartLeftToolbar=0&chartTheme=dark&theme=dark&chartStyle=1&chartType=usd&interval=15`, inside `.chart` (56% aspect padding; 460px tall on mobile). Verified live with the PONKE CA.
- **Marquee:** `.mq > .mq-track > span`. JS duplicates the span for a seamless loop. Set speed with `--mq-speed`; `.rev` reverses direction.
- **Socials:** `[[SOCIALS]]` expands to inline SVG X, Telegram and Dexscreener icons. `a[data-s]` with an empty href is hidden.
- **Reveal:** add `.rv` and an IntersectionObserver adds `.in`.
- **Utilities:** `[data-year]` fills the current year; `[data-menu]` toggles the menu.
- **Structure:** each archetype is a fragment `templates_src/<arch>.html` with `@@FONTS@@ @@CSS@@ @@BODY@@ @@JS@@`. `python3 assemble.py [arch]` writes `templates/<arch>/index.html`, and `shoot.py` makes desktop (1440) and mobile (390@2x) screenshots, checking for overflow and JS errors.
- **Adding archetype #21:** copy a fragment, change layout + fonts + palette + hero + motion + voice (not just colours), assemble, shoot.

## 8. Top 15 reference sites (all alive in sites.csv)
1. https://www.moodengsol.com/: an illustrated cartoon world where the mascot lives in the scene. The gold standard for cute.
2. https://www.pnutsol.com/: a comic and cartoon collage with lots of sticker-style mascot reuse.
3. https://boysclubandy.com: comic purple and yellow, chunky outlines, and a strong character voice.
4. https://mew.xyz/: bold red, black and white comic art with confident type. Proof that two colours are enough.
5. https://www.ponke.xyz: a rich multi-section brand site with consistent illustration throughout.
6. https://www.pepe.vip/: a classic green cartoon meme page, simple and iconic.
7. https://www.basedbrett.com/: a big Base mascot brand with a playful illustrated layout.
8. https://cattleaxe.lol: a storybook quest with chapters and narrative scroll.
9. https://bobothebear.io: an editorial, magazine-like layout with Fraunces serif. Shows that luxury irony works.
10. https://wojak.art/: a black-and-white sketch aesthetic where the hand-drawn feel is the brand.
11. https://www.toshithecat.com/: a big-brand blue site with polished corporate execution.
12. https://gigachadsolana.com/: brutal black, white and red with giant type.
13. https://retardio.xyz/: a Win95 and retro-OS joke carried through every element.
14. https://www.ownthedoge.com/?wow=doge: a museum and provenance concept for the original Doge.
15. https://www.fartcoinsol.wtf/: a terminal and absurd-humour aesthetic.

Honourable mentions:
- https://rizzmas.org (casino/Christmas)
- https://itsafwog.com/ (3D clay)
- https://deliveryguy.fun (corporate parody)
- https://asteroidonlong.com/ (lime corporate)
- https://rageguy.meme/ (doodle)
- https://www.degen.tips/ (purple illustrated)

## 9. Files
- `sites.csv`: 420 checked sites (298 alive), with token, ticker, chain, url, liquidity, 24h volume, mcap, boosts, alive and http status
- `html/` holds the raw HTML; `rendered/` holds rendered DOM data
- `shots/` holds 271 hero shots; `shots/full/` holds 28 full-page shots; `raw/sheets/` holds contact sheets
- `templates/<arch>/`: `index.html` plus `desktop.jpg`, `mobile.jpg`, `desktop-hero.jpg` and `mobile-hero.jpg`
- `templates_src/` contains the fragments and core; `assemble.py`, `build.py` and `shoot.py` are the tools
- `sample/`: the Bonkle demo inputs and logo; `sample/out/` holds all 20 built demo sites

## 4b. The 50 archetypes (2026-10-26 upgrade)

Existing 20 upgraded with shared motion (scroll-reveal variants, float/parallax, copy-CA sparkles, optional particles, prefers-reduced-motion). Plus 30 new styles. Research list: `research50/research50.md`.

| # | archetype | vibe |
|---|---|---|
| 1 | `sticker-cartoon` | Sticker Cartoon — Sky & cloud backdrop, thick-outline stickers, bouncy mascot · cute |
| 2 | `comic-book` | Comic Book — Halftone panel grid, POW bursts, trading-card stats · comic |
| 3 | `retro-pixel` | Retro Pixel — CRT arcade, PRESS START, HP bars & world map · 8-bit game |
| 4 | `terminal-hacker` | Terminal Hacker — Matrix rain, terminal windows, ASCII tokenomics · dev/edgy |
| 5 | `win95-desktop` | Windows 95 — Draggable windows, install-wizard buy steps, taskbar · retro OS |
| 6 | `neon-degen` | Neon Degen — Glitch title, spinning ring logo, bento grid · hype degen |
| 7 | `luxury-editorial` | Luxury Editorial — Cream & gold, serif type, framed plates & stamps · glossy magazine |
| 8 | `brutalist-bold` | Brutalist — Black, white & red, giant type, bordered grid · alpha/sigma |
| 9 | `y2k-vaporwave` | Y2K Vaporwave — Striped sun, perspective grid, chrome text · aesthetic |
| 10 | `doodle-notebook` | Doodle Notebook — Lined paper, sticky notes, polaroids, handwriting · lo-fi handmade |
| 11 | `storybook-quest` | Storybook Quest — Parchment book, crest, chapters & quests · fantasy tale |
| 12 | `corporate-parody` | Corporate Parody — SaaS landing, fake swap widget, pricing-tier roadmap · deadpan |
| 13 | `casino-jackpot` | Casino Jackpot — Marquee lights, working slot machine, chip tokenomics · Las Vegas |
| 14 | `tabloid-newspaper` | Tabloid Newspaper — Blackletter masthead, EXTRA ticker, 3-column story, clip-out CA coupon · satire |
| 15 | `cosmic-space` | Cosmic Mission — Starfield canvas, planet logo & orbits, countdown · mission control |
| 16 | `acid-pop` | Acid Pop — Lime & black, pill buttons, morphing blobs, party mode · Gen Z |
| 17 | `clay-bubbly` | Clay Bubbly — Pastel 3D clay, squishy mascot, bubble tokenomics · soft |
| 18 | `museum-gallery` | Museum Gallery — Gilded frames & spotlights, plaques, catalog · straight-faced irony |
| 19 | `political-campaign` | Political Campaign — “X for President” hero, rosette badges, ballot steps · campaign parody |
| 20 | `anime-tokyo` | Anime Tokyo — Speed lines, vertical kanji, manga panels & SFX, gacha cards · shonen |
| 21 | `blueprint-tech` | Blueprint Tech — Cyan grid paper, schematics, stamps · engineering |
| 22 | `candy-shop` | Candy Shop — Gummy buttons, sugar stripes, jelly cards · sweets |
| 23 | `chalkboard-school` | Chalkboard School — Chalk dust type, ruled lessons, gold stars · classroom |
| 24 | `cyberpunk-noir` | Cyberpunk Noir — Rainy neon alleys, chrome HUD, magenta/cyan · night city |
| 25 | `desert-oasis` | Desert Oasis — Sand dunes, mirage heat, sunset gradient · arid |
| 26 | `disco-fever` | Disco Fever — Mirrorball, sequin stripes, 70s gold · dance floor |
| 27 | `farm-country` | Farm Country — Barn wood, gingham, wheat icons · wholesome farm |
| 28 | `food-truck` | Food Truck — Menu board, neon OPEN, ketchup/mustard · street food |
| 29 | `glassmorphism-ui` | Glassmorphism UI — Frosted panels, soft blur orbs, modern SaaS-meme |
| 30 | `glitch-corrupt` | Glitch Corrupt — RGB split titles, scan tear, corrupted UI · broken VHS |
| 31 | `graffiti-street` | Graffiti Street — Brick wall tags, spray drips, street art stickers · urban |
| 32 | `horror-midnight` | Horror Midnight — Fog, blood drip type, crescent moon · spooky |
| 33 | `jungle-safari` | Jungle Safari — Leaf frames, vine borders, explorer map · tropical |
| 34 | `kids-crayon` | Kids Crayon — Crayon strokes, construction paper, stickers · handmade kid |
| 35 | `lego-blocks` | Lego Blocks — Stud grid, brick stack hero, primary toys · playful build |
| 36 | `liquid-metal` | Liquid Metal — Chrome gradients, mercury blobs, specular shine · fluid |
| 37 | `mecha-bot` | Mecha Bot — HUD frames, warning stripes, robot panel · sci-fi mech |
| 38 | `metal-band` | Metal Band — Tour poster, distressed type, stage lights · concert |
| 39 | `pastel-kawaii` | Pastel Kawaii — Soft pastels, sparkles, rounded stickers · cute JP |
| 40 | `pirate-ship` | Pirate Ship — Parchment map, compass rose, treasure chest · high seas |
| 41 | `polaroid-film` | Polaroid Film — Photo stacks, film strip edges, flash white · analog cam |
| 42 | `rave-flyer` | Rave Flyer — Acid flyer, strobe type, underground stamp · club night |
| 43 | `skate-zine` | Skate Zine — Xerox collage, sticker scraps, DIY mag · skate culture |
| 44 | `snow-blizzard` | Snow Blizzard — Frost glass, snowfall, aurora accents · arctic |
| 45 | `sports-jersey` | Sports Jersey — Locker-room board, jersey numbers, stadium lights · athletic |
| 46 | `subway-map` | Subway Map — Transit lines, station dots, route legend · metro |
| 47 | `synthwave-drive` | Synthwave Drive — Dashboard HUD, sunset strip, chrome dials · 80s drive |
| 48 | `tarot-mystic` | Tarot Mystic — Gold foil cards, crescent, velvet dark · occult chic |
| 49 | `underwater-reef` | Underwater Reef — Bubbles, coral bento, sun rays through water · ocean |
| 50 | `zen-garden` | Zen Garden — Sand ripples, stone logo, ink wash · calm minimal |

Auto meme images: Studio generates 6–9 canvas memes offline from logo/banner/name/ticker; selected ones embed as `assets/memeN.*` on export/deploy.

Namecheap: browser CORS blocked on api.namecheap.com — use `namecheap-proxy/` on Vercel; whitelist proxy egress IP; Deploy can merge A/@ + CNAME/www via getHosts→setHosts.
