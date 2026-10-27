/* Offline rich meme generator v3 — bright scenes, fitted captions, dynamic stickers.
   No external APIs. window.MemeGen */
(function(global){
'use strict';

var EMOJI=['🔥','💎','🚀','🌕','💰','👑','✨','👀','📈','🤑','⚡','🎉','🏆','💸','🌟','😎','🐸','🎯'];
var BUBBLES=['LFG','WAGMI','BASED','GM','HODL','MOON','PUMP','NGMI'];
var CAPTIONS=[
  function(n,t){return {a:'WHEN $'+t,b:'HITS DIFFERENT'}},
  function(n,t){return {a:'STILL HOLDING',b:'$'+t}},
  function(n,t){return {a:n.toUpperCase(),b:'SEASON'}},
  function(n,t){return {a:'$'+t,b:'TO THE MOON'}},
  function(n,t){return {a:'NOT FINANCIAL',b:'ADVICE SER'}},
  function(n,t){return {a:'CHART LOOKIN',b:'KINDA NICE'}},
  function(n,t){return {a:'THIS IS $'+t,b:"YOU'RE WELCOME"}},
  function(n,t){return {a:'FEW UNDERSTAND',b:'$'+t}},
  function(n,t){return {a:'WAGMI',b:'$'+t}},
  function(n,t){return {a:'BASED $'+t,b:'ONLY'}},
  function(n,t){return {a:'LIVING ON',b:'$'+t+' VIBES'}},
  function(n,t){return {a:'JOIN THE',b:n.toUpperCase()+' CREW'}}
];
var LAYOUTS=['center','low-left','low-right','peek-left','peek-right','break-bottom','rail-left','rail-right'];

function mulberry32(a){return function(){var t=a+=0x6D2B79F5;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296}}
function pick(rng,arr){return arr[Math.floor(rng()*arr.length)]}
function shuffle(rng,arr){var a=arr.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(rng()*(i+1));var tmp=a[i];a[i]=a[j];a[j]=tmp}return a}
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function hexToRgb(h){h=String(h||'#888').replace('#','');if(h.length===3)h=h[0]+h[0]+h[1]+h[1]+h[2]+h[2];var n=parseInt(h,16);return {r:(n>>16)&255,g:(n>>8)&255,b:n&255}}
function rgbToHex(r,g,b){return '#'+[r,g,b].map(function(x){return ('0'+clamp(x|0,0,255).toString(16)).slice(-2)}).join('')}
function mix(a,b,t){a=hexToRgb(a);b=hexToRgb(b);return rgbToHex(a.r+(b.r-a.r)*t,a.g+(b.g-a.g)*t,a.b+(b.b-a.b)*t)}
function rgba(h,a){var c=hexToRgb(h);return 'rgba('+c.r+','+c.g+','+c.b+','+a+')'}

function extractPalette(logo,banner){
  var cvs=document.createElement('canvas');cvs.width=48;cvs.height=48;var ctx=cvs.getContext('2d',{willReadFrequently:true});
  var cols=[];
  function sample(im){if(!im)return;ctx.clearRect(0,0,48,48);ctx.drawImage(im,0,0,48,48);var d;try{d=ctx.getImageData(0,0,48,48).data}catch(e){return}
    for(var i=0;i<d.length;i+=16){var r=d[i],g=d[i+1],b=d[i+2],a=d[i+3];if(a<200)continue;var mx=Math.max(r,g,b),mn=Math.min(r,g,b);if(mx-mn<20&&mx>220)continue;if(mx<30)continue;cols.push({r:r,g:g,b:b,s:mx-mn})}
  }
  sample(logo);sample(banner);
  if(!cols.length)return {prim:'#FFD21F',sec:'#FF4D8D',acc:'#4CC9F0',dark:'#1B1F4B',light:'#FFF8DC'};
  cols.sort(function(a,b){return b.s-a.s});
  function at(i){var c=cols[Math.min(i,cols.length-1)];return rgbToHex(c.r,c.g,c.b)}
  var prim=at(0),sec=at(Math.floor(cols.length*0.3)),acc=at(Math.floor(cols.length*0.55));
  // if palette collapsed to one hue, inject vivid accent pair so captions/rims stay punchy
  var pr=hexToRgb(prim),sr=hexToRgb(sec);
  var same=Math.abs(pr.r-sr.r)+Math.abs(pr.g-sr.g)+Math.abs(pr.b-sr.b)<40;
  if(same){sec='#FF4D8D';acc='#4CC9F0'}
  return {prim:prim,sec:sec,acc:acc,dark:'#1B1F4B',light:'#FFF8DC'};
}

function lightGrain(ctx,W,H,rng){
  var tw=96,th=96,c=document.createElement('canvas');c.width=tw;c.height=th;var g=c.getContext('2d');
  var id=g.createImageData(tw,th),d=id.data;
  for(var i=0;i<d.length;i+=4){var v=(rng()*255)|0;d[i]=d[i+1]=d[i+2]=v;d[i+3]=18}
  g.putImageData(id,0,0);
  ctx.save();ctx.globalCompositeOperation='soft-light';ctx.globalAlpha=0.35;
  ctx.fillStyle=ctx.createPattern(c,'repeat');ctx.fillRect(0,0,W,H);ctx.restore();
}
function softVignette(ctx,W,H){ /* intentionally empty — keep scenes bright */ }
function halftone(ctx,W,H,color,step){
  ctx.save();ctx.fillStyle=color;step=step||14;
  for(var y=0;y<H;y+=step)for(var x=0;x<W;x+=step){
    var n=0.3+0.5*((Math.sin(x*0.03)+Math.cos(y*0.04)+2)/4);
    ctx.beginPath();ctx.arc(x+(y%(2*step)===0?step/2:0),y,step*0.16*n,0,Math.PI*2);ctx.fill();
  }
  ctx.restore();
}
function sunburst(ctx,W,H,cx,cy,c1,c2,rays){
  rays=rays||20;for(var i=0;i<rays;i++){
    var a0=(i/rays)*Math.PI*2,a1=((i+0.55)/rays)*Math.PI*2;
    ctx.beginPath();ctx.moveTo(cx,cy);ctx.arc(cx,cy,Math.max(W,H)*1.25,a0,a1);ctx.closePath();
    ctx.fillStyle=i%2?c1:c2;ctx.fill();
  }
}
function stars(ctx,W,H,n,rng){
  for(var i=0;i<n;i++){ctx.fillStyle='rgba(255,255,255,'+(0.5+rng()*0.5)+')';
    ctx.beginPath();ctx.arc(rng()*W,rng()*H*0.65,0.8+rng()*2.8,0,Math.PI*2);ctx.fill()}
}
function cloud(ctx,x,y,s,col){
  ctx.fillStyle=col||'rgba(255,255,255,.95)';
  ctx.beginPath();ctx.arc(x,y,s*0.55,0,Math.PI*2);ctx.arc(x+s*0.5,y-s*0.18,s*0.48,0,Math.PI*2);
  ctx.arc(x+s*0.95,y,s*0.55,0,Math.PI*2);ctx.arc(x+s*0.45,y+s*0.22,s*0.42,0,Math.PI*2);ctx.fill();
}
function palm(ctx,x,y,h,col){
  ctx.strokeStyle=col||'#1B4332';ctx.lineWidth=Math.max(8,h*0.07);ctx.lineCap='round';
  ctx.beginPath();ctx.moveTo(x,y);ctx.quadraticCurveTo(x+h*0.1,y-h*0.45,x-h*0.05,y-h);ctx.stroke();
  ctx.fillStyle=mix(col||'#1B4332','#52B788',0.35);
  for(var i=0;i<7;i++){var ang=-Math.PI/2+(i-3)*0.32;
    ctx.beginPath();ctx.moveTo(x-h*0.05,y-h);
    ctx.quadraticCurveTo(x-h*0.05+Math.cos(ang)*h*0.6,y-h+Math.sin(ang)*h*0.4,x-h*0.05+Math.cos(ang)*h*1.05,y-h+Math.sin(ang)*h*0.65);
    ctx.quadraticCurveTo(x-h*0.05+Math.cos(ang)*h*0.45,y-h+Math.sin(ang)*h*0.18,x-h*0.05,y-h);ctx.fill()}
}
function building(ctx,x,base,w,h,col,rng){
  ctx.fillStyle=col;ctx.fillRect(x,base-h,w,h);
  ctx.fillStyle='rgba(0,0,0,0.2)';ctx.fillRect(x+w*0.65,base-h,w*0.35,h);
  // antenna
  if(h>160&&rng()>0.5){ctx.strokeStyle='#FFD60A';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x+w/2,base-h);ctx.lineTo(x+w/2,base-h-30);ctx.stroke();
    ctx.fillStyle='#FF4D6D';ctx.beginPath();ctx.arc(x+w/2,base-h-30,4,0,Math.PI*2);ctx.fill()}
  var rows=Math.max(4,(h/22)|0),cols=Math.max(2,(w/16)|0);
  for(var r=0;r<rows;r++)for(var c=0;c<cols;c++){
    if(rng()>0.55)continue;
    ctx.fillStyle=rng()>0.3?pick(rng,['#FFE566','#90E0EF','#FF70A6','#C77DFF']):'rgba(20,20,40,0.5)';
    ctx.fillRect(x+5+c*((w-8)/cols),base-h+8+r*((h-14)/rows),Math.max(4,(w-8)/cols-5),Math.max(5,(h-14)/rows-5));
  }
}
function roundPath(ctx,x,y,w,h,r){ctx.moveTo(x+r,y);ctx.arcTo(x+w,y,x+w,y+h,r);ctx.arcTo(x+w,y+h,x,y+h,r);ctx.arcTo(x,y+h,x,y,r);ctx.arcTo(x,y,x+w,y,r);ctx.closePath()}

