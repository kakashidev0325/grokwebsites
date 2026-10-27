"""Section builders and illustrated scenes for the user templates."""

def svg(sid, inner):
    return (
        '<svg class="scene" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
        + inner.replace("GID", sid)
        + "</svg>"
    )

SCENES = {}

def _reg(name, inner):
    SCENES[name] = inner

_reg("halftone", '''
<defs><radialGradient id="GIDg" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#2a2a2a"/><stop offset="1" stop-color="#050505"/></radialGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="#ff2d2d" opacity=".35">''' + "".join(
    f'<circle cx="{(i*97)%1440}" cy="{(i*53)%900}" r="{2+(i%5)}"/>' for i in range(0,180,1)
) + '''</g>
<circle cx="720" cy="360" r="280" fill="none" stroke="#fff" stroke-opacity=".08" stroke-width="40"/>
<circle cx="720" cy="360" r="180" fill="none" stroke="#ff2d2d" stroke-opacity=".4" stroke-width="2"/>
''')

_reg("corner", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a1014"/><stop offset="1" stop-color="#14080c"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g stroke="#e23b2f" stroke-width="3" fill="none" opacity=".8"><path d="M80 80h120M80 80v120M1360 80h-120M1360 80v120M80 820h120M80 820v-120M1360 820h-120M1360 820v-120"/></g>
<g stroke="#ffb703" stroke-opacity=".25">''' + "".join(f'<line x1="0" y1="{y}" x2="1440" y2="{y}"/>' for y in range(40,900,46)) + '''</g>
<circle cx="1180" cy="220" r="90" fill="#e23b2f" opacity=".25"/>
''')

_reg("blobs", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff6ee"/><stop offset="1" stop-color="#ffe1d2"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<ellipse cx="260" cy="180" rx="220" ry="140" fill="#ffd166" opacity=".7"/>
<ellipse cx="1180" cy="160" rx="260" ry="150" fill="#ffb4a2" opacity=".8"/>
<ellipse cx="720" cy="760" rx="480" ry="180" fill="#fff" opacity=".65"/>
<circle cx="180" cy="640" r="70" fill="#ff7a59" opacity=".35"/>
<circle cx="1260" cy="620" r="46" fill="#ffd166"/>
''')

_reg("bubbles", '''
<rect width="1440" height="900" fill="#f6f1e7"/>
<g fill="none" stroke="#1a1a1a" stroke-width="3">
<circle cx="180" cy="160" r="70"/><circle cx="1240" cy="200" r="110"/><circle cx="980" cy="680" r="80"/><circle cx="300" cy="700" r="40"/>
</g>
<path d="M200 400c80-80 160-20 220 10" stroke="#ff5d2e" stroke-width="8" fill="none" stroke-linecap="round"/>
<path d="M1100 420c60 40 140 20 180-30" stroke="#2f6fed" stroke-width="8" fill="none" stroke-linecap="round"/>
<g fill="#ff5d2e">''' + "".join(f'<circle cx="{80+i*90}" cy="{120+(i%4)*30}" r="6"/>' for i in range(14)) + '''</g>
''')

_reg("appcards", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef3ff"/><stop offset="1" stop-color="#f7f9fc"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g opacity=".9">
<rect x="160" y="140" width="280" height="170" rx="22" fill="#fff" stroke="#d5def0"/>
<rect x="980" y="180" width="300" height="150" rx="22" fill="#fff" stroke="#d5def0"/>
<rect x="1040" y="560" width="240" height="140" rx="22" fill="#3b5bfd" opacity=".15"/>
<rect x="180" y="600" width="220" height="120" rx="22" fill="#fff" stroke="#d5def0"/>
</g>
<circle cx="720" cy="420" r="180" fill="#3b5bfd" opacity=".06"/>
''')

_reg("hills", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c2418"/><stop offset=".55" stop-color="#123222"/><stop offset="1" stop-color="#07110c"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<circle cx="1120" cy="180" r="70" fill="#c6f54e" opacity=".85"/>
<g fill="#0a1c12"><path d="M0 620c160-80 280-40 420-90s260-20 400 40 280 30 620-60v390H0z"/><path d="M0 740c200-60 360-20 520-70s300 10 460 30 240-20 460-80v280H0z" opacity=".8"/></g>
<g fill="#c6f54e" opacity=".35">''' + "".join(f'<circle cx="{(i*137)%1440}" cy="{(i*61)%280}" r="1.4"/>' for i in range(80)) + '''</g>
''')

_reg("blobblue", '''
<rect width="1440" height="900" fill="#ffffff"/>
<ellipse cx="1080" cy="420" rx="340" ry="300" fill="#0052ff"/>
<ellipse cx="1180" cy="360" rx="180" ry="160" fill="#3b7cff" opacity=".8"/>
<circle cx="200" cy="160" r="40" fill="#0052ff" opacity=".12"/>
<circle cx="260" cy="760" r="90" fill="#0052ff" opacity=".08"/>
''')

