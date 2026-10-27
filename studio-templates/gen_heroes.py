"""Twenty-seven hero scenes. Each composition is unique.
Logos are cutouts (no sticker frame) except the two stamp heroes.
Colors are semantic tokens so presets recolor the scene."""
from gen_sections import ACTIONS, scene

def cut(cls):
    return '<img class="gchar %s" data-tilt src="{{LOGO}}" alt="" width="800" height="800">' % cls

HERO = cut("hero-main")
SMALL = cut("floater")
TINY = cut("floater tiny")

RESET = r'''
.hero{position:relative;isolation:isolate;overflow:hidden;min-height:100svh;background:var(--bg);color:var(--ink)}
.hero .gchar{background:transparent!important;border:0!important;box-shadow:none!important;border-radius:0!important;padding:0!important;width:100%;height:auto;object-fit:contain;filter:drop-shadow(0 22px 16px color-mix(in srgb,#000 45%,transparent))}
.hero .scene{position:absolute;inset:-12% -4% auto -4%;width:108%;height:130%;z-index:0;pointer-events:none}
.hero .grain{position:absolute;inset:0;z-index:5;pointer-events:none;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)' opacity='.55'/%3E%3C/svg%3E")}
.hero .hero-mq{position:absolute;left:0;right:0;bottom:0;z-index:6}
.hero .bubble{position:absolute;z-index:4;background:var(--surface);color:var(--ink);border:3px solid var(--ink);border-radius:18px 18px 18px 4px;padding:8px 12px;font-family:var(--display);font-weight:800;box-shadow:4px 4px 0 var(--a)}
.hero .floater{position:absolute;z-index:3;width:min(120px,18vw);pointer-events:none}
.hero .floater.tiny{width:min(72px,12vw)}
.hero .hero-copy{position:relative;z-index:4}
.hero h1{position:relative;z-index:4;margin:0;line-height:.86;letter-spacing:-.04em}
.hero .lede{color:var(--muted);max-width:42ch;position:relative;z-index:4}
.hero .kicker,.hero .hero-actions{position:relative;z-index:4}
.hero .props{position:absolute;inset:0;z-index:1;pointer-events:none}
.hero .props svg{width:100%;height:100%;display:block}
@media(min-width:801px){.hero{height:100svh}}
@media(max-width:800px){
  .hero{height:auto;min-height:auto;padding:92px 16px 72px}
  .hero .hero-main,.hero .floater{position:relative!important;left:auto!important;right:auto!important;top:auto!important;bottom:auto!important;width:min(240px,64vw)!important;margin:8px auto;transform:none!important}
  .hero h1{font-size:clamp(2.6rem,12vw,4.2rem)!important}
}
'''

MQ = '<div class="mq hero-mq" style="--mq-speed:20s"><div class="mq-track"><span>${{TICKER}} ✦ {{NAME}} ✦ {{TAGLINE}} ✦ {{CHAIN_NAME}} ✦ {{DEX}} ✦ </span></div></div>'
GRAIN = '<div class="grain" aria-hidden="true"></div>'

HEROES = {}

def add(name, css, html):
    HEROES[name] = (css, html)

# 1 poster — mascot stands on the wordmark
add("poster", '''
.hero{display:block}
.hero h1{position:absolute;z-index:4;left:4vw;right:6vw;bottom:96px;font-size:clamp(3rem,7.2vw,5.6rem);text-transform:uppercase;line-height:.78}
.hero .stand{position:absolute;z-index:3;left:62%;bottom:24%;width:min(400px,42vw);transform:translateX(-50%)}
.hero .floater.a{left:6%;top:16%}.hero .floater.b{right:8%;top:22%;width:min(90px,14vw)}
.hero .bubble{left:14%;top:22%}
.hero .hero-copy{position:absolute;z-index:5;left:5vw;top:16vh;max-width:360px}
''', '''
<section class="hero"><div class="props" data-parallax="-0.12">@@SCENE@@</div>
'''+GRAIN+SMALL.replace('floater','floater a m-float')+TINY.replace('floater tiny','floater tiny b m-bob')+'''
<div class="bubble m-bob">${{TICKER}}</div>
<div class="stand m-bob" data-mouse="16">'''+HERO+'''</div>
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}} · {{DEX}}</p><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<h1 data-letters>{{NAME}}</h1>'''+MQ+'''</section>''')