/* ===== Bright, distinct scenes (natural colors; palette unused for wash) ===== */
var SCENES=[
  {id:'comic-sunburst',draw:function(ctx,W,H,p,rng){
    sunburst(ctx,W,H,W*0.5,H*0.35,'#FFF3A0','#FFB703',24);
    var g=ctx.createRadialGradient(W/2,H*0.35,30,W/2,H*0.35,Math.max(W,H)*0.75);
    g.addColorStop(0,'rgba(255,255,255,0.7)');g.addColorStop(0.45,'rgba(255,214,10,0.2)');g.addColorStop(1,'rgba(255,107,53,0.35)');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    cloud(ctx,W*0.06,H*0.14,150,'#fff');cloud(ctx,W*0.68,H*0.1,170,'#fff');cloud(ctx,W*0.38,H*0.06,110,'rgba(255,255,255,0.9)');
    // bright comic ground
    ctx.fillStyle='#FF8FAB';ctx.fillRect(0,H*0.68,W,H*0.32);
    ctx.fillStyle='#FFD6A5';ctx.beginPath();ctx.ellipse(W*0.3,H*0.76,200,50,0,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#FFC2D1';ctx.beginPath();ctx.ellipse(W*0.72,H*0.84,240,55,0,0,Math.PI*2);ctx.fill();
    // POW star
    ctx.fillStyle='#FF006E';ctx.beginPath();
    for(var i=0;i<8;i++){var a=-Math.PI/2+i*Math.PI/4,r=i%2?40:90;var px=W*0.82+Math.cos(a)*r,py=H*0.55+Math.sin(a)*r;i?ctx.lineTo(px,py):ctx.moveTo(px,py)}
    ctx.closePath();ctx.fill();
  }},
  {id:'neon-city',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#0B1026');g.addColorStop(0.4,'#3A0CA3');g.addColorStop(0.7,'#7209B7');g.addColorStop(1,'#F72585');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);stars(ctx,W,H,70,rng);
    // big moon
    ctx.beginPath();ctx.arc(W*0.82,H*0.18,70,0,Math.PI*2);ctx.fillStyle='#F8F7FF';ctx.shadowColor='#C77DFF';ctx.shadowBlur=30;ctx.fill();ctx.shadowBlur=0;
    ctx.beginPath();ctx.arc(W*0.85,H*0.15,55,0,Math.PI*2);ctx.fillStyle='#3A0CA3';ctx.fill();
    var base=H*0.7,xs=0;
    var heights=[0.62,0.42,0.78,0.5,0.7,0.45,0.66,0.38,0.8,0.55,0.48,0.72];
    for(var i=0;i<heights.length;i++){var bw=W*0.09,bh=H*heights[i];building(ctx,xs,base,bw,bh,pick(rng,['#1A1A2E','#16213E','#0F3460','#1B1F4B']),rng);xs+=bw+4}
    // neon strip
    ctx.fillStyle='#00F5D4';ctx.shadowColor='#00F5D4';ctx.shadowBlur=20;ctx.fillRect(0,base,W,8);ctx.shadowBlur=0;
    ctx.fillStyle='#0A0A12';ctx.fillRect(0,base+8,W,H-base);
    // reflections
    ctx.globalAlpha=0.3;for(var r=0;r<8;r++){ctx.fillStyle=pick(rng,['#F72585','#00F5D4','#FFE566']);ctx.fillRect(rng()*W,base+20+rng()*60,4+rng()*20,3)}
    ctx.globalAlpha=1;
  }},
  {id:'tropical-beach',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#48CAE4');g.addColorStop(0.35,'#90E0EF');g.addColorStop(0.55,'#FFD166');g.addColorStop(0.72,'#FF9F1C');g.addColorStop(1,'#F4A261');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    // big sun
    ctx.beginPath();ctx.arc(W*0.78,H*0.26,120,0,Math.PI*2);ctx.fillStyle='#FFDD00';ctx.shadowColor='#FF9F1C';ctx.shadowBlur=50;ctx.fill();ctx.shadowBlur=0;
    cloud(ctx,W*0.08,H*0.14,170,'#fff');cloud(ctx,W*0.42,H*0.08,130,'rgba(255,255,255,0.95)');
    // ocean bands
    ctx.fillStyle='#0077B6';ctx.fillRect(0,H*0.55,W,H*0.2);
    ctx.fillStyle='#00B4D8';ctx.beginPath();
    for(var x=0;x<=W;x+=10)ctx.lineTo(x,H*0.55+Math.sin(x/50)*16);ctx.lineTo(W,H*0.75);ctx.lineTo(0,H*0.75);ctx.fill();
    ctx.fillStyle='#CAF0F8';for(var i=0;i<30;i++){ctx.beginPath();ctx.arc(rng()*W,H*0.58+rng()*40,2+rng()*5,0,Math.PI*2);ctx.fill()}
    // sand
    ctx.fillStyle='#FFE8A3';ctx.fillRect(0,H*0.72,W,H*0.28);
    palm(ctx,W*0.08,H*0.98,H*0.7,'#1B4332');palm(ctx,W*0.92,H*0.99,H*0.75,'#2D6A4F');palm(ctx,W*0.78,H*0.96,H*0.5,'#40916C');
  }},
  {id:'outer-space',draw:function(ctx,W,H,p,rng){
    var g=ctx.createRadialGradient(W*0.4,H*0.35,10,W*0.5,H*0.5,Math.max(W,H)*0.85);
    g.addColorStop(0,'#7B2CBF');g.addColorStop(0.35,'#3C096C');g.addColorStop(0.7,'#10002B');g.addColorStop(1,'#000000');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    // nebulae
    for(var i=0;i<4;i++){var nx=rng()*W,ny=rng()*H*0.6,nr=100+rng()*180;
      var ng=ctx.createRadialGradient(nx,ny,0,nx,ny,nr);ng.addColorStop(0,rgba(pick(rng,['#FF70A6','#C77DFF','#4CC9F0','#FFD60A']),0.5));ng.addColorStop(1,'rgba(0,0,0,0)');
      ctx.fillStyle=ng;ctx.fillRect(0,0,W,H)}
    stars(ctx,W,H,180,rng);
    // big planet
    var px=W*0.75,py=H*0.3,pr=110;
    var pg=ctx.createRadialGradient(px-30,py-30,10,px,py,pr);pg.addColorStop(0,'#90E0EF');pg.addColorStop(0.5,'#0077B6');pg.addColorStop(1,'#023E8A');
    ctx.beginPath();ctx.arc(px,py,pr,0,Math.PI*2);ctx.fillStyle=pg;ctx.fill();
    ctx.strokeStyle='rgba(255,214,10,0.7)';ctx.lineWidth=10;ctx.beginPath();ctx.ellipse(px,py,pr*1.45,pr*0.35,0.35,0,Math.PI*2);ctx.stroke();
    // small planet
    ctx.beginPath();ctx.arc(W*0.18,H*0.22,45,0,Math.PI*2);ctx.fillStyle='#FF70A6';ctx.fill();
  }},
  {id:'moon-surface',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#020617');g.addColorStop(0.45,'#1E293B');g.addColorStop(1,'#94A3B8');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);stars(ctx,W,H,100,rng);
    // BIG Earth
    ctx.beginPath();ctx.arc(W*0.7,H*0.2,140,0,Math.PI*2);ctx.fillStyle='#1D3557';ctx.shadowColor='#4CC9F0';ctx.shadowBlur=40;ctx.fill();ctx.shadowBlur=0;
    ctx.fillStyle='#52B788';ctx.beginPath();ctx.ellipse(W*0.64,H*0.14,55,38,0.4,0,Math.PI*2);ctx.fill();
    ctx.beginPath();ctx.ellipse(W*0.78,H*0.28,48,32,-0.3,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#48CAE4';ctx.beginPath();ctx.ellipse(W*0.72,H*0.2,80,58,0,0,Math.PI*2);ctx.globalAlpha=0.35;ctx.fill();ctx.globalAlpha=1;
    // rocket
    ctx.fillStyle='#E9ECEF';ctx.fillRect(W*0.2,H*0.28,28,70);ctx.fillStyle='#F72585';ctx.beginPath();ctx.moveTo(W*0.2,H*0.28);ctx.lineTo(W*0.214+14,H*0.18);ctx.lineTo(W*0.228+28,H*0.28);ctx.fill();
    ctx.fillStyle='#FF9F1C';ctx.beginPath();ctx.moveTo(W*0.2,H*0.98-H*0.62);ctx.lineTo(W*0.214+14,H*0.42);ctx.lineTo(W*0.228+28,H*0.98-H*0.62);ctx.fill();
    // moon ground — big craters
    ctx.fillStyle='#CBD5E1';ctx.beginPath();ctx.moveTo(0,H*0.52);ctx.quadraticCurveTo(W*0.35,H*0.42,W*0.6,H*0.55);ctx.quadraticCurveTo(W*0.85,H*0.68,W,H*0.5);ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.fill();
    for(var i=0;i<12;i++){var cx=rng()*W,cy=H*0.58+rng()*H*0.35,cr=20+rng()*55;
      ctx.beginPath();ctx.arc(cx,cy,cr,0,Math.PI*2);ctx.fillStyle='rgba(100,116,139,0.45)';ctx.fill();
      ctx.beginPath();ctx.arc(cx-cr*0.2,cy-cr*0.2,cr*0.55,0,Math.PI*2);ctx.fillStyle='rgba(148,163,184,0.4)';ctx.fill()}
  }},
  {id:'candlestick-pump',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#0B132B');g.addColorStop(1,'#1C2541');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(76,201,240,0.25)';ctx.lineWidth=1.5;
    for(var x=0;x<W;x+=50){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}
    for(var y=0;y<H;y+=50){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
    var n=12,bw=(W*0.82)/n,price=H*0.62;
    for(var i=0;i<n;i++){var up=i>n-5||rng()>0.3;var body=35+rng()*90;var wick=15+rng()*50;
      var cx=W*0.09+i*bw+bw*0.5;price+=up?-(20+rng()*30):(10+rng()*20);price=clamp(price,H*0.18,H*0.7);
      ctx.strokeStyle=up?'#00F5A0':'#FF4D6D';ctx.fillStyle=up?'#00F5A0':'#FF4D6D';
      ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(cx,price-wick);ctx.lineTo(cx,price+body+wick);ctx.stroke();
      ctx.fillRect(cx-bw*0.32,price,bw*0.64,body)}
    // big green arrow
    ctx.fillStyle='#00F5A0';ctx.shadowColor='#00F5A0';ctx.shadowBlur=25;
    ctx.beginPath();ctx.moveTo(W*0.88,H*0.18);ctx.lineTo(W*0.96,H*0.32);ctx.lineTo(W*0.91,H*0.32);ctx.lineTo(W*0.91,H*0.48);ctx.lineTo(W*0.85,H*0.48);ctx.lineTo(W*0.85,H*0.32);ctx.lineTo(W*0.8,H*0.32);ctx.closePath();ctx.fill();
    ctx.shadowBlur=0;ctx.font='900 48px system-ui';ctx.fillText('+420%',W*0.72,H*0.2);
  }},
  {id:'money-rain',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#D8F3DC');g.addColorStop(0.5,'#95D5B2');g.addColorStop(1,'#2D6A4F');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    for(var i=0;i<40;i++){
      var x=rng()*W,y=rng()*H,s=28+rng()*50,rot=(rng()-0.5)*0.9;
      ctx.save();ctx.translate(x,y);ctx.rotate(rot);
      if(rng()>0.4){ctx.fillStyle='#40916C';ctx.fillRect(-s*0.75,-s*0.4,s*1.5,s*0.8);ctx.strokeStyle='#fff';ctx.lineWidth=3;ctx.strokeRect(-s*0.75,-s*0.4,s*1.5,s*0.8);
        ctx.fillStyle='#fff';ctx.font='bold '+(s*0.5|0)+'px serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('$',0,0);
      } else {ctx.beginPath();ctx.arc(0,0,s*0.45,0,Math.PI*2);ctx.fillStyle='#FFD60A';ctx.fill();ctx.lineWidth=4;ctx.strokeStyle='#E09F3E';ctx.stroke();
        ctx.fillStyle='#7F5539';ctx.font='bold '+(s*0.4|0)+'px serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('$',0,1)}
      ctx.restore();
    }
  }},
  {id:'casino-lights',draw:function(ctx,W,H,p,rng){
    var g=ctx.createRadialGradient(W/2,H*0.25,10,W/2,H/2,Math.max(W,H)*0.75);
    g.addColorStop(0,'#FFE566');g.addColorStop(0.35,'#F72585');g.addColorStop(1,'#1A000F');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    for(var i=0;i<36;i++){var a=(i/36)*Math.PI*2,r=Math.min(W,H)*0.36;var x=W/2+Math.cos(a)*r,y=H*0.38+Math.sin(a)*r*0.65;
      ctx.beginPath();ctx.arc(x,y,8+rng()*5,0,Math.PI*2);ctx.fillStyle=pick(rng,['#FFE566','#FF4D6D','#fff','#4CC9F0']);ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=14;ctx.fill()}
    ctx.shadowBlur=0;
    for(var j=0;j<10;j++){ctx.fillStyle=j%2?'#1A000F':'#F72585';ctx.fillRect(0,H*0.72+j*14,W,14)}
    for(var k=0;k<6;k++){ctx.save();ctx.translate(W*(0.12+k*0.14),H*0.82);ctx.rotate((k-2.5)*0.12);
      ctx.fillStyle='#fff';ctx.fillRect(-42,-60,84,120);ctx.strokeStyle='#1B1F4B';ctx.lineWidth=4;ctx.strokeRect(-42,-60,84,120);
      ctx.fillStyle=k%2?'#E63946':'#1D3557';ctx.font='900 36px serif';ctx.textAlign='center';ctx.fillText(pick(rng,['A','K','Q','J','10','$']),0,8);ctx.restore()}
  }},
  {id:'tokyo-street',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#12002A');g.addColorStop(0.45,'#3A0CA3');g.addColorStop(1,'#F72585');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(200,240,255,0.45)';ctx.lineWidth=2;
    for(var i=0;i<80;i++){var x=rng()*W,y=rng()*H;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x-5,y+32);ctx.stroke()}
    var signs=[{t:'OPEN 24H',c:'#F72585'},{t:'BUY NOW',c:'#00F5D4'},{t:'NEON',c:'#FF70A6'},{t:'TOKEN',c:'#FFE566'},{t:'WAGMI',c:'#C77DFF'},{t:'LFG',c:'#4CC9F0'}];
    for(var s=0;s<signs.length;s++){var sx=20+s*((W-40)/signs.length),sy=40+(s%3)*70,sw=130+rng()*30,sh=56;
      ctx.fillStyle=signs[s].c;ctx.shadowColor=signs[s].c;ctx.shadowBlur=28;ctx.fillRect(sx,sy,sw,sh);ctx.shadowBlur=0;
      ctx.fillStyle='#0A0A12';ctx.font='900 26px system-ui';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(signs[s].t,sx+sw/2,sy+sh/2)}
    ctx.fillStyle='#0A0A12';ctx.fillRect(0,H*0.65,W,H*0.35);
    ctx.strokeStyle='#FFE566';ctx.setLineDash([44,28]);ctx.lineWidth=10;ctx.beginPath();ctx.moveTo(0,H*0.82);ctx.lineTo(W,H*0.82);ctx.stroke();ctx.setLineDash([]);
    var pud=ctx.createLinearGradient(0,H*0.65,0,H);pud.addColorStop(0,'rgba(247,37,133,0.45)');pud.addColorStop(1,'rgba(0,245,212,0.25)');
    ctx.fillStyle=pud;ctx.fillRect(0,H*0.65,W,H*0.35);
  }},
  {id:'mountain-summit',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#89C2D9');g.addColorStop(0.4,'#E0FBFC');g.addColorStop(0.7,'#F4A261');g.addColorStop(1,'#E76F51');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    // sun
    ctx.beginPath();ctx.arc(W*0.2,H*0.22,70,0,Math.PI*2);ctx.fillStyle='#FFE566';ctx.shadowColor='#FF9F1C';ctx.shadowBlur=35;ctx.fill();ctx.shadowBlur=0;
    cloud(ctx,W*0.35,H*0.2,140,'#fff');cloud(ctx,W*0.7,H*0.14,160,'rgba(255,255,255,0.9)');cloud(ctx,W*0.15,H*0.35,100,'rgba(255,255,255,0.75)');
    // big peaks
    ctx.fillStyle='#3D405B';ctx.beginPath();ctx.moveTo(0,H);ctx.lineTo(W*0.2,H*0.35);ctx.lineTo(W*0.4,H*0.55);ctx.lineTo(W*0.55,H*0.28);ctx.lineTo(W*0.75,H*0.5);ctx.lineTo(W,H*0.38);ctx.lineTo(W,H);ctx.fill();
    ctx.fillStyle='#2B2D42';ctx.beginPath();ctx.moveTo(0,H);ctx.lineTo(W*0.15,H*0.5);ctx.lineTo(W*0.35,H*0.38);ctx.lineTo(W*0.55,H*0.58);ctx.lineTo(W*0.8,H*0.42);ctx.lineTo(W,H*0.55);ctx.lineTo(W,H);ctx.fill();
    // snow caps
    ctx.fillStyle='#fff';ctx.beginPath();ctx.moveTo(W*0.5,H*0.28);ctx.lineTo(W*0.55,H*0.38);ctx.lineTo(W*0.6,H*0.32);ctx.closePath();ctx.fill();
    ctx.beginPath();ctx.moveTo(W*0.18,H*0.35);ctx.lineTo(W*0.22,H*0.42);ctx.lineTo(W*0.26,H*0.38);ctx.closePath();ctx.fill();
  }},
  {id:'vaporwave-sun',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#240046');g.addColorStop(0.4,'#FF006E');g.addColorStop(0.55,'#FFBE0B');g.addColorStop(1,'#3A0CA3');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    // BIG banded sun
    var R=Math.min(W,H)*0.32;
    ctx.beginPath();ctx.arc(W/2,H*0.4,R,0,Math.PI*2);ctx.fillStyle='#FF4D6D';ctx.fill();
    ctx.save();ctx.beginPath();ctx.arc(W/2,H*0.4,R,0,Math.PI*2);ctx.clip();
    for(var i=0;i<14;i++){ctx.fillStyle=i%2?'rgba(255,255,255,0.2)':'rgba(255,0,110,0.35)';ctx.fillRect(0,H*0.25+i*22,W,12)}
    ctx.restore();
    stars(ctx,W,H*0.5,50,rng);
    // perspective grid
    var horizon=H*0.55;ctx.strokeStyle='rgba(76,201,240,0.85)';ctx.lineWidth=2.5;
    for(var k=1;k<18;k++){var y=horizon+Math.pow(k/18,1.5)*(H-horizon);ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
    for(var x=-12;x<=24;x++){ctx.beginPath();ctx.moveTo(W/2,horizon);ctx.lineTo(W/2+(x-6)*W*0.1,H);ctx.stroke()}
  }},
  {id:'cyberpunk-alley',draw:function(ctx,W,H,p,rng){
    ctx.fillStyle='#06060C';ctx.fillRect(0,0,W,H);
    ctx.fillStyle='#1A1A2E';ctx.fillRect(0,0,W*0.26,H);ctx.fillRect(W*0.74,0,W*0.26,H);
    // big neon panels
    var cols=['#F72585','#00F5D4','#FFE566','#C77DFF','#4CC9F0'];
    for(var i=0;i<6;i++){ctx.fillStyle=cols[i%cols.length];ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=28;
      var left=rng()>0.5;ctx.fillRect(left?W*0.04:W*0.78,50+i*85,W*0.18,36+rng()*20)}
    ctx.shadowBlur=0;
    ctx.fillStyle='#0A0A12';ctx.fillRect(W*0.26,H*0.62,W*0.48,H*0.38);
    var pud=ctx.createLinearGradient(0,H*0.62,0,H);pud.addColorStop(0,'rgba(247,37,133,0.4)');pud.addColorStop(1,'rgba(0,245,212,0.2)');
    ctx.fillStyle=pud;ctx.fillRect(W*0.26,H*0.62,W*0.48,H*0.38);
    ctx.strokeStyle='rgba(200,230,255,0.3)';for(var r=0;r<70;r++){var x=rng()*W,y=rng()*H;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x-5,y+26);ctx.stroke()}
  }},
  {id:'party-confetti',draw:function(ctx,W,H,p,rng){
    var g=ctx.createRadialGradient(W/2,H*0.15,10,W/2,H,Math.max(W,H));
    g.addColorStop(0,'#FFF0F3');g.addColorStop(0.35,'#FF70A6');g.addColorStop(0.7,'#C77DFF');g.addColorStop(1,'#3A0CA3');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    for(var i=0;i<4;i++){var sx=W*(0.15+i*0.23);ctx.beginPath();ctx.moveTo(sx,0);ctx.lineTo(sx-100,H);ctx.lineTo(sx+100,H);ctx.closePath();
      var lg=ctx.createLinearGradient(sx,0,sx,H);lg.addColorStop(0,rgba(pick(rng,['#FFE566','#00F5D4','#FF4D6D','#4CC9F0']),0.5));lg.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=lg;ctx.fill()}
    for(var c=0;c<110;c++){ctx.save();ctx.translate(rng()*W,rng()*H);ctx.rotate(rng()*Math.PI);
      ctx.fillStyle=pick(rng,['#FFE566','#FF4D6D','#00F5D4','#C77DFF','#fff','#4CC9F0']);
      if(rng()>0.5)ctx.fillRect(-8,-4,16,8);else{ctx.beginPath();ctx.arc(0,0,5,0,Math.PI*2);ctx.fill()}
      ctx.restore()}
    ctx.fillStyle='#1B1F4B';ctx.fillRect(0,H*0.78,W,H*0.22);ctx.fillStyle='#FFE566';ctx.fillRect(0,H*0.78,W,10);
  }},
  {id:'desert-road',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#48CAE4');g.addColorStop(0.35,'#FFD166');g.addColorStop(0.65,'#FB8500');g.addColorStop(1,'#BC6C25');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.beginPath();ctx.arc(W*0.7,H*0.25,80,0,Math.PI*2);ctx.fillStyle='#FFE566';ctx.shadowColor='#FB8500';ctx.shadowBlur=40;ctx.fill();ctx.shadowBlur=0;
    // dunes
    ctx.fillStyle='#E9C46A';ctx.beginPath();ctx.moveTo(0,H*0.5);ctx.quadraticCurveTo(W*0.3,H*0.4,W*0.55,H*0.55);ctx.quadraticCurveTo(W*0.8,H*0.68,W,H*0.5);ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.fill();
    // BIG road
    ctx.fillStyle='#2B2D42';ctx.beginPath();ctx.moveTo(W*0.4,H*0.52);ctx.lineTo(W*0.6,H*0.52);ctx.lineTo(W*0.98,H);ctx.lineTo(W*0.02,H);ctx.closePath();ctx.fill();
    ctx.strokeStyle='#FFE566';ctx.setLineDash([28,32]);ctx.lineWidth=8;ctx.beginPath();ctx.moveTo(W/2,H*0.52);ctx.lineTo(W/2,H);ctx.stroke();ctx.setLineDash([]);
    // cactus
    ctx.fillStyle='#2D6A4F';ctx.fillRect(W*0.15,H*0.45,22,H*0.25);ctx.fillRect(W*0.08,H*0.52,18,12);ctx.fillRect(W*0.08,H*0.52,12,60);
    ctx.fillRect(W*0.85,H*0.5,18,H*0.2);ctx.fillRect(W*0.9,H*0.55,14,10);ctx.fillRect(W*0.9,H*0.55,10,45);
  }},
  {id:'underwater',draw:function(ctx,W,H,p,rng){
    var g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#90E0EF');g.addColorStop(0.4,'#00B4D8');g.addColorStop(0.75,'#0077B6');g.addColorStop(1,'#023E8A');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    for(var i=0;i<8;i++){ctx.beginPath();ctx.moveTo(W*0.25+i*50,0);ctx.lineTo(W*0.05+i*70,H);ctx.lineTo(W*0.18+i*70,H);ctx.closePath();
      ctx.fillStyle='rgba(255,255,255,'+(0.05+rng()*0.05)+')';ctx.fill()}
    ctx.strokeStyle='rgba(255,255,255,0.55)';ctx.lineWidth=2.5;
    for(var b=0;b<40;b++){var x=rng()*W,y=rng()*H,r=4+rng()*18;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.stroke();ctx.fillStyle='rgba(255,255,255,0.1)';ctx.fill()}
    // seaweed
    for(var s=0;s<10;s++){var sx=30+s*(W/10);ctx.strokeStyle=pick(rng,['#2D6A4F','#F72585','#FF9F1C','#52B788']);ctx.lineWidth=6;ctx.beginPath();ctx.moveTo(sx,H);
      for(var y=H;y>H*0.5;y-=25)ctx.quadraticCurveTo(sx+(rng()-0.5)*40,y-12,sx+(rng()-0.5)*25,y-25);ctx.stroke()}
    // fish
    for(var f=0;f<7;f++){var fx=rng()*W,fy=H*0.2+rng()*H*0.4;ctx.fillStyle=pick(rng,['#FFE566','#FF70A6','#00F5D4']);
      ctx.beginPath();ctx.ellipse(fx,fy,24,12,0,0,Math.PI*2);ctx.fill();ctx.beginPath();ctx.moveTo(fx-24,fy);ctx.lineTo(fx-40,fy-12);ctx.lineTo(fx-40,fy+12);ctx.fill()}
  }},
  {id:'banner-blur',draw:function(ctx,W,H,p,rng,banner){
    if(banner){ctx.save();ctx.filter='blur(14px) saturate(1.4) brightness(1.1)';
      var s=Math.max(W/banner.width,H/banner.height)*1.2;var nw=banner.width*s,nh=banner.height*s;
      ctx.drawImage(banner,(W-nw)/2,(H-nh)/2,nw,nh);ctx.restore();
      ctx.fillStyle='rgba(255,255,255,0.12)';ctx.fillRect(0,0,W,H);
    } else {var g=ctx.createLinearGradient(0,0,W,H);g.addColorStop(0,'#4CC9F0');g.addColorStop(0.5,'#F72585');g.addColorStop(1,'#FFE566');ctx.fillStyle=g;ctx.fillRect(0,0,W,H)}
    sunburst(ctx,W,H,W/2,H/2,'rgba(255,255,255,0.12)','rgba(255,255,255,0.04)',18);
    halftone(ctx,W,H,'rgba(0,0,0,0.08)',14);
  }}
];

