(function(){
var CA="{{CA}}";
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var fine=window.matchMedia&&window.matchMedia('(pointer:fine)').matches;
var mobile=/Mobi|Android/i.test(navigator.userAgent)||window.innerWidth<700;
function toast(m){var t=document.getElementById('toast');if(!t){t=document.createElement('div');t.id='toast';document.body.appendChild(t)}t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('show')},1800)}
window.memeToast=toast;
function burst(x,y,n,cls){if(reduce)return;n=n||14;cls=cls||'sparkle-burst';
 for(var i=0;i<n;i++){var s=document.createElement('span');s.className=cls;var ang=Math.random()*Math.PI*2,dist=24+Math.random()*90;
  s.style.left=x+'px';s.style.top=y+'px';s.style.setProperty('--dx',Math.cos(ang)*dist+'px');s.style.setProperty('--dy',Math.sin(ang)*dist+'px');
  s.style.setProperty('--rot',(Math.random()*720-360)+'deg');
  s.style.background=['#ffd23f','#ff6fa8','#7c4dff','#39ff14','#01cdfe','#fff','#ff9f1c'][i%7];document.body.appendChild(s);setTimeout(function(el){el.remove()},1000,s)}}
function confetti(x,y){burst(x,y,mobile?12:28,'confetti-piece')}
function copy(ev){var done=function(){toast('Contract address copied ✓');if(ev&&ev.clientX)confetti(ev.clientX,ev.clientY)};if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(CA).then(done,fb)}else fb();function fb(){var ta=document.createElement('textarea');ta.value=CA;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy')}catch(e){}ta.remove();done()}}
document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();copy(e);b.classList.add('copied');setTimeout(function(){b.classList.remove('copied')},1200)})});
document.querySelectorAll('a[href="{{BUY_URL}}"],a.btn-pulse,[data-buy]').forEach(function(a){a.addEventListener('click',function(e){if(e.clientX)confetti(e.clientX,e.clientY)})});
document.querySelectorAll('a[data-s]').forEach(function(a){var h=a.getAttribute('href');if(!h||h==='#'||h.indexOf('{{')===0){a.style.display='none'}else{a.target='_blank';a.rel='noopener'}});
document.querySelectorAll('.mq').forEach(function(m){var t=m.querySelector('.mq-track');if(t){m.appendChild(t.cloneNode(true)).setAttribute('aria-hidden','true')}});
/* reveals */
var revealSel='.rv,.rv-l,.rv-r,.rv-z,.rv-rot,.rv-blur,.rv-stagger';
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});document.querySelectorAll(revealSel).forEach(function(el){io.observe(el)})}else document.querySelectorAll(revealSel).forEach(function(el){el.classList.add('in')});
document.querySelectorAll('[data-banner]').forEach(function(b){var i=b.querySelector('img');if(!i||!i.getAttribute('src')||i.getAttribute('src').indexOf('{{')===0)b.remove()});
document.querySelectorAll('[data-xlinks]').forEach(function(x){if(!x.querySelector('a'))x.remove()});
document.querySelectorAll('[data-year]').forEach(function(y){y.textContent=new Date().getFullYear()});
document.querySelectorAll('[data-menu]').forEach(function(b){b.addEventListener('click',function(){document.body.classList.toggle('menu-open')})});
document.querySelectorAll('nav a[href^="#"]').forEach(function(a){a.addEventListener('click',function(){document.body.classList.remove('menu-open')})});
/* short CA helpers */
document.querySelectorAll('[data-ca-short]').forEach(function(el){var c=CA||'';if(c.length>12)el.textContent=c.slice(0,6)+'…'+c.slice(-4);else el.textContent=c});
/* count-up stats */
document.querySelectorAll('[data-count]').forEach(function(el){
 var target=parseFloat(el.getAttribute('data-count'))||0,suf=el.getAttribute('data-suf')||'',pre=el.getAttribute('data-pre')||'',dec=parseInt(el.getAttribute('data-dec')||'0',10);
 function run(){if(reduce){el.textContent=pre+target.toFixed(dec)+suf;return}
  var t0=performance.now(),dur=1200;function step(t){var p=Math.min(1,(t-t0)/dur);p=1-Math.pow(1-p,3);el.textContent=pre+(target*p).toFixed(dec)+suf;if(p<1)requestAnimationFrame(step)}requestAnimationFrame(step)}
 if('IntersectionObserver' in window){var cio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run();cio.unobserve(e.target)}})},{threshold:.4});cio.observe(el)}else run()
});
/* letter-split titles */
document.querySelectorAll('[data-letters]').forEach(function(el){if(reduce)return;var txt=el.textContent;el.textContent='';el.classList.add('intro-title');
 var words=txt.split(/(\s+)/),di=0;words.forEach(function(w){if(/^\s+$/.test(w)){el.appendChild(document.createTextNode(' '));return}
  var wrap=document.createElement('span');wrap.className='word';
  for(var i=0;i<w.length;i++){var sp=document.createElement('span');sp.textContent=w[i];sp.style.animationDelay=Math.min(0.04*di+0.15,0.9)+'s';wrap.appendChild(sp);di++}
  el.appendChild(wrap)});setTimeout(function(){el.querySelectorAll('.word>span').forEach(function(s){s.style.opacity='1';s.style.transform='none';s.style.animation='none'})},1400);});
