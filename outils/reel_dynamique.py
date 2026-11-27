# MODÈLE REEL DYNAMIQUE (validé « fort » par NS le 27/11) — Reel 27/11 vitrine/vol/vandalisme.
# Usage : depuis outils/ (avec node_modules/@fontsource-variable/dm-sans@5.1.0), adapter S (écrans), DUR et les temps des sons ;
# python3 reel_dynamique.py -> fr/*.png + a.wav ; puis ffmpeg (images+son) et concat avec ../assets/fin-instagram-abonne-cloche-like-partage.mp4 (fin rapide sans Merci, avec son).
import os,subprocess,wave,numpy as np
from scipy.signal import butter,sosfilt
from playwright.sync_api import sync_playwright
F=os.path.abspath('node_modules/@fontsource-variable/dm-sans/files')
exec(open('lib_tail.py').read().split('def build')[0])
CSS=f"""@font-face{{font-family:'DM Sans';font-weight:100 1000;src:url(file://{F}/dm-sans-latin-wght-normal.woff2);unicode-range:U+0000-00FF,U+0152-0153,U+2000-206F,U+20AC,U+2212}}
@font-face{{font-family:'DM Sans';font-weight:100 1000;src:url(file://{F}/dm-sans-latin-ext-wght-normal.woff2);unicode-range:U+0100-02BA,U+1E00-1EFF}}
*{{box-sizing:border-box}}body{{margin:0;background:#0a111f}}
#v{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'DM Sans',sans-serif;color:#f6f7f9;background:#0a111f}}
.sc{{position:absolute;inset:0;padding:220px 80px 380px;display:flex;flex-direction:column;justify-content:center;gap:40px}}
.e{{opacity:0}}
.pill{{align-self:flex-start;color:#fff;font-weight:800;font-size:36px;letter-spacing:2px;padding:16px 32px;border-radius:999px}}
.big{{font-weight:800;font-size:150px;line-height:1.02;letter-spacing:-0.03em}}
.h{{font-weight:800;font-size:96px;line-height:1.08;letter-spacing:-0.02em}}
.p{{font-size:44px;line-height:1.35;color:#c9d3dc}}
.row{{display:flex;align-items:center;gap:32px;background:#16213a;border:2px solid #24324f;border-radius:32px;padding:40px 44px}}
.row .ic{{font-size:76px;flex:none}} .row .t{{font-weight:800;font-size:56px;line-height:1.15}} .row .s{{font-size:38px;color:#9aa6b2;margin-top:6px}}
.chip{{align-self:flex-start;font-weight:800;font-size:66px;padding:26px 40px;border-radius:26px}}
.foot{{position:absolute;left:80px;right:80px;bottom:300px;font-size:28px;line-height:1.45;color:#8a96a3}}
#bar{{position:absolute;left:0;top:0;height:12px;background:linear-gradient(90deg,#2f6bff,#19c99a);z-index:9}}
#logo{{position:absolute;left:80px;top:80px;z-index:9;display:flex;align-items:center;gap:18px}}
"""
LOGO='''<div id="logo"><svg width="72" height="72" viewBox="0 0 64 64"><path d="M32 4 L55 12.5 V30 C55 45 45.5 55.5 32 60 C18.5 55.5 9 45 9 30 V12.5 Z" fill="none" stroke="#2f6bff" stroke-width="5.5" stroke-linejoin="round"/><path d="M21.5 18.5 H35 L42.5 26 V46 H21.5 Z" fill="none" stroke="#19c99a" stroke-width="4.5" stroke-linejoin="round"/><path d="M27 33.5 L30.8 37.3 L37.5 30" fill="none" stroke="#19c99a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-weight:800;font-size:50px;letter-spacing:-0.02em"><span style="color:#7fa2ff">Clear</span><span style="color:#12a982">Insure</span></span></div>'''
LEG='Information générale, pas un conseil en assurance.'
def E(t,html,kind='up'): return f'<div class="e" data-t="{t}" data-k="{kind}">{html}</div>' if not html.startswith('<div class=') else html.replace('<div class="','<div data-t="%s" data-k="%s" class="e '%(t,kind),1)
S=[]
S.append((0,3.7,'radial-gradient(1200px 900px at 80% 20%,#3a1220,#0a111f 70%)',f'''
{E(0.1,'<div class="pill" style="background:#dc473c">ACTU · PARIS · 14/11/2026</div>')}
{E(0.45,'<div class="big">Vitrine<br>cassée.</div>','slam')}
{E(1.05,'<div class="big" style="color:#ff6b5e">Boutique<br>pillée.</div>','slam')}
{E(1.65,'<div class="big">Vandalisme.</div>','slam')}
{E(2.35,'<div class="h" style="align-self:flex-start;background:#19c99a;color:#0a111f;padding:16px 30px;border-radius:22px;margin-top:20px;font-size:82px;white-space:nowrap">Ton assurance paie&#8239;?</div>','pop')}
<div class="foot">Source&#8239;: Le JDD, 16/11/2026<br>{LEG}</div>'''))
S.append((3.7,7.8,'radial-gradient(1200px 900px at 20% 30%,#2a1430,#0a111f 70%)',f'''
{E(3.9,'<div class="pill" style="background:#f2b233;color:#0a111f">⚠️ CE QUE DIT LA LOI</div>')}
{E(4.2,'<div class="h">Les dégâts d’émeutes&#8239;:</div>')}
{E(4.8,'<div style="align-self:flex-start;transform-origin:left center"><div style="border:12px solid #ff4d4d;color:#ff4d4d;font-weight:900;font-size:118px;line-height:1;white-space:nowrap;letter-spacing:-0.03em;padding:20px 40px;border-radius:24px;transform:rotate(-6deg);margin:40px 0">PAS COUVERTS</div></div>','stamp')}
{E(5.7,'<div class="h" style="font-size:72px">…sauf si ton contrat<br><span style="color:#19c99a">le prévoit.</span></div>')}
<div class="foot">Source&#8239;: Code des assurances, art. L121-8<br>{LEG}</div>'''))
S.append((7.8,12.3,'radial-gradient(1200px 900px at 80% 70%,#10264a,#0a111f 70%)',f'''
{E(8.0,'<div class="pill" style="background:#2f6bff">⏱️ LE CHRONO TOURNE</div>')}
{E(8.3,'<div class="h" style="font-size:72px">Pour déclarer un <span style="color:#ff6b5e">vol</span>,<br>tu peux n’avoir que&#8239;:</div>')}
{E(8.7,'<div style="display:flex;align-items:baseline;gap:30px"><span id="cnt" style="font-weight:900;font-size:420px;line-height:0.85;color:#ff6b5e;letter-spacing:-0.04em">2</span><span class="h" style="font-size:110px">jours<br>ouvrés</span></div>','pop')}
{E(10.0,'<div class="row"><div class="ic">🪟</div><div><div class="t">5 jours ouvrés</div><div class="s">vitrine cassée sans vol</div></div></div>')}
{E(10.6,'<div class="p" style="font-size:40px">Minimum légal. Ton contrat peut prévoir plus.</div>')}
<div class="foot">Source&#8239;: Code des assurances, art. L113-2<br>{LEG}</div>'''))
S.append((12.3,16.8,'radial-gradient(1200px 900px at 20% 70%,#0c3a30,#0a111f 70%)',f'''
{E(12.5,'<div class="pill" style="background:#12a982">✅ TOUT DE SUITE</div>')}
{E(12.8,'<div class="h">Les 3 réflexes</div>')}
{E(13.3,'<div class="row"><div class="ic">📸</div><div><div class="t">Photos</div><div class="s">dégâts, stock, matériel, avant de ranger</div></div></div>','left')}
{E(14.0,'<div class="row"><div class="ic">🧾</div><div><div class="t">Plainte</div><div class="s">en ligne si l’auteur est inconnu</div></div></div>','left')}
{E(14.7,'<div class="row"><div class="ic">✉️</div><div><div class="t">Déclaration écrite</div><div class="s">à ton assureur, dans les délais</div></div></div>','left')}
<div class="foot">Source&#8239;: service-public.gouv.fr (vandalisme)<br>{LEG}</div>'''))
S.append((16.8,20.6,'radial-gradient(1200px 900px at 70% 30%,#1a2a5a,#0a111f 70%)',f'''
{E(17.0,'<div class="pill" style="background:#7fa2ff;color:#0a111f">🔎 DANS TON CONTRAT</div>')}
{E(17.3,'<div class="h">Cherche ces mots&#8239;:</div>')}
{E(17.8,'<div class="chip" style="background:#e8efff;color:#2a5ef5">« Émeutes et<br>mouvements populaires »</div>','pop')}
{E(18.4,'<div class="chip" style="background:#e7f7f1;color:#0e8a6a">« Vandalisme »</div>','pop')}
{E(19.0,'<div class="chip" style="background:#ffe9e7;color:#d63b2f">« Vol »</div>','pop')}
{E(19.6,'<div class="h" style="font-size:76px">Ce sont elles<br>qui décident.</div>')}
<div class="foot">{LEG}</div>'''))
S.append((20.6,25.4,'radial-gradient(1200px 900px at 50% 40%,#0f3d3a,#0a111f 70%)',f'''
{E(20.8,'<div class="h" style="font-size:92px">Tu ne sais pas<br>ce que dit <span style="color:#19c99a">ton</span><br>contrat&#8239;?</div>')}
{E(21.5,'<div class="pill" style="background:#2f6bff">BIENTÔT · L’APPLI CLEARINSURE</div>','pop')}
{E(21.9,'<div class="row"><div class="ic">1️⃣</div><div class="t">Tu ajoutes ton contrat</div></div>','left')}
{E(22.4,'<div class="row"><div class="ic">2️⃣</div><div class="t">Tu vois ce qui est couvert</div></div>','left')}
{E(22.9,'<div class="row"><div class="ic">3️⃣</div><div class="t">Un pro si besoin</div></div>','left')}
{E(23.5,'<div style="background:#12a982;border-radius:26px;padding:26px 34px;text-align:center"><div style="font-weight:800;font-size:52px">100 % gratuit, pour toujours</div><div style="font-size:32px;margin-top:6px">Ça ne te coûte rien&#8239;: ça te protège.</div></div>','pop')}
<div class="foot">{LEG}</div>'''))
DUR=25.4
html='<div id="v"><div id="bar"></div>'+LOGO+''.join(f'<div class="sc" data-a="{a}" data-b="{b}" style="background:{bg}">{c}</div>' for a,b,bg,c in S)+'</div>'
JS="""window.setT=function(T){const ez=x=>{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)};
document.getElementById('bar').style.width=(T/%s*100)+'%%';
document.querySelectorAll('.sc').forEach(s=>{const a=+s.dataset.a,b=+s.dataset.b;let o=1,x=0;
 if(T<a||T>=b+0.25){s.style.display='none';return} s.style.display='flex';
 const ki=ez((T-a)/0.25); if(a>0){x=(1-ki)*1080} if(T>=b){const ko=ez((T-b)/0.25);x=-ko*300;o=1-ko}
 s.style.transform=`translateX(${x}px)`;s.style.opacity=o;s.style.zIndex=T>=b?1:2;});
document.querySelectorAll('.e').forEach(e=>{const t=+e.dataset.t,k=e.dataset.k;const p=ez((T-t)/(k=='slam'?0.22:0.4));e.style.opacity=Math.min(1,p*1.5);
 if(k=='slam')e.style.transform=`scale(${1.35-0.35*p})`;else if(k=='pop')e.style.transform=`scale(${0.8+0.2*p})`;
 else if(k=='stamp')e.style.transform=`scale(${2.2-1.2*p})`;else if(k=='left')e.style.transform=`translateX(${(1-p)*-120}px)`;else e.style.transform=`translateY(${(1-p)*40}px)`;
 e.style.transformOrigin='left center'});
const c=document.getElementById('cnt');const kc=Math.max(0,Math.min(1,(T-8.7)/0.9));c.textContent=kc<1?String(Math.max(2,Math.round(9-7*ez(kc)))):'2';
const sh=document.getElementById('v');let shk=0;[[0.45],[1.05],[1.65],[4.8]].forEach(([t])=>{if(T>=t&&T<t+0.18)shk=(1-(T-t)/0.18)*14});sh.style.transform=`translate(${shk*Math.sin(T*90)}px,${shk*Math.cos(T*70)}px)`;}"""%DUR
open('reel.html','w').write(f'<!doctype html><html lang=fr><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>')
os.makedirs('fr',exist_ok=True);[os.remove('fr/'+x) for x in os.listdir('fr')]
import sys
frames=[int(a) for a in sys.argv[1:]] if len(sys.argv)>1 else range(int(30*DUR))
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1)
    pg.goto('file://'+os.path.abspath('reel.html'));pg.evaluate('document.fonts.ready');pg.wait_for_timeout(300);pg.evaluate(JS)
    for n in frames: pg.evaluate(f'setT({n/30})');pg.screenshot(path=f'fr/{n:04d}.png')
    b.close()
