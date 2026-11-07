#!/usr/bin/env python3
"""Meme-coin site generator.
Usage:
  python3 build.py inputs.json <archetype|random|all> [--out OUTDIR]
  python3 build.py --list
inputs.json keys (required*): name*, ticker*, logo* (local path or http URL), ca*, chain* (solana|ethereum|base|bsc|...),
  x_url, tg_url, banner (path/URL), socials ([{type:website|discord|tiktok|instagram|youtube|link, url, label}]), buy_url, chart_url, tagline, about, supply, tax,
  dex (DEX id from templates_src/dex_registry.json, e.g. pumpfun|jupiter|uniswap-v4|pancakeswap|stonfi|custom; empty = chain default), dex_name (label for dex=custom), native, wallet, dexs_url, images (list of extra meme image paths/URLs)
Output: OUTDIR/<slug>-<archetype>/index.html + assets/ (logo copied in). Missing socials are auto-hidden by the page JS.
"""
import json,sys,os,re,shutil,html,random,urllib.request,urllib.parse,argparse
HERE=os.path.dirname(os.path.abspath(__file__));TPL=os.path.join(HERE,'templates')
def archs(): return sorted(d for d in os.listdir(TPL) if os.path.isfile(os.path.join(TPL,d,'index.html')))
CHAIN={'solana':('Solana','SOL','Phantom'),'ethereum':('Ethereum','ETH','MetaMask'),'base':('Base','ETH','Coinbase Wallet'),
 'bsc':('BNB Chain','BNB','MetaMask'),'arbitrum':('Arbitrum','ETH','MetaMask'),'sui':('Sui','SUI','Sui Wallet'),'ton':('TON','TON','Tonkeeper'),'tron':('TRON','TRX','TronLink')}
REG=json.load(open(os.path.join(HERE,'templates_src','dex_registry.json')));DEXES={d['id']:d for d in REG['dexes']}
DEX_LOGOS=os.path.join(HERE,'templates_src','dex_logos')
BUY_SVG='<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h11l-3-3 1.4-1.4L21.8 8l-5.4 5.4L15 12l3-3H7zm10 10H6l3 3-1.4 1.4L2.2 16l5.4-5.4L9 12l-3 3h11z"/></svg>'
def dex_auto(chain,ca):
    d=REG['defaults'].get(chain)
    if d=='auto-solana': return 'pumpfun' if ca.endswith('pump') else 'bonkfun' if ca.endswith('bonk') else 'jupiter'
    return d
def dex_url(e,chain,ca):
    u=e.get('url')
    if isinstance(u,dict): u=u.get(chain)
    if not u and e.get('fallback'): return dex_url(DEXES[e['fallback']],chain,ca)
    return (u or '').replace('{ca}',urllib.parse.quote(ca,safe="-_.!~*'()"))
def resolve_dex(inp,chain,ca):
    """-> (id|'custom', display name, auto buy url, logo file or None). Mirrors resolveDex() in app/src/app.js."""
    sel=(inp.get('dex') or '').strip();name=(inp.get('dex_name') or '').strip()
    if inp.get('dex_auto'): sel=''
    if sel and sel!='custom' and sel not in DEXES:  # legacy free-text DEX name
        m=[d for d in REG['dexes'] if chain in d['chains'] and d['name'].lower()==sel.lower()]
        if m: sel=m[0]['id']
        else: name,sel=sel,'custom'
    if sel and sel!='custom' and chain not in DEXES[sel]['chains']: sel=''
    if not sel: sel=dex_auto(chain,ca) or 'custom'
    if sel=='custom':
        a=DEXES.get(dex_auto(chain,ca) or '')
        return 'custom',name or 'a DEX',(dex_url(a,chain,ca) if a else f'https://dexscreener.com/{chain}/{ca}'),None
    e=DEXES[sel];return sel,e['name'],dex_url(e,chain,ca),e.get('logo')
ALIAS={'sol':'solana','eth':'ethereum','bnb':'bsc','binance':'bsc','arb':'arbitrum'}
def fetch_asset(src,dst_dir,stem):
    os.makedirs(dst_dir,exist_ok=True)
    ext=os.path.splitext(src.split('?')[0])[1].lower() or '.png'
    if ext not in ('.png','.jpg','.jpeg','.gif','.webp','.svg','.avif'): ext='.png'
    dst=os.path.join(dst_dir,stem+ext)
    if re.match(r'https?://',src):
        req=urllib.request.Request(src,headers={'User-Agent':'Mozilla/5.0'})
        open(dst,'wb').write(urllib.request.urlopen(req,timeout=30).read())
    else: shutil.copyfile(os.path.expanduser(src),dst)
    return 'assets/'+os.path.basename(dst)