/* typing taglines */
document.querySelectorAll('[data-type]').forEach(function(el){if(reduce)return;var full=el.getAttribute('data-type')||el.textContent;el.textContent='';el.classList.add('typing');
 var i=0;function tick(){el.textContent=full.slice(0,++i);if(i<full.length)setTimeout(tick,28+Math.random()*40);else el.classList.remove('typing')}setTimeout(tick,600)});
/* scroll progress */
if(!reduce){var bar=document.createElement('div');bar.className='scroll-progress';bar.setAttribute('aria-hidden','true');document.body.appendChild(bar);
 window.addEventListener('scroll',function(){var h=document.documentElement.scrollHeight-window.innerHeight;bar.style.width=(h>0?(window.scrollY/h*100):0)+'%'},{passive:true})}
/* parallax */
if(!reduce){var layers=document.querySelectorAll('[data-parallax]');
 if(layers.length){window.addEventListener('scroll',function(){var y=window.scrollY||0;layers.forEach(function(el){var s=parseFloat(el.getAttribute('data-parallax')||'0.2');el.style.transform='translate3d(0,'+(y*s)+'px,0)'})},{passive:true})}
 /* ambient particles */
 if(document.body.hasAttribute('data-particles')){var p=document.createElement('div');p.className='particles';p.setAttribute('aria-hidden','true');document.body.prepend(p);
  var n=mobile?12:28;for(var i=0;i<n;i++){var d=document.createElement('i');d.style.left=(Math.random()*100)+'%';d.style.bottom=(-10-Math.random()*20)+'vh';d.style.animationDuration=(8+Math.random()*14)+'s';d.style.animationDelay=(-Math.random()*12)+'s';d.style.background=getComputedStyle(document.body).getPropertyValue('--part')||'currentColor';d.style.opacity=String(0.25+Math.random()*0.45);p.appendChild(d)}}
 /* canvas sparkles / particles overlay */
 if(document.body.hasAttribute('data-sparkles')){(function(){var c=document.createElement('canvas');c.setAttribute('aria-hidden','true');c.style.cssText='position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:1';document.body.prepend(c);var ctx=c.getContext('2d'),dots=[],N=mobile?18:40;
  function resize(){c.width=window.innerWidth;c.height=window.innerHeight}resize();window.addEventListener('resize',resize);
  for(var i=0;i<N;i++)dots.push({x:Math.random()*c.width,y:Math.random()*c.height,r:1+Math.random()*2.2,vx:(Math.random()-.5)*.4,vy:-.2-Math.random()*.6,a:.2+Math.random()*.5});
  function frame(){ctx.clearRect(0,0,c.width,c.height);dots.forEach(function(d){d.x+=d.vx;d.y+=d.vy;if(d.y<-10){d.y=c.height+10;d.x=Math.random()*c.width}ctx.beginPath();ctx.arc(d.x,d.y,d.r,0,6.28);ctx.fillStyle='rgba(255,255,255,'+d.a+')';ctx.fill()});requestAnimationFrame(frame)}frame()})()}
}
/* magnetic buttons */
if(!reduce&&fine){document.querySelectorAll('[data-magnetic]').forEach(function(btn){btn.addEventListener('mousemove',function(e){var r=btn.getBoundingClientRect(),dx=(e.clientX-r.left-r.width/2)*.28,dy=(e.clientY-r.top-r.height/2)*.28;btn.style.transform='translate('+dx+'px,'+dy+'px)'});btn.addEventListener('mouseleave',function(){btn.style.transform=''})})}
/* hover tilt 3d */
if(!reduce&&fine){document.querySelectorAll('[data-tilt]').forEach(function(el){el.classList.add('tilt-3d');el.addEventListener('mousemove',function(e){var r=el.getBoundingClientRect(),rx=((e.clientY-r.top)/r.height-.5)*-10,ry=((e.clientX-r.left)/r.width-.5)*10;el.style.transform='perspective(700px) rotateX('+rx+'deg) rotateY('+ry+'deg)'});el.addEventListener('mouseleave',function(){el.style.transform=''})})}
/* cursor follower */
if(!reduce&&fine&&document.body.hasAttribute('data-cursor')){(function(){var d=document.createElement('div'),r=document.createElement('div');d.className='cursor-dot';r.className='cursor-ring';d.style.display=r.style.display='block';document.body.appendChild(d);document.body.appendChild(r);var x=0,y=0,rx=0,ry=0;
 document.addEventListener('mousemove',function(e){x=e.clientX;y=e.clientY;d.style.left=x+'px';d.style.top=y+'px'});
 (function loop(){rx+=(x-rx)*.18;ry+=(y-ry)*.18;r.style.left=rx+'px';r.style.top=ry+'px';requestAnimationFrame(loop)})();
 document.querySelectorAll('a,button,[data-magnetic]').forEach(function(el){el.addEventListener('mouseenter',function(){d.style.width=d.style.height='4px';r.style.width=r.style.height='44px'});el.addEventListener('mouseleave',function(){d.style.width=d.style.height='10px';r.style.width=r.style.height='28px'})})})()}
