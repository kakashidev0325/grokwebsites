"""Twenty-seven hero compositions. CSS uses semantic tokens only."""
from gen_sections import ACTIONS, scene

IMG = '<img class="gchar m-bob" data-tilt data-mouse="18" src="{{LOGO}}" alt="{{NAME}}" width="800" height="800">'

def _css(extra):
    return extra

HEROES = {}

def add(name, css, html):
    HEROES[name] = (css, html)

add("poster", _css('''
.hero{min-height:100svh;display:flex;align-items:flex-end;position:relative;overflow:hidden;background:var(--bg);padding:96px 0 28px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero h1{font-size:clamp(3.4rem,13vw,10rem);line-height:.78;letter-spacing:-.06em;text-transform:uppercase;margin:0;position:relative;z-index:2}
.hero .mascot{position:absolute;z-index:1;left:50%;top:12%;width:min(440px,68vw);transform:translateX(-50%)}
.hero .mascot img{width:100%;background:var(--surface);border:6px solid var(--ink);box-shadow:14px 14px 0 var(--a)}
.hero-copy{position:relative;z-index:3;display:flex;justify-content:space-between;gap:24px;align-items:end;width:min(1120px,calc(100% - 40px));margin:0 auto}
.hero .lede{max-width:34ch;color:var(--muted)}
@media(max-width:800px){.hero{min-height:auto;display:block;padding-top:96px}.hero .mascot{position:relative;left:auto;top:auto;transform:none;margin:0 auto 12px}.hero-copy{flex-direction:column;align-items:flex-start}}
'''), '''
<section class="hero"><div class="mascot">'''+IMG+'''</div>@@SCENE@@
<div class="hero-copy"><div><p class="kicker">{{CHAIN_NAME}} · {{DEX}}</p><h1 data-letters>{{NAME}}</h1></div>
<div><p class="tag">${{TICKER}}</p><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></div></section>''')

