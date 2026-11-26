import numpy as np, wave
SR=44100; D=16.0; N=int(SR*D); t=np.arange(N)/SR
L=np.zeros(N); R=np.zeros(N)
def note(f): return 440*2**((f-69)/12)
def env(n,a,r):
    e=np.ones(n); A=int(a*SR); Rr=int(r*SR)
    if A: e[:A]=np.linspace(0,1,A)
    if Rr: e[-Rr:]*=np.linspace(1,0,Rr)
    return e
def add(sig,start,gl=1,gr=1):
    s=int(start*SR); e=min(N,s+len(sig)); L[s:e]+=sig[:e-s]*gl; R[s:e]+=sig[:e-s]*gr
B=0.5  # 120 bpm
# chords Am F C G, 2 bars each (4 beats=2s)
prog=[[50,53,57],[46,50,53],[53,57,60],[48,52,55]]
for i in range(8):
    st=i*2.0; ch=prog[i%4]; n=int(2.2*SR); tt=np.arange(n)/SR
    for m in ch:
        f=note(m)
        w=sum(np.sin(2*np.pi*f*(1+d)*tt) for d in (-.003,0,.003))/3
        w+=0.3*np.sin(2*np.pi*2*f*tt)
        add(w*env(n,.4,.6)*0.06, st, .9,1.1)
# bass from 5.3
for i in range(8):
    st=i*2.0
    if st<2: continue
    s0=max(st,3.2); f=note(prog[i%4][0]-12); n=int((st+2-s0)*SR); tt=np.arange(n)/SR
    add(np.tanh(2*np.sin(2*np.pi*f*tt))*env(n,.01,.3)*0.12, s0)
# kick
def kick():
    n=int(.35*SR); tt=np.arange(n)/SR; f=50+90*np.exp(-tt*30)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*9)
k=kick()
for b in np.arange(3.25,12.5,B): add(k*0.55,b)
for b in np.arange(13.0,15.0,B): add(k*0.45,b)
# hats
rng=np.random.default_rng(7)
def hat():
    n=int(.06*SR); x=rng.standard_normal(n); x=np.diff(np.r_[0,x]); return x*np.exp(-np.arange(n)/SR*70)
for b in np.arange(3.5,12.5,B): add(hat()*0.12,b,.7,1.3)
for b in np.arange(6.6,12.5,B/2): add(hat()*0.06,b,1.3,.7)
# pluck arpeggio intro + section
def pluck(m,l=.4):
    f=note(m); n=int(l*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*2*f*tt))*np.exp(-tt*7)
arp=[62,65,69,74]
for j,b in enumerate(np.arange(0.1,3.1,B/2)): add(pluck(arp[j%4]+(0 if b<1.6 else -2))*0.13,b,1.2 if j%2 else .8,.8 if j%2 else 1.2)
for j,b in enumerate(np.arange(3.2,12.5,B/2)):
    ch=prog[int(b//2)%4]; add(pluck(ch[j%3]+12,.3)*0.05,b)
# risers (noise sweep) before 5.3 and 12.8
def riser(l):
    n=int(l*SR); x=rng.standard_normal(n); tt=np.linspace(0,1,n)
    y=np.zeros(n); a=0
    for i in range(n):
        c=.02+.4*tt[i]**2; a+=c*(x[i]-a); y[i]=a
    return y*tt**2
add(riser(1.4)*0.35,1.8); add(riser(1.0)*0.3,11.8)
# impacts
def impact():
    n=int(1.6*SR); tt=np.arange(n)/SR
    return (np.sin(2*np.pi*45*tt)*np.exp(-tt*3)+rng.standard_normal(n)*np.exp(-tt*12)*.3)
add(impact()*0.5,3.2); add(impact()*0.45,12.9)
# end chime
for m,dt in [(74,0),(77,.12),(81,.24)]: add(pluck(m,2.0)*0.06,13.4+dt)
mix=np.stack([L,R],1)
mix*=np.r_[np.ones(N-int(1.2*SR)),np.linspace(1,0,int(1.2*SR))][:,None]
mix/=np.abs(mix).max()/0.89
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix*32767).astype('<i2').tobytes()); w.close()