_reg("clouds", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd3ff"/><stop offset=".6" stop-color="#d8f3ff"/><stop offset="1" stop-color="#fff6d8"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="#fff">
<ellipse cx="200" cy="180" rx="120" ry="46"/><ellipse cx="280" cy="170" rx="80" ry="40"/><ellipse cx="140" cy="190" rx="70" ry="36"/>
<ellipse cx="980" cy="140" rx="150" ry="50"/><ellipse cx="1080" cy="130" rx="90" ry="42"/>
<ellipse cx="620" cy="220" rx="100" ry="36"/>
</g>
<path d="M0 700c120-70 200-20 320-50s220-10 320 40 240 20 360-30 220-40 440 20v220H0z" fill="#2f9e44"/>
<path d="M0 780c180-40 300-10 460-36s280 8 420 20 260-20 560-10v146H0z" fill="#1f7a32"/>
<circle cx="1180" cy="250" r="54" fill="#ffd000"/>
''')

_reg("rings", '''
<defs><radialGradient id="GIDg" cx="50%" cy="45%" r="65%"><stop offset="0" stop-color="#2a1840"/><stop offset="1" stop-color="#090411"/></radialGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="none" stroke="#c084fc" stroke-opacity=".55"><circle cx="720" cy="430" r="120"/><circle cx="720" cy="430" r="200"/><circle cx="720" cy="430" r="290"/><circle cx="720" cy="430" r="380"/></g>
<g fill="#f0abfc">''' + "".join(
    f'<circle cx="{720+int(__import__("math").cos(i)*r)}" cy="{430+int(__import__("math").sin(i)*r)}" r="5"/>'
    for i,r in ((0.2,200),(1.2,290),(2.4,380),(3.6,120),(4.4,290),(5.2,200))
) + '''</g>
<g fill="#fff" opacity=".7">''' + "".join(f'<circle cx="{(i*113)%1440}" cy="{(i*47)%900}" r="1.2"/>' for i in range(70)) + '''</g>
''')

_reg("marks", '''
<rect width="1440" height="900" fill="#0d0c0a"/>
<g stroke="#e8543f" stroke-width="8" fill="none" opacity=".8"><path d="M160 220l70 70M230 220l-70 70"/><path d="M1180 560l80 80M1260 560l-80 80"/></g>
<g fill="#f3eee3" opacity=".05" font-family="sans-serif" font-size="180" font-weight="700"><text x="80" y="760">?</text><text x="980" y="280">?</text></g>
''')

_reg("grid", '''
<rect width="1440" height="900" fill="#05060a"/>
<g stroke="#39ff88" stroke-opacity=".18">''' + "".join(f'<path d="M{x} 0v900M0 {y}h1440"/>' for x in range(0,1440,48) for y in [0]) + "".join(f'<path d="M0 {y}h1440"/>' for y in range(0,900,48)) + '''</g>
<rect x="80" y="80" width="200" height="120" fill="none" stroke="#39ff88"/>
<rect x="1100" y="640" width="240" height="140" fill="none" stroke="#b8ff57"/>
<circle cx="720" cy="450" r="8" fill="#39ff88"/>
''')

_reg("rules", '''
<rect width="1440" height="900" fill="#0a0a0a"/>
<g stroke="#fff" stroke-opacity=".12">''' + "".join(f'<path d="M80 {y}h1280"/>' for y in range(120,860,36)) + '''</g>
<rect x="70" y="70" width="6" height="760" fill="#fff"/>
''')

_reg("roof", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f2b56b"/><stop offset=".45" stop-color="#e36a4a"/><stop offset="1" stop-color="#2a1c4a"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="#1a1030" opacity=".85">
<rect x="40" y="420" width="70" height="280"/><rect x="130" y="360" width="90" height="340"/><rect x="240" y="470" width="60" height="230"/>
<rect x="1040" y="390" width="80" height="310"/><rect x="1140" y="330" width="110" height="370"/><rect x="1270" y="450" width="90" height="250"/>
</g>
<g fill="#ffd27a" opacity=".8">''' + "".join(f'<rect x="{60+(i%8)*28}" y="{440+(i%5)*36}" width="8" height="12"/>' for i in range(40)) + '''</g>
<path d="M0 700h1440v200H0z" fill="#24160f"/>
<rect x="0" y="690" width="1440" height="16" fill="#6a4a38"/>
''')

_reg("spots", '''
<rect width="1440" height="900" fill="#fffdf8"/>
<g fill="#e6b325" opacity=".18">''' + "".join(f'<ellipse cx="{(i*173)%1440}" cy="{(i*97)%900}" rx="{30+(i%4)*12}" ry="{18+(i%3)*8}"/>' for i in range(18)) + '''</g>
<circle cx="1180" cy="200" r="90" fill="none" stroke="#e6b325" stroke-width="14"/>
''')

_reg("grain", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a241c"/><stop offset="1" stop-color="#140c09"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<rect x="80" y="70" width="1280" height="760" fill="none" stroke="#d4a373" stroke-opacity=".4"/>
<rect x="100" y="90" width="1240" height="720" fill="none" stroke="#d4a373" stroke-opacity=".2"/>
<g fill="#f3e6d8" opacity=".15">''' + "".join(f'<circle cx="{(i*89)%1440}" cy="{(i*57)%900}" r="1"/>' for i in range(120)) + '''</g>
''')

_reg("circuit", '''
<rect width="1440" height="900" fill="#071116"/>
<g stroke="#2ee6a6" stroke-width="2" fill="none" opacity=".7">
<path d="M80 200h300l40 40h200l40-40h400"/><path d="M200 700h240l50-80h180l40 80h500"/>
<path d="M400 200v180h120v120"/><path d="M1000 160v240h160"/>
</g>
<g fill="#2ee6a6"><circle cx="380" cy="200" r="6"/><circle cx="620" cy="240" r="6"/><circle cx="1020" cy="160" r="6"/><circle cx="440" cy="620" r="6"/><circle cx="1160" cy="700" r="6"/></g>
<g stroke="#7cf0ff" stroke-opacity=".25">''' + "".join(f'<path d="M{x} 0v900"/>' for x in range(0,1440,80)) + '''</g>
''')

_reg("ghost", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9e6ff"/><stop offset="1" stop-color="#f7f9ff"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<ellipse cx="300" cy="200" rx="180" ry="80" fill="#fff" opacity=".8"/>
<ellipse cx="1100" cy="160" rx="220" ry="90" fill="#fff"/>
<path d="M520 760c40-80 80-80 120 0s80 80 120 0 80-80 120 0v140H520z" fill="#fff"/>
<circle cx="200" cy="640" r="16" fill="#2f6bff" opacity=".4"/>
''')