/* meme rail drag + auto */
document.querySelectorAll('.meme-rail').forEach(function(rail){var track=rail.querySelector('.rail-track');if(!track)return;
 if(track.children.length){Array.prototype.slice.call(track.children).forEach(function(ch){track.appendChild(ch.cloneNode(true))})}
 var down=false,sx=0,sl=0;
 rail.addEventListener('pointerdown',function(e){down=true;rail.classList.add('is-drag');sx=e.clientX;sl=rail.scrollLeft||0;rail.setPointerCapture(e.pointerId)});
 rail.addEventListener('pointermove',function(e){if(!down)return;rail.scrollLeft=sl-(e.clientX-sx)});
 function up(){down=false;rail.classList.remove('is-drag')}rail.addEventListener('pointerup',up);rail.addEventListener('pointercancel',up)});
/* faq accordion + wave letters */
document.querySelectorAll('[data-acc] .acc-q').forEach(function(q){q.addEventListener('click',function(){var item=q.parentElement;var open=item.classList.toggle('open');q.setAttribute('aria-expanded',open?'true':'false')})});
document.querySelectorAll('[data-wave]').forEach(function(el){if(reduce)return;var txt=el.textContent;el.textContent='';el.classList.add('wave-text');for(var i=0;i<txt.length;i++){var s=document.createElement('span');s.textContent=txt[i]===' '?'\u00a0':txt[i];s.style.animationDelay=(i*0.045)+'s';el.appendChild(s)}});
/* sticky header helper */
document.querySelectorAll('[data-sticky-header]').forEach(function(h){var on=function(){h.classList.toggle('is-stuck',window.scrollY>40)};window.addEventListener('scroll',on,{passive:true});on()});
/* topbar rotator */
document.querySelectorAll('[data-topbar]').forEach(function(bar){var msgs=bar.querySelectorAll('.topbar__msg');if(msgs.length<2)return;var i=0;msgs[0].classList.add('is-on');
 setInterval(function(){msgs[i].classList.remove('is-on');i=(i+1)%msgs.length;msgs[i].classList.add('is-on')},3200)});
/* live Dexscreener market bar */
document.querySelectorAll('[data-dexs-live]').forEach(function(box){
 var ca=(CA||'').trim();if(!ca||ca.indexOf('{{')===0)return;
 var chain=box.getAttribute('data-chain')||'';
 function fmt(n){n=+n||0;if(n>=1e9)return'$'+(n/1e9).toFixed(2)+'B';if(n>=1e6)return'$'+(n/1e6).toFixed(2)+'M';if(n>=1e3)return'$'+(n/1e3).toFixed(1)+'K';return'$'+n.toFixed(2)}
 function set(sel,v){var el=box.querySelector(sel);if(el)el.textContent=v}
 fetch('https://api.dexscreener.com/latest/dex/tokens/'+encodeURIComponent(ca)).then(function(r){return r.json()}).then(function(j){
  var pairs=(j&&j.pairs)||[];if(!pairs.length)return;
  if(chain){var c=chain.toLowerCase();var pref=pairs.filter(function(p){return(p.chainId||'').toLowerCase().indexOf(c)>=0});if(pref.length)pairs=pref}
  pairs.sort(function(a,b){return(+b.liquidity&&b.liquidity.usd||0)-(+a.liquidity&&a.liquidity.usd||0)});
  var p=pairs[0],px=+p.priceUsd||0;set('[data-price]',px>=1?('$'+px.toFixed(4)):('$'+px.toPrecision(4)));
  set('[data-mcap]',fmt(p.marketCap||p.fdv));set('[data-vol]',fmt(p.volume&&p.volume.h24));set('[data-liq]',fmt(p.liquidity&&p.liquidity.usd));
  var ch=p.priceChange&&p.priceChange.h24;if(ch!=null){var el=box.querySelector('[data-chg]');if(el){el.textContent=(ch>0?'+':'')+(+ch).toFixed(2)+'%';el.style.color=ch>=0?'#16a34a':'#dc2626'}}
 }).catch(function(){})});
})();