ICONS=json.load(open(os.path.join(HERE,'templates_src','social_icons.json')))
def norm_url(u):
    u=(u or '').strip()
    if not u: return ''
    if not re.match(r'^(https?:|mailto:)',u,re.I): u='https://'+u.lstrip('/')
    return u
def svg(t): return '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="'+ICONS.get(t,ICONS['link'])['path']+'"/></svg>'
def social_html(inp):
    ex=[];row=[]
    for t,u in (('x',inp.get('x_url')),('telegram',inp.get('tg_url'))):
        u=norm_url(u)
        if u: row.append((t,ICONS[t]['label'],u))
    for s in inp.get('socials',[]) or []:
        u=norm_url(s.get('url'));t=(s.get('type') or 'link').lower()
        if not u: continue
        if t not in ICONS: t='link'
        lab=(s.get('label') or '').strip() or ICONS[t]['label']
        ex.append(f'<a data-s class="xs" href="{html.escape(u,True)}" aria-label="{html.escape(lab,True)}">{svg(t)}</a>')
        row.append((t,lab,u))
    rh=''.join(f'<a href="{html.escape(u,True)}" target="_blank" rel="noopener">{svg(t)}<span>{html.escape(l)}</span></a>' for t,l,u in row)
    return ''.join(ex),rh
def short_ca(ca):
    ca=str(ca or '').strip()
    if not ca: return '—'
    if len(ca)<=12: return ca
    return ca[:6]+'…'+ca[-4:]
def compact_num(s):
    s=str(s or '').strip()
    if not s: return '—'
    try: n=float(str(s).replace(',',''))
    except Exception: return s
    absn=abs(n)
    if absn>=1e12: return (f"{n/1e12:.1f}".rstrip('0').rstrip('.'))+'T'
    if absn>=1e9: return (f"{n/1e9:.1f}".rstrip('0').rstrip('.'))+'B'
    if absn>=1e6: return (f"{n/1e6:.1f}".rstrip('0').rstrip('.'))+'M'
    if absn>=1e3: return (f"{n/1e3:.1f}".rstrip('0').rstrip('.'))+'K'
    return str(s)
def values(inp,out_dir):
    c=ALIAS.get(inp['chain'].lower(),inp['chain'].lower())
    cname,native,wallet=CHAIN.get(c,(c.title(),c.upper()[:4],'your wallet'))
    ca=inp['ca'].strip();tk=inp['ticker'].strip().lstrip('$')
    did,dname,dbuy,dlogo=resolve_dex(inp,c,ca)
    supply=inp.get('supply') or '1,000,000,000'; tax=inp.get('tax') or '0/0'; lp=inp.get('lp') or 'Burned'
    # Selectable color theme (independent of chain)
    theme_mode=(inp.get('theme_mode') or 'original').lower()
    if theme_mode not in ('original','preset','custom'): theme_mode='original'
    theme_preset=(inp.get('theme_preset') or '').strip()
    t1=(inp.get('theme_primary') or '').strip(); t2=(inp.get('theme_secondary') or '').strip()
    theme_style=''
    if theme_mode=='custom' and t1 and t2:
        def _luma(hexs):
            h=hexs.strip().lstrip('#')
            if len(h)==3: h=''.join(c*2 for c in h)
            try: n=int(h[:6],16)
            except Exception: return 0.2
            r,g,b=((n>>16)&255)/255,((n>>8)&255)/255,(n&255)/255
            def f(v): return v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4
            return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
        ink='#0a0a0a' if _luma(t1)>0.45 else '#f6f7fb'
        theme_style=f'--theme-1:{t1};--theme-2:{t2};--theme-glow:color-mix(in srgb,{t1} 50%,transparent);--theme-grad:linear-gradient(135deg,{t1},{t2});--theme-ink:{ink}'
    elif theme_mode=='preset' and not theme_preset:
        theme_mode='original'
    v={'NAME':inp['name'],'TICKER':tk,'CA':ca,'CA_SHORT':short_ca(ca),'CHAIN':c,'CHAIN_NAME':cname,
       'THEME_MODE':theme_mode,'THEME_PRESET':theme_preset if theme_mode=='preset' else '','THEME_STYLE':theme_style,
       'X_URL':norm_url(inp.get('x_url')),'TG_URL':norm_url(inp.get('tg_url')),
       'BUY_URL':norm_url(inp.get('buy_url')) or dbuy,
       'CHART_URL':inp.get('chart_url') or f'https://dexscreener.com/{c}/{ca}?embed=1&loadChartSettings=0&trades=0&tabs=0&info=0&chartLeftToolbar=0&chartTheme=dark&theme=dark&chartStyle=1&chartType=usd&interval=15',
       'DEXS_URL':inp.get('dexs_url') or f'https://dexscreener.com/{c}/{ca}',
       'TAGLINE':inp.get('tagline') or f"The most memeable {inp['name']} on {cname}.",
       'ABOUT':inp.get('about') or f"{inp['name']} (${tk}) is a community-driven meme coin on {cname}. No team allocation, no roadmap promises, just vibes, memes and a community that refuses to sell.",
       'CTA':inp.get('cta') or inp.get('tagline') or f"Join the {inp['name']} community. Buy ${tk}. Make memes. Never sell.",
       'SUPPLY':supply,'SUPPLY_SHORT':compact_num(supply),'TAX':tax,'LP':lp,'LP_SHORT':compact_num(lp),
       'PRICE':inp.get('price') or '—','MCAP':inp.get('mcap') or '—','VOL':inp.get('vol') or '—','LIQ':inp.get('liq') or '—',
       'DEX':dname,'NATIVE':inp.get('native') or native,'WALLET':inp.get('wallet') or wallet}
    icon=BUY_SVG
    if dlogo:
        os.makedirs(os.path.join(out_dir,'assets'),exist_ok=True);shutil.copyfile(os.path.join(DEX_LOGOS,dlogo),os.path.join(out_dir,'assets','dex.png'))
        icon='<img class="dexic" src="assets/dex.png" alt="'+html.escape(dname,True)+'">'
    v['_BUY_ICON']=icon
    v['LOGO']=fetch_asset(inp['logo'],os.path.join(out_dir,'assets'),'logo')
    v['BANNER']=fetch_asset(inp['banner'],os.path.join(out_dir,'assets'),'banner') if inp.get('banner') else ''
    imgs=[fetch_asset(s,os.path.join(out_dir,'assets'),f'meme{i+1}') for i,s in enumerate(inp.get('images',[]))]
    chars_src=inp.get('characters') or []
    chars=[fetch_asset(s,os.path.join(out_dir,'assets'),f'char{i+1}') for i,s in enumerate(chars_src)]
    if not chars and v.get('LOGO'): chars=[v['LOGO']]
    return v,imgs,chars