/* ===== Caption fitting: measure, shrink, wrap to 2 lines, never clip ===== */
function fontSpec(size){return '900 '+size+'px Impact, Haettenschweiler, "Arial Black", "Franklin Gothic Heavy", system-ui, sans-serif'}
function wrapTwoLines(ctx,text,maxW){
  text=String(text||'').toUpperCase().trim();
  if(ctx.measureText(text).width<=maxW)return [text];
  var words=text.split(/\s+/),best=null;
  // try every split point
  for(var i=1;i<words.length;i++){
    var a=words.slice(0,i).join(' '),b=words.slice(i).join(' ');
    if(ctx.measureText(a).width<=maxW&&ctx.measureText(b).width<=maxW){
      var score=Math.abs(ctx.measureText(a).width-ctx.measureText(b).width);
      if(!best||score<best.s)best={a:a,b:b,s:score};
    }
  }
  if(best)return [best.a,best.b];
  // hard wrap mid-word if needed
  if(words.length===1){var mid=Math.ceil(text.length/2);return [text.slice(0,mid)+'-',text.slice(mid)]}
  // fallback: put as many words on line1 as fit
  var l1='',l2='';
  for(var j=0;j<words.length;j++){var trial=l1?(l1+' '+words[j]):words[j];
    if(ctx.measureText(trial).width<=maxW&&!l2)l1=trial;else l2=l2?(l2+' '+words[j]):words[j]}
  if(!l1)l1=words[0];
  return l2?[l1,l2]:[l1];
}
function fitCaption(ctx,text,maxW,maxSize,minSize){
  text=String(text||'').toUpperCase();
  maxSize=maxSize||72;minSize=minSize||22;maxW=maxW||400;
  var size=maxSize,lines;
  while(size>=minSize){
    ctx.font=fontSpec(size);
    lines=wrapTwoLines(ctx,text,maxW);
    var ok=lines.every(function(ln){return ctx.measureText(ln).width<=maxW+0.5});
    if(ok)break;size-=2;
  }
  ctx.font=fontSpec(size);
  lines=wrapTwoLines(ctx,text,maxW);
  // final shrink if still over
  while(size>minSize&&lines.some(function(ln){return ctx.measureText(ln).width>maxW})){size-=2;ctx.font=fontSpec(size);lines=wrapTwoLines(ctx,text,maxW)}
  var widths=lines.map(function(ln){return ctx.measureText(ln).width});
  var lineH=size*1.05;
  return {lines:lines,size:size,width:Math.max.apply(null,widths),height:lineH*lines.length,lineH:lineH};
}
function drawFittedCaption(ctx,text,cx,cy,opts){
  opts=opts||{};
  var margin=opts.margin||36, W=opts.W, H=opts.H;
  // reserve room for stroke/glow bleed on both axes
  var strokeBudget=Math.max(14, Math.floor(Math.min(W,H)*0.018));
  var maxW=opts.maxW||(W-margin*2-strokeBudget*2);
  var fit=fitCaption(ctx,text,maxW,opts.maxSize||Math.floor(Math.min(W,H)*0.075),opts.minSize||20);
  var glowW=Math.max(8,fit.size/5), strokeW=Math.max(5,fit.size/7);
  var bleed=glowW/2+4;
  var ascent=fit.size*0.55+bleed, descent=fit.size*0.5+bleed;
  var startY=-((fit.lines.length-1)*fit.lineH)/2;
  var topExt=-startY+ascent, botExt=startY+(fit.lines.length-1)*fit.lineH+descent;
  var sidePad=margin+bleed;
  cy=clamp(cy,sidePad+topExt,H-sidePad-botExt);
  cx=clamp(cx,sidePad+fit.width/2,W-sidePad-fit.width/2);
  // tiny tilt only — large rotations clip corners
  var rot=clamp(opts.rot||0,-0.03,0.03);
  ctx.save();ctx.translate(cx,cy);ctx.rotate(rot);ctx.textAlign='center';ctx.textBaseline='middle';ctx.lineJoin='round';
  ctx.font=fontSpec(fit.size);
  var bounds={left:Infinity,right:-Infinity,top:Infinity,bottom:-Infinity};
  for(var i=0;i<fit.lines.length;i++){
    var ln=fit.lines[i],y=startY+i*fit.lineH,w=ctx.measureText(ln).width;
    ctx.fillStyle='rgba(0,0,0,0.35)';ctx.fillText(ln,3,y+4);
    ctx.lineWidth=glowW;ctx.strokeStyle=opts.glow||'rgba(255,80,140,0.3)';ctx.strokeText(ln,0,y);
    ctx.lineWidth=strokeW;ctx.strokeStyle=opts.stroke||'#12081F';ctx.strokeText(ln,0,y);
    var g=ctx.createLinearGradient(0,y-fit.size/2,0,y+fit.size/2);
    g.addColorStop(0,opts.fill1||'#FFFFFF');g.addColorStop(0.55,opts.fill2||'#FFE566');g.addColorStop(1,opts.fill3||'#FF9F1C');
    ctx.fillStyle=g;ctx.fillText(ln,0,y);
    bounds.left=Math.min(bounds.left,cx-w/2-bleed);bounds.right=Math.max(bounds.right,cx+w/2+bleed);
    bounds.top=Math.min(bounds.top,cy+y-ascent);bounds.bottom=Math.max(bounds.bottom,cy+y+descent);
  }
  ctx.restore();
  return {fit:fit,bounds:bounds,cx:cx,cy:cy};
}

