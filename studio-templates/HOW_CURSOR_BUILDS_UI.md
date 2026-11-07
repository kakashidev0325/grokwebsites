# How Cursor builds these landing pages

This is the working method for a MemeSiteStudio template: a long, illustrated campaign page that still drops into `assemble.py` / `build.py`. A new template is not a palette swap of the last one. It is a different poster, with its own type, hero, scene, and one idea the lower page keeps repeating.

The contract stays fixed. Placeholders (`{{NAME}}`, `{{TICKER}}`, `{{LOGO}}`, `{{CA}}`, `{{BUY_URL}}`, `{{THEME_MODE}}`, `{{THEME_STYLE}}`, and the rest `build.py` fills) are the only copy. Art slots are `img.gchar` and `img.gimg` with the class **before** `src="{{LOGO}}"`. Put `<!--BANNER_SLOT-->` where the banner should land. Fragments use `@@FONTS@@` `@@CSS@@` `@@BODY@@` `@@JS@@`.

Chain choice never picks the theme. Color comes from `theme_mode` / `theme_preset` / the two custom colors only.

## 1. Design one page

1. Read the reference as a poster, not a sitemap. Note the hero crop, the type pairing, the background drawing, and the one repeated motif (halftone, torii, candle tape, sticker pile).
2. Write a one-line art direction: "black poster, giant wordmark on the floor, mascot centered" or "cream magazine, vertical spine, one red rule." If two templates share that sentence, one of them is wrong.
3. Pick a type pair from Google Fonts. Display face does the names. Body face does the paragraphs. Do not reuse the previous template's pair.
4. Set the original palette on `:root` as semantic tokens (below). Accents, paper, and ink are chosen together so text passes on the first try.
5. Draw one SVG scene with classes `.bg .bg2 .surf .a .a2 .ink .line`. The hero is that drawing plus the mascot, not a flat color block.
6. Stack 8–12 sections: nav, hero, marquee, banner slot, lore, a signature section, tokenomics, how-to-buy, roadmap, meme gallery, FAQ, closing CTA, footer. Rotate the order and the component mode (quote vs split, tickets vs bars, stations vs chapters) so neighbors do not share a rhythm.
7. Hang motion on the shared system (`_motion.css`, `_motion.js`, and the behaviors in `templates_src/_core.js`). Do not invent a second animation library.
8. Assemble, fill the sample token, and look at a full-page screenshot plus a scroll. Fix contrast, overflow, and collisions before calling it done.

## 2. Layout, type, color

- One idea per band. A section is a headline, one paragraph, and one visual. Cards are a last resort, and they should not all be the same rectangle.
- The hero is at least one viewport. The name is the biggest type on the page. The mascot is a placed object (floor, orbit, sticker pile, desk), not a thumbnail in the corner of a card.
- Body copy stays under about 65 characters. Kickers are short labels, not sentences.
- Original colors live on `:root`:

```css
:root{
  --a:#ff2d2d; --a2:#fff; --on:#1a0505; --acc:var(--a); --part:var(--a);
  --bg:#070707; --bg-2:#141414; --surface:#161616; --card:var(--surface);
  --ink:#f6f3ee; --muted:#b9b3a8; --line:rgba(255,255,255,.16);
  --glow:rgba(255,45,45,.45); --grad:linear-gradient(135deg,var(--a),var(--a2));
}
```

`--a` / `--a2` are the two accents. `--on` is text **on** the accent (button label). `--ink` is text on the page. `--part` tints particles. Scene paints use the classes above, and strokes that must stay hollow use `fill="none"` (the CSS keeps `fill:none` on those).

Backgrounds are layered: a base `--bg`, one or two radial washes mixed from `--a` and `--a2`, then the SVG scene. A flat `background:#111` is not a finished page.

## 3. Theme change

The selector in the app offers Original, twelve presets, and Custom (primary + secondary). Recoloring has to change the page, not only the buttons.

### Tokens

| Token | Role |
| --- | --- |
| `--theme-1`, `--theme-2` | The two chosen colors. Presets set them in `_core.css`. Custom sets them inline on `<html style="{{THEME_STYLE}}">`. |
| `--theme-ink` | Text that sits on `--theme-1` (buy button). |
| `--theme-glow`, `--theme-grad` | Glow and the moving gradient. |
| `--theme-bg`, `--theme-bg-2`, `--theme-surface` | Page, secondary wash, cards. |
| `--theme-text`, `--theme-muted`, `--theme-line` | Reading text, secondary text, hairlines. |