_reg("mag", '''
<rect width="1440" height="900" fill="#f7f4ef"/>
<rect x="0" y="0" width="1440" height="18" fill="#111"/>
<rect x="0" y="882" width="1440" height="18" fill="#111"/>
<g stroke="#111" stroke-opacity=".15">''' + "".join(f'<path d="M{x} 40v820"/>' for x in (360,720,1080)) + '''</g>
''')

_reg("seal", '''
<rect width="1440" height="900" fill="#f7f1e8"/>
<g stroke="#c4312e" stroke-opacity=".25">''' + "".join(f'<path d="M0 {y}h1440"/>' for y in range(0,900,28)) + '''</g>
<circle cx="1180" cy="220" r="92" fill="none" stroke="#c4312e" stroke-width="8"/>
<circle cx="1180" cy="220" r="70" fill="none" stroke="#c4312e" stroke-width="2"/>
''')

_reg("planet", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b0c18"/><stop offset=".5" stop-color="#6a1d14"/><stop offset="1" stop-color="#c4532a"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="#fff" opacity=".85">''' + "".join(f'<circle cx="{(i*131)%1440}" cy="{(i*47)%420}" r="{1+(i%3)}"/>' for i in range(60)) + '''</g>
<ellipse cx="720" cy="980" rx="820" ry="360" fill="#8d2f1e"/>
<ellipse cx="720" cy="900" rx="700" ry="180" fill="#c4532a"/>
<ellipse cx="980" cy="760" rx="80" ry="28" fill="#6a1d14" opacity=".5"/>
<circle cx="240" cy="180" r="36" fill="#ffd166" opacity=".8"/>
''')

_reg("sun", '''
<rect width="1440" height="900" fill="#fbfff2"/>
<g fill="#c6ff00" opacity=".35">''' + "".join(
    f'<polygon points="720,180 {720+int(__import__("math").cos(i)*40)},{180+int(__import__("math").sin(i)*40)} {720+int(__import__("math").cos(i+0.18)*520)},{180+int(__import__("math").sin(i+0.18)*520)}"/>'
    for i in [n*0.52 for n in range(12)]
) + '''</g>
<circle cx="720" cy="180" r="70" fill="#c6ff00"/>
''')

_reg("galaxy", '''
<defs><radialGradient id="GIDg" cx="60%" cy="40%" r="70%"><stop offset="0" stop-color="#1a3c8c"/><stop offset=".5" stop-color="#0a1230"/><stop offset="1" stop-color="#03050d"/></radialGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<g fill="#fff">''' + "".join(f'<circle cx="{(i*97)%1440}" cy="{(i*71)%900}" r="{0.8+(i%4)*0.6}" opacity="{0.4+(i%5)*0.1}"/>' for i in range(90)) + '''</g>
<ellipse cx="860" cy="420" rx="340" ry="90" fill="none" stroke="#7eb6ff" stroke-opacity=".45" transform="rotate(-18 860 420)"/>
<ellipse cx="860" cy="420" rx="220" ry="50" fill="#3d7eff" opacity=".15" transform="rotate(-18 860 420)"/>
''')

_reg("candles", '''
<rect width="1440" height="900" fill="#07140f"/>
<g>''' + "".join(
    '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#163028" stroke-width="2"/>'
    '<rect x="%d" y="%d" width="20" height="%d" fill="%s" opacity=".85"/>' % (
        40+i*46, 700-(i*17%220), 40+i*46, 700-(i*17%220)-80-(i%5)*20,
        40+i*46-10, 640-(i*13%180), 50+(i%4)*18, "#c8f542" if i%3 else "#19c37d"
    )
    for i in range(30)
) + '''</g>
''')

_reg("waves", '''
<defs><linearGradient id="GIDg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe4f4"/><stop offset="1" stop-color="#fff5fb"/></linearGradient></defs>
<rect width="1440" height="900" fill="url(#GIDg)"/>
<path d="M0 640c120 40 240-40 360-20s240 60 360 20 240-70 360-20 240 40 360 10v270H0z" fill="#ffd0ea"/>
<path d="M0 720c160 30 280-30 420-10s260 40 400 10 240-40 360-16 180 20 260 8v188H0z" fill="#ff4fa3" opacity=".35"/>
<circle cx="240" cy="180" r="40" fill="#fff"/>
''')

_reg("torii", '''
<rect width="1440" height="900" fill="#f4ead4"/>
<g fill="none" stroke="#b45309" stroke-width="10"><path d="M420 760V340h600v420"/><path d="M360 340h720"/><path d="M400 400h640"/></g>
<circle cx="720" cy="250" r="46" fill="#b45309" opacity=".85"/>
<g fill="#1d1712" opacity=".06">''' + "".join(f'<circle cx="{200+i*80}" cy="800" r="18"/>' for i in range(14)) + '''</g>
''')

_reg("stickers", '''
<rect width="1440" height="900" fill="#161616"/>
<g>
<rect x="120" y="120" width="180" height="140" rx="16" fill="#ffe14a" transform="rotate(-8 210 190)"/>
<rect x="1100" y="160" width="200" height="150" rx="18" fill="#ff5d8f" transform="rotate(7 1200 235)"/>
<rect x="180" y="620" width="160" height="120" rx="14" fill="#7cffb2" transform="rotate(6 260 680)"/>
<rect x="1080" y="600" width="220" height="150" rx="16" fill="#8ab4ff" transform="rotate(-6 1190 675)"/>
</g>
''')

_reg("stripes", '''
<rect width="1440" height="900" fill="#140306"/>
<g>''' + "".join(
    f'<rect x="{i*48}" y="0" width="24" height="900" fill="#ff2442" opacity="{0.15+(i%3)*0.08}"/>' for i in range(30)
) + '''</g>
<circle cx="720" cy="450" r="220" fill="none" stroke="#fff" stroke-opacity=".2" stroke-width="2"/>
''')

def scene(name, sid):
    from gen_scenes import scene_svg
    return scene_svg(name)

NAV = '''
<header class="top">
  <a class="brand" href="#top"><img src="{{LOGO}}" alt="" width="64" height="64"><b>{{NAME}}</b><em>${{TICKER}}</em></a>
  <nav class="navlinks">
    <a href="#lore">Lore</a><a href="#token">Token</a><a href="#buy">Buy</a><a href="#road">Road</a><a href="#memes">Memes</a><a href="#faq">FAQ</a>
  </nav>
  <div class="top-actions">
    [[SOCIALS]]
    <a class="btn btn-main btn-shine" data-magnetic data-buy href="{{BUY_URL}}">[[BUY]] Buy</a>
    <button class="burger" type="button" data-menu aria-label="Open menu"><i></i><i></i><i></i></button>
  </div>
</header>
'''

def marquee(speed, rev=False):
    cls = "mq rev" if rev else "mq"
    return f'''<div class="{cls}" style="--mq-speed:{speed}s"><div class="mq-track"><span>${{{{TICKER}}}} ✦ {{{{NAME}}}} ✦ {{{{TAGLINE}}}} ✦ LP {{{{LP}}}} ✦ TAX {{{{TAX}}}} ✦ {{{{CHAIN_NAME}}}} ✦ {{{{CTA}}}} ✦ BUY ${{{{TICKER}}}} ✦ </span></div></div>'''

ACTIONS = '''
<div class="hero-actions">
  <a class="btn btn-main btn-shine btn-pulse" data-magnetic data-buy href="{{BUY_URL}}">[[BUY]] Buy ${{TICKER}}</a>
  <a class="btn btn-ghost" href="{{DEXS_URL}}" target="_blank" rel="noopener">[[DEX]] Chart</a>
  <button class="btn btn-ghost" type="button" data-copy>[[COPY]] <code>{{CA_SHORT}}</code></button>
</div>
'''

def about(mode):
    if mode == "split":
        return '''
<section class="sec about" id="lore">
  <div class="wrap split">
    <figure class="frame rv-l"><img class="gchar" data-tilt src="{{LOGO}}" alt="{{NAME}}" width="800" height="800"></figure>
    <div class="rv-r">
      <p class="kicker">Lore</p>
      <h2>The story of <em>{{NAME}}</em></h2>
      <p class="prose">{{ABOUT}}</p>
      <p class="prose">{{CTA}} Born on {{CHAIN_NAME}}, traded on {{DEX}}, carried by whoever decides to make the next meme.</p>
      <ul class="facts"><li><b>{{SUPPLY_SHORT}}</b><span>Supply</span></li><li><b>{{TAX}}</b><span>Tax</span></li><li><b>{{LP}}</b><span>LP</span></li></ul>
    </div>
  </div>
</section>'''
    if mode == "quote":
        return '''
<section class="sec about about-quote" id="lore">
  <div class="wrap">
    <p class="kicker">Lore</p>
    <blockquote class="rv">“{{TAGLINE}}”</blockquote>
    <div class="cols">
      <p class="prose">{{ABOUT}}</p>
      <p class="prose">{{CTA}} There is no team allocation hiding in a footnote. The chart is public, the contract is <button type="button" data-copy><code class="ca-text">{{CA}}</code></button>, and the only roadmap that matters is whether people keep posting.</p>
    </div>
  </div>
</section>'''
    if mode == "beats":
        return '''
<section class="sec about" id="lore">
  <div class="wrap">
    <p class="kicker">Lore</p>
    <h2>{{NAME}} in three beats</h2>
    <div class="beats rv-stagger">
      <article><strong>01</strong><h3>A name</h3><p>{{TAGLINE}}</p></article>
      <article><strong>02</strong><h3>A chain</h3><p>{{ABOUT}}</p></article>
      <article><strong>03</strong><h3>A crowd</h3><p>{{CTA}}</p></article>
    </div>
  </div>
</section>'''
    return '''
<section class="sec about about-overlap" id="lore">
  <div class="wrap stage">
    <div class="rv">
      <p class="kicker">Lore</p>
      <h2><em>{{NAME}}</em> showed up and stayed.</h2>
      <p class="prose">{{ABOUT}}</p>
      <p class="prose">{{TAGLINE}} {{CTA}}</p>
    </div>
    <img class="gchar m-float" data-parallax="0.08" data-mouse="14" src="{{LOGO}}" alt="{{NAME}}" width="800" height="800">
  </div>
</section>'''

def tokenomics(mode):
    cells = '''
<article><b>{{SUPPLY_SHORT}}</b><span>Supply</span><small>{{SUPPLY}} tokens. That is the whole pile.</small></article>
<article><b>{{TAX}}</b><span>Tax</span><small>Buy / sell tax printed in the open.</small></article>
<article><b>{{LP_SHORT}}</b><span>Liquidity</span><small>LP status: {{LP}}.</small></article>
<article><b>{{CHAIN_NAME}}</b><span>Chain</span><small>Swap it on {{DEX}} with {{WALLET}}.</small></article>
'''
    stat = '<p class="statline rv"><b data-count="100" data-suf="%">0%</b> crowd-owned joke. Supply {{SUPPLY_SHORT}}.</p>'
    if mode == "bars":
        return f'''
<section class="sec tok tok-bars" id="token">
  <div class="wrap">
    <p class="kicker">Tokenomics</p>
    <h2>The whole balance sheet</h2>
    <div class="bars rv-stagger">{cells}</div>
    {stat}
    <div class="market" data-dexs-live data-chain="{{{{CHAIN}}}}">
      <div><span>Price</span><b data-price>{{{{PRICE}}}}</b></div>
      <div><span>Mcap</span><b data-mcap>{{{{MCAP}}}}</b></div>
      <div><span>Volume</span><b data-vol>{{{{VOL}}}}</b></div>
      <div><span>Liq</span><b data-liq>{{{{LIQ}}}}</b></div>
    </div>
  </div>
</section>'''
    if mode == "tickets":
        return f'''
<section class="sec tok tok-tickets" id="token">
  <div class="wrap">
    <p class="kicker">Tokenomics</p>
    <h2>Four tickets. No fine print.</h2>
    <div class="tickets rv-stagger">{cells}</div>
    {stat}
  </div>
</section>'''
    if mode == "donut":
        return f'''
<section class="sec tok tok-donut" id="token">
  <div class="wrap donut-wrap">
    <div class="donut rv-z" aria-hidden="true"><i></i><b>${{{{TICKER}}}}</b></div>
    <div>
      <p class="kicker">Tokenomics</p>
      <h2>What you are actually buying</h2>
      <div class="bars">{cells}</div>
      {stat}
    </div>
  </div>
</section>'''
    return f'''
<section class="sec tok" id="token">
  <div class="wrap">
    <p class="kicker">Tokenomics</p>
    <h2>${{{{TICKER}}}} by the numbers</h2>
    <div class="cards rv-stagger">{cells}</div>
    {stat}
  </div>
</section>'''

HOWTO = '''
<section class="sec how" id="buy">
  <div class="wrap">
    <p class="kicker">How to buy</p>
    <h2>Four steps on {{DEX}}</h2>
    <ol class="steps rv-stagger">
      <li class="step"><span class="n">01</span><h3>Get {{WALLET}}</h3><p>Install the wallet, write the seed down offline, and add the {{CHAIN_NAME}} network.</p></li>
      <li class="step"><span class="n">02</span><h3>Fund {{NATIVE}}</h3><p>Buy or bridge a little {{NATIVE}} so you can pay for the swap and the fee.</p></li>
      <li class="step"><span class="n">03</span><h3>Paste the CA</h3><p>Open {{DEX}}, paste <button type="button" data-copy><code>{{CA_SHORT}}</code></button>, and check the name is {{NAME}}.</p></li>
      <li class="step"><span class="n">04</span><h3>Swap ${{TICKER}}</h3><p>Set slippage you can live with, confirm in {{WALLET}}, then go make a meme.</p></li>
    </ol>
    <div class="chartbox rv">
      <div class="chart"><iframe title="{{NAME}} chart" src="{{CHART_URL}}" loading="lazy"></iframe></div>
    </div>
  </div>
</section>
'''

def roadmap(mode):
    items = '''
<li><span>01</span><h3>Launch</h3><p>The site, the socials, and the first people who held ${{TICKER}} without being asked twice.</p></li>
<li><span>02</span><h3>Culture</h3><p>Meme contests, sticker dumps, and a timeline that looks like {{NAME}} lives there.</p></li>
<li><span>03</span><h3>Listings</h3><p>Trackers, a louder chart on {{DEX}}, and whoever wants the ticker in public.</p></li>
<li><span>04</span><h3>The long game</h3><p>Merch, meetups, and ideas the community actually bothers to finish.</p></li>
'''
    if mode == "stations":
        return f'<section class="sec road road-stations" id="road"><div class="wrap"><p class="kicker">Roadmap</p><h2>Stations, not promises</h2><ol class="stations rv-stagger">{items}</ol></div></section>'
    if mode == "chapters":
        return f'<section class="sec road road-chapters" id="road"><div class="wrap"><p class="kicker">Roadmap</p><h2>Chapters of ${{{{TICKER}}}}</h2><ol class="chapters rv-stagger">{items}</ol></div></section>'
    return f'<section class="sec road" id="road"><div class="wrap"><p class="kicker">Roadmap</p><h2>Four phases</h2><ol class="stack rv-stagger">{items}</ol></div></section>'

def gallery(mode):
    figs = "\n".join(
        f'<figure class="rv"><img class="gimg" src="{{{{LOGO}}}}" alt="{{{{NAME}}}} meme {i}" width="800" height="800" loading="lazy"><figcaption>0{i}</figcaption></figure>'
        for i in range(1, 9)
    )
    if mode == "rail":
        return f'''
<section class="sec gal gal-rail" id="memes">
  <div class="wrap"><p class="kicker">Memes</p><h2>Made for the timeline</h2></div>
  <div class="meme-rail"><div class="rail-track">{figs}</div></div>
</section>'''
    if mode == "polaroid":
        return f'''
<section class="sec gal gal-polaroid" id="memes">
  <div class="wrap">
    <p class="kicker">Memes</p><h2>A wall of {{NAME}}</h2>
    <div class="polaroids rv-stagger">{figs}</div>
  </div>
</section>'''
    return f'''
<section class="sec gal" id="memes">
  <div class="wrap">
    <p class="kicker">Memes</p><h2>The gallery</h2>
    <div class="mosaic rv-stagger">{figs}</div>
  </div>
</section>'''

FAQ = '''
<section class="sec faq" id="faq">
  <div class="wrap faq-grid">
    <header><p class="kicker">FAQ</p><h2>Ask, then ape or don't.</h2><p class="prose">{{CTA}}</p></header>
    <div data-acc>
      <div class="acc open"><button class="acc-q" type="button" aria-expanded="true">What is {{NAME}}?</button><div class="acc-a"><p>{{ABOUT}}</p></div></div>
      <div class="acc"><button class="acc-q" type="button" aria-expanded="false">Where is the contract?</button><div class="acc-a"><p class="ca-text">{{CA}}</p><p>Chain: {{CHAIN_NAME}}. DEX: {{DEX}}.</p></div></div>
      <div class="acc"><button class="acc-q" type="button" aria-expanded="false">How do I buy?</button><div class="acc-a"><p>Install {{WALLET}}, get {{NATIVE}}, open {{DEX}}, paste the CA, swap for ${{TICKER}}.</p></div></div>
      <div class="acc"><button class="acc-q" type="button" aria-expanded="false">Tax, supply, liquidity?</button><div class="acc-a"><p>Tax {{TAX}}. Supply {{SUPPLY}}. LP {{LP}}.</p></div></div>
      <div class="acc"><button class="acc-q" type="button" aria-expanded="false">Is this financial advice?</button><div class="acc-a"><p>${{TICKER}} is a meme coin with no intrinsic value or expectation of financial return. Not financial advice.</p></div></div>
    </div>
  </div>
</section>
'''

def cta(mode):
    if mode == "split":
        return '''
<section class="sec cta cta-split" id="join">
  <div class="wrap split">
    <div>
      <p class="kicker">Join</p>
      <h2>Come for the ticker. Stay for the bit.</h2>
      <p class="prose">{{CTA}}</p>
      <div class="hero-actions">
        <a class="btn btn-main btn-shine btn-pulse" data-magnetic data-buy href="{{BUY_URL}}">[[BUY]] Buy ${{TICKER}}</a>
        <a class="btn btn-ghost" data-s href="{{X_URL}}">[[X]] X</a>
        <a class="btn btn-ghost" data-s href="{{TG_URL}}">[[TG]] Telegram</a>
      </div>
    </div>
    <img class="gchar m-bob" data-tilt data-mouse="16" src="{{LOGO}}" alt="" width="640" height="640">
  </div>
</section>'''
    if mode == "ticket":
        return '''
<section class="sec cta cta-ticket" id="join">
  <div class="wrap ticket rv-z">
    <div>
      <p class="kicker">Admit one</p>
      <h2>${{TICKER}}</h2>
      <p>{{TAGLINE}}</p>
    </div>
    <div class="hero-actions">
      <a class="btn btn-main btn-shine" data-magnetic data-buy href="{{BUY_URL}}">[[BUY]] Buy ${{TICKER}}</a>
      <a class="btn btn-ghost" data-s href="{{TG_URL}}">[[TG]] Telegram</a>
      <a class="btn btn-ghost" data-s href="{{X_URL}}">[[X]] X</a>
    </div>
  </div>
</section>'''
    return '''
<section class="sec cta cta-band m-grad" id="join">
  <div class="wrap">
    <p class="kicker">Community</p>
    <h2 data-wave>{{NAME}}</h2>
    <p class="prose">{{CTA}}</p>
    <div class="hero-actions">
      <a class="btn btn-main btn-shine btn-pulse" data-magnetic data-buy href="{{BUY_URL}}">[[BUY]] Buy ${{TICKER}}</a>
      <a class="btn btn-ghost" data-s href="{{X_URL}}">[[X]] Follow</a>
      <a class="btn btn-ghost" data-s href="{{TG_URL}}">[[TG]] Chat</a>
      <a class="btn btn-ghost" href="{{DEXS_URL}}">[[DEX]] Chart</a>
    </div>
  </div>
</section>'''

FOOT = '''
<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <a class="brand" href="#top"><img src="{{LOGO}}" alt="" width="64" height="64"><b>{{NAME}}</b></a>
      <p>{{TAGLINE}}</p>
    </div>
    <div><b>Explore</b><a href="#lore">Lore</a><a href="#token">Tokenomics</a><a href="#buy">How to buy</a><a href="#memes">Memes</a><a href="#faq">FAQ</a></div>
    <div><b>Trade</b><a href="{{BUY_URL}}">{{DEX}}</a><a href="{{DEXS_URL}}">Dexscreener</a><button type="button" data-copy>Copy CA</button></div>
    <div><b>Community</b><a data-s href="{{X_URL}}">X</a><a data-s href="{{TG_URL}}">Telegram</a>{{EXTRA_SOCIALS}}</div>
  </div>
  <div class="wrap legal"><p>${{TICKER}} is a meme coin with no intrinsic value or expectation of financial return. Not financial advice. Art on this page is the token logo, banner, and uploaded memes.</p><p>© <span data-year>2026</span> ${{TICKER}}</p></div>
</footer>
'''

def _li(points):
    out=[]
    for i,(h,p) in enumerate(points):
        out.append('<li><b>%02d</b><div><h3>%s</h3><p>%s</p></div></li>'%(i+1,h,p))
    return ''.join(out)

def signature(kind, kicker, title, text, points):
    lis=_li(points)
    if kind=='principles':
        return '<section class="sec sig sig-pr"><div class="wrap"><p class="kicker">%s</p><h2>%s</h2><p class="prose">%s</p><ol class="sig-ol rv-stagger">%s</ol></div></section>'%(kicker,title,text,lis)
    if kind=='manifesto':
        return '<section class="sec sig sig-man"><div class="wrap man"><div><p class="kicker">%s</p><h2>%s</h2></div><div><p class="prose">%s</p><ol class="rv-stagger">%s</ol></div></div></section>'%(kicker,title,text,lis)
    if kind=='meter':
        bars=''.join('<div class="meter"><span>%s</span><i style="--w:%d%%"><b data-count="%d" data-suf="%%"></b></i><small>%s</small></div>'%(h,70+i*8,70+i*8,p) for i,(h,p) in enumerate(points))
        return '<section class="sec sig sig-meter"><div class="wrap"><p class="kicker">%s</p><h2>%s</h2><p class="prose">%s</p><div class="meters rv">%s</div></div></section>'%(kicker,title,text,bars)
    return '<section class="sec sig sig-slab"><div class="wrap slab"><p class="kicker">%s</p><h2>%s</h2><p>%s</p><ol>%s</ol></div></section>'%(kicker,title,text,lis)

SECTION_CSS = r'''
.top{position:sticky;top:0;z-index:40;display:flex;align-items:center;gap:18px;padding:12px 22px;background:color-mix(in srgb,var(--bg) 86%,transparent);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;font-family:var(--display);font-weight:700}
.brand img{width:40px;height:40px;border-radius:12px;object-fit:cover;background:var(--card);border:2px solid var(--line)}
.brand em{font-style:normal;color:var(--a);font-size:.85rem}
.navlinks{display:flex;gap:16px;margin-left:auto;font-size:.82rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.top-actions{display:flex;align-items:center;gap:8px}
.top-actions a[data-s]{width:40px;height:40px;display:grid;place-items:center;border-radius:999px;border:1px solid var(--line)}
.burger{display:none;width:44px;height:44px;border-radius:12px;border:1px solid var(--line);place-items:center;gap:4px}
.burger i{display:block;width:16px;height:2px;background:currentColor}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 16px;border-radius:var(--radius);border:var(--border);font-weight:800;background:transparent;color:inherit;white-space:nowrap}
.btn-main{background:var(--a);color:var(--on);border-color:transparent}
.btn-ghost{background:var(--card)}
.hero-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.kicker{color:var(--a);font-weight:800;letter-spacing:.16em;text-transform:uppercase;font-size:.72rem;margin:0 0 8px}
h2{font-size:clamp(2rem,4.6vw,3.8rem);margin:0 0 12px}
h2 em{font-style:normal;color:var(--a)}
.prose{color:var(--muted);max-width:62ch}
.sec{padding:clamp(64px,8vw,110px) 0;position:relative}
.wrap{width:min(1120px,calc(100% - 40px));margin-inline:auto}
.mq{background:var(--a);color:var(--on);font-family:var(--display);font-weight:700;padding:12px 0;font-size:1.05rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:42px;align-items:center}
.frame{background:var(--card);border:var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px}
.frame img,.gchar{width:100%;height:auto;object-fit:contain}
.facts{display:flex;gap:18px;list-style:none;padding:0;margin:18px 0 0}
.facts b{display:block;font-family:var(--display);font-size:1.6rem}
.facts span,.cards span,.bars span,.tickets span{color:var(--muted);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
blockquote{font-family:var(--display);font-size:clamp(2rem,5vw,4rem);line-height:1.02;margin:0 0 18px}
.cols,.beats,.cards,.tickets,.steps,.stack,.stations,.chapters,.mosaic,.polaroids{display:grid;gap:14px}
.cols{grid-template-columns:1fr 1fr}
.beats{grid-template-columns:repeat(3,1fr);margin-top:22px}
.beats article,.cards article,.tickets article,.steps li,.stack li,.chapters li{background:var(--card);border:var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:18px}
.beats strong,.step .n,.stack span,.chapters span,.stations span{font-family:var(--display);font-size:2rem;color:var(--a)}
.cards,.tickets{grid-template-columns:repeat(4,1fr)}
.cards b,.tickets b,.bars b{font-family:var(--display);font-size:clamp(1.6rem,3vw,2.4rem);display:block}
.tok-bars .bars{display:grid;gap:10px}
.tok-bars article{display:grid;grid-template-columns:160px 1fr;gap:8px 18px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line);background:transparent;box-shadow:none;border-radius:0}
.tok-bars article small{grid-column:2}
.tickets article{border-style:dashed;position:relative}
.tickets article:before,.tickets article:after{content:"";position:absolute;width:18px;height:18px;background:var(--bg);border-radius:50%;top:50%;margin-top:-9px}
.tickets article:before{left:-9px}.tickets article:after{right:-9px}
.donut-wrap{display:grid;grid-template-columns:280px 1fr;gap:36px;align-items:center}
.donut{width:240px;height:240px;border-radius:50%;background:conic-gradient(var(--a) 0 70%, var(--a2) 0 88%, var(--card) 0 100%);display:grid;place-items:center;position:relative}
.donut i{position:absolute;inset:28px;background:var(--bg);border-radius:50%}
.donut b{position:relative;font-family:var(--display)}
.steps{grid-template-columns:repeat(4,1fr);list-style:none;padding:0}
.steps p,.stack p,.chapters p,.stations p{color:var(--muted);margin:.3rem 0 0}
.chartbox{margin-top:28px;border:var(--border);border-radius:var(--radius);overflow:hidden;background:var(--bg-2);box-shadow:var(--shadow)}
.stack{grid-template-columns:repeat(4,1fr);list-style:none;padding:0}
.stations{grid-auto-flow:column;grid-auto-columns:minmax(220px,1fr);overflow:auto;list-style:none;padding:18px 0 8px;scroll-snap-type:x mandatory}
.stations li{scroll-snap-align:start;min-height:180px;background:var(--card);border:var(--border);border-radius:var(--radius);padding:16px;position:relative}
.stations li:not(:last-child):after{content:"";position:absolute;right:-14px;top:28px;width:14px;height:3px;background:var(--a)}
.chapters{list-style:none;padding:0;gap:0}
.chapters li{display:grid;grid-template-columns:90px 1fr;gap:12px;border-radius:0;border-left:3px solid var(--a);box-shadow:none}
.mosaic{grid-template-columns:2fr 1fr 1fr;grid-auto-rows:180px}
.mosaic figure:first-child{grid-row:span 2}
.mosaic figure,.polaroids figure,.gal-rail figure{margin:0;background:var(--card);border:var(--border);border-radius:var(--radius);overflow:hidden;position:relative}
.mosaic img,.polaroids img,.gal-rail img{width:100%;height:100%;object-fit:cover;background:
  radial-gradient(circle at 30% 30%, color-mix(in srgb,var(--a) 55%,#fff), transparent 55%),
  var(--card)}
.mosaic figcaption,.polaroids figcaption{position:absolute;left:8px;bottom:8px;background:var(--bg);padding:2px 6px;font-size:.72rem;border-radius:999px}
.polaroids{grid-template-columns:repeat(4,1fr)}
.polaroids figure{padding:10px 10px 28px;background:var(--surface);color:var(--ink);transform:rotate(var(--rot,-2deg));box-shadow:var(--shadow)}
.polaroids figure:nth-child(2n){transform:rotate(2.5deg)}
.polaroids figure:nth-child(3n){transform:rotate(-3deg)}
.gal-rail .meme-rail{padding:10px 0 20px}
.gal-rail figure{width:260px;height:260px}
.faq-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:32px}
.acc{border-bottom:1px solid var(--line)}
.acc-q{width:100%;text-align:left;padding:16px 0;font-weight:800;font-size:1.05rem;display:flex;justify-content:space-between}
.acc-q:after{content:"+";color:var(--a);font-size:1.3rem}
.acc.open .acc-q:after{content:"–"}
.acc-a p{margin:0 0 14px;color:var(--muted)}
.cta-band{background:var(--grad);color:var(--on)}
.statline{font-family:var(--display);font-size:clamp(1.4rem,3vw,2rem);margin:18px 0 0}
.statline b{color:var(--a)}
.cta-band .kicker,.cta-band h2,.cta-band .prose{color:inherit}
.cta-band .btn-ghost{background:transparent;color:inherit;border-color:currentColor}
.cta-ticket .ticket{display:flex;justify-content:space-between;gap:20px;align-items:center;border:var(--border);border-radius:var(--radius);padding:28px;background:var(--card);box-shadow:var(--shadow);background-image:radial-gradient(circle at left, transparent 12px, var(--card) 13px)}
.market{display:flex;flex-wrap:wrap;gap:18px;margin-top:22px;padding:14px 16px;border:1px solid var(--line);border-radius:var(--radius);background:var(--card)}
.market span{display:block;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.sig-ol,.sig-man ol,.sig-slab ol{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:12px}
.sig-pr .sig-ol{grid-template-columns:repeat(3,1fr)}
.sig-ol li,.sig-man li,.sig-slab li{display:flex;gap:12px;align-items:flex-start}
.sig-slab{background:var(--ink);color:var(--bg)}
.sig-slab .kicker,.sig-slab h2,.sig-slab p,.sig-slab li{color:inherit}
.meters{display:grid;gap:14px;margin-top:16px}
.meter i{display:block;height:14px;border-radius:99px;background:var(--line);position:relative;margin:6px 0}
.meter i:after{content:"";position:absolute;inset:0 auto 0 0;width:var(--w);background:var(--a);border-radius:inherit}
.foot{padding:48px 0 28px;border-top:1px solid var(--line);color:var(--muted);font-size:.92rem}
.foot-grid{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:18px}
.foot a,.foot button{display:block;padding:4px 0;color:inherit;background:none;border:0;text-align:left}
.legal{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap;margin-top:22px;font-size:.8rem}
.about-overlap .stage{display:grid;grid-template-columns:1.1fr .9fr;align-items:end}
.about-overlap img{max-width:420px;margin-left:auto;filter:drop-shadow(0 24px 30px rgba(0,0,0,.25))}
@media(max-width:900px){
  .navlinks{display:none;position:absolute;left:12px;right:12px;top:70px;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px}
  body.menu-open .navlinks{display:flex}
  .burger{display:grid}
  .split,.cols,.beats,.cards,.tickets,.steps,.stack,.faq-grid,.donut-wrap,.foot-grid,.about-overlap .stage,.sig-pr .sig-ol,.cta-ticket .ticket{grid-template-columns:1fr}
  .tok-bars article{grid-template-columns:1fr}
  .mosaic{grid-template-columns:1fr 1fr;grid-auto-rows:160px}
  .polaroids{grid-template-columns:1fr 1fr}
  .cards,.tickets,.steps,.stack{grid-template-columns:1fr 1fr}
}
@media(max-width:560px){.cards,.tickets,.steps,.stack,.mosaic,.polaroids{grid-template-columns:1fr}}
'''