function drawSticker(ctx,img,x,y,size,rot,opts){
  if(!img||!img.width)return;opts=opts||{};
  var pad=opts.pad||24, rim=opts.rim||8, shape=opts.shape||'round';
  var S=Math.ceil(size+pad*2+rim*2+48);
  var off=document.createElement('canvas');off.width=S;off.height=S;var o=off.getContext('2d');
  var cx=S/2,cy=S/2;
  if(opts.glow){
    o.save();o.shadowColor=opts.glow;o.shadowBlur=42;o.globalAlpha=0.9;
    o.beginPath();
    if(shape==='round')o.arc(cx,cy,size/2+pad+6,0,Math.PI*2);
    else roundPath(o,cx-size/2-pad-6,cy-size/2-pad-6,size+pad*2+12,size+pad*2+12,36);
    o.fillStyle=opts.glow;o.fill();o.restore();
  }
  o.save();o.shadowColor='rgba(0,0,0,0.5)';o.shadowBlur=28;o.shadowOffsetY=18;
  o.beginPath();
  if(shape==='round')o.arc(cx,cy,size/2+pad,0,Math.PI*2);
  else roundPath(o,cx-size/2-pad,cy-size/2-pad,size+pad*2,size+pad*2,32);
  o.fillStyle='#fff';o.fill();o.restore();
  o.beginPath();
  if(shape==='round')o.arc(cx,cy,size/2+pad,0,Math.PI*2);
  else roundPath(o,cx-size/2-pad,cy-size/2-pad,size+pad*2,size+pad*2,32);
  o.lineWidth=rim;o.strokeStyle=opts.rimColor||'#1B1F4B';o.stroke();
  // accent rim (token palette)
  if(opts.accent){o.beginPath();
    if(shape==='round')o.arc(cx,cy,size/2+pad+4,0,Math.PI*2);
    else roundPath(o,cx-size/2-pad-4,cy-size/2-pad-4,size+pad*2+8,size+pad*2+8,34);
    o.strokeStyle=opts.accent;o.lineWidth=5;o.stroke()}
  o.save();o.beginPath();
  if(shape==='round')o.arc(cx,cy,size/2,0,Math.PI*2);
  else roundPath(o,cx-size/2,cy-size/2,size,size,26);
  o.clip();
  var sc=Math.max(size/img.width,size/img.height);var nw=img.width*sc,nh=img.height*sc;
  o.drawImage(img,cx-nw/2,cy-nh/2,nw,nh);
  var hg=o.createRadialGradient(cx-size*0.25,cy-size*0.3,size*0.05,cx,cy,size*0.7);
  hg.addColorStop(0,'rgba(255,255,255,0.3)');hg.addColorStop(1,'rgba(255,255,255,0)');
  o.fillStyle=hg;o.fillRect(cx-size/2,cy-size/2,size,size);o.restore();
  ctx.save();ctx.translate(x,y);ctx.rotate(rot||0);ctx.drawImage(off,-S/2,-S/2);ctx.restore();
}
function speechBubble(ctx,x,y,text,scale){
  scale=scale||1;text=String(text||'').toUpperCase();
  var fs=30*scale;ctx.save();ctx.font='900 '+fs+'px Impact, "Arial Black", system-ui';
  var tw=ctx.measureText(text).width;var w=Math.max(160*scale,tw+48*scale),h=78*scale;
  // keep bubble on-canvas
  if(x+w>ctx.canvas.width-12)x=ctx.canvas.width-12-w;
  if(x<12)x=12;
  if(y<12)y=12;
  ctx.shadowColor='rgba(0,0,0,.35)';ctx.shadowBlur=14;ctx.shadowOffsetY=6;
  ctx.beginPath();roundPath(ctx,x,y,w,h,22*scale);ctx.fillStyle='#fff';ctx.fill();
  ctx.shadowBlur=0;ctx.beginPath();ctx.moveTo(x+w*0.28,y+h);ctx.lineTo(x+w*0.18,y+h+30*scale);ctx.lineTo(x+w*0.48,y+h);ctx.fill();
  ctx.lineWidth=5*scale;ctx.strokeStyle='#1B1F4B';ctx.beginPath();roundPath(ctx,x,y,w,h,22*scale);ctx.stroke();
  ctx.fillStyle='#1B1F4B';ctx.font='900 '+fs+'px Impact, "Arial Black", system-ui';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.fillText(text,x+w/2,y+h/2);ctx.restore();
}
function badgeStamp(ctx,x,y,label,color,rng){
  ctx.save();ctx.translate(x,y);ctx.rotate((rng()-0.5)*0.28);
  ctx.beginPath();ctx.arc(0,0,88,0,Math.PI*2);ctx.fillStyle=color||'#F72585';ctx.fill();
  ctx.lineWidth=7;ctx.strokeStyle='#fff';ctx.stroke();
  ctx.beginPath();ctx.arc(0,0,70,0,Math.PI*2);ctx.stroke();
  ctx.fillStyle='#fff';ctx.font='900 28px system-ui';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(label,0,0);ctx.restore();
}