When `data-theme-mode` is `preset` or `custom`, `_core.css` points the semantic tokens at that set:

`--bg`, `--bg-2`, `--surface`, `--card`, `--ink`, `--muted`, `--line`, `--a`, `--a2`, `--on`, `--glow`, `--grad`, `--part`, `--acc`, plus `--border` and `--shadow`.

`bnb-1` also reads older names (`--paper`, `--yellow`, `--orange`, `--navy`, `--mute`, …). Those are aliased to the same semantic tokens so the existing stylesheet recolors without a rewrite.

Templates must paint with these variables. A hardcoded accent hex in a hero will ignore the preset. Borders and card fills included.

### Presets are drawn, custom is derived

Each preset sets `--theme-1/2/glow/grad/ink` and then a hand-tuned canvas (`--theme-bg`, surface, text, muted, line). `base-blue`, `mint-pastel`, and `monochrome` are light pages. The others are dark tinted pages. Hand-tuned values win over the generic mix because `html[data-theme-preset="…"]` is more specific than `html[data-theme-mode="preset"]`.

Custom only has two hex values, so `templates_src/_core.js` derives the canvas when `data-theme-mode="custom"`:

- Read `--theme-1` and `--theme-2`.
- Relative luminance decides light vs dark. Both accents very dark, or both very light, produce a light page. Otherwise the page is a dark tint of the two colors.
- Mix each accent toward paper or toward near-black for background, surface, and muted text.
- Write `--theme-bg`, `--theme-bg-2`, `--theme-surface`, `--theme-text`, `--theme-muted` as inline properties.

The script does not run for `preset` or `original`, or it would cover the hand-tuned preset colors. It never reads the chain.

Original mode matches none of those selectors. The template's `:root` palette stays.

### What a preset has to change

Background washes, SVG scene fills, cards, borders, headlines, kickers, marquees, particle color (`--part`), glow, gradient bands, and button faces. The buy label uses `--on` / `--theme-ink` so light accents get dark text and dark accents get light text.

`theme_selector_demo.html` is the reference UI: large swatch cards, the name under the chips, a real `<input type="color">` with a hex field, and a live preview. The chain dropdown only changes a label.

## 4. Animation insertion

Motion lives in two shared files plus the behaviors already in `_core.js`. `assemble.py` appends `_motion.css` and `_motion.js` after the core files, so every template gets them. Colors inside the motion CSS use `var(--glow)`, `var(--a)`, and `var(--on)`, so a preset recolors the glow and the shine.

### Motion tokens

Set on `:root` in `_motion.css`:

| Token | Default | Use |
| --- | --- | --- |
| `--dur-fast` | 160ms | Press, hover |
| `--dur` | 480ms | Reveals |
| `--dur-slow` | 900ms | Larger entrances |
| `--dur-loop` | 3.4s | Bob, float |
| `--ease-out` | cubic-bezier(.16,1,.3,1) | Entrances |
| `--ease-in-out` | cubic-bezier(.45,0,.2,1) | Loops |
| `--ease-spring` | cubic-bezier(.2,1.35,.3,1) | Playful overshoot |
| `--shift` / `--shift-lg` | 28px / 48px | Reveal distance |
| `--mq-speed` | 28s | Marquee duration (override per strip) |

### Patterns and the hook to use

| Pattern | Hook | Where it runs |
| --- | --- | --- |
| Entrance / scroll reveal | `.rv`, `.rv-l`, `.rv-r`, `.rv-z`, `.rv-rot`, `.rv-blur` | `_core.js` adds `.in` via `IntersectionObserver` |
| Staggered sequence | `.rv-stagger` on the parent, or `data-stagger` | CSS nth-child delays; `_motion.js` writes `--i` and a delay per child |
| Parallax | `data-parallax="0.08"` (scroll), `data-mouse="18"` (pointer) | Scroll in `_core.js`, pointer in `_motion.js` (fine pointers only) |
| Marquee / ticker | `.mq` > `.mq-track`, optional `.rev`, `--mq-speed` | `_core.js` clones the track; CSS animates `translateX` |
| Float / bob | `.m-bob`, `.m-float`, `.m-spin`, `.m-pulse`, `.m-glow` | `_motion.css` keyframes. Legacy `.bob` / `.floaty` still exist in core |
| Hover / press | `.m-press` (added to `.btn` by `_motion.js`), `data-magnetic`, `data-tilt` | Press is CSS. Magnetic and tilt are pointer moves in `_core.js` |
| Shine | `.btn-shine` or `.m-shine` | A skewed gradient sweeps with `transform` |
| Animated gradient | `.m-grad` on an element whose background is `var(--grad)` | `background-position` only |
| Particles / sparkles | `data-particles`, `data-sparkles` on `<body>` | DOM specks or a `requestAnimationFrame` canvas in `_core.js`, tinted with `--part` |
| Counters | `data-count`, optional `data-pre` `data-suf` `data-dec` | rAF ease-out when the node enters view |
| Letter / wave entrance | `data-letters`, `data-wave`, `data-type` | `_core.js` splits text. Needs `data-intro` on `<body>` for the letter keyframes |
| Copy confetti | `data-copy`, `data-buy` | Burst on copy and on buy click |
| Scroll progress | automatic | A fixed bar, colored with `--theme-grad` under a preset |