/* fit-text: shrink font so nowrap lines fit their container */
function fitText(root){root=root||document;root.querySelectorAll('h1.stacked .line, [data-fit]').forEach(function(el){
  var box=el.closest('.hero-copy, .hero-inner, .wrap')||el.parentElement;
  var limit=Math.max(120,(box&&box.clientWidth||el.parentElement.clientWidth)-8);
  var max=parseFloat(getComputedStyle(el).fontSize)||48, min=16, lo=min, hi=max, best=min;
  el.style.whiteSpace='nowrap';el.style.display='block';
  for(var i=0;i<14;i++){var mid=(lo+hi)/2;el.style.fontSize=mid+'px';
    if(el.scrollWidth<=limit){best=mid;lo=mid}else hi=mid}
  el.style.fontSize=best+'px'})}
function refit(){fitText()}refit();window.addEventListener('resize',refit);if(document.fonts&&document.fonts.ready)document.fonts.ready.then(refit);window.addEventListener('load',refit);

/* Derive a full page palette from --theme-1/2 when the visitor picked Custom.
   Presets ship hand-tuned --theme-bg/surface/text in CSS. Original mode bails out.
   Chain is not an input. */
(function(){
  var root=document.documentElement;
  var mode=root.getAttribute('data-theme-mode')||'original';
  if(mode!=='custom') return;
  var cs=getComputedStyle(root);
  function parse(h){
    h=String(h||'').trim().replace('#','');
    if(h.length===3)h=h[0]+h[0]+h[1]+h[1]+h[2]+h[2];
    var n=parseInt(h,16);
    if(!isFinite(n)||h.length<6)return {r:136,g:136,b:136};
    return {r:(n>>16)&255,g:(n>>8)&255,b:n&255};
  }
  function luma(c){function f(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)}return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b)}
  function mix(a,b,t){return {r:a.r+(b.r-a.r)*t,g:a.g+(b.g-a.g)*t,b:a.b+(b.b-a.b)*t}}
  function hex(c){function h(v){return ('0'+Math.max(0,Math.min(255,Math.round(v))).toString(16)).slice(-2)}return '#'+h(c.r)+h(c.g)+h(c.b)}
  var A=parse(cs.getPropertyValue('--theme-1'));
  var B=parse(cs.getPropertyValue('--theme-2'));
  var L=luma(A), L2=luma(B);
  var light=(L<0.18 && L2<0.5) || (L>0.78 && L2>0.62);
  var bg,bg2,surface,text,muted;
  if(light){
    bg=hex(mix(A,{r:247,g:246,b:242},0.9));
    bg2=hex(mix(B,{r:255,g:255,b:255},0.78));
    surface='#ffffff';
    text=hex(mix(A,{r:16,g:16,b:16},0.78));
    muted=hex(mix(A,{r:70,g:64,b:58},0.5));
  }else{
    bg=hex(mix(A,{r:9,g:10,b:14},0.84));
    bg2=hex(mix(B,{r:16,g:18,b:24},0.78));
    surface=hex(mix(A,{r:20,g:22,b:30},0.8));
    text='#f4f6fb';
    muted=hex(mix(B,{r:190,g:196,b:208},0.55));
  }
  var ink=L>0.45?'#0a0a0a':'#f6f7fb';
  root.style.setProperty('--theme-bg',bg);
  root.style.setProperty('--theme-bg-2',bg2);
  root.style.setProperty('--theme-surface',surface);
  root.style.setProperty('--theme-text',text);
  root.style.setProperty('--theme-muted',muted);
  root.style.setProperty('--theme-ink',ink);
})();

/* intro-logo force visible after letter anim window */
setTimeout(function(){
  document.querySelectorAll('.intro-logo,.frame-card img').forEach(function(el){
    el.style.opacity='1'; el.style.transform='none'; el.style.animation='none';
  });
}, 1600);