def render(arch,inp,out_root):
    slug=re.sub(r'[^a-z0-9]+','-',inp['ticker'].lower()).strip('-') or 'token'
    out=os.path.join(out_root,f'{slug}-{arch}');os.makedirs(out,exist_ok=True)
    v,imgs,chars=values(inp,out)
    t=open(os.path.join(TPL,arch,'index.html')).read()
    if imgs:  # replace gallery logo slots with provided meme images, cycling
        i=[0]
        def sub(m): s=imgs[i[0]%len(imgs)];i[0]+=1;return m.group(1)+s+m.group(2)
        t=re.sub(r'(<img[^>]*class="[^"]*\bgimg\b[^"]*"[^>]*src=")\{\{LOGO\}\}(")',sub,t)
    if chars:
        ci=[0]
        def csub(m): s=chars[ci[0]%len(chars)];ci[0]+=1;return m.group(1)+s+m.group(2)
        t=re.sub(r'(<img[^>]*class="[^"]*\bgchar\b[^"]*"[^>]*src=")\{\{LOGO\}\}(")',csub,t)
    ex,row=social_html(inp)
    t=t.replace('{{EXTRA_SOCIALS}}',ex).replace('{{LINKS_ROW}}',row).replace('{{BUY_ICON}}',v.pop('_BUY_ICON'))
    for k,val in v.items():
        t=t.replace('{{'+k+'}}',html.escape(str(val),quote=True))
    left=set(re.findall(r'\{\{([A-Z_]+)\}\}',t))
    if left: print('WARNING unfilled placeholders:',left,file=sys.stderr)
    open(os.path.join(out,'index.html'),'w').write(t)
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('inputs',nargs='?');ap.add_argument('arch',nargs='?',default='random');ap.add_argument('--out',default=os.path.join(HERE,'out'));ap.add_argument('--list',action='store_true')
    a=ap.parse_args()
    if a.list or not a.inputs: print('\n'.join(archs()));sys.exit(0)
    inp=json.load(open(a.inputs))
    for k in ('name','ticker','logo','ca','chain'):
        if not inp.get(k): sys.exit(f'missing required input: {k}')
    sel=archs() if a.arch=='all' else [random.choice(archs())] if a.arch=='random' else a.arch.split(',')
    for ar in sel:
        if ar not in archs(): sys.exit(f'unknown archetype {ar}; use --list')
        print(render(ar,inp,a.out))