function placeCharacter(layout,W,H,rng){
  rng=rng||Math.random;var minSide=Math.min(W,H);
  switch(layout){
    case 'low-left': return {x:W*0.26,y:H*0.7,size:minSide*0.72,rot:-0.14};
    case 'low-right': return {x:W*0.74,y:H*0.7,size:minSide*0.72,rot:0.14};
    case 'peek-left': return {x:W*0.02,y:H*0.58,size:minSide*0.7,rot:-0.22};
    case 'peek-right': return {x:W*0.98,y:H*0.58,size:minSide*0.7,rot:0.22};
    case 'break-bottom': return {x:W*0.5,y:H*0.88,size:minSide*0.82,rot:(rng()-0.5)*0.08};
    case 'rail-left': return {x:W*0.2,y:H*0.58,size:Math.min(W,H)*0.78,rot:-0.1};
    case 'rail-right': return {x:W*0.8,y:H*0.58,size:Math.min(W,H)*0.78,rot:0.1};
    default: return {x:W*0.5,y:H*0.55,size:minSide*0.68,rot:(rng()-0.5)*0.12};
  }
}

function renderMeme(opts){
  var W=opts.W||1080,H=opts.H||1080,logo=opts.logo,banner=opts.banner,name=opts.name||'Token',tk=opts.ticker||'TOKEN';
  var p=opts.palette,rng=opts.rng||Math.random,scene=opts.scene,layout=opts.layout||'center';
  var c=document.createElement('canvas');c.width=W;c.height=H;var ctx=c.getContext('2d');
  scene.draw(ctx,W,H,p,rng,banner);
  // tiny edge shade only — keep scenes bright/saturated
  softVignette(ctx,W,H);

  var place=placeCharacter(layout,W,H,rng);
  // jitter
  place.x+= (rng()-0.5)*W*0.04; place.y+=(rng()-0.5)*H*0.03;
  place.size*=0.92+rng()*0.16;
  ctx.save();ctx.fillStyle='rgba(0,0,0,.28)';ctx.beginPath();ctx.ellipse(place.x,place.y+place.size*0.42,place.size*0.34,place.size*0.08,0,0,Math.PI*2);ctx.fill();ctx.restore();
  drawSticker(ctx,logo,place.x,place.y,place.size,place.rot,{shape:rng()>0.45?'round':'rect',rimColor:'#1B1F4B',accent:p.sec,glow:p.prim,pad:26,rim:9});

  // BIG readable bubbles + emoji
  if(rng()>0.15)speechBubble(ctx,W*0.03+rng()*W*0.05,H*0.12+rng()*H*0.05,pick(rng,BUBBLES),1.45+rng()*0.4);
  if(rng()>0.3)badgeStamp(ctx,W*0.86,H*0.16,pick(rng,['LIVE','HOT','NEW','#1']),p.sec||'#F72585',rng);
  ctx.font=(96+rng()*48|0)+'px serif';
  var spots=shuffle(rng,[[0.88,0.72],[0.12,0.78],[0.9,0.38],[0.5,0.72],[0.08,0.42]]);
  for(var e=0;e<Math.min(3,spots.length);e++){ctx.save();ctx.translate(spots[e][0]*W,spots[e][1]*H);ctx.rotate((rng()-0.5)*0.35);ctx.fillText(pick(rng,EMOJI),0,0);ctx.restore()}

  var cap=opts.caption||pick(rng,CAPTIONS)(name,tk);
  var margin=Math.max(56,Math.min(W,H)*0.055);
  var topY=margin+Math.min(W,H)*0.055;
  var botY=H-margin-Math.min(W,H)*0.055;
  if(layout==='break-bottom'){botY=H*0.38}
  if(layout==='center'){botY=H-margin-Math.min(W,H)*0.08}
  var fill2=p.prim||'#FFE566', fill3=mix(p.sec||'#FF4D8D','#FF9F1C',0.4);
  var b1=drawFittedCaption(ctx,cap.a,W/2,topY,{W:W,H:H,margin:margin,maxSize:Math.floor(Math.min(W,H)*0.078),fill1:'#FFFFFF',fill2:fill2,fill3:fill3,glow:rgba(p.sec||'#FF4D8D',0.35),rot:(rng()-0.5)*0.02});
  var b2=drawFittedCaption(ctx,cap.b,W/2,botY,{W:W,H:H,margin:margin,maxSize:Math.floor(Math.min(W,H)*0.072),fill1:'#FFFFFF',fill2:p.acc||'#4CC9F0',fill3:p.sec||'#FF70A6',glow:rgba(p.acc||'#4CC9F0',0.3),rot:(rng()-0.5)*0.02});

  return {canvas:c,captionBounds:[b1.bounds,b2.bounds],layout:layout,scene:scene.id};
}

