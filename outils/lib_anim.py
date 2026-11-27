import os, subprocess, sys, wave, numpy as np
from scipy.signal import butter, sosfilt
from playwright.sync_api import sync_playwright
exec(open('caro.py',encoding='utf-8').read().split('N=7')[0])  # CSS, LOGO
LOGOW=LOGO.replace('color:#2f6bff">Clear','color:#7fa2ff">Clear')
def serie(extra,col,sub): return f'<div class="blk" style="display:flex;align-items:center;gap:22px"><div style="background:{col};color:#fff;font-weight:800;font-size:32px;letter-spacing:2px;padding:16px 30px;border-radius:999px">TU SAURAIS ?</div><div style="font-weight:700;font-size:30px;letter-spacing:2px;color:{sub}">SAISON 1 · ÉPISODE 1/8{extra}</div></div>'
BTN='''<div class="blk" id="ctaw" style="display:flex;justify-content:center"><div id="wrap" style="position:relative;display:inline-flex">
<div id="btn" style="position:relative;display:inline-flex;align-items:center;justify-content:center;width:470px;height:96px;border-radius:999px;background:linear-gradient(90deg,#2f6bff,#12a982);color:#fff;font-weight:800;font-size:40px;box-shadow:0 14px 30px rgba(47,107,255,.30),0 0 0 8px rgba(47,107,255,.10),inset 0 -5px 0 rgba(0,0,0,.14),inset 0 2px 0 rgba(255,255,255,.25)">
<span id="l1" style="display:inline-flex;align-items:center;gap:16px;position:absolute"><svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6"/><path d="M19 8v6M16 11h6"/></svg>Abonne-toi</span>
<span id="l2" style="display:inline-flex;align-items:center;gap:14px;position:absolute;opacity:0;color:#12a982"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#12a982" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 L9.5 18 L20 6.5"/></svg>Abonné(e)</span></div>
<div id="rip" style="position:absolute;border-radius:50%;border:4px solid #12a982;box-sizing:border-box;opacity:0"></div>
<svg id="cur" width="60" height="70" viewBox="0 0 60 70" style="position:absolute;left:0;top:0;overflow:visible"><path d="M4 4 L4 56 L16 44 L25 64 L35 59 L26 40 L43 40 Z" fill="#0b1220" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" style="filter:drop-shadow(0 6px 8px rgba(11,18,32,.35))"/></svg>
</div></div>'''

JS=r"""
window.setup=()=>{window.B=[...document.querySelectorAll('.blk')];};
window.setT=(T,STEP,T0)=>{
 const ez=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), ease=x=>x<0?0:x>1?1:(x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2), lerp=(a,b,k)=>a+(b-a)*k;
 B.forEach((e,i)=>{const k=ez((T-(0.3+i*STEP))/0.8);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*50}px)`;});
 const t=T-T0; const btn=document.getElementById('btn'),l1=document.getElementById('l1'),l2=document.getElementById('l2'),rip=document.getElementById('rip'),cur=document.getElementById('cur');
 const tx=330,ty=50,sx=620,sy=240; let k=ease((t-0.2)/0.5); let cx=lerp(sx,tx,k),cy=lerp(sy,ty,k)-Math.sin(k*Math.PI)*60;
 if(t>1.5){const k2=ease((t-1.5)/0.7);cx=lerp(tx,tx+120,k2);cy=lerp(ty,ty+110,k2);}
 cur.style.opacity=t<0?0:1;
 const press=(t>0.7&&t<0.9)?Math.sin((t-0.7)/0.2*Math.PI):0;
 cur.style.transform=`translate(${cx-4}px,${cy-4}px) scale(${1-0.12*press})`; btn.style.transform=`scale(${1-0.06*press})`;
 const f=Math.min(1,Math.max(0,(t-0.8)/0.15)); const done=t>=0.8;
 btn.style.background=done?`linear-gradient(90deg,rgba(255,255,255,${f}),rgba(255,255,255,${f})),linear-gradient(90deg,#2f6bff,#12a982)`:'linear-gradient(90deg,#2f6bff,#12a982)';
 btn.style.outline=done?`3px solid rgba(18,169,130,${f})`:'none'; btn.style.outlineOffset='-3px';
 l1.style.opacity=1-f; l2.style.opacity=f; l2.style.transform=`scale(${0.8+0.2*f})`;
 const r=Math.min(1,Math.max(0,(t-0.75)/0.5)); rip.style.opacity=(t>0.75&&r<1)?(1-r)*0.9:0; const d=30+140*r;
 rip.style.width=rip.style.height=d+'px'; rip.style.left=(tx-d/2)+'px'; rip.style.top=(ty-d/2)+'px';
};0;"""