add("splitR", _css('''
.hero{min-height:100svh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;position:relative;overflow:hidden;background:var(--bg);padding:80px 4vw 40px;gap:24px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%;opacity:.9}
.hero-copy,.hero .mascot{position:relative;z-index:2}
.hero h1{font-size:clamp(3rem,6vw,6.2rem);letter-spacing:-.045em;margin:0}
.hero .mascot img{width:min(520px,100%);background:var(--surface);border:var(--border);border-radius:var(--radius);box-shadow:var(--shadow)}
.hero .lede{color:var(--muted);max-width:42ch}
@media(max-width:860px){.hero{grid-template-columns:1fr;min-height:auto;padding-top:96px}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">{{DEX}} on {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("splitL", _css('''
.hero{min-height:100svh;display:grid;grid-template-columns:.9fr 1.1fr;background:var(--bg);position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero .mascot{position:relative;z-index:1;display:grid;place-items:end center;padding:80px 0 0 4vw}
.hero .mascot img{width:min(560px,46vw);filter:drop-shadow(16px 24px 0 var(--a))}
.hero-copy{position:relative;z-index:2;align-self:center;padding:40px 6vw}
.hero h1{font-size:clamp(3rem,6.4vw,6.6rem);margin:0;letter-spacing:-.04em}
.hero .lede{color:var(--muted)}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .mascot img{width:min(420px,80vw)}}
'''), '''
<section class="hero">@@SCENE@@<div class="mascot">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">${{TICKER}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("center", _css('''
.hero{min-height:100svh;display:grid;place-items:center;text-align:center;position:relative;overflow:hidden;background:var(--bg);padding:100px 20px 60px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2;max-width:760px}
.hero h1{font-size:clamp(3.2rem,8vw,7rem);margin:10px 0}
.hero .frame{width:min(280px,60vw);margin:0 auto 16px;padding:12px;border-radius:36px;background:var(--surface);border:var(--border);box-shadow:var(--shadow)}
.hero .frame img{width:100%;border-radius:28px}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><div class="frame">'''+IMG+'''</div><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("scatter", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);padding:110px 6vw 50px;display:grid;align-items:center}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero h1{font-size:clamp(4rem,12vw,9rem);margin:0;position:relative;z-index:2;transform:rotate(-2deg)}
.hero h1 span{display:inline-block}
.hero .mascot{position:absolute;right:6vw;bottom:8vh;width:min(380px,46vw);z-index:2;transform:rotate(6deg)}
.hero .mascot img{width:100%;background:var(--surface);border:4px solid var(--ink);border-radius:24px;box-shadow:10px 10px 0 var(--a)}
.hero-copy{position:relative;z-index:2;max-width:640px}
.hero .lede{color:var(--muted)}
@media(max-width:800px){.hero .mascot{position:relative;right:auto;bottom:auto;width:min(280px,70vw);margin-top:12px}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">Say it out loud</p><h1 data-wave>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("app", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);display:grid;place-items:center;padding:100px 20px 70px;text-align:center}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2;max-width:720px}
.hero h1{font-size:clamp(2.8rem,6vw,5rem);letter-spacing:-.04em;margin:8px 0}
.hero .phone{width:min(260px,70vw);margin:22px auto 0;background:var(--surface);border:var(--border);border-radius:32px;padding:14px;box-shadow:var(--shadow)}
.hero .phone img{width:100%;border-radius:22px}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}} social coin</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''<div class="phone">'''+IMG+'''</div></div></section>''')

add("cinema", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);display:flex;align-items:flex-end;padding:0 0 7vh}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero:before,.hero:after{content:"";position:absolute;left:0;right:0;height:28px;background:#000;z-index:3}
.hero:before{top:0}.hero:after{bottom:0}
.hero-copy{position:relative;z-index:2;width:min(720px,calc(100% - 48px));margin:0 auto 0 6vw;background:color-mix(in srgb,var(--bg) 70%,transparent);padding:22px;border-left:4px solid var(--a)}
.hero h1{font-size:clamp(3rem,7vw,6.4rem);margin:0}
.hero .mascot{position:absolute;z-index:2;right:4vw;bottom:40px;width:min(420px,40vw)}
.hero .mascot img{width:100%;filter:drop-shadow(0 20px 30px var(--glow))}
.hero .lede{color:var(--muted)}
@media(max-width:800px){.hero .mascot{position:relative;right:auto;width:min(260px,60vw);margin:12px 0 0 6vw}}
'''), '''
<section class="hero">@@SCENE@@<div class="mascot">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">${{TICKER}} · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("sky", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);display:flex;flex-direction:column;justify-content:flex-end;text-align:center;padding-bottom:0}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero h1{position:relative;z-index:2;font-size:clamp(3.4rem,10vw,8rem);margin:0;text-shadow:4px 4px 0 var(--ink)}
.hero .mascot{position:relative;z-index:2;width:min(380px,70vw);margin:-10px auto -30px}
.hero .mascot img{width:100%;filter:drop-shadow(0 18px 0 var(--a))}
.hero-copy{position:relative;z-index:2}
.hero .lede{color:var(--ink)}
.hero .hero-actions{justify-content:center;margin-bottom:18px}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("orbit", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);display:grid;place-items:center;text-align:center;padding:90px 16px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero .mascot{position:relative;z-index:2;width:min(260px,50vw)}
.hero .mascot img{width:100%;border-radius:50%;background:var(--surface);border:3px solid var(--a);box-shadow:0 0 0 12px color-mix(in srgb,var(--a) 25%,transparent),0 0 60px var(--glow)}
.hero-copy{position:relative;z-index:2;margin-top:18px}
.hero h1{font-size:clamp(2.6rem,6vw,4.6rem);margin:0}
.hero .lede{color:var(--muted)}
'''), '''
<section class="hero">@@SCENE@@<div><div class="mascot m-spin" style="animation-duration:28s">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">Participation layer</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></div></section>''')