# 2 splitR — climbs a torn edge
add("splitR", '''
.hero{display:grid;grid-template-columns:1fr .9fr;align-items:center;padding:80px 4vw 70px}
.hero h1{font-size:clamp(3.2rem,6vw,6.4rem)}
.hero .tear{position:absolute;z-index:2;right:34%;top:0;bottom:0;width:80px}
.hero .climb{position:absolute;z-index:3;right:6%;bottom:8%;width:min(520px,46vw);transform:rotate(-8deg)}
.hero .floater{left:8%;bottom:18%}
.hero .bubble{right:18%;top:18%}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .climb{position:relative;right:auto;width:min(300px,70vw);transform:none}}
''', '''
<section class="hero"><div data-parallax="-0.08">@@SCENE@@</div>
<svg class="tear" viewBox="0 0 80 900" aria-hidden="true"><path class="a" d="M40 0c18 40-10 70 8 110s-20 80 4 120-16 90 6 130 8 100-8 140 20 90-4 140-22 80 6 130 4 70-10 130v40H0V0z" fill="var(--a)" opacity=".9"/></svg>
'''+GRAIN+'''<div class="bubble m-bob">hold</div>
<div class="climb" data-mouse="18">'''+HERO+'''</div>
'''+SMALL.replace('floater','floater m-float')+'''
<div class="hero-copy"><p class="kicker">{{DEX}} on {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 3 center — giant bust under giant type (no frame)
add("center", '''
.hero{display:block;text-align:center}
.hero h1{font-size:clamp(3.6rem,9vw,7.2rem);text-transform:uppercase}
.hero .hero-copy{position:absolute;left:0;right:0;top:12vh;z-index:5}
.hero .bust{position:absolute;z-index:3;left:50%;bottom:-2vh;width:min(560px,68vw);transform:translateX(-50%)}
.hero .floater.a{left:8%;top:22%}.hero .floater.b{right:10%;top:30%}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div data-parallax="-0.06">@@SCENE@@</div>'''+GRAIN+'''
'''+SMALL.replace('floater','floater a m-float')+TINY.replace('floater tiny','floater tiny b m-bob')+'''
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="bust m-bob" data-mouse="12">'''+HERO+'''</div>'''+MQ+'''</section>''')

# 4 scatter — peeking from the corner, type tilted
add("scatter", '''
.hero{padding:110px 6vw 70px}
.hero h1{font-size:clamp(4rem,12vw,9rem);transform:rotate(-3deg);display:inline-block}
.hero .peek{position:absolute;z-index:3;left:-4%;bottom:-6%;width:min(480px,52vw);transform:rotate(-8deg)}
.hero .floater{right:10%;top:18%;transform:rotate(12deg)}
.hero .bubble{right:22%;top:34%}
.hero .hero-copy{position:relative;z-index:4;max-width:680px;margin-left:auto}
''', '''
<section class="hero"><div data-parallax="0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="peek" data-mouse="20">'''+HERO+'''</div>
'''+SMALL.replace('floater','floater m-spin')+'''
<div class="bubble m-bob">say it</div>
<div class="hero-copy"><p class="kicker">Out loud</p><h1 data-wave>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 5 app — mascot breaks out of a phone
add("app", '''
.hero{display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:90px 5vw 70px}
.hero h1{font-size:clamp(3rem,5.5vw,5.2rem)}
.hero .rig{position:relative;z-index:3;height:min(640px,78vh)}
.hero .phone{position:absolute;right:8%;top:8%;width:min(260px,28vw);height:72%;border:3px solid var(--ink);border-radius:36px;background:color-mix(in srgb,var(--surface) 70%,transparent);box-shadow:12px 16px 0 var(--a)}
.hero .breakout{position:absolute;left:0;bottom:0;width:min(420px,40vw);z-index:2}
.hero .card{position:absolute;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px 14px;font-weight:800;box-shadow:var(--shadow)}
.hero .card.c1{left:0;top:10%}.hero .card.c2{right:0;bottom:18%}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .rig{height:420px}}
''', '''
<section class="hero"><div data-parallax="-0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}} social coin</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="rig">
  <div class="card c1 m-float">${{TICKER}}</div>
  <div class="card c2 m-bob">{{CHAIN_NAME}}</div>
  <div class="phone" aria-hidden="true"></div>
  <div class="breakout" data-mouse="14">'''+HERO+'''</div>
</div>'''+MQ+'''</section>''')

# 6 cinema — stands on the horizon
add("cinema", '''
.hero{display:block}
.hero:before,.hero:after{content:"";position:absolute;left:0;right:0;height:36px;background:#000;z-index:7}
.hero:before{top:0}.hero:after{bottom:46px}
.hero .ground{position:absolute;z-index:2;left:0;right:0;bottom:12%;height:28%;background:linear-gradient(180deg,transparent,color-mix(in srgb,var(--a) 35%,var(--bg)))}
.hero .actor{position:absolute;z-index:3;right:4%;bottom:14%;width:min(480px,42vw)}
.hero .extra{position:absolute;z-index:2;left:18%;bottom:20%;width:min(140px,16vw);opacity:.85}
.hero .hero-copy{position:absolute;z-index:4;left:5vw;bottom:22%;width:min(520px,46vw);background:color-mix(in srgb,var(--bg) 62%,transparent);padding:16px 18px;border-left:4px solid var(--a)}
.hero h1{font-size:clamp(3rem,6vw,5.6rem)}
''', '''
<section class="hero"><div data-parallax="-0.1">@@SCENE@@</div><div class="ground"></div>'''+GRAIN+'''
<div class="extra m-bob" data-parallax="0.04">'''+SMALL+'''</div>
<div class="actor" data-mouse="16">'''+HERO+'''</div>
<div class="hero-copy"><p class="kicker">${{TICKER}} · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 7 splitL — full-bleed field, bust fills the right
add("splitL", '''
.hero{display:grid;grid-template-columns:.9fr 1.1fr;align-items:end}
.hero h1{font-size:clamp(4rem,8vw,8rem);text-transform:uppercase}
.hero .hero-copy{position:relative;z-index:4;padding:12vh 4vw 12vh 6vw;align-self:center}
.hero .bust{position:relative;z-index:3;width:min(640px,52vw);margin-bottom:-4vh;justify-self:end}
.hero .floater{left:4%;bottom:16%}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .bust{width:min(360px,80vw);justify-self:center}}
''', '''
<section class="hero"><div data-parallax="-0.04">@@SCENE@@</div>'''+GRAIN+TINY.replace('floater tiny','floater tiny m-float')+'''
<div class="hero-copy"><p class="kicker">${{TICKER}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="bust m-bob" data-mouse="10">'''+HERO+'''</div>'''+MQ+'''</section>''')

# 8 sky — standing on a cloud, friends on higher clouds
add("sky", '''
.hero{text-align:center;padding-top:90px}
.hero h1{font-size:clamp(3.6rem,10vw,8rem);text-shadow:4px 4px 0 var(--a)}
.hero .cloud{position:absolute;z-index:2;border-radius:50%;background:var(--surface);filter:blur(.2px)}
.hero .cloud.c1{left:8%;top:22%;width:180px;height:70px}
.hero .cloud.c2{right:10%;top:30%;width:220px;height:80px}
.hero .cloud.c3{left:50%;bottom:16%;width:min(520px,70vw);height:90px;transform:translateX(-50%);background:color-mix(in srgb,var(--surface) 80%,var(--a))}
.hero .rider{position:absolute;z-index:3;left:50%;bottom:18%;width:min(380px,54vw);transform:translateX(-50%)}
.hero .pal{position:absolute;z-index:3;width:min(110px,16vw)}
.hero .pal.p1{left:12%;top:14%}.hero .pal.p2{right:12%;top:20%}
.hero .lede{color:var(--ink)}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div data-parallax="-0.15">@@SCENE@@</div>'''+GRAIN+'''
<div class="cloud c1 m-float"></div><div class="cloud c2 m-bob"></div><div class="cloud c3"></div>
<div class="pal p1 m-float">'''+SMALL+'''</div>
<div class="pal p2 m-bob">'''+TINY+'''</div>
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="rider" data-mouse="12">'''+HERO+'''</div>
<div class="bubble" style="left:58%;bottom:42%">gm</div>
'''+MQ+'''</section>''')

# 9 orbit — copies ride the rings
add("orbit", '''
.hero{display:block;text-align:center}
.hero h1{font-size:clamp(2.6rem,5vw,4.2rem)}
.hero .system{position:absolute;z-index:3;left:50%;top:40%;width:min(520px,78vw);height:min(460px,54vh);transform:translate(-50%,-50%)}
.hero .hero-copy{position:absolute;left:0;right:0;bottom:62px;z-index:5}
.hero .core{position:absolute;left:50%;top:46%;width:42%;transform:translate(-50%,-50%)}
.hero .sat{position:absolute;width:18%}
.hero .sat.s1{left:6%;top:20%}.hero .sat.s2{right:4%;top:28%}.hero .sat.s3{left:40%;bottom:6%}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div class="m-spin" data-parallax="-0.05" style="position:absolute;inset:-10%">@@SCENE@@</div>'''+GRAIN+'''
<div class="system">
  <div class="sat s1 m-float">'''+TINY+'''</div>
  <div class="sat s2 m-bob">'''+TINY+'''</div>
  <div class="sat s3 m-float">'''+SMALL+'''</div>
  <div class="core m-bob" data-mouse="8">'''+HERO+'''</div>
</div>
<div class="hero-copy"><p class="kicker">Orbit · {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 10 question — sits on the question mark
add("question", '''
.hero{display:grid;align-items:center;padding:100px 6vw 70px}
.hero h1{font-size:clamp(2.8rem,6vw,5.4rem);max-width:16ch}
.hero .q{position:absolute;right:-2vw;bottom:-8vh;font-family:var(--display);font-size:62vh;line-height:.8;color:var(--a);z-index:1;opacity:.9}
.hero .sit{position:absolute;z-index:3;right:14%;bottom:10%;width:min(340px,36vw)}
.hero .bubble{right:28%;bottom:48%}
.hero .hero-copy{position:relative;z-index:4;max-width:640px}
''', '''
<section class="hero"><div data-parallax="-0.04">@@SCENE@@</div>'''+GRAIN+'''
<div class="q" aria-hidden="true" data-parallax="0.06">?</div>
<div class="bubble m-bob">you?</div>
<div class="sit m-bob" data-mouse="14">'''+HERO+'''</div>
<div class="hero-copy"><p class="kicker">A real question</p><h1>Are you holding ${{TICKER}}?</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 11 craft — on a rooftop in the grid
add("craft", '''
.hero{display:grid;align-items:end;padding:0}
.hero .skyline{position:absolute;z-index:2;left:0;right:0;bottom:48px;height:42%}
.hero .roof{position:absolute;z-index:3;right:8%;bottom:16%;width:min(380px,40vw)}
.hero .hero-copy{position:relative;z-index:4;margin:18vh 0 18vh 6vw;max-width:560px;background:color-mix(in srgb,var(--bg) 72%,transparent);border:1px solid var(--a);padding:22px}
.hero h1{font-size:clamp(3rem,6vw,5.4rem);text-transform:uppercase}
''', '''
<section class="hero"><div data-parallax="-0.08">@@SCENE@@</div>
<svg class="skyline" viewBox="0 0 1440 400" preserveAspectRatio="none" aria-hidden="true">
  <g fill="var(--bg-2)"><rect x="40" y="120" width="160" height="280"/><rect x="220" y="40" width="120" height="360"/><rect x="360" y="160" width="200" height="240"/><rect x="900" y="80" width="140" height="320"/><rect x="1060" y="150" width="180" height="250"/><rect x="1260" y="60" width="140" height="340"/></g>
  <g fill="var(--a)" opacity=".8"><rect x="70" y="150" width="18" height="22"/><rect x="110" y="150" width="18" height="22"/><rect x="250" y="80" width="16" height="20"/><rect x="940" y="120" width="16" height="18"/><rect x="1100" y="190" width="18" height="20"/></g>
</svg>'''+GRAIN+'''
<div class="roof" data-mouse="12">'''+HERO+'''</div>
<div class="bubble" style="right:22%;bottom:52%">build</div>
<div class="hero-copy"><p class="kicker">Build log · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 12 index — mascot is the full-bleed crop, type is the essay
add("index", '''
.hero{display:block}
.hero .bleed{position:absolute;z-index:1;right:-6%;top:0;width:min(720px,58vw);height:120%;object-fit:cover}
.hero .idx{position:absolute;z-index:4;left:4vw;top:18vh;font-family:var(--display);font-size:clamp(4rem,10vw,8rem);line-height:.8;color:var(--a)}
.hero .hero-copy{position:absolute;z-index:4;left:4vw;bottom:12vh;max-width:520px;background:color-mix(in srgb,var(--bg) 78%,transparent);padding:16px}
.hero h1{font-size:clamp(2.6rem,5vw,4.4rem)}
''', '''
<section class="hero"><div data-parallax="-0.06">@@SCENE@@</div>
<div class="bleed" data-mouse="8" data-parallax="0.04">'''+HERO+'''</div>'''+GRAIN+'''
<div class="idx">01</div>
<div class="hero-copy"><p class="kicker">${{TICKER}}</p><h1>{{NAME}}</h1><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 13 roof — sits on the skyline under a neon sign
add("roof", '''
.hero{display:block}
.hero .sign{position:absolute;z-index:4;left:6vw;top:16vh;padding:8px 4px}
.hero h1{font-size:clamp(3rem,7vw,6rem);color:var(--a);text-shadow:0 0 18px var(--glow),0 0 2px var(--a)}
.hero .sitter{position:absolute;z-index:3;left:42%;bottom:12%;width:min(420px,46vw)}
.hero .chimney{position:absolute;z-index:3;left:12%;bottom:22%;width:min(100px,14vw)}
.hero .ledge{position:absolute;z-index:2;left:0;right:0;bottom:10%;height:14px;background:var(--ink)}
''', '''
<section class="hero"><div data-parallax="-0.1">@@SCENE@@</div>'''+GRAIN+'''
<div class="ledge"></div>
<div class="chimney m-bob">'''+TINY+'''</div>
<div class="sitter" data-mouse="14">'''+HERO+'''</div>
<div class="sign"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 14 product — spotlight stage, coins, not a frame
add("product", '''
.hero{display:grid;grid-template-columns:1.05fr .95fr;align-items:center;padding:90px 6vw 70px}
.hero h1{font-size:clamp(3rem,6vw,5.6rem)}
.hero .stage{position:relative;z-index:3;height:min(560px,70vh)}
.hero .spot{position:absolute;left:10%;right:10%;top:0;bottom:18%;background:radial-gradient(circle at 50% 30%, color-mix(in srgb,var(--a) 55%,transparent), transparent 68%)}
.hero .floor{position:absolute;left:8%;right:8%;bottom:8%;height:70px;border-radius:50%;background:color-mix(in srgb,var(--ink) 18%,transparent)}
.hero .star{position:absolute;left:18%;right:18%;bottom:14%;width:auto}
.hero .coin{position:absolute;width:54px;height:54px;border-radius:50%;background:radial-gradient(circle at 35% 35%, var(--a2), var(--a));border:3px solid var(--ink)}
.hero .coin.a{left:6%;bottom:20%}.hero .coin.b{right:8%;bottom:28%}
@media(max-width:860px){.hero{grid-template-columns:1fr}}
''', '''
<section class="hero"><div data-parallax="-0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">{{DEX}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="stage"><div class="spot"></div><div class="floor"></div>
<div class="coin a m-bob"></div><div class="coin b m-float"></div>
<div class="star m-bob" data-mouse="10">'''+HERO+'''</div></div>
'''+MQ+'''</section>''')

# 15 letterbox — walks through the frame, subtitle bar
add("letterbox", '''
.hero{display:block}
.hero .holes{position:absolute;z-index:6;top:0;bottom:52px;width:28px;background:radial-gradient(circle at 14px 18px,var(--bg) 7px,transparent 8px) 0 0/28px 36px}
.hero .holes.r{right:0}.hero .holes.l{left:0}
.hero .walker{position:absolute;z-index:3;left:50%;bottom:8%;width:min(520px,60vw);transform:translateX(-50%)}
.hero .sub{position:absolute;z-index:4;left:10%;right:10%;bottom:108px;text-align:center}
.hero .sub .lede{display:none}
.hero h1{font-size:clamp(2.6rem,5.5vw,4.6rem)}
''', '''
<section class="hero"><div data-parallax="-0.06">@@SCENE@@</div>'''+GRAIN+'''
<div class="holes l"></div><div class="holes r"></div>
<div class="walker m-bob" data-mouse="8">'''+HERO+'''</div>
<div class="sub"><p class="kicker">Chapter 01</p><h1>{{NAME}}</h1><p class="lede" style="margin-inline:auto">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 16 hud — crosshair, not a photo box
add("hud", '''
.hero{display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:90px 4vw 70px}
.hero h1{font-size:clamp(2.8rem,5vw,4.8rem);text-transform:uppercase}
.hero .lock{position:relative;z-index:3;width:min(460px,42vw);justify-self:center}
.hero .lock:before,.hero .lock:after{content:"";position:absolute;background:var(--a);z-index:4}
.hero .lock:before{left:50%;top:-6%;bottom:-6%;width:1px}
.hero .lock:after{top:50%;left:-6%;right:-6%;height:1px}
.hero .readouts{display:flex;gap:12px;margin:12px 0;font-family:ui-monospace,monospace}
.hero .readouts b{display:block;color:var(--a);font-size:1.2rem}
.hero .hero-copy{position:relative;z-index:4;border:1px solid var(--line);padding:20px;background:color-mix(in srgb,var(--bg) 70%,transparent)}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .lock{width:min(280px,70vw)}}
''', '''
<section class="hero"><div data-parallax="-0.04">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">SYS / {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>
<div class="readouts"><div><span>SUP</span><b>{{SUPPLY_SHORT}}</b></div><div><span>TAX</span><b>{{TAX}}</b></div><div><span>LP</span><b>{{LP_SHORT}}</b></div></div>
'''+ACTIONS+'''</div>
<div class="lock m-pulse" data-mouse="10">'''+HERO+'''</div>'''+MQ+'''</section>''')

# 17 ghost — a parade of sizes
add("ghost", '''
.hero{display:block;text-align:center}
.hero h1{font-size:clamp(2.8rem,6vw,5rem)}
.hero .parade{position:absolute;z-index:3;left:50%;top:16%;width:min(760px,92vw);height:min(380px,46vh);transform:translateX(-50%)}
.hero .hero-copy{position:absolute;left:0;right:0;bottom:58px;z-index:5}
.hero .parade .hero-main{position:absolute;left:30%;bottom:0;width:46%}
.hero .parade .floater{width:22%}
.hero .parade .f1{left:4%;bottom:10%}.hero .parade .f2{right:2%;bottom:18%;width:16%}
.hero .moon{position:absolute;z-index:1;right:12%;top:14%;width:min(180px,24vw);height:auto;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 35% 35%, var(--a2), var(--a))}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div data-parallax="-0.08">@@SCENE@@</div><div class="moon m-pulse"></div>'''+GRAIN+'''
<div class="parade">
  <div class="floater f1 m-float">'''+SMALL+'''</div>
  <div class="floater f2 m-bob">'''+TINY+'''</div>
  <div data-mouse="12">'''+HERO+'''</div>
</div>
<div class="bubble" style="left:18%;top:24%">boo</div>
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 18 magazine — masthead the mascot crashes through
add("magazine", '''
.hero{display:block;padding-top:0}
.hero .mast{position:relative;z-index:4;padding:88px 4vw 0;border-bottom:8px solid var(--a)}
.hero .mast b{display:block;font-family:var(--display);font-size:clamp(3.4rem,9vw,8rem);line-height:.8;letter-spacing:-.04em}
.hero .spine{position:absolute;z-index:4;left:0;top:0;bottom:48px;width:42px;writing-mode:vertical-rl;display:grid;place-items:center;background:var(--ink);color:var(--bg);letter-spacing:.2em;font-size:.8rem}
.hero .coverstar{position:absolute;z-index:3;right:4%;bottom:6%;width:min(520px,48vw)}
.hero .dek{position:relative;z-index:4;max-width:460px;margin:16px 0 0 64px}
''', '''
<section class="hero"><div data-parallax="-0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="spine">${{TICKER}}</div>
<div class="mast"><b>{{NAME}}</b></div>
<div class="coverstar" data-mouse="12">'''+HERO+'''</div>
<div class="dek"><p class="kicker">Cover</p><p class="lede">{{TAGLINE}}</p><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 19 seal — one of two framed moments: a stamp overlapping the cutout
add("seal", '''
.hero{display:grid;grid-template-columns:1.1fr .9fr;align-items:center;padding:80px 5vw 70px}
.hero h1{font-size:clamp(3rem,6vw,5.6rem)}
.hero .cast{position:relative;z-index:3;width:min(520px,46vw);justify-self:end}
.hero .stamp{position:absolute;right:-4%;top:-6%;width:42%;aspect-ratio:1;border-radius:50%;border:8px solid var(--a);display:grid;place-items:center;background:color-mix(in srgb,var(--a) 18%,var(--surface));transform:rotate(12deg)}
.hero .stamp img{position:relative;width:70%}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .cast{width:min(340px,80vw)}}
''', '''
<section class="hero"><div data-parallax="-0.04">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="cast"><div data-mouse="10">'''+HERO+'''</div><div class="stamp m-spin" style="animation-duration:28s">'''+TINY+'''</div></div>
'''+MQ+'''</section>''')

# 20 planet — stands on the curve
add("planet", '''
.hero{display:block;padding-top:90px}
.hero h1{font-size:clamp(3rem,7vw,6rem);text-transform:uppercase}
.hero .hero-copy{position:relative;z-index:4;width:min(640px,calc(100% - 40px));margin-left:6vw}
.hero .lander{position:absolute;z-index:3;left:50%;bottom:6%;width:min(380px,48vw);transform:translateX(-50%)}
.hero .flag{position:absolute;z-index:3;left:62%;bottom:28%;width:min(90px,12vw)}
''', '''
<section class="hero"><div data-parallax="-0.12">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">Mission · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="flag m-bob">'''+TINY+'''</div>
<div class="lander" data-mouse="10">'''+HERO+'''</div>
<div class="bubble" style="left:58%;bottom:46%">landed</div>
'''+MQ+'''</section>''')

# 21 launch — in front of the sun, rocket underneath
add("launch", '''
.hero{display:flex;flex-direction:column;align-items:center;text-align:center;padding:80px 16px 64px}
.hero h1{font-size:clamp(3.2rem,8vw,7rem);text-transform:uppercase}
.hero .ship{position:relative;z-index:3;width:min(460px,70vw);margin-top:8px}
.hero .rocket{position:absolute;z-index:2;left:18%;bottom:8%;width:70%;height:46%;background:linear-gradient(90deg,var(--a),var(--a2));clip-path:polygon(10% 40%,40% 0,60% 0,90% 40%,78% 100%,22% 100%);opacity:.9}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div data-parallax="-0.08">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">Fair launch · {{DEX}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="ship"><div class="rocket m-pulse" aria-hidden="true"></div><div class="m-float" data-mouse="12">'''+HERO+'''</div></div>
'''+MQ+'''</section>''')

# 22 impact — sticker cluster + huge type
add("impact", '''
.hero{display:grid;grid-template-columns:1.15fr .85fr;align-items:center;padding:90px 4vw 70px}
.hero h1{font-size:clamp(3.6rem,8vw,7.4rem);text-transform:uppercase}
.hero .cluster{position:relative;z-index:3;height:min(560px,72vh)}
.hero .cluster .hero-main{position:absolute;right:0;bottom:0;width:78%}
.hero .cluster .floater{width:28%}
.hero .cluster .a{left:0;top:8%;transform:rotate(-12deg)}.hero .cluster .b{left:18%;top:0;transform:rotate(8deg);width:20%}
.hero .lede{font-family:ui-monospace,monospace}
@media(max-width:800px){.hero{grid-template-columns:1fr}.hero .cluster{height:320px}}
''', '''
<section class="hero"><div data-parallax="-0.06">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker glitch" data-text="{{TICKER}}">${{TICKER}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="cluster">
  <div class="floater a m-float">'''+SMALL+'''</div>
  <div class="floater b m-bob">'''+TINY+'''</div>
  <div data-mouse="16">'''+HERO+'''</div>
</div>'''+MQ+'''</section>''')

# 23 desk — behind the desk, candles behind
add("desk", '''
.hero{display:block}
.hero .deskbar{position:absolute;z-index:4;left:0;right:0;bottom:48px;height:22%;background:linear-gradient(180deg,color-mix(in srgb,var(--a) 25%,var(--bg-2)), var(--bg));border-top:3px solid var(--a)}
.hero .trader{position:absolute;z-index:3;right:8%;bottom:16%;width:min(420px,42vw)}
.hero .laptop{position:absolute;z-index:5;left:8%;bottom:14%;width:min(220px,24vw);height:120px;background:var(--bg);border:2px solid var(--a);border-radius:8px}
.hero .laptop i{display:block;height:8px;margin:16px 12px;background:var(--a);opacity:.7}
.hero .hero-copy{position:absolute;z-index:5;left:6vw;top:18vh;max-width:480px}
.hero h1{font-size:clamp(2.8rem,5vw,4.8rem)}
''', '''
<section class="hero"><div data-parallax="-0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="trader" data-mouse="8">'''+HERO+'''</div>
<div class="deskbar"></div>
<div class="laptop" aria-hidden="true"><i></i><i></i><i style="width:60%"></i></div>
<div class="hero-copy"><p class="kicker">Desk · {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 24 chapter — walking the wave
add("chapter", '''
.hero{display:grid;grid-template-columns:1.1fr .9fr;align-items:center;padding:90px 0 60px 6vw}
.hero h1{font-size:clamp(3.2rem,6vw,6rem)}
.hero .num{position:absolute;z-index:1;right:4%;top:10%;font-family:var(--display);font-size:28vw;color:var(--a);opacity:.18;line-height:.8}
.hero .wade{position:relative;z-index:3;width:min(500px,46vw);justify-self:end;margin-bottom:-4vh}
@media(max-width:860px){.hero{grid-template-columns:1fr;padding-right:6vw}.hero .wade{width:min(300px,74vw)}}
''', '''
<section class="hero"><div data-parallax="-0.1">@@SCENE@@</div><div class="num" data-parallax="0.04">01</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">Chapter</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div>
<div class="wade m-bob" data-mouse="14">'''+HERO+'''</div>
<div class="bubble" style="right:18%;top:28%">hey</div>
'''+MQ+'''</section>''')

# 25 shrine — type left, mascot in front of the torii
add("shrine", '''
.hero{display:grid;grid-template-columns:1.05fr .95fr;align-items:end;padding:80px 4vw 64px}
.hero h1{font-size:clamp(3.4rem,7vw,6.4rem);text-transform:uppercase}
.hero .yard{position:relative;z-index:3;height:min(640px,78vh)}
.hero .gate{position:absolute;inset:8% 10% 18% 10%}
.hero .figure{position:absolute;left:18%;bottom:6%;width:62%}
.hero .lantern{position:absolute;right:6%;bottom:20%;width:18%}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .yard{height:420px}}
''', '''
<section class="hero"><div data-parallax="-0.08">@@SCENE@@</div>'''+GRAIN+'''
<div class="hero-copy"><p class="kicker">Fortune · {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="yard">
  <svg class="gate" viewBox="0 0 400 460" aria-hidden="true"><path d="M40 80h320M20 120h360M70 120v300M330 120v300M70 200h260" fill="none" stroke="var(--a)" stroke-width="14"/><circle cx="200" cy="48" r="28" fill="var(--a2)"/></svg>
  <div class="lantern m-pulse">'''+TINY+'''</div>
  <div class="figure m-bob" data-mouse="10">'''+HERO+'''</div>
  <div class="bubble" style="left:8%;top:18%">luck</div>
</div>'''+MQ+'''</section>''')

# 26 stickers — die-cut cluster, second allowed "sticker" moment, no white cards
add("stickers", '''
.hero{display:block;text-align:center}
.hero h1{font-size:clamp(2.8rem,6.4vw,5.2rem)}
.hero .pile{position:absolute;z-index:3;left:50%;top:48%;width:min(620px,88vw);height:min(400px,50vh);transform:translate(-50%,-46%)}
.hero .hero-copy{position:absolute;left:0;right:0;top:13vh;z-index:5}
.hero .pile img{position:absolute;width:42%;filter:drop-shadow(0 12px 0 var(--a)) drop-shadow(0 18px 16px rgba(0,0,0,.35))}
.hero .pile img:nth-child(1){left:4%;top:8%;transform:rotate(-14deg);width:34%}
.hero .pile img:nth-child(2){right:2%;top:0;transform:rotate(10deg);width:30%}
.hero .pile img:nth-child(3){left:22%;bottom:0;width:52%;transform:rotate(-3deg)}
.hero .hero-actions{justify-content:center}
''', '''
<section class="hero"><div data-parallax="-0.05">@@SCENE@@</div>'''+GRAIN+'''
<div class="pile">'''+TINY+SMALL+HERO+'''</div>
<div class="hero-copy"><p class="kicker">${{TICKER}}</p><h1 data-wave>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
'''+MQ+'''</section>''')

# 27 vertical — stripes, mascot overlapping the rail
add("vertical", '''
.hero{display:block}
.hero .vtitle{position:absolute;z-index:4;right:0;top:0;bottom:46px;width:128px;writing-mode:vertical-rl;display:grid;place-items:center;background:var(--a);color:var(--on);font-family:var(--display);font-size:clamp(2rem,3.6vw,3.4rem);letter-spacing:.14em}
.hero .overlap{position:absolute;z-index:3;left:6%;bottom:4%;width:min(560px,54vw)}
.hero .floater{left:42%;top:18%}
.hero .hero-copy{position:absolute;z-index:4;left:6vw;top:18vh;max-width:420px}
@media(max-width:800px){.hero .vtitle{writing-mode:horizontal-tb;position:relative;width:auto;bottom:auto;right:auto;padding:78px 16px 8px;font-size:2rem}}
''', '''
<section class="hero"><div data-parallax="-0.06">@@SCENE@@</div>'''+GRAIN+'''
'''+SMALL.replace('floater','floater m-float')+'''
<div class="overlap" data-mouse="12">'''+HERO+'''</div>
<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}} · {{DEX}}</p><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div>
<div class="vtitle">{{NAME}} · ${{TICKER}}</div>
'''+MQ+'''</section>''')

def hero_parts(kind, scene_name):
    css, html = HEROES[kind]
    body = html.replace("@@SCENE@@", scene(scene_name, "s"))
    return RESET + css, body
