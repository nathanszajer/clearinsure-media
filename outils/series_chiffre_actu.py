import os,subprocess,wave,numpy as np
from scipy.signal import butter,sosfilt
from playwright.sync_api import sync_playwright
exec(open('lib_anim.py',encoding='utf-8').read())
H=1350
def row(label,col,extra=''): return f'<div class="blk" style="display:flex;align-items:center;gap:20px"><div style="background:{col};color:#fff;font-weight:800;font-size:28px;letter-spacing:2px;padding:14px 26px;border-radius:999px">{label}</div><div style="font-weight:700;font-size:26px;letter-spacing:2px;color:#667085">{extra}</div></div>'
TIP=lambda t: f'''<div class="blk" style="display:flex;gap:22px;align-items:flex-start;background:#0b1220;border-radius:28px;padding:24px 32px"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#7fe0c0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg><div style="display:flex;flex-direction:column;gap:6px"><div style="font-weight:800;font-size:22px;letter-spacing:3px;color:#7fe0c0">L’ASTUCE CLEARINSURE</div><div style="font-size:28px;line-height:1.3;color:#f6f7f9">{t}</div><div style="font-size:22px;font-weight:700;color:#7fe0c0">100 % gratuit, pour toujours.</div></div></div>'''
BTNS=BTN.replace('class="blk" id="ctaw" style="display:flex;justify-content:center"','class="blk" id="ctaw" style="display:flex;justify-content:center;margin-top:4px"')
CH=f'''<div class="s" style="height:{H}px;padding:60px 76px 50px;gap:22px">{LOGO}
{row('LE CHIFFRE QUI PIQUE','#2a5ef5','SAISON 1 · ÉPISODE 1/8')}
<div class="blk" style="display:flex;align-items:baseline;gap:22px"><div style="font-weight:800;font-size:190px;line-height:.9;letter-spacing:-0.04em;color:#2a5ef5">1<span style="font-size:90px;color:#0b1220"> sur </span><span id="cnt">11</span></div></div>
<div class="blk" style="font-size:44px;font-weight:800;line-height:1.15">Un logement assuré sur 11 a eu un sinistre indemnisé en 2025.</div>
<div class="card blk" style="padding:24px 34px;gap:6px"><div class="p" style="font-size:31px">Soit <b>4,2 millions de sinistres</b>, pour un coût moyen de <b><span id="cnt2">1 901</span>&nbsp;€</b> chacun.</div></div>
<div class="card blk" style="background:#e7f7f1;padding:24px 34px;gap:6px"><div style="font-weight:800;font-size:30px;color:#0e8a6a">Le réflexe</div><div class="p" style="font-size:30px">Regarde <b>ta franchise</b> et <b>tes plafonds</b> avant d’en avoir besoin.</div></div>
{TIP('Bientôt dans l’appli : <b>ta franchise et tes plafonds en clair</b>, en un clic.')}
{BTNS}
<div style="margin-top:auto;font-size:19px;color:#667085">Source : France Assureurs, « L’assurance habitation en 2025 » (juillet 2026) · Information générale, pas un conseil en assurance.</div></div>'''
NEWS=f'''<div class="s" style="height:{H}px;padding:52px 76px 44px;gap:18px">{LOGO}
<div class="blk" style="position:relative;overflow:hidden;flex:none;background:#0b1220;border-radius:18px;height:60px;display:flex;align-items:center"><div style="position:absolute;left:0;top:0;bottom:0;z-index:2;background:#dc483c;color:#fff;font-weight:800;font-size:28px;letter-spacing:3px;padding:0 26px;display:flex;align-items:center">ACTU</div><div id="tick" style="white-space:nowrap;color:#f6f7f9;font-weight:700;font-size:26px;letter-spacing:2px;padding-left:180px">CE QUI CHANGE POUR TOI · 1ER JANVIER 2027 · TAXE ATTENTAT · AUTO · HABITATION · CE QUI CHANGE POUR TOI · 1ER JANVIER 2027 · TAXE ATTENTAT · AUTO · HABITATION ·</div></div>
<div class="blk" style="font-weight:800;font-size:34px;letter-spacing:2px;color:#dc483c">AU 1ER JANVIER 2027</div>
<h1 class="blk" style="font-size:60px">La « taxe attentat » passe de 6,50 € à <span style="color:#dc483c">8,50 €</span> par contrat.</h1>
<div class="card blk" style="padding:22px 32px;gap:4px"><div style="font-weight:800;font-size:28px;color:#2a5ef5">Qui est concerné ?</div><div class="p" style="font-size:29px">Chaque contrat d’assurance de biens : <b>auto, habitation…</b> Elle est prélevée avec ta cotisation.</div></div>
<div class="card blk" style="background:#e8efff;padding:22px 32px;gap:4px"><div style="font-weight:800;font-size:28px;color:#2a5ef5">À quoi elle sert ?</div><div class="p" style="font-size:29px">Elle finance le fonds qui indemnise les victimes d’attentats et d’autres infractions (FGTI).</div></div>
<div class="card blk" style="background:#e7f7f1;padding:22px 32px;gap:4px"><div style="font-weight:800;font-size:28px;color:#0e8a6a">Ce que tu fais</div><div class="p" style="font-size:29px">Rien à faire. Sur ton prochain avis d’échéance, la ligne « contribution FGTI » passera à <b>8,50 €</b>.</div></div>
{TIP('Bientôt dans l’appli : <b>chaque montant de ton contrat expliqué en clair</b>.')}
{BTNS}
<div style="margin-top:auto;font-size:19px;color:#667085">Source : service-public.gouv.fr · arrêté du 24 juillet 2026 · Information générale, pas un conseil en assurance.</div></div>'''
JS2=JS.replace("window.setT=(T,STEP,T0)=>{","window.setT=(T,STEP,T0,MODE)=>{").replace(
"B.forEach((e,i)=>{const k=ez((T-(0.3+i*STEP))/0.8);e.style.opacity=k;e.style.transform=`translateY(${(1-k)*50}px)`;});",
"""B.forEach((e,i)=>{const k=ez((T-(0.3+i*STEP))/0.7);e.style.opacity=k;
 if(MODE==='chiffre'){e.style.transform=`scale(${0.9+0.1*k})`;} else {e.style.transform=`translateX(${(1-k)*-60}px)`;}});
 if(MODE==='chiffre'){const c=document.getElementById('cnt'),c2=document.getElementById('cnt2'); const i1=B.findIndex(b=>b.contains(c)),i2=B.findIndex(b=>b.contains(c2));
   const k1=Math.min(1,Math.max(0,(T-(0.3+i1*STEP))/1.0)); c.textContent=Math.max(1,Math.round(1+ (11-1)*(1-Math.pow(1-k1,3))));
   const k2=Math.min(1,Math.max(0,(T-(0.3+i2*STEP))/1.0)); c2.textContent=Math.round(1901*(1-Math.pow(1-k2,3))).toLocaleString('fr-FR').replace(/\\u202f|\\u00a0| /g,'\\u00a0');}
 else {const tk=document.getElementById('tick'); tk.style.transform=`translateX(${-T*90}px)`;}""")