function colorVariance(dataUrl){
  return new Promise(function(res){
    var im=new Image();im.onload=function(){
      var c=document.createElement('canvas');c.width=64;c.height=64;var ctx=c.getContext('2d',{willReadFrequently:true});
      ctx.drawImage(im,0,0,64,64);var d=ctx.getImageData(0,0,64,64).data;
      var n=0,sum=0,sum2=0,uniq={},rSum=0,gSum=0,bSum=0;
      for(var i=0;i<d.length;i+=4){var r=d[i],g=d[i+1],b=d[i+2];var key=((r>>4)<<8)|((g>>4)<<4)|(b>>4);uniq[key]=1;
        var l=(r+g+b)/3;sum+=l;sum2+=l*l;rSum+=r;gSum+=g;bSum+=b;n++}
      res({variance:sum2/n-(sum/n)*(sum/n),unique:Object.keys(uniq).length,meanR:rSum/n,meanG:gSum/n,meanB:bSum/n});
    };im.src=dataUrl;
  });
}

/** Test helper: render every caption × layout and assert text bounds fit */
function validateAllCaptions(opts){
  opts=opts||{};
  var logo=opts.logo,banner=opts.banner,name=opts.name||'Token',tk=opts.ticker||'TOKEN';
  var p=opts.palette||extractPalette(logo,banner);
  var W=opts.W||1080,H=opts.H||1080,margin=Math.max(40,Math.min(W,H)*0.045);
  var scene=SCENES[0];
  var fails=[];
  CAPTIONS.forEach(function(fn,ci){
    LAYOUTS.forEach(function(layout){
      var cap=fn(name,tk);
      var rng=mulberry32(ci*100+LAYOUTS.indexOf(layout)+1);
      var r=renderMeme({W:W,H:H,logo:logo,banner:banner,name:name,ticker:tk,palette:p,rng:rng,scene:scene,layout:layout,caption:cap});
      r.captionBounds.forEach(function(b,bi){
        if(b.left<margin-1||b.right>W-margin+1||b.top<margin-1||b.bottom>H-margin+1){
          fails.push({caption:ci,line:bi,layout:layout,text:bi===0?cap.a:cap.b,bounds:b,W:W,H:H,margin:margin});
        }
      });
    });
  });
  return {ok:!fails.length,fails:fails,checked:CAPTIONS.length*LAYOUTS.length};
}

