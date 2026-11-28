# Original synth track for the aid-links reel: 96 bpm, Am-F-C-G, impacts at 3.2 and 14.0
import numpy as np, wave
SR=44100; D=17.0; N=int(SR*D)
L=np.zeros(N); R=np.zeros(N); rng=np.random.default_rng(23)
def note(m): return 440*2**((m-69)/12)
def env(n,a,r):
    e=np.ones(n); A=int(a*SR); Rr=int(r*SR)
    if A: e[:A]=np.linspace(0,1,A)
    if Rr: e[-Rr:]*=np.linspace(1,0,Rr)
    return e
def add(sig,start,gl=1,gr=1):
    s=int(start*SR)
    if s>=N: return
    e=min(N,s+len(sig)); L[s:e]+=sig[:e-s]*gl; R[s:e]+=sig[:e-s]*gr
B=0.625; BAR=2.5
prog=[[45,48,52],[41,45,48],[48,52,55],[43,47,50]]
for i in range(8):
    st=i*BAR; ch=prog[i%4]; n=int((BAR+.3)*SR); tt=np.arange(n)/SR
    for m in ch:
        f=note(m+12); w=sum(np.sin(2*np.pi*f*(1+d)*tt) for d in(-.004,0,.004))/3+.25*np.sin(2*np.pi*2*f*tt)
        add(w*env(n,.5,.7)*0.055,st,1.1,.9)
def pluck(m,l=.45):
    f=note(m); n=int(l*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*f*tt)+.35*np.sin(2*np.pi*3*f*tt))*np.exp(-tt*6)
mel=[76,72,69,72,77,72,76,74]
for j,b in enumerate(np.arange(0.05,3.1,B/2)): add(pluck(mel[j%8])*0.12,b,1.2 if j%2 else .8,.8 if j%2 else 1.2)
for j,b in enumerate(np.arange(3.2,13.8,B/2)):
    ch=prog[int(b//BAR)%4]; add(pluck(ch[(j*2)%3]+24,.3)*0.05,b)
for i in range(8):
    st=i*BAR
    if st+BAR<3.2: continue
    s0=max(st,3.2); e0=min(st+BAR,13.9)
    if e0<=s0: continue
    f=note(prog[i%4][0]-12); n=int((e0-s0)*SR); tt=np.arange(n)/SR
    add(np.tanh(2.2*np.sin(2*np.pi*f*tt))*env(n,.01,.25)*0.12,s0)
def kick():
    n=int(.35*SR); tt=np.arange(n)/SR; f=48+95*np.exp(-tt*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*9)
k=kick()
for b in np.arange(3.2,13.6,B): add(k*0.55,b)
def hat():
    n=int(.05*SR); x=np.diff(np.r_[0,rng.standard_normal(n)]); return x*np.exp(-np.arange(n)/SR*80)
for b in np.arange(3.5,13.6,B): add(hat()*0.11,b,.7,1.3)
for b in np.arange(7.2,13.6,B/2): add(hat()*0.05,b,1.3,.7)
def clap():
    n=int(.18*SR); return rng.standard_normal(n)*np.exp(-np.arange(n)/SR*25)
for b in np.arange(3.8,13.6,2*B): add(clap()*0.10,b)
def riser(l):
    n=int(l*SR); x=rng.standard_normal(n); tt=np.linspace(0,1,n); y=np.zeros(n); a=0
    for i in range(n):
        c=.02+.4*tt[i]**2; a+=c*(x[i]-a); y[i]=a
    return y*tt**2
add(riser(1.4)*0.35,1.8); add(riser(1.0)*0.3,13.0)
def impact():
    n=int(1.6*SR); tt=np.arange(n)/SR
    return np.sin(2*np.pi*45*tt)*np.exp(-tt*3)+rng.standard_normal(n)*np.exp(-tt*12)*.3
add(impact()*0.5,3.2); add(impact()*0.45,14.0)
for m,dt in [(69,0),(72,.12),(76,.24),(81,.36)]: add(pluck(m,2.0)*0.06,14.4+dt)
mix=np.stack([L,R],1)
mix*=np.r_[np.ones(N-int(1.2*SR)),np.linspace(1,0,int(1.2*SR))][:,None]
mix/=np.abs(mix).max()/0.89
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix*32767).astype('<i2').tobytes()); w.close()