exec(open('lib_tail.py',encoding='utf-8').read().split('def build')[0])
def tac(y,t0,amp):
    i=int(t0*sr);L=int(0.05*sr);t=np.arange(L)/sr; s=(np.sin(2*np.pi*180*t)*np.exp(-t*90)+sosfilt(butter(2,3000,'highpass',fs=sr,output='sos'),rs.randn(L))*np.exp(-t*400)*0.4)*amp
    y[i:i+L,0]+=s;y[i:i+L,1]+=s
def tickr(y,t0,amp,dur=0.9):
    for k in range(9):
        i=int((t0+k*dur/9)*sr);L=int(0.012*sr);t=np.arange(L)/sr; s=np.sin(2*np.pi*2400*t)*np.exp(-t*500)*amp*(0.6+0.4*k/8); y[i:i+L,0]+=s;y[i:i+L,1]+=s
def jingle(y,t0,amp):
    for j,f in enumerate([783.99,1046.5,1318.5]):
        bell(y,t0+j*0.12,f,amp*(0.8 if j<2 else 1),dec=7)
def build(name,html,MODE,STEP=1.15):
    page=f'<!doctype html><html lang=fr><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>'
    open('caro/b.html','w',encoding='utf-8').write(page)
    fr=f'fr_{name}';os.makedirs(fr,exist_ok=True);[os.remove(f'{fr}/{x}') for x in os.listdir(fr)]
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':H},device_scale_factor=1)
        pg.goto('file://'+os.path.abspath('caro/b.html'));pg.evaluate('document.fonts.ready');pg.wait_for_timeout(300);pg.evaluate(JS2);pg.evaluate('setup()')
        nb=pg.evaluate('B.length');T0=0.3+(nb-1)*STEP+0.3;DUR=T0+4.6
        for n in range(int(30*DUR)):
            pg.evaluate(f"setT({n/30},{STEP},{T0},'{MODE}')");pg.screenshot(path=f'{fr}/{n:04d}.png')
        b.close()
    y=np.zeros((int(sr*DUR),2))
    if MODE=='news': jingle(y,0.05,0.35)
    for i in range(nb-1):
        t=0.3+i*STEP
        if MODE=='chiffre': tac(y,t,0.5)
        else: whoosh(y,t-0.1,0.12)
    if MODE=='chiffre':
        tickr(y,0.3+2*STEP,0.18); tickr(y,0.3+4*STEP,0.18)
    mclick(y,T0+1.60,0.7);bell(y,T0+1.75,1318.5,0.5);bell(y,T0+1.86,1975.5,0.45)
    y=y/np.max(np.abs(y))*0.8;w=wave.open(f'{fr}.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((y*32767).astype('<i2').tobytes());w.close()
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',f'{fr}/%04d.png','-i',f'{fr}.wav','-shortest','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-c:a','aac','-b:a','192k','-movflags','+faststart',f'out/{name}.mp4'],check=True)
    print(name,nb,round(DUR,1),int(30*DUR)-1)
build('ChiffreQuiPique-S1E1',CH,'chiffre')
