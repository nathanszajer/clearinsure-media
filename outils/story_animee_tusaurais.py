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
Q=f'''<div class="s" style="height:1920px;padding:120px 90px 110px;background:#0b1220;color:#f6f7f9;gap:40px">{LOGOW}
<div style="height:120px"></div>{serie('','#12a982','#c9d3dc')}
<div class="blk" style="font-size:52px;color:#12d39f;font-weight:800">Tu saurais quoi faire…</div>
<h1 class="blk" style="font-size:104px;color:#f6f7f9">…pour retrouver tes <span style="color:#7fa2ff">conditions générales</span>&#8239;?</h1>
<div class="blk" style="font-size:38px;color:#c9d3dc;line-height:1.35">Elles disent ce qui est couvert… et ce qui ne l’est pas.</div>
<div style="height:440px"></div>
<div class="blk" style="font-size:36px;color:#c9d3dc">Réponse en story demain.</div>
{BTN}
<div style="margin-top:auto;font-size:24px;color:#8a96a3">Information générale, pas un conseil en assurance.</div></div>'''
R=f'''<div class="s" style="height:1920px;padding:110px 90px 100px;gap:34px">{LOGO}
{serie(' · RÉPONSE','#2a5ef5','#667085')}
<h1 class="blk" style="font-size:80px">Dans ton <span style="color:#12a982">espace client</span>, ou dans les papiers reçus à la signature.</h1>
<div class="card blk" style="padding:36px 44px"><div class="p" style="font-size:38px">Introuvables&#8239;? <b>Demande-les à ton assureur</b> : on doit te les remettre avant la signature.</div></div>
<div class="card blk" style="background:#e8efff;padding:28px 40px;gap:8px"><div style="font-weight:800;font-size:40px;color:#2a5ef5">Conditions générales</div><div class="p" style="font-size:34px">Les règles communes à <b>tous les assurés de la compagnie</b> pour ce contrat : garanties, exclusions, délais.</div></div>
<div class="card blk" style="background:#e7f7f1;padding:28px 40px;gap:8px"><div style="font-weight:800;font-size:40px;color:#0e8a6a">Conditions particulières</div><div class="p" style="font-size:34px">Ton contrat à toi : montants, franchises, options.</div></div>
<div class="blk" style="display:flex;gap:26px;align-items:flex-start;background:#0b1220;border-radius:32px;padding:32px 40px">
<svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#7fe0c0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg>
<div style="display:flex;flex-direction:column;gap:10px"><div style="font-weight:800;font-size:28px;letter-spacing:3px;color:#7fe0c0">L’ASTUCE CLEARINSURE</div>
<div style="font-size:36px;line-height:1.3;color:#f6f7f9">Bientôt dans l’appli : <b>ajoute ton contrat une seule fois</b>, et retrouve tes conditions générales <b>en un clic</b>.</div>
<div style="font-size:28px;font-weight:700;color:#7fe0c0">100 % gratuit, pour toujours.</div></div></div>
{BTN}
<div style="margin-top:auto;font-size:24px;color:#667085">Information générale, pas un conseil en assurance.</div></div>'''
JS=r"""
window.setup=()=>{window.B=[...document.querySelectorAll('.blk')];};
window.setT=(T,STEP,T0)=>{
 const ez=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), ease=x=>x<0?0:x>1?1:(x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2), lerp=(a,b,k)=>a+(b-a)*k;
 B.forEach((e,i)=>{const k=ez((T-(0.3+i*STEP))/0.8);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*50}px)`;});
 const t=T-T0; const btn=document.getElementById('btn'),l1=document.getElementById('l1'),l2=document.getElementById('l2'),rip=document.getElementById('rip'),cur=document.getElementById('cur');
 const tx=330,ty=50,sx=620,sy=240; let k=ease((t-0.5)/1.1); let cx=lerp(sx,tx,k),cy=lerp(sy,ty,k)-Math.sin(k*Math.PI)*60;
 if(t>2.6){const k2=ease((t-2.6)/0.9);cx=lerp(tx,tx+120,k2);cy=lerp(ty,ty+110,k2);}
 cur.style.opacity=t<0.3?0:1;
 const press=(t>1.6&&t<1.85)?Math.sin((t-1.6)/0.25*Math.PI):0;
 cur.style.transform=`translate(${cx-4}px,${cy-4}px) scale(${1-0.12*press})`; btn.style.transform=`scale(${1-0.06*press})`;
 const f=Math.min(1,Math.max(0,(t-1.75)/0.2)); const done=t>=1.75;
 btn.style.background=done?`linear-gradient(90deg,rgba(255,255,255,${f}),rgba(255,255,255,${f})),linear-gradient(90deg,#2f6bff,#12a982)`:'linear-gradient(90deg,#2f6bff,#12a982)';
 btn.style.outline=done?`3px solid rgba(18,169,130,${f})`:'none'; btn.style.outlineOffset='-3px';
 l1.style.opacity=1-f; l2.style.opacity=f; l2.style.transform=`scale(${0.8+0.2*f})`;
 const r=Math.min(1,Math.max(0,(t-1.65)/0.6)); rip.style.opacity=(t>1.65&&r<1)?(1-r)*0.9:0; const d=30+140*r;
 rip.style.width=rip.style.height=d+'px'; rip.style.left=(tx-d/2)+'px'; rip.style.top=(ty-d/2)+'px';
};0;"""
sr=48000; rs=np.random.RandomState(7)
def env(L,a,d): t=np.arange(L)/sr; return (1-np.exp(-t*a))*np.exp(-t*d)
def mclick(y,t0,amp):
    for k,(dt,g) in enumerate([(0,1.0),(0.075,0.55)]):
        i=int((t0+dt)*sr); L=int(0.025*sr); n=sosfilt(butter(4,[1800,9000],'bandpass',fs=sr,output='sos'),rs.randn(L)); t=np.arange(L)/sr
        y[i:i+L,0]+=(n*1.4+np.sin(2*np.pi*(1150 if k==0 else 1400)*t)*0.6)*env(L,20000,260)*amp*g; y[i:i+L,1]=y[i:i+L,0]