Character art uses `class="gchar m-bob"` plus `data-tilt` and `data-mouse`. Buy links use `btn btn-main btn-shine btn-pulse` and `data-magnetic`.

`animation_demo.html` shows each of these on one scrollable page.

### Many animations, no jank

- Animate `transform` and `opacity` only. Leave `top`, `left`, `width`, `height`, and `filter` alone on anything that loops. `filter` is reserved for a single glow on a small mascot.
- Promote the layer you actually move: `will-change:transform` on `[data-parallax]` and `.m-layer`. Do not set `will-change` on every card.
- One scroll listener, one pointer listener. Read the scroll position and write transforms. Do not bind a listener per element.
- Loops that follow the pointer or paint particles go through `requestAnimationFrame`. Counters do too.
- Pause or skip work you cannot see. Marquees are `overflow:hidden`. Particle counts drop on small screens.
- `prefers-reduced-motion: reduce` turns loops off, shows reveals in their final state, and hides the custom cursor and particle field. `_motion.js` also sets `reduced-motion` on `<html>` and skips the pointer parallax.

### Checklist — packed with animations

Every template has to pass this before it is done:

- [ ] Hero mascot bobs or floats (`.m-bob` or `.m-float`) and tilts (`data-tilt`).
- [ ] At least one marquee (`.mq`) and, on long pages, a second strip the other way (`.mq.rev`).
- [ ] Scroll reveals on lore, tokenomics, steps, gallery, and the closing band (`.rv*` / `.rv-stagger`).
- [ ] One staggered group (steps, tickets, roadmap, or the signature list).
- [ ] One parallax or mouse-follow layer (`data-parallax` or `data-mouse`).
- [ ] Buy button shines and pulses (`.btn-shine.btn-pulse`) and presses (`.m-press` / magnetic).
- [ ] A gradient, glow, particle, or sparkle field that uses `--a` / `--glow` / `--part` (`m-grad`, `m-glow`, `data-particles`, or `data-sparkles`).
- [ ] One counter (`data-count`) that eases in when scrolled into view.
- [ ] Copy and buy fire the confetti burst (`data-copy`, `data-buy`).
- [ ] `prefers-reduced-motion` leaves the page readable: no infinite motion, reveals visible, no horizontal overflow.
- [ ] Nothing animated depends on a color that is not a theme token.

## 5. Hero composition

A hero is a scene, not a logo dropped on a card. The framed sticker (white pad, border, radius, shadow) is allowed twice in the whole set: once as a stamp overlapping a cutout, once as a die-cut pile. Everywhere else the logo is a cutout (`background:transparent`, no border) sitting in the drawing.

Build the frame in this order:

1. **Background.** The SVG scene (`gen_scenes.py`, classes `.bg .bg2 .surf .a .a2 .ink .line`) fills the viewport and moves slower than the page (`data-parallax` around `-0.1`). Theme presets recolor it because the paints are tokens, not hex.
2. **Midground props.** Extra SVG drawn in the hero: a torn edge, a skyline, a torii, a ledge, a moon, coins, a rocket silhouette, film sprockets, a crosshair. These are shapes, not photos, and they use `var(--a)`, `var(--bg-2)`, `var(--ink)`.
3. **The mascot, interacting.** It stands on the wordmark, climbs the tear, breaks out of a phone outline, sits on a question mark or a ledge, rides a cloud, lands on a planet curve, or wades a wave. Add one or two smaller copies (peek, satellite, lantern, flag) with `.m-bob` or `.m-float` and `data-mouse`. A speech bubble is a short label (`${{TICKER}}` or one word), not a paragraph.
4. **Type as part of the art.** The name is display type at viewport scale: on the floor, as a vertical rail, as a neon sign, as a magazine masthead, or tilted behind the mascot. It is not a heading sitting in a padded column beside a thumbnail.
5. **Foreground.** Grain overlay (SVG turbulence, `mix-blend-mode:overlay`), a ticker band (`.mq.hero-mq`), and floating stickers. These sit above the scene and below the sticky nav.

