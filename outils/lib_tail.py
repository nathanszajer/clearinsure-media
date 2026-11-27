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