if len(sys.argv)>1: sys.exit()
y=np.zeros((int(sr*DUR)+sr,2))
def tac(t0,amp):
    i=int(t0*sr);L=int(0.06*sr);t=np.arange(L)/sr; s=(np.sin(2*np.pi*120*t)*np.exp(-t*60)+sosfilt(butter(2,3000,'highpass',fs=sr,output='sos'),rs.randn(L))*np.exp(-t*300)*0.5)*amp; y[i:i+L,0]+=s;y[i:i+L,1]+=s
def kick(t0,amp):
    i=int(t0*sr);L=int(0.25*sr);t=np.arange(L)/sr; f=50+90*np.exp(-t*30); s=np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*12)*amp; y[i:i+L,0]+=s;y[i:i+L,1]+=s
def hat(t0,amp):
    i=int(t0*sr);L=int(0.04*sr);s=sosfilt(butter(2,7000,'highpass',fs=sr,output='sos'),rs.randn(L))*np.exp(-np.arange(L)/sr*120)*amp; y[i:i+L,0]+=s;y[i:i+L,1]+=s
def tick(t0,amp):
    i=int(t0*sr);L=int(0.015*sr);t=np.arange(L)/sr;s=np.sin(2*np.pi*2400*t)*np.exp(-t*400)*amp;y[i:i+L,0]+=s;y[i:i+L,1]+=s
bpm=0.5
for k in np.arange(0,DUR-0.3,bpm): kick(k,0.35); hat(k+bpm/2,0.06)
for a,b_,bg,c in S[1:]: whoosh(y,a-0.15,0.25)
for t in [0.45,1.05,1.65,4.8]: tac(t,0.9)
for t in [2.35,8.7,17.8,18.4,19.0,21.5,23.5]: tac(t,0.45)
for t in [13.3,14.0,14.7,21.9,22.4,22.9]: tac(t,0.3)
for k in range(9): tick(8.7+k*0.1,0.25)
for t in np.arange(10.0,12.2,0.5): tick(t,0.12)
bell(y,23.5,1318.5,0.3);bell(y,23.62,1975.5,0.25)
y=y[:int(sr*DUR)]; y=y/np.max(np.abs(y))*0.85
w=wave.open('a.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((y*32767).astype('<i2').tobytes());w.close()
