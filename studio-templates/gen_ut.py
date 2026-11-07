#!/usr/bin/env python3
"""Generate the 27 reference-inspired user templates."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_sections import (
    NAV, SECTION_CSS, about, tokenomics, HOWTO, roadmap, gallery, FAQ, cta, FOOT,
    marquee, signature,
)
from gen_heroes import hero_parts

OUT = os.path.join(HERE, "templates_src")

def P(h, p):
    return (h, p)

SPECS = [
dict(id="ut-kendu", fonts="family=Archivo+Black&family=Inter:wght@400;600;800", display="'Archivo Black',Impact,sans-serif", body="Inter,system-ui,sans-serif",
     a="#ff2d2d", a2="#ffffff", on="#1a0505", bg="#070707", bg2="#141414", surface="#161616", ink="#f6f3ee", muted="#b9b3a8", line="rgba(255,255,255,.16)", glow="rgba(255,45,45,.45)",
     radius="2px", shadow="8px 8px 0 #000", border="2px solid #f6f3ee", hero="poster", scene="halftone", about="quote", tok="bars", road="stack", gal="rail", cta="band",
     sig=("manifesto","In public","The whole joke is the product","{{CTA}}",[P("No hidden pile","Supply is {{SUPPLY}}. Tax is {{TAX}}."),P("Chain","{{CHAIN_NAME}}, swapped on {{DEX}}."),P("Crowd","{{NAME}} only works if people keep posting.")]),
     voice="h1,h2{text-transform:uppercase;letter-spacing:-.05em}.sec{border-top:1px solid var(--line)}", attr="data-particles data-intro data-sparkles"),
dict(id="ut-dustaster", fonts="family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Outfit:wght@400;600;800", display="Fraunces,Georgia,serif", body="Outfit,system-ui,sans-serif",
     a="#e23b2f", a2="#ffb703", on="#1a0a08", bg="#14080c", bg2="#2a1216", surface="#241014", ink="#f8efe8", muted="#d2b8b0", line="rgba(255,183,3,.35)", glow="rgba(226,59,47,.45)",
     radius="0px", shadow="none", border="1px solid rgba(255,183,3,.45)", hero="splitR", scene="corner", about="split", tok="cards", road="chapters", gal="grid", cta="split",
     sig=("principles","Corner marks","What the mark means","{{TAGLINE}}",[P("One character","The logo is the whole cast until you upload more."),P("One contract","{{CA_SHORT}} on {{CHAIN_NAME}}."),P("One job","Make the timeline worse in a good way.")]),
     voice="h1,h2{font-weight:560}.kicker{letter-spacing:.28em}", attr="data-intro data-sparkles"),
dict(id="ut-lmeow", fonts="family=Fraunces:opsz,wght@9..144,560&family=Nunito:wght@500;800", display="Fraunces,Georgia,serif", body="Nunito,system-ui,sans-serif",
     a="#ff7a59", a2="#ffd166", on="#2a120c", bg="#fff6ef", bg2="#ffe7da", surface="#ffffff", ink="#241812", muted="#6d584e", line="rgba(36,24,18,.12)", glow="rgba(255,122,89,.35)",
     radius="28px", shadow="0 24px 50px rgba(80,40,20,.12)", border="1px solid rgba(36,24,18,.08)", hero="center", scene="blobs", about="overlap", tok="tickets", road="stations", gal="polaroid", cta="ticket",
     sig=("slab","Soft launch","Come sit in the sun","{{CTA}}",[P("Wallet","{{WALLET}} and a little {{NATIVE}}."),P("Swap","{{DEX}}, paste the CA."),P("Stay","{{NAME}} is a mood, not a promise.")]),
     voice=".top{background:color-mix(in srgb,var(--bg) 80%,white)}h2{font-weight:560}", attr="data-intro"),
dict(id="ut-hmmmm", fonts="family=Lilita+One&family=Fredoka:wght@500;700", display="'Lilita One',system-ui,sans-serif", body="Fredoka,system-ui,sans-serif",
     a="#ff5d2e", a2="#2f6fed", on="#1a0c08", bg="#f6f1e7", bg2="#fff", surface="#fffdf8", ink="#1a1a1a", muted="#5c564c", line="#1a1a1a", glow="rgba(255,93,46,.35)",
     radius="18px", shadow="6px 6px 0 #1a1a1a", border="3px solid #1a1a1a", hero="scatter", scene="bubbles", about="beats", tok="cards", road="stack", gal="polaroid", cta="band",
     sig=("meter","Brain noise","How sure are you","{{TAGLINE}}",[P("Curious","You opened the page."),P("Committed","You copied the CA."),P("Unhinged","You made a meme.")]),
     voice="h1,h2{letter-spacing:.01em}", attr="data-particles data-intro"),
dict(id="ut-memebook", fonts="family=Outfit:wght@500;800&family=Inter:wght@400;600", display="Outfit,system-ui,sans-serif", body="Inter,system-ui,sans-serif",
     a="#3b5bfd", a2="#7aa2ff", on="#ffffff", bg="#f4f7fb", bg2="#e7eeff", surface="#ffffff", ink="#12141a", muted="#5c6578", line="rgba(18,20,26,.1)", glow="rgba(59,91,253,.3)",
     radius="22px", shadow="0 20px 50px rgba(30,40,80,.12)", border="1px solid rgba(18,20,26,.08)", hero="app", scene="appcards", about="split", tok="cards", road="stations", gal="rail", cta="ticket",
     sig=("principles","The feed","Three reasons it spreads","{{ABOUT}}",[P("A face","People post the logo before they post the chart."),P("A ticker","${{TICKER}} fits in a caption."),P("A chain","{{CHAIN_NAME}} is where the swap lives.")]),
     voice=".btn{border-radius:999px}", attr="data-intro"),
dict(id="ut-peppin", fonts="family=Anton&family=Manrope:wght@500;800", display="Anton,Impact,sans-serif", body="Manrope,system-ui,sans-serif",
     a="#c6f54e", a2="#8fd14f", on="#102006", bg="#07110c", bg2="#102418", surface="#102016", ink="#e9f6ea", muted="#b7d0bc", line="rgba(198,245,78,.3)", glow="rgba(198,245,78,.4)",
     radius="4px", shadow="none", border="1px solid rgba(198,245,78,.35)", hero="cinema", scene="hills", about="quote", tok="bars", road="chapters", gal="grid", cta="band",
     sig=("manifesto","Field notes","Walk up the hill","{{TAGLINE}}",[P("Night vision","The chart is the landscape."),P("Supply","{{SUPPLY}} and that is the pile."),P("Exit","There isn't a team door. LP is {{LP}}.")]),
     voice="h1{letter-spacing:.02em}h2{font-family:Anton,Impact,sans-serif;letter-spacing:.03em}", attr="data-sparkles data-intro"),
dict(id="ut-toshithecat", fonts="family=Inter+Tight:wght@500;800&family=Inter:wght@400;600", display="'Inter Tight',Inter,sans-serif", body="Inter,system-ui,sans-serif",
     a="#0052ff", a2="#3b7cff", on="#ffffff", bg="#ffffff", bg2="#eef3ff", surface="#f5f8ff", ink="#0b0d12", muted="#4d596c", line="rgba(11,13,18,.1)", glow="rgba(0,82,255,.28)",
     radius="18px", shadow="0 18px 40px rgba(0,40,120,.12)", border="1px solid rgba(11,13,18,.08)", hero="splitL", scene="blobblue", about="split", tok="tickets", road="stations", gal="grid", cta="split",
     sig=("principles","Face of the page","Simple on purpose","{{CTA}}",[P("Blue","The accent is a decision, not a gradient soup."),P("Type","Tight grotesk, lots of air."),P("Trade","{{DEX}} on {{CHAIN_NAME}}.")]),
     voice=".top{border-bottom:1px solid var(--line)}", attr="data-intro"),
dict(id="ut-bnbtiger", fonts="family=Lilita+One&family=Nunito:wght@600;800", display="'Lilita One',system-ui,sans-serif", body="Nunito,system-ui,sans-serif",
     a="#ffd000", a2="#ff7a00", on="#1a1400", bg="#dff4ff", bg2="#bfe8ff", surface="#ffffff", ink="#102033", muted="#3d5870", line="rgba(16,32,51,.15)", glow="rgba(255,208,0,.5)",
     radius="22px", shadow="0 16px 0 rgba(16,32,51,.08)", border="4px solid #102033", hero="sky", scene="clouds", about="overlap", tok="cards", road="stack", gal="polaroid", cta="band",
     sig=("meter","Roar meter","How loud is the jungle","{{TAGLINE}}",[P("Paws","First holders."),P("Stripes","Meme output."),P("Moon","A direction, not a date.")]),
     voice="h1,h2{letter-spacing:.02em}", attr="data-particles data-intro"),
dict(id="ut-avirvox", fonts="family=Instrument+Serif:ital@0;1&family=Poppins:wght@400;600", display="'Instrument Serif',Georgia,serif", body="Poppins,system-ui,sans-serif",
     a="#c084fc", a2="#f0abfc", on="#1a0824", bg="#090411", bg2="#160a24", surface="#140a22", ink="#f6edf8", muted="#cbb8d8", line="rgba(192,132,252,.3)", glow="rgba(192,132,252,.45)",
     radius="16px", shadow="0 0 40px rgba(192,132,252,.15)", border="1px solid rgba(192,132,252,.35)", hero="orbit", scene="rings", about="beats", tok="donut", road="chapters", gal="grid", cta="split",
     sig=("principles","Nodes","A participation layer, remixed","{{ABOUT}}",[P("Signal","Price is just one node."),P("Voice","{{NAME}} is the mascot of showing up."),P("Chain","{{CHAIN_NAME}} carries the swap.")]),
     voice="h1,h2{font-weight:500}", attr="data-particles data-sparkles data-intro"),
dict(id="ut-builderbnb", fonts="family=Syne:wght@700;800&family=Inter:wght@400;600", display="Syne,system-ui,sans-serif", body="Inter,system-ui,sans-serif",
     a="#e8543f", a2="#ffb4a2", on="#1a0806", bg="#0d0c0a", bg2="#1a1210", surface="#161311", ink="#f3eee3", muted="#cbbfb0", line="rgba(243,238,227,.16)", glow="rgba(232,84,63,.4)",
     radius="0px", shadow="none", border="1px solid rgba(243,238,227,.2)", hero="question", scene="marks", about="quote", tok="bars", road="stack", gal="grid", cta="band",
     sig=("manifesto","The test","Builders answer in public","{{CTA}}",[P("Ship","A page, a chart, a meme."),P("Don't hide","CA is on this page."),P("Don't promise","Roadmap is a sequence, not a guarantee.")]),
     voice="h1,h2{letter-spacing:-.04em}", attr="data-intro"),
dict(id="ut-buildon", fonts="family=Montserrat:wght@700;800&family=Inter:wght@400;600", display="Montserrat,system-ui,sans-serif", body="Inter,system-ui,sans-serif",
     a="#39ff88", a2="#b8ff57", on="#041208", bg="#05060a", bg2="#0c1410", surface="#0c1210", ink="#e7ffef", muted="#9dccb0", line="rgba(57,255,136,.28)", glow="rgba(57,255,136,.35)",
     radius="0px", shadow="none", border="1px solid rgba(57,255,136,.4)", hero="craft", scene="grid", about="beats", tok="bars", road="chapters", gal="rail", cta="split",
     sig=("meter","Craft","Tools on the bench","{{TAGLINE}}",[P("Wallet","{{WALLET}}."),P("Native","{{NATIVE}} for gas."),P("DEX","{{DEX}} and the pasted CA.")]),
     voice="h1,h2{text-transform:uppercase;letter-spacing:.04em}.kicker{font-family:ui-monospace,monospace}", attr="data-particles data-intro"),
dict(id="ut-bytedog", fonts="family=Space+Grotesk:wght@500;700&family=Space+Grotesk:wght@400", display="'Space Grotesk',system-ui,sans-serif", body="'Space Grotesk',system-ui,sans-serif",
     a="#ffffff", a2="#9aa0a6", on="#0a0a0a", bg="#0a0a0a", bg2="#141414", surface="#111", ink="#f2f2f2", muted="#a3a3a3", line="rgba(255,255,255,.16)", glow="rgba(255,255,255,.2)",
     radius="0px", shadow="none", border="1px solid rgba(255,255,255,.2)", hero="index", scene="rules", about="split", tok="bars", road="chapters", gal="grid", cta="ticket",
     sig=("manifesto","Paper","A long page on purpose","{{ABOUT}}",[P("01","Name the thing: {{NAME}}."),P("02","Print the numbers: {{SUPPLY}}, tax {{TAX}}."),P("03","Leave the rest to the readers.")]),
     voice="h2{font-weight:500}p{font-size:1.05rem}", attr="data-intro"),
dict(id="ut-cheems", fonts="family=Baloo+2:wght@600;800&family=Outfit:wght@400;700", display="'Baloo 2',system-ui,sans-serif", body="Outfit,system-ui,sans-serif",
     a="#ffb703", a2="#fb8500", on="#1a1204", bg="#1b2430", bg2="#2a1c4a", surface="#241a16", ink="#f7f3ea", muted="#d9cbb8", line="rgba(255,183,3,.3)", glow="rgba(255,183,3,.4)",
     radius="10px", shadow="0 20px 40px rgba(0,0,0,.35)", border="3px solid #ffb703", hero="roof", scene="roof", about="overlap", tok="cards", road="stations", gal="polaroid", cta="band",
     sig=("slab","After dusk","The sign stays on","{{CTA}}",[P("Roof","The hero is a place, not a card."),P("Sign","{{NAME}} in lights."),P("Swap","{{DEX}} when you climb down.")]),
     voice="", attr="data-sparkles data-intro"),
dict(id="ut-cow", fonts="family=Fraunces:opsz,wght@9..144,560&family=Figtree:wght@400;700", display="Fraunces,Georgia,serif", body="Figtree,system-ui,sans-serif",
     a="#e6b325", a2="#8d6a12", on="#1a1404", bg="#fffdf8", bg2="#fff4d6", surface="#ffffff", ink="#1a1208", muted="#6b5c45", line="rgba(26,18,8,.12)", glow="rgba(230,179,37,.4)",
     radius="24px", shadow="0 24px 40px rgba(80,60,10,.1)", border="1px solid rgba(141,106,18,.25)", hero="product", scene="spots", about="split", tok="tickets", road="stations", gal="grid", cta="ticket",
     sig=("principles","Pasture","A clean product page","{{TAGLINE}}",[P("Gold","One metal, used sparingly."),P("White","Room for the character."),P("Numbers","{{SUPPLY_SHORT}} supply, tax {{TAX}}.")]),
     voice="h1,h2{font-weight:560}", attr="data-intro"),
dict(id="ut-dorausd1", fonts="family=Playfair+Display:wght@500;700&family=Libre+Baskerville:ital,wght@0,400;1,400", display="'Playfair Display',Georgia,serif", body="'Libre Baskerville',Georgia,serif",
     a="#d4a373", a2="#f1d7b5", on="#1a100c", bg="#1a100c", bg2="#2a1a14", surface="#241610", ink="#f3e6d8", muted="#d9c4b0", line="rgba(212,163,115,.35)", glow="rgba(212,163,115,.35)",
     radius="0px", shadow="none", border="1px solid rgba(212,163,115,.4)", hero="letterbox", scene="grain", about="quote", tok="bars", road="chapters", gal="grid", cta="band",
     sig=("slab","Still","A portrait, not a dashboard","{{ABOUT}}",[P("Frame","Letterbox the hero."),P("Voice","Serif, slow, specific."),P("Trade","Still just {{DEX}} and a CA.")]),
     voice="h1,h2{font-weight:500}p{font-size:1.05rem}", attr="data-intro"),
dict(id="ut-dragonx", fonts="family=Chakra+Petch:wght@600;700&family=Sora:wght@400;600", display="'Chakra Petch',system-ui,sans-serif", body="Sora,system-ui,sans-serif",
     a="#2ee6a6", a2="#7cf0ff", on="#04140f", bg="#071116", bg2="#0c1c22", surface="#0c1818", ink="#e7fff8", muted="#9dccc0", line="rgba(46,230,166,.3)", glow="rgba(46,230,166,.4)",
     radius="2px", shadow="none", border="1px solid rgba(46,230,166,.4)", hero="hud", scene="circuit", about="beats", tok="donut", road="stack", gal="rail", cta="split",
     sig=("meter","Telemetry","Readouts, not slogans","{{TAGLINE}}",[P("Link","Contract copied, not trusted blindly."),P("Fuel","{{NATIVE}} on {{CHAIN_NAME}}."),P("Hull","LP {{LP}}.")]),
     voice=".kicker{font-family:ui-monospace,monospace}", attr="data-particles data-intro"),
dict(id="ut-bnboo", fonts="family=Nunito:wght@700;900&family=Quicksand:wght@500;700", display="Nunito,system-ui,sans-serif", body="Quicksand,system-ui,sans-serif",
     a="#2f6bff", a2="#9db7ff", on="#ffffff", bg="#f3f7ff", bg2="#e4edff", surface="#ffffff", ink="#122033", muted="#54657c", line="rgba(18,32,51,.1)", glow="rgba(47,107,255,.3)",
     radius="32px", shadow="0 20px 40px rgba(40,70,140,.12)", border="0px solid transparent", hero="ghost", scene="ghost", about="overlap", tok="tickets", road="stations", gal="polaroid", cta="ticket",
     sig=("principles","Soft","A ghost with a ticker","{{CTA}}",[P("Round","Circles, not knives."),P("Blue","One cool color."),P("Swap","{{WALLET}} to {{DEX}}.")]),
     voice="", attr="data-intro"),
dict(id="ut-lolonhood", fonts="family=Bodoni+Moda:opsz,wght@6..96,500;6..96,700&family=Newsreader:opsz,wght@6..72,400", display="'Bodoni Moda',Georgia,serif", body="Newsreader,Georgia,serif",
     a="#111111", a2="#e10600", on="#f7f4ef", bg="#f7f4ef", bg2="#fff", surface="#fff", ink="#141414", muted="#4e4944", line="rgba(20,20,20,.16)", glow="rgba(225,6,0,.25)",
     radius="0px", shadow="none", border="1px solid #141414", hero="magazine", scene="mag", about="quote", tok="cards", road="chapters", gal="grid", cta="band",
     sig=("manifesto","Cover lines","The reaction is the brand","{{TAGLINE}}",[P("Masthead","Name enormous, body quiet."),P("Red","One alarm color."),P("Footer","The disclaimer stays in the colophon.")]),
     voice="h2{font-weight:500}.btn-main{border-radius:0}", attr="data-intro"),
dict(id="ut-mamesuke", fonts="family=Shippori+Mincho:wght@500;700&family=Zen+Kaku+Gothic+New:wght@400;700", display="'Shippori Mincho',serif", body="'Zen Kaku Gothic New',system-ui,sans-serif",
     a="#c4312e", a2="#e8b86d", on="#fff8f2", bg="#f7f1e8", bg2="#f3e2c8", surface="#fffaf3", ink="#2a1c14", muted="#6d5648", line="rgba(196,49,46,.3)", glow="rgba(196,49,46,.25)",
     radius="4px", shadow="none", border="1px solid rgba(196,49,46,.4)", hero="seal", scene="seal", about="split", tok="tickets", road="stack", gal="polaroid", cta="ticket",
     sig=("slab","Seal","Small dog energy, big page","{{ABOUT}}",[P("Paper","Warm, ruled, unhurried."),P("Red","A stamp, not a neon sign."),P("Numbers","{{SUPPLY_SHORT}} / tax {{TAX}}.")]),
     voice="h1,h2{font-weight:500}", attr="data-intro"),
dict(id="ut-marscoinbnb", fonts="family=Russo+One&family=Sora:wght@400;600", display="'Russo One',sans-serif", body="Sora,system-ui,sans-serif",
     a="#ff6b35", a2="#ffd166", on="#2a0c06", bg="#1a0b0c", bg2="#3a1610", surface="#2a1210", ink="#ffe8d6", muted="#e2b8a4", line="rgba(255,107,53,.35)", glow="rgba(255,107,53,.4)",
     radius="8px", shadow="none", border="1px solid rgba(255,107,53,.4)", hero="planet", scene="planet", about="beats", tok="bars", road="chapters", gal="rail", cta="band",
     sig=("meter","Descent","Dust, then a ticker","{{TAGLINE}}",[P("Orbit","The hero is a horizon."),P("Cargo","{{NATIVE}} in {{WALLET}}."),P("Landing","Swap on {{DEX}}.")]),
     voice="h1{letter-spacing:.04em}", attr="data-sparkles data-intro"),
dict(id="ut-penpehood", fonts="family=Lilita+One&family=Mulish:wght@500;800", display="'Lilita One',system-ui,sans-serif", body="Mulish,system-ui,sans-serif",
     a="#c6ff00", a2="#10180a", on="#10180a", bg="#fbfff2", bg2="#f0ffc8", surface="#ffffff", ink="#10180a", muted="#3d4a28", line="rgba(16,24,10,.14)", glow="rgba(198,255,0,.5)",
     radius="999px", shadow="0 10px 0 #10180a", border="3px solid #10180a", hero="launch", scene="sun", about="overlap", tok="cards", road="stations", gal="grid", cta="ticket",
     sig=("principles","Open","A launch you can read","{{CTA}}",[P("Button","One lime action."),P("Name","Giant, centered, no mystery."),P("Steps","Wallet, {{NATIVE}}, {{DEX}}, done.")]),
     voice=".btn-main{border-radius:999px}", attr="data-intro"),
dict(id="ut-pepeacc", fonts="family=Anton&family=IBM+Plex+Mono:wght@400;600", display="Anton,Impact,sans-serif", body="'IBM Plex Mono',ui-monospace,monospace",
     a="#3d7eff", a2="#9ec1ff", on="#ffffff", bg="#03050d", bg2="#0c1428", surface="#0b1224", ink="#f4f7ff", muted="#b7c3dd", line="rgba(61,126,255,.35)", glow="rgba(61,126,255,.45)",
     radius="0px", shadow="none", border="1px solid rgba(61,126,255,.4)", hero="impact", scene="galaxy", about="quote", tok="bars", road="stack", gal="rail", cta="band",
     sig=("manifesto","Accelerate","Poster first, dashboard never","{{TAGLINE}}",[P("Type","Impact, stacked, too big."),P("Space","A glow, not a stock photo."),P("CA","{{CA_SHORT}} — copy it or don't.")]),
     voice="h2{text-transform:uppercase;letter-spacing:.03em}", attr="data-sparkles data-intro"),
dict(id="ut-therobincoin", fonts="family=IBM+Plex+Mono:wght@500;700&family=DM+Sans:wght@400;700", display="'IBM Plex Mono',ui-monospace,monospace", body="'DM Sans',system-ui,sans-serif",
     a="#c8f542", a2="#19c37d", on="#07140a", bg="#07140f", bg2="#0d2418", surface="#0e1c16", ink="#e7f7ee", muted="#b7d2c4", line="rgba(200,245,66,.3)", glow="rgba(200,245,66,.35)",
     radius="6px", shadow="none", border="1px solid rgba(200,245,66,.35)", hero="desk", scene="candles", about="beats", tok="donut", road="chapters", gal="grid", cta="split",
     sig=("meter","Tape","A desk, not a cinematic","{{ABOUT}}",[P("Candles","The background is the chart joke."),P("Mono","Numbers in a terminal face."),P("Swap","{{DEX}} still, like everyone else.")]),
     voice=".kicker{font-family:ui-monospace,monospace}", attr="data-intro"),
dict(id="ut-swappymascot", fonts="family=Lilita+One&family=DM+Sans:wght@400;700", display="'Lilita One',system-ui,sans-serif", body="'DM Sans',system-ui,sans-serif",
     a="#ff4fa3", a2="#ffd0ea", on="#2a1020", bg="#fff5fb", bg2="#ffe4f3", surface="#ffffff", ink="#2a1028", muted="#7a4b68", line="rgba(255,79,163,.28)", glow="rgba(255,79,163,.3)",
     radius="20px", shadow="0 16px 40px rgba(120,30,70,.1)", border="2px solid #2a1028", hero="chapter", scene="waves", about="split", tok="tickets", road="stations", gal="polaroid", cta="band",
     sig=("principles","Lore","Chapters, not feature grids","{{TAGLINE}}",[P("01","A character walks into the page."),P("02","The contract is a footnote you can copy."),P("03","The community writes chapter two.")]),
     voice="", attr="data-intro data-particles"),
dict(id="ut-tanukibnb", fonts="family=Cormorant+Garamond:wght@600;700&family=Inter:wght@400;600", display="'Cormorant Garamond',Georgia,serif", body="Inter,system-ui,sans-serif",
     a="#b45309", a2="#f5d39a", on="#fff8ef", bg="#f4ead4", bg2="#efe0c4", surface="#fffaf1", ink="#1d1712", muted="#6b5644", line="rgba(180,83,9,.3)", glow="rgba(180,83,9,.25)",
     radius="2px", shadow="none", border="1px solid rgba(180,83,9,.4)", hero="shrine", scene="torii", about="quote", tok="cards", road="chapters", gal="polaroid", cta="ticket",
     sig=("slab","Shrine","Luck you can screenshot","{{CTA}}",[P("Gate","The hero is a place."),P("Coin","${{TICKER}} on {{CHAIN_NAME}}."),P("Leave","Not advice. A visit.")]),
     voice="h1,h2{font-weight:600}", attr="data-intro"),
dict(id="ut-thejoecoin", fonts="family=Bangers&family=Poppins:wght@400;600", display="Bangers,system-ui,sans-serif", body="Poppins,system-ui,sans-serif",
     a="#ffe14a", a2="#ff5d8f", on="#1a1404", bg="#121212", bg2="#1c1c1c", surface="#1a1a1a", ink="#f7f7f5", muted="#c8c8c4", line="rgba(255,255,255,.14)", glow="rgba(255,225,74,.4)",
     radius="14px", shadow="6px 6px 0 #000", border="3px solid #ffe14a", hero="stickers", scene="stickers", about="beats", tok="cards", road="stack", gal="polaroid", cta="band",
     sig=("principles","Stickers","A sheet, not a brand system","{{TAGLINE}}",[P("Peel","The logo repeats until you upload poses."),P("Caption","{{NAME}} does not need a tagline team."),P("Buy","{{DEX}}, if you want.")]),
     voice="h1{letter-spacing:.04em}", attr="data-particles data-intro"),
dict(id="ut-komabnb", fonts="family=Dela+Gothic+One&family=Zen+Maru+Gothic:wght@500;700", display="'Dela Gothic One',system-ui,sans-serif", body="'Zen Maru Gothic',system-ui,sans-serif",
     a="#ff2442", a2="#ffd1dc", on="#ffffff", bg="#140306", bg2="#2a0a10", surface="#24080e", ink="#fff5f6", muted="#e7b8c0", line="rgba(255,36,66,.4)", glow="rgba(255,36,66,.4)",
     radius="0px", shadow="10px 10px 0 #ff2442", border="2px solid #ff2442", hero="vertical", scene="stripes", about="quote", tok="bars", road="chapters", gal="rail", cta="split",
     sig=("manifesto","Poster","Vertical type, red bars","{{ABOUT}}",[P("Column","The name reads down the side."),P("Stripe","The background is a rhythm."),P("Exit","Footer, disclaimer, done.")]),
     voice="h2{letter-spacing:.04em}", attr="data-intro data-sparkles"),
]

BASE = """
:root{
 --a:__A__;--a2:__A2__;--on:__ON__;--acc:var(--a);--part:var(--a);
 --bg:__BG__;--bg-2:__BG2__;--surface:__SURF__;--card:var(--surface);
 --ink:__INK__;--muted:__MUTED__;--line:__LINE__;
 --glow:__GLOW__;--grad:linear-gradient(135deg,var(--a),var(--a2));
 --radius:__RADIUS__;--shadow:__SHADOW__;--border:__BORDER__;
 --display:__DISPLAY__;--body:__BODY__;
}
*{box-sizing:border-box}
html,body{overflow-x:clip}
body{margin:0;color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.6;
 background:
  radial-gradient(1000px 520px at 100% -10%, color-mix(in srgb, var(--a) 32%, transparent), transparent 62%),
  radial-gradient(800px 480px at -10% 20%, color-mix(in srgb, var(--a2) 26%, transparent), transparent 60%),
  var(--bg)}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit}