def bell(y,t0,f,amp,dec=6):
    i=int(t0*sr); L=min(int(1.4*sr),len(y)-i); t=np.arange(L)/sr; s=np.zeros(L)
    for r,g,dd in [(1,1,1),(2.0,0.35,1.6),(3.01,0.18,2.4),(4.2,0.08,3.5)]: s+=g*np.sin(2*np.pi*f*r*t)*np.exp(-t*dec*dd)
    s*=(1-np.exp(-t*3000))*amp; y[i:i+L,0]+=s; y[i:i+L,1]+=s
def whoosh(y,t0,amp,L=0.45):
    n=int(L*sr); t=np.arange(n)/sr; x=rs.randn(n); out=np.zeros(n); ch=int(0.015*sr)
    for k in range(0,n,ch):
        fc=600+3000*(k/n)**1.3; f=sosfilt(butter(2,[fc*0.7,fc*1.4],'bandpass',fs=sr,output='sos'),x[max(0,k-ch):k+ch])[-min(ch,n-k):]; out[k:k+len(f)]=f
    s=out*np.sin(np.pi*np.clip(t/L,0,1))**2*np.exp(-t*2.5); s/=np.max(np.abs(s)); i=int(t0*sr); pan=np.linspace(-0.4,0.4,n)
    y[i:i+n,0]+=s*amp*(1-pan); y[i:i+n,1]+=s*amp*(1+pan)
def build(name,html,STEP=1.3):
    page=f'<!doctype html><html lang=fr><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>'
    open('caro/a.html','w',encoding='utf-8').write(page)
    fr=f'fr_{name}'; os.makedirs(fr,exist_ok=True); [os.remove(f'{fr}/{x}') for x in os.listdir(fr)]
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
        pg.goto('file://'+os.path.abspath('caro/a.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300); pg.evaluate(JS); pg.evaluate('setup()')
        nb=pg.evaluate('B.length'); T0=0.3+(nb-1)*STEP+0.3; DUR=T0+5.0
        for n in range(int(30*DUR)):
            pg.evaluate(f'setT({n/30},{STEP},{T0})'); pg.screenshot(path=f'{fr}/{n:04d}.png')
        b.close()
    y=np.zeros((int(sr*DUR),2))
    for i in range(nb): whoosh(y,0.3+i*STEP-0.12,0.16 if i<nb-1 else 0.12)
    mclick(y,T0+1.60,0.7); bell(y,T0+1.75,1318.5,0.5); bell(y,T0+1.86,1975.5,0.45)
    y=y/np.max(np.abs(y))*0.8; w=wave.open(f'{fr}.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((y*32767).astype('<i2').tobytes()); w.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',f'{fr}/%04d.png','-i',f'{fr}.wav','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',f'out/{name}.mp4'],check=True)
    print(name,nb,round(DUR,1),'s')
build('TuSaurais-S1E1-question',Q); build('TuSaurais-S1E1-reponse',R,1.2)