async function generate(opts){
  opts=opts||{};
  var logo=opts.logo,banner=opts.banner||null,name=opts.name||'Token',tk=(opts.ticker||'TOKEN').replace(/^\$/,'');
  var count=opts.count||9,seed=opts.seed||(Date.now()&0xffffffff);
  var palette=extractPalette(logo,banner);
  var rng0=mulberry32(seed);
  var scenes=shuffle(rng0,SCENES);
  if(banner){var bi=scenes.findIndex(function(s){return s.id==='banner-blur'});if(bi>0){var tmp=scenes[0];scenes[0]=scenes[bi];scenes[bi]=tmp}}
  var layouts=shuffle(rng0,LAYOUTS.filter(function(l){return l.indexOf('rail')<0}));
  var captions=shuffle(rng0,CAPTIONS);
  var out=[];
  for(var i=0;i<count;i++){
    var scene=scenes[i%scenes.length];
    var isRail=i%3===2;
    var W=isRail?1600:1080,H=isRail?900:1080;
    var layout=isRail?pick(rng0,['rail-left','rail-right']):layouts[i%layouts.length];
    var rng=mulberry32((seed^(i*2654435761))>>>0);
    var rendered=renderMeme({W:W,H:H,logo:logo,banner:banner,name:name,ticker:tk,palette:palette,rng:rng,scene:scene,layout:layout,caption:captions[i%captions.length](name,tk)});
    var mime=isRail?'image/jpeg':'image/png';
    var d=mime==='image/jpeg'?rendered.canvas.toDataURL(mime,0.92):rendered.canvas.toDataURL(mime);
    out.push({kind:scene.id+(isRail?'-rail':'-sq'),d:d,on:i<3,w:W,h:H,scene:scene.id,layout:layout});
  }
  return {memes:out,palette:palette,sceneCount:SCENES.length,scenes:SCENES.map(function(s){return s.id})};
}

global.MemeGen={
  SCENES:SCENES,CAPTIONS:CAPTIONS,LAYOUTS:LAYOUTS,
  sceneCount:function(){return SCENES.length},
  extractPalette:extractPalette,generate:generate,colorVariance:colorVariance,
  renderMeme:renderMeme,fitCaption:fitCaption,drawFittedCaption:drawFittedCaption,
  validateAllCaptions:validateAllCaptions
};
})(typeof window!=='undefined'?window:globalThis);
