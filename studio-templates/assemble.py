"""Assemble templates_src/<arch>.html fragments into self-contained templates/<arch>/index.html"""
import os,re,sys,glob,json
sys.path.insert(0,'templates_src');from banner_spec import SPEC as BSPEC
SRC='templates_src';OUT='templates'
ICONS={
'X':'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
'TG':'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg>',
'DEX':'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 3h2v16h16v2H3zm4 11l4-4 3 3 5-6 1.5 1.3L14 16l-3-3-2.6 2.6z"/></svg>',
'BUY':'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h11l-3-3 1.4-1.4L21.8 8l-5.4 5.4L15 12l3-3H7zm10 10H6l3 3-1.4 1.4L2.2 16l5.4-5.4L9 12l-3 3h11z"/></svg>',
'COPY':'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M16 1H4a2 2 0 00-2 2v14h2V3h12zm3 4H8a2 2 0 00-2 2v14a2 2 0 002 2h11a2 2 0 002-2V7a2 2 0 00-2-2zm0 16H8V7h11z"/></svg>',
}
SOC='<a data-s href="{{X_URL}}" aria-label="X / Twitter">[[X]]</a><a data-s href="{{TG_URL}}" aria-label="Telegram">[[TG]]</a><a data-s href="{{DEXS_URL}}" aria-label="Dexscreener">[[DEX]]</a>{{EXTRA_SOCIALS}}'
core_css=open(f'{SRC}/_core.css').read();core_js=open(f'{SRC}/_core.js').read()
_ROOT=os.path.dirname(os.path.abspath(__file__))
motion_css=open(os.path.join(_ROOT,'_motion.css')).read();motion_js=open(os.path.join(_ROOT,'_motion.js')).read()
core_css=core_css+"\n/* ===== motion system ===== */\n"+motion_css
core_js=core_js+"\n"+motion_js
def parts(t):
    d={};cur=None
    for line in t.split('\n'):
        m=re.match(r'^@@(\w+)@@\s*(.*)$',line)
        if m: cur=m.group(1);d[cur]=m.group(2)+'\n' if m.group(2) else '';continue
        if cur: d[cur]+=line+'\n'
    return d
LABEL_OVERRIDE={"./buy.sh":"./buy.sh --dex {{DEX}}","ok let's go →":"ok let's go → {{DEX}}"}
def dexify(html):
    """Buy CTAs: DEX logo (or buy arrow) via {{BUY_ICON}} + the DEX name ("on {{DEX}}")."""
    def f(m):
        a,inner=m.group(1),m.group(2)
        if 'style="color:#fff"' in a: return m.group(0)          # corporate nav link
        if not ('[[BUY]]' in inner or '{{TICKER}}' in inner or '{{DEX}}' in inner): return m.group(0)  # win95 'Next >' / 'Fix this'
        lab=inner.replace('[[BUY]]','').strip()
        if '{{DEX}}' not in lab: lab=LABEL_OVERRIDE.get(lab) or (lab+' <span class="dexon">on {{DEX}}</span>')
        return a+'{{BUY_ICON}} '+lab+'</a>'
    return re.sub(r'(<a class="(?:btn|chip3d)[^"]*"[^>]*href="\{\{BUY_URL\}\}"[^>]*>)(.*?)</a>',f,html)
def build(arch):
    p=parts(open(f'{SRC}/{arch}.html').read())
    p['BODY']=dexify(p['BODY'])
    pos,anchor,bhtml,bcss=BSPEC[arch]
    body=p['BODY']
    assert anchor in body,(arch,anchor)
    body=body.replace(anchor,(bhtml+'\n'+anchor) if pos=='before' else (anchor+'\n'+bhtml),1)
    xl='<div class="xlinks" data-xlinks>{{LINKS_ROW}}</div>\n'
    fa='<footer' if '<footer' in body else '<p class="legal"'
    body=body.replace(fa,xl+fa,1)
    p['BODY']=body;p['CSS']=p['CSS']+'\n/* banner */\n'+bcss
    fonts=p.get('FONTS','').strip()
    body_html=p['BODY']
    body_attrs=''
    mbody=re.match(r'\s*<body([^>]*)>(.*)</body>\s*\Z', body_html, re.S)
    if mbody:
        body_attrs=mbody.group(1)
        body_html=mbody.group(2)
    html=f'''<!doctype html>
<html lang="en" data-theme-mode="{{{{THEME_MODE}}}}" data-theme-preset="{{{{THEME_PRESET}}}}" style="{{{{THEME_STYLE}}}}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<!-- archetype: {arch} | placeholders: {{{{NAME}}}} {{{{TICKER}}}} {{{{LOGO}}}} {{{{CA}}}} {{{{CHAIN}}}} {{{{X_URL}}}} {{{{TG_URL}}}} {{{{BUY_URL}}}} {{{{CHART_URL}}}} (+ optional {{{{TAGLINE}}}} {{{{ABOUT}}}} {{{{SUPPLY}}}} {{{{TAX}}}} {{{{DEX}}}} {{{{NATIVE}}}} {{{{WALLET}}}} {{{{DEXS_URL}}}} {{{{CHAIN_NAME}}}} {{{{BUY_ICON}}}}=raw html) -->
<title>{{{{NAME}}}} (${{{{TICKER}}}}) | {{{{TAGLINE}}}}</title>
<meta name="description" content="{{{{ABOUT}}}}">
<meta property="og:title" content="{{{{NAME}}}} (${{{{TICKER}}}})"><meta property="og:description" content="{{{{TAGLINE}}}}"><meta property="og:image" content="{{{{LOGO}}}}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{{{{LOGO}}}}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
{core_css}
/* ===== {arch} ===== */
{p['CSS']}
</style>
</head>
<body class="a-{arch}"{body_attrs}>
{body_html}
<div id="toast" role="status" aria-live="polite"></div>
<script>
{core_js}
</script>
<script>
{p.get('JS','')}
</script>
</body>
</html>
'''
    html=html.replace('[[SOCIALS]]',SOC)
    for k,v in ICONS.items(): html=html.replace(f'[[{k}]]',v)
    os.makedirs(f'{OUT}/{arch}',exist_ok=True)
    open(f'{OUT}/{arch}/index.html','w').write(html)
    return arch
if __name__=='__main__':
    archs=sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{SRC}/*.html') if not os.path.basename(f).startswith('_'))
    for a in archs: print('built',build(a))
