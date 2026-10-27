import json,asyncio,re,sys
from playwright.async_api import async_playwright
R=[x for x in json.load(open('raw/fetched.json')) if x['alive']=='yes']
JS='''()=>{const fam=new Set(),cols={},anim=new Set();let n=0;
for(const el of document.querySelectorAll('body *')){if(n++>3000)break;const s=getComputedStyle(el);fam.add(s.fontFamily.split(',')[0].replace(/["']/g,'').trim());
for(const c of [s.backgroundColor,s.color]){if(c&&c!=='rgba(0, 0, 0, 0)')cols[c]=(cols[c]||0)+1}
if(s.animationName&&s.animationName!=='none')anim.add(s.animationName)}
const h=[...document.querySelectorAll('h1,h2,h3')].map(e=>e.innerText.trim()).filter(Boolean).slice(0,30);
return {title:document.title,fonts:[...fam].slice(0,15),colors:Object.entries(cols).sort((a,b)=>b[1]-a[1]).slice(0,8),anims:[...anim].slice(0,20),heads:h,text:document.body.innerText.slice(0,2500),height:document.body.scrollHeight,
iframes:[...document.querySelectorAll('iframe')].map(f=>f.src).slice(0,5),links:[...document.querySelectorAll('a[href]')].map(a=>a.href).filter(u=>/raydium|pump\\.fun|uniswap|jup\\.ag|dexscreener|dextools|birdeye|x\\.com|twitter|t\\.me|pancake|aerodrome|coingecko|coinmarketcap/.test(u)).slice(0,25),
imgs:document.images.length,videos:document.querySelectorAll('video').length,canvas:document.querySelectorAll('canvas').length}}'''
async def one(b,x,i,sem):
    async with sem:
        ctx=await b.new_context(viewport={'width':1440,'height':900},user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36')
        p=await ctx.new_page()
        try:
            await p.goto(x['url'],timeout=25000,wait_until='domcontentloaded'); await p.wait_for_timeout(3500)
            d=await p.evaluate(JS); d['domain']=x['domain']
            if i<80: await p.screenshot(path=f"shots/{x['domain']}.jpg",type='jpeg',quality=60)
            json.dump(d,open(f"rendered/{x['domain']}.json",'w'))
        except Exception as e: print('fail',x['domain'],str(e)[:80],flush=True)
        await ctx.close()
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        sem=asyncio.Semaphore(8)
        await asyncio.gather(*[one(b,x,i,sem) for i,x in enumerate(R)])
        await b.close()
asyncio.run(main()); print('DONE')
