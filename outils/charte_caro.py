import os
from playwright.sync_api import sync_playwright
from PIL import Image
fd='file://'+os.path.abspath('node_modules/@fontsource-variable/dm-sans/files')+'/'
CSS=f"""@font-face{{font-family:'DM Sans';font-weight:100 1000;src:url({fd}dm-sans-latin-ext-wght-normal.woff2);unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+20A0-20AB,U+20AD-20C0,U+2C60-2C7F,U+A720-A7FF;}}
@font-face{{font-family:'DM Sans';font-weight:100 1000;src:url({fd}dm-sans-latin-wght-normal.woff2);unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}}
body{{margin:0}} *{{box-sizing:border-box}}
.s{{width:1080px;height:1350px;padding:72px 80px 64px;display:flex;flex-direction:column;gap:34px;background:#f6f7f9;color:#0b1220;font-family:'DM Sans',sans-serif}}
.eb{{font-size:30px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#12a982}}
h1{{margin:0;font-weight:800;letter-spacing:-0.02em;line-height:1.05}}
.card{{background:#fff;border-radius:32px;padding:44px 48px;display:flex;flex-direction:column;gap:14px}}
.p{{font-size:44px;line-height:1.35;color:#3b4658}} .p b{{color:#0b1220}}
.num{{width:120px;height:120px;border-radius:50%;background:#e8efff;color:#2a5ef5;font-weight:800;font-size:64px;display:flex;align-items:center;justify-content:center}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;font-size:24px;color:#667085}}
.pg{{font-weight:800;color:#2a5ef5;font-size:30px}}
"""
LOGO='<div style="display:flex;align-items:center;gap:18px"><svg width="70" height="70" viewBox="0 0 64 64"><path d="M32 4 L55 12.5 V30 C55 45 45.5 55.5 32 60 C18.5 55.5 9 45 9 30 V12.5 Z" fill="none" stroke="#2f6bff" stroke-width="5.5" stroke-linejoin="round"/><path d="M21.5 18.5 H35 L42.5 26 V46 H21.5 Z" fill="none" stroke="#19c99a" stroke-width="4.5" stroke-linejoin="round"/><path d="M27 33.5 L30.8 37.3 L37.5 30" fill="none" stroke="#19c99a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span style="font-weight:800;letter-spacing:-0.02em;font-size:50px"><span style="color:#2f6bff">Clear</span><span style="color:#12a982">Insure</span></span></div>'
N=7
def foot(i,extra=''): return f'<div class="foot"><span>Information générale, pas un conseil en assurance.</span><span class="pg">{extra}{i}/{N}</span></div>'
def step(i,n,title,body,note=''):
    return f'''<div class="s">{LOGO}<div class="eb">Habitation · Cambriolage</div>
<div style="margin:auto 0;display:flex;flex-direction:column;gap:44px"><div style="display:flex;align-items:center;gap:36px"><div class="num" style="flex:none;width:150px;height:150px;font-size:80px">{n}</div><h1 style="font-size:90px;flex:1">{title}</h1></div>
<div class="card"><div class="p">{body}</div></div>{note}</div>{foot(i,'Fais défiler → &nbsp;')}</div>'''
BOOK='<svg width="170" height="170" viewBox="0 0 24 24" fill="#2a5ef5" stroke="#2a5ef5" stroke-width="1.6" stroke-linejoin="round"><path d="M6 3h12v18l-6-4.5L6 21z"/></svg>'
slides=[
f'''<div class="s">{LOGO}<div class="eb" style="margin-top:60px">Habitation · Cambriolage</div>
<h1 style="font-size:140px;margin-top:20px">Cambriolé(e)&#8239;?<br><span style="color:#2a5ef5">5 réflexes,</span><br>dans l’ordre.</h1>
<div class="p" style="font-size:46px">Les premières heures comptent pour ton indemnisation.</div>
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center"><span style="font-size:24px;color:#667085">Information générale, pas un conseil en assurance.</span><span style="background:#2a5ef5;color:#fff;font-weight:800;font-size:34px;padding:20px 34px;border-radius:999px">Fais défiler →</span></div></div>''',
step(2,1,'Ne touche à rien, photographie tout.','<b>Avant de ranger</b>, prends en photo chaque pièce, les traces d’effraction (porte, serrure, fenêtre) et les meubles fouillés.','<div class="p" style="font-size:38px">Ces photos montrent l’état des lieux à ton assureur.</div>'),
step(3,2,'Porte plainte.','Au <b>commissariat</b> ou à la <b>gendarmerie</b>, avec la liste de ce qui a été volé.','<div class="p" style="font-size:38px">Garde le <b>récépissé</b> : ton assureur te le demandera.</div>'),
step(4,3,'Fais opposition.','Sur tes <b>cartes bancaires</b> et tes <b>chéquiers</b> volés, le plus vite possible, auprès de ta banque.','<div class="p" style="font-size:38px">Pense aussi aux papiers d’identité et aux clés.</div>'),
step(5,4,'Déclare-le à ton assureur.','Pour un vol, la loi te laisse <b>au moins 2 jours ouvrés</b>. Regarde ce que prévoit ton contrat, et joins le récépissé de plainte.','<div class="p" style="font-size:38px">Passé le délai, l’assureur peut refuser de t’indemniser s’il prouve que ton retard lui a causé un préjudice.</div>'),
step(6,5,'Rassemble les preuves.','<b>Factures, photos, certificats</b> et une <b>liste détaillée</b> des objets volés, avec leur valeur.','<div class="p" style="font-size:38px">Sans preuve, l’indemnisation des objets de valeur peut être limitée.</div>'),
f'''<div class="s">{LOGO}<div class="eb" style="color:#2a5ef5;margin-top:20px">À retenir</div>
<div style="display:flex;flex-direction:column;gap:20px">
<div class="card" style="background:#e8efff;padding:26px 36px"><div class="p" style="font-size:42px"><b>Photos → plainte → opposition → déclaration → preuves.</b></div></div>
<div class="card" style="background:#e7f7f1;padding:26px 36px"><div style="font-weight:800;font-size:46px;color:#0e8a6a">100 % gratuit, pour toujours</div><div class="p" style="font-size:36px">Bientôt l’appli ClearInsure : tu vois en clair ce que couvre ton contrat. Ça ne te coûte rien : ça te protège.</div></div></div>
<div style="display:flex;align-items:center;gap:48px;margin:auto 0"><div style="position:relative;flex:none">{BOOK}<svg width="64" height="70" viewBox="0 0 60 70" style="position:absolute;right:-34px;bottom:-30px"><path d="M4 4 L4 56 L16 44 L25 64 L35 59 L26 40 L43 40 Z" fill="#0b1220" stroke="#fff" stroke-width="4" stroke-linejoin="round"/></svg></div>
<div><div style="font-weight:800;font-size:72px;letter-spacing:-0.02em;line-height:1.05">Enregistre ce post.</div><div class="p" style="font-size:38px;margin-top:10px">Le jour où ça t’arrive, tu l’auras sous la main.</div></div></div>
<div style="font-size:36px;font-weight:800;color:#2a5ef5">Abonne-toi + active la cloche · Like · Partage</div>
{foot(7)}</div>''']
os.makedirs('caro',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    for k,h in enumerate(slides,1):
        open('caro/s.html','w',encoding='utf-8').write(f'<!doctype html><html lang=fr><head><meta charset=utf-8><style>{CSS}</style></head><body>{h}</body></html>')
        pg.goto('file://'+os.path.abspath('caro/s.html')); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(200)
        pg.screenshot(path='caro/t.png',clip={'x':0,'y':0,'width':1080,'height':1350})
        Image.open('caro/t.png').convert('RGB').save(f'out/30-11-Carrousel-cambriolage-{k:02d}.jpg','JPEG',quality=92)
    b.close()
ims=[Image.open(f'out/30-11-Carrousel-cambriolage-{k:02d}.jpg').resize((540,675)) for k in range(1,8)]
W=Image.new('RGB',(540*4,675*2),'white')
for i,im in enumerate(ims): W.paste(im,((i%4)*540,(i//4)*675))
W.save('caro/all.png')