add("question", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;align-items:center;padding:100px 6vw}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero h1{font-size:clamp(3.2rem,8vw,7.2rem);margin:0;max-width:14ch;position:relative;z-index:2}
.hero .q{position:absolute;right:4vw;top:18vh;font-family:var(--display);font-size:28vw;line-height:.8;color:var(--a);opacity:.9;z-index:1}
.hero-copy{position:relative;z-index:2;max-width:680px}
.hero .lede{color:var(--muted)}
.hero .mascot{width:120px;margin-bottom:12px}
.hero .mascot img{width:100%;border-radius:20px;border:3px solid var(--ink);background:var(--surface)}
@media(max-width:800px){.hero .q{font-size:48vw;top:8vh;opacity:.35}}
'''), '''
<section class="hero">@@SCENE@@<div class="q" aria-hidden="true">?</div><div class="hero-copy"><div class="mascot">'''+IMG+'''</div><p class="kicker">A real question</p><h1>Are you holding ${{TICKER}}?</h1><p class="lede">{{TAGLINE}} {{ABOUT}}</p>'''+ACTIONS+'''</div></section>''')

add("craft", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;align-items:center;padding:100px 5vw}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2;border:1px solid var(--a);padding:28px;max-width:760px;background:color-mix(in srgb,var(--bg) 78%,transparent)}
.hero h1{font-size:clamp(3rem,7vw,6rem);margin:0;text-transform:uppercase}
.hero .mascot{position:absolute;right:6vw;bottom:8vh;width:min(340px,40vw);z-index:2}
.hero .mascot img{width:100%;border:1px solid var(--a);background:var(--surface)}
.hero .lede{color:var(--muted)}
@media(max-width:800px){.hero .mascot{position:relative;right:auto;width:min(240px,70vw);margin-top:16px}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">Build log · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("index", _css('''
.hero{min-height:100svh;background:var(--bg);display:grid;grid-template-columns:120px 1fr;position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%;opacity:.45}
.hero .idx{position:relative;z-index:2;border-right:1px solid var(--line);display:grid;place-items:center;font-family:var(--display);font-size:1.2rem;letter-spacing:.2em}
.hero-copy{position:relative;z-index:2;align-self:end;padding:40px 6vw 10vh;max-width:900px}
.hero h1{font-size:clamp(3rem,7vw,6.5rem);margin:0;font-weight:500}
.hero .mascot{position:absolute;right:6vw;top:18vh;width:min(300px,32vw);z-index:2}
.hero .mascot img{width:100%;background:var(--surface);border:1px solid var(--line)}
.hero .lede{color:var(--muted);font-size:1.15rem}
@media(max-width:800px){.hero{grid-template-columns:1fr}.hero .idx{display:none}.hero .mascot{position:relative;top:auto;right:auto;width:min(220px,60vw);margin:80px 0 0 6vw}}
'''), '''
<section class="hero">@@SCENE@@<div class="idx">01 — ${{TICKER}}</div><div class="mascot">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">Essay</p><h1>{{NAME}}</h1><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div></section>''')

