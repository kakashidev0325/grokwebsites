import asyncio,sys,os,json,subprocess
from playwright.async_api import async_playwright
archs=sys.argv[1:] or sorted(d for d in os.listdir('templates') if os.path.exists(f'templates/{d}/index.html'))
for a in archs: subprocess.run(['python3','build.py','sample/inputs.json',a,'--out','sample/out'],check=True,capture_output=True)
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for a in archs:
            f='file://'+os.path.abspath(f'sample/out/bonkle-{a}/index.html')
            for name,vp,mob in [('desktop',{'width':1440,'height':900},False),('mobile',{'width':390,'height':844},True)]:
                ctx=await b.new_context(viewport=vp,is_mobile=mob,device_scale_factor=1 if not mob else 2,has_touch=mob);p=await ctx.new_page()
                errs=[];p.on('pageerror',lambda e:errs.append(str(e)))
                await p.goto(f);await p.wait_for_timeout(1200)
                h=await p.evaluate('document.body.scrollHeight')
                for y in range(0,h,600): await p.evaluate(f'window.scrollTo(0,{y})');await p.wait_for_timeout(60)
                await p.evaluate("document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));window.scrollTo(0,0)");await p.wait_for_timeout(900)
                ow=await p.evaluate('document.documentElement.scrollWidth>window.innerWidth+2')
                await p.screenshot(path=f'templates/{a}/{name}.jpg',full_page=True,type='jpeg',quality=70)
                await p.screenshot(path=f'templates/{a}/{name}-hero.jpg',type='jpeg',quality=80)
                print(a,name,'h',h,'overflowX' if ow else 'ok',errs[:2],flush=True);await ctx.close()
        await b.close()
asyncio.run(main())