h1,h2,h3{font-family:var(--display);line-height:.95}
.scene .bg{fill:var(--bg)}
.scene .bg2{fill:var(--bg-2)}
.scene .surf{fill:var(--surface)}
.scene .a{fill:var(--a);stroke:var(--a)}
.scene .a2{fill:var(--a2);stroke:var(--a2)}
.scene .ink{fill:var(--ink);stroke:var(--ink)}
.scene .line,.scene .a[fill="none"],.scene .a2[fill="none"],.scene .ink[fill="none"]{fill:none}
.scene{display:block}
.gchar{background:
  radial-gradient(circle at 30% 30%, color-mix(in srgb, var(--a) 35%, var(--surface)), var(--surface));
  border:var(--border);border-radius:var(--radius);box-shadow:var(--shadow);object-fit:contain}
"""

def css_for(s, hero_css):
    out = (BASE
        .replace("__A__", s["a"]).replace("__A2__", s["a2"]).replace("__ON__", s["on"])
        .replace("__BG__", s["bg"]).replace("__BG2__", s["bg2"]).replace("__SURF__", s["surface"])
        .replace("__INK__", s["ink"]).replace("__MUTED__", s["muted"]).replace("__LINE__", s["line"])
        .replace("__GLOW__", s["glow"]).replace("__RADIUS__", s["radius"])
        .replace("__SHADOW__", s["shadow"]).replace("__BORDER__", s["border"])
        .replace("__DISPLAY__", s["display"]).replace("__BODY__", s["body"]))
    return out + "\n" + SECTION_CSS + "\n" + hero_css + "\n" + s.get("voice","")

def body_for(s, hero_html):
    sig = signature(*s["sig"])
    blocks = {
        "hero": hero_html,
        "mq": marquee(26) + marquee(34, True),
        "banner": "<!--BANNER_SLOT-->",
        "about": about(s["about"]),
        "sig": sig,
        "tok": tokenomics(s["tok"]),
        "how": HOWTO,
        "road": roadmap(s["road"]),
        "gal": gallery(s["gal"]),
        "faq": FAQ,
        "cta": cta(s["cta"]),
        "foot": FOOT,
    }
    order = ["hero","mq","banner","about","sig","tok","how","road","gal","faq","cta","foot"]
    # rotate middle so neighboring templates don't share a rhythm
    i = SPECS.index(s) % 3
    if i == 1:
        order = ["hero","mq","banner","sig","about","tok","road","how","gal","faq","cta","foot"]
    elif i == 2:
        order = ["hero","banner","mq","about","tok","sig","how","gal","road","faq","cta","foot"]
    inner = NAV + "\n".join(blocks[k] for k in order)
    return "<body %s>\n%s\n</body>" % (s["attr"], inner)

def banner_line(s):
    css = (".mbanner{max-width:min(1120px,calc(100% - 40px));margin:8px auto 28px}"
           ".mbanner img{width:100%;height:auto;max-height:460px;object-fit:cover;border-radius:"
           + s["radius"] + ";border:" + s["border"] + ";box-shadow:" + s["shadow"] + "}")
    return "'%s':('before','<!--BANNER_SLOT-->',FIG,%s)," % (s["id"], repr(css))

def main():
    spec_path = os.path.join(OUT, "banner_spec.py")
    text = open(spec_path).read()
    for s in SPECS:
        hero_css, hero_html = hero_parts(s["hero"], s["scene"])
        doc = "@@FONTS@@ %s\n@@CSS@@\n%s\n@@BODY@@\n%s\n@@JS@@\n" % (s["fonts"], css_for(s, hero_css), body_for(s, hero_html))
        open(os.path.join(OUT, s["id"] + ".html"), "w").write(doc)
        text2, n = re.subn(r"^'%s':\(.*\),$" % s["id"], banner_line(s), text, count=1, flags=re.M)
        if n != 1:
            raise SystemExit("banner spec miss " + s["id"])
        text = text2
        print("wrote", s["id"], "chars", len(doc))
    open(spec_path, "w").write(text)

if __name__ == "__main__":
    main()