add("roof", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg)}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero .sign{position:absolute;z-index:3;left:6vw;top:22vh;background:color-mix(in srgb,var(--bg) 55%,transparent);border:3px solid var(--a);padding:16px 20px;box-shadow:0 0 32px var(--glow)}
.hero h1{margin:0;font-size:clamp(2.6rem,6vw,5rem);color:var(--a);text-shadow:0 0 18px var(--glow)}
.hero .mascot{position:absolute;z-index:3;right:8vw;bottom:16vh;width:min(360px,42vw)}
.hero .mascot img{width:100%;filter:drop-shadow(0 12px 0 var(--bg-2))}
.hero .lede{color:var(--ink);margin:.4rem 0 0}
@media(max-width:800px){.hero .sign{left:16px;right:16px;top:90px}.hero .mascot{right:16px;width:min(220px,50vw)}}
'''), '''
<section class="hero">@@SCENE@@<div class="sign"><p class="kicker">{{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("product", _css('''
.hero{min-height:92svh;display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:100px 6vw 40px;background:var(--bg);position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%;opacity:.7}
.hero-copy,.hero .stage{position:relative;z-index:2}
.hero h1{font-size:clamp(3rem,6vw,5.6rem);margin:0;font-weight:560}
.hero .stage{width:min(420px,100%);aspect-ratio:1;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 40% 35%, var(--surface), var(--a));box-shadow:var(--shadow)}
.hero .stage img{width:68%;border-radius:28px;background:var(--bg)}
.hero .lede{color:var(--muted)}
@media(max-width:860px){.hero{grid-template-columns:1fr}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">{{DEX}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="stage m-float">'''+IMG+'''</div></section>''')

add("letterbox", _css('''
.hero{min-height:100svh;background:var(--bg);display:grid;place-items:center;position:relative;overflow:hidden;text-align:center;padding:70px 16px}
.hero .scene{position:absolute;inset:8vh 0;width:100%;height:auto}
.hero-copy{position:relative;z-index:2}
.hero h1{font-family:var(--display);font-size:clamp(3rem,7vw,6.4rem);font-weight:500;margin:0}
.hero .mascot{width:min(220px,40vw);margin:0 auto 12px}
.hero .mascot img{width:100%;border-radius:8px;border:1px solid var(--a)}
.hero .lede{color:var(--muted);font-style:italic}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><div class="mascot">'''+IMG+'''</div><p class="kicker">Chapter 01</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("hud", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:90px 4vw}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2;border:1px solid var(--a);padding:22px;background:color-mix(in srgb,var(--bg) 72%,transparent)}
.hero h1{font-size:clamp(2.6rem,5vw,4.8rem);margin:0;text-transform:uppercase;letter-spacing:.04em}
.hero .readouts{display:flex;gap:14px;margin-top:12px;font-family:ui-monospace,monospace;font-size:.8rem}
.hero .readouts b{display:block;color:var(--a);font-size:1.2rem}
.hero .mascot{position:relative;z-index:2;justify-self:center;width:min(420px,42vw);outline:1px dashed var(--a);outline-offset:12px}
.hero .mascot img{width:100%}
.hero .lede{color:var(--muted)}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .mascot{width:min(280px,70vw)}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">SYS / {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p><div class="readouts"><div><span>SUP</span><b>{{SUPPLY_SHORT}}</b></div><div><span>TAX</span><b>{{TAX}}</b></div><div><span>LP</span><b>{{LP_SHORT}}</b></div></div>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("ghost", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;place-items:center;text-align:center;padding:90px 16px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2}
.hero h1{font-size:clamp(3.4rem,9vw,7rem);margin:6px 0;font-weight:800}
.hero .mascot{width:min(300px,64vw);margin:0 auto}
.hero .mascot img{width:100%;border-radius:50% 50% 46% 46%;background:var(--surface);box-shadow:0 24px 40px color-mix(in srgb,var(--a) 25%,transparent)}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><div class="mascot m-float">'''+IMG+'''</div><p class="kicker">Boo · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("magazine", _css('''
.hero{min-height:100svh;display:grid;grid-template-columns:160px 1fr .8fr;background:var(--bg);position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%;opacity:.35}
.hero .spine{writing-mode:vertical-rl;transform:rotate(180deg);display:grid;place-items:center;font-family:var(--display);font-size:clamp(2rem,4vw,3.4rem);letter-spacing:.12em;border-right:1px solid var(--ink);position:relative;z-index:2}
.hero-copy{position:relative;z-index:2;align-self:center;padding:40px}
.hero h1{font-size:clamp(3rem,6vw,5.5rem);margin:0;font-weight:500}
.hero .mascot{position:relative;z-index:2;align-self:end}
.hero .mascot{display:flex;align-items:flex-end;justify-content:center}
.hero .mascot img{width:min(100%,520px);height:auto;max-height:78vh;object-fit:contain;object-position:bottom}
.hero .lede{color:var(--muted);font-family:var(--body);font-size:1.2rem}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .spine{writing-mode:horizontal-tb;transform:none;border-right:0;border-bottom:1px solid var(--ink);padding:70px 16px 8px}.hero .mascot img{height:auto}}
'''), '''
<section class="hero">@@SCENE@@<div class="spine">{{NAME}}</div><div class="hero-copy"><p class="kicker">Cover · ${{TICKER}}</p><h2 style="font-family:var(--display);font-size:clamp(1.4rem,2vw,2rem);font-weight:500">{{TAGLINE}}</h2><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("seal", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:80px 5vw}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2}
.hero h1{font-size:clamp(3rem,6vw,5.8rem);margin:0}
.hero .seal{position:relative;z-index:2;width:min(460px,46vw);aspect-ratio:1;border-radius:50%;border:10px solid var(--a);display:grid;place-items:center;margin-left:auto;background:color-mix(in srgb,var(--surface) 80%,transparent)}
.hero .seal img{width:70%}
.hero .lede{color:var(--muted)}
@media(max-width:860px){.hero{grid-template-columns:1fr}.hero .seal{width:min(300px,70vw);margin:20px auto}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">Luck · fortune · {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="seal m-spin" style="animation-duration:36s">'''+IMG+'''</div></section>''')

add("planet", _css('''
.hero{min-height:100svh;position:relative;overflow:hidden;background:var(--bg);display:flex;flex-direction:column;justify-content:space-between;padding:100px 0 0}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2;width:min(800px,calc(100% - 40px));margin-left:6vw}
.hero h1{font-size:clamp(3rem,7vw,6.2rem);margin:0;text-transform:uppercase}
.hero .mascot{position:relative;z-index:2;width:min(340px,50vw);margin:0 auto -20px}
.hero .mascot img{width:100%;filter:drop-shadow(0 20px 0 var(--a))}
.hero .lede{color:var(--muted)}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">Mission · {{CHAIN_NAME}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("launch", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:90px 16px 0}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero-copy{position:relative;z-index:2}
.hero h1{font-size:clamp(3.4rem,10vw,8rem);margin:0;text-transform:uppercase}
.hero .btn-main{min-height:64px;padding:0 28px;font-size:1.1rem;border-radius:999px}
.hero .mascot{position:relative;z-index:2;width:min(420px,80vw);margin-top:10px}
.hero .mascot img{width:100%}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker">Fair launch · {{DEX}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot m-float">'''+IMG+'''</div></section>''')

add("impact", _css('''
.hero{min-height:100svh;background:var(--bg);color:var(--ink);display:grid;grid-template-columns:1.2fr .8fr;align-items:center;padding:90px 5vw;position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero h1{font-size:clamp(3.6rem,8vw,7.5rem);line-height:.84;text-transform:uppercase;margin:0;position:relative;z-index:2}
.hero-copy{position:relative;z-index:2}
.hero .mascot{position:relative;z-index:2;width:min(460px,40vw);justify-self:end;filter:drop-shadow(0 0 40px var(--glow))}
.hero .mascot img{width:100%}
.hero .lede{color:var(--muted);font-family:ui-monospace,monospace}
@media(max-width:800px){.hero{grid-template-columns:1fr}.hero .mascot{width:min(280px,70vw)}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="kicker glitch" data-text="{{TICKER}}">${{TICKER}}</p><h1 data-letters>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("desk", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;align-items:end}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.dock{position:relative;z-index:2;display:flex;justify-content:space-between;gap:20px;align-items:end;width:min(1180px,calc(100% - 36px));margin:0 auto 28px}
.hero h1{font-size:clamp(2.8rem,6vw,5.4rem);margin:0;font-family:var(--display)}
.hero .ticker{font-family:ui-monospace,monospace;background:color-mix(in srgb,var(--bg) 75%,transparent);border:1px solid var(--a);padding:12px 14px}
.hero .ticker b{color:var(--a);font-size:1.4rem}
.hero .mascot{width:min(300px,36vw)}
.hero .mascot img{width:100%;background:var(--surface);border-radius:18px;border:2px solid var(--a)}
.hero .lede{color:var(--muted)}
@media(max-width:800px){.dock{flex-direction:column;align-items:flex-start}.hero .mascot{width:min(220px,60vw)}}
'''), '''
<section class="hero">@@SCENE@@<div class="dock"><div><p class="kicker">Desk · {{CHAIN_NAME}}</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="ticker"><div>${{TICKER}}</div><b data-count="100" data-suf="%">100%</b><div>vibe / not advice</div></div><div class="mascot">'''+IMG+'''</div></div></section>''')

add("chapter", _css('''
.hero{min-height:92svh;background:var(--bg);display:grid;grid-template-columns:1.15fr .85fr;align-items:center;padding:90px 0 40px 6vw;position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%;opacity:.8}
.hero-copy{position:relative;z-index:2}
.hero .ch{font-family:var(--display);color:var(--a);letter-spacing:.18em;font-size:.8rem}
.hero h1{font-size:clamp(3.2rem,7vw,6.6rem);margin:8px 0;line-height:.9}
.hero .mascot{position:relative;z-index:2;justify-self:end;width:min(520px,46vw);transform:translateX(8%)}
.hero .mascot img{width:100%;filter:drop-shadow(-12px 16px 0 var(--a))}
.hero .lede{color:var(--muted);font-size:1.15rem}
@media(max-width:860px){.hero{grid-template-columns:1fr;padding-right:6vw}.hero .mascot{width:min(320px,80vw);transform:none;justify-self:start}}
'''), '''
<section class="hero">@@SCENE@@<div class="hero-copy"><p class="ch">CHAPTER 01</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p><p class="lede">{{ABOUT}}</p>'''+ACTIONS+'''</div><div class="mascot">'''+IMG+'''</div></section>''')

add("shrine", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:80px 16px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero .mascot{position:relative;z-index:2;width:min(280px,60vw)}
.hero .mascot img{width:100%;border-radius:20px;background:var(--surface);border:4px solid var(--a)}
.hero-copy{position:relative;z-index:2}
.hero h1{font-size:clamp(3rem,8vw,6rem);margin:8px 0}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div class="mascot m-float">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">Fortune</p><h1>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></section>''')

add("stickers", _css('''
.hero{min-height:100svh;background:var(--bg);position:relative;overflow:hidden;display:grid;place-items:center;padding:90px 16px}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.pile{position:relative;z-index:2;width:min(560px,90vw);height:min(420px,60vh)}
.pile img{position:absolute;width:46%;background:#fff;padding:8px;border:3px solid var(--ink);box-shadow:6px 6px 0 var(--a)}
.pile img:nth-child(1){left:6%;top:10%;transform:rotate(-8deg)}
.pile img:nth-child(2){right:4%;top:0;transform:rotate(7deg)}
.pile img:nth-child(3){left:24%;bottom:0;transform:rotate(-2deg);width:52%}
.hero-copy{position:relative;z-index:3;text-align:center;margin-top:10px}
.hero h1{font-size:clamp(3rem,8vw,6rem);margin:0}
.hero .lede{color:var(--muted)}
.hero .hero-actions{justify-content:center}
'''), '''
<section class="hero">@@SCENE@@<div><div class="pile">'''+IMG+IMG+IMG+'''</div><div class="hero-copy"><p class="kicker">${{TICKER}}</p><h1 data-wave>{{NAME}}</h1><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div></div></section>''')

add("vertical", _css('''
.hero{min-height:100svh;background:var(--bg);display:grid;grid-template-columns:1fr 120px;position:relative;overflow:hidden}
.hero .scene{position:absolute;inset:0;width:100%;height:100%}
.hero .mascot{position:relative;z-index:2;align-self:center;padding-left:8vw;width:min(480px,50vw)}
.hero .mascot img{width:100%;border:8px solid var(--ink);box-shadow:16px 16px 0 var(--a);background:var(--surface)}
.vtitle{position:relative;z-index:2;writing-mode:vertical-rl;display:grid;place-items:center;font-family:var(--display);font-size:clamp(2rem,4vw,3.2rem);letter-spacing:.2em;background:var(--a);color:var(--on)}
.hero-copy{position:absolute;z-index:3;left:8vw;bottom:8vh;max-width:460px}
.hero .lede{color:var(--muted)}
@media(max-width:800px){.hero{grid-template-columns:1fr}.vtitle{writing-mode:horizontal-tb;padding:78px 16px 10px}.hero .mascot{width:min(300px,80vw);padding:10px 16px}.hero-copy{position:relative;left:auto;bottom:auto;padding:10px 16px 30px}}
'''), '''
<section class="hero">@@SCENE@@<div class="mascot">'''+IMG+'''</div><div class="hero-copy"><p class="kicker">{{CHAIN_NAME}} · {{DEX}}</p><p class="lede">{{TAGLINE}}</p>'''+ACTIONS+'''</div><div class="vtitle">{{NAME}} · ${{TICKER}}</div></section>''')

def hero_parts(kind, scene_name):
    css, html = HEROES[kind]
    return css, html.replace("@@SCENE@@", scene(scene_name, "s"))