No two heroes share that arrangement. `gen_heroes.py` keeps one function per kind (`poster`, `splitR`, `center`, `scatter`, `app`, `cinema`, `splitL`, `sky`, `orbit`, `question`, `craft`, `index`, `roof`, `product`, `letterbox`, `hud`, `ghost`, `magazine`, `seal`, `planet`, `launch`, `impact`, `desk`, `chapter`, `shrine`, `stickers`, `vertical`). `bnb-1` is the twenty-eighth: a full-bleed split field, a tear, and a large cutout overlapping it, with smaller ghosts in the sky.

Motion comes only from `_motion.css` / `_core.js`: bob, float, spin on a slow ring, mouse parallax, letter entrance, marquee. The hero CSS resets `.hero .gchar` so the global sticker frame does not come back. On small screens the absolute mascots drop back into flow so nothing hangs off the side.

## 6. Meme-image art direction

`app_meme/meme_gen.js` keeps the same public API (`MemeGen.SCENES`, `CAPTIONS`, `LAYOUTS`, `sceneCount`, `extractPalette`, `generate`, `colorVariance`, `renderMeme`, `fitCaption`, `drawFittedCaption`, `validateAllCaptions`). `generate()` still returns `{memes, palette, sceneCount, scenes}` and each meme is `{kind, d, on, w, h, scene, layout}` at 1080 and 1600×900.

The picture is built in layers, the way the reference 3D memes read:

1. **A deep scene.** Twenty-six scenes (sunburst, neon city, beach, space, moon, candles, money rain, casino, street, summit, vaporwave, alley, party, desert, underwater, banner, rocket ride, coin vault, rain alley, shrine dusk, stadium, candy sky, subway, volcano, arcade, trading floor). Each has a ground plane, a horizon, and a light source. They are illustrative, not a mesh.
2. **Atmosphere on top of the scene.** The painted background is blurred a little (stronger on a close-up) so the character stays sharp. Then light rays, a top haze, bokeh discs, and a vignette.
3. **A pseudo-3D character.** `drawOrb` clips the logo to a circle, shades it with a radial gradient (highlight upper-left, shadow lower-right), paints a specular blob, strokes a glowing rim, drops a soft ground ellipse, and skews the disc (`transform(1, 0, -0.08, 0.94)`) so it is not a flat sticker. A white sticker frame is the rare case (under one in five), not the default.
4. **Composition, not one crop.** Layouts are `center`, `low-left`, `low-right`, `peek-left`, `peek-right`, `break-bottom`, `rail-left`, `rail-right`, `duo` (a second smaller orb), `closeup`, and `scenic` (character smaller, scene larger).
5. **A prop in the hand.** After the orb, `drawProp` paints coins, a rocket, or a laptop chart overlapping the lower-right of the character so it reads as held.
6. **Caption style changes; the fit does not.** Every image still draws both lines through `drawFittedCaption`, which shrinks and wraps until the bounds sit inside the margin. The style around those lines rotates: impact fill, neon glow, a newspaper band (dark type on a paper rect), a sign board tilted near the character, or a speech bubble. `validateAllCaptions` checks every caption against every layout.

`meme_demo.html` appends the canvas elements. It does not call `toDataURL` while the page is opened from disk, because a `file://` logo taints the canvas.

## 7. Quality pass

Look at the filled sample page, desktop and a 390px width.

- The name is readable in one glance. It is not cut off, not mid-word hyphenated, not hidden under the sticky nav.
- Text on `--bg` uses `--ink`. Text on `--a` uses `--on`. Muted text still clears the background.
- The mascot is the logo (or a character frame around it), not a missing image.
- Sections do not collide. Marquees do not cover the hero type. The banner slot is a frame, not a 220px afterthought.
- Preset mode recolors the background and the scene, not only the button. Original mode still matches the authored palette.
- Horizontal overflow is zero. Buttons are at least 44px tall. The FAQ opens. The contract copies.
- Motion is visible on a scroll and gone when reduced motion is requested.

Ship the screenshot with the template. A page that only looks right in the generator output is not finished.
