import subprocess, os, sys
D='/home/claude/nexa-posts/design'
O=sys.argv[1]
os.makedirs(O+'/html',exist_ok=True)
def render(name,html,w=1080,h=1350):
    f=f'{D}/_tmp_{name}.html'; open(f,'w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',f'--screenshot={O}/{name}.png',f'--window-size={w},{h}','file://'+f],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    os.rename(f,f'{O}/html/{name}.html')
head='<html dir="rtl" lang="ar"><head><link rel="stylesheet" href="base2.css"><style>%s</style></head><body>'
grad='background:linear-gradient(90deg,#e9d5ff,#a855f7);-webkit-background-clip:text;color:transparent;display:inline-block;padding-bottom:14px'
card='border-radius:26px;background:linear-gradient(160deg,rgba(124,58,237,.16),rgba(255,255,255,.03));border:1px solid rgba(192,132,252,.22)'
story='html,body{width:1080px;height:1920px}.logo{top:200px;-webkit-mask-image:linear-gradient(transparent,#000 20%,#000 70%,transparent)}'

# ---------- 1. Which AI (Mon Nov 23) ----------
render('which-ai',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.33;left:-300px;top:450px}}
.pill{{position:absolute;top:380px;right:80px}}
h1{{position:absolute;top:435px;right:80px;font-size:92px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
.vs{{position:absolute;top:720px;right:80px;left:80px;display:flex;gap:24px}}
.c{{flex:1;{card};padding:30px 18px;text-align:center}}
.n{{width:78px;height:78px;margin:0 auto 14px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:900}}
.c b{{display:block;font-size:44px;font-weight:900;direction:ltr}}
.c span{{display:block;font-size:26px;font-weight:600;color:#a99bc7;margin-top:6px;line-height:1.4}}
.q{{position:absolute;top:1075px;right:80px;font-size:40px;font-weight:800;color:#e2d7f5}}
.q i{{font-style:normal;color:#c084fc}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">سؤال سريع</div>
<h1>مساعدك بالشغل<br><em>والدراسة مين؟</em></h1>
<div class="vs">
<div class="c"><div class="n">1</div><b>ChatGPT</b><span>الأشهر وبيعرف<br>بكل إشي</span></div>
<div class="c"><div class="n">2</div><b>Gemini</b><span>مربوط بجوجل<br>وبالـ Gmail</span></div>
<div class="c"><div class="n">3</div><b>Claude</b><span>كتابة وتحليل<br>ملفات طويلة</span></div>
</div>
<div class="q">اكتب <i>1</i> أو <i>2</i> أو <i>3</i> بالكومنتات 👇</div>
<div class="foot"><div class="muted">اشتراكهم الرسمي متوفر عنا</div><div class="h">@nexa.ryx</div></div>
</body></html>''')

# ---------- 2. Poll story (Tue Nov 24) ----------
render('poll-story',head%(story+f'''
.logo{{top:90px}}
.glow.a{{width:900px;height:900px;background:#7c3aed;opacity:.4;left:-300px;top:700px}}
.pill{{position:absolute;top:540px;right:90px;font-size:34px}}
h1{{position:absolute;top:635px;right:90px;font-size:96px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
.qa{{position:absolute;top:990px;right:90px;left:90px;display:flex;flex-direction:column;gap:18px}}
.it{{{card};padding:20px 32px;display:flex;align-items:center;gap:26px}}
.n{{width:64px;height:64px;border-radius:50%;flex:none;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900}}
.it b{{font-size:44px;font-weight:800;direction:ltr}}
.r{{position:absolute;top:1570px;right:90px;font-size:42px;font-weight:800;color:#e2d7f5}}
.r i{{font-style:normal;color:#c084fc}}
.h{{position:absolute;bottom:170px;right:90px;font-size:40px}}
''')+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">صوّت إنت</div>
<h1>شو بدك نوفّر<br><em>الشهر الجاي؟</em></h1>
<div class="qa">
<div class="it"><div class="n">1</div><b>ChatGPT Plus</b></div>
<div class="it"><div class="n">2</div><b>CapCut Pro</b></div>
<div class="it"><div class="n">3</div><b>Netflix</b></div>
<div class="it"><div class="n">4</div><b>Spotify Premium</b></div>
</div>
<div class="r">ردّ على الستوري <i>بالرقم</i> 👇</div>
<div class="h">@nexa.ryx</div>
</body></html>''',1080,1920)

# ---------- 3. Contest 2 last chance story (Wed Nov 25) ----------
render('contest2-last-story',head%(story+f'''
.glow.a{{width:900px;height:900px;background:#7c3aed;opacity:.42;left:-300px;top:700px}}
.pill{{position:absolute;top:700px;right:90px;font-size:34px}}
h1{{position:absolute;top:770px;right:90px;font-size:150px;font-weight:900;line-height:1.25}}
h1 em{{font-style:normal;{grad}}}
p{{position:absolute;top:1215px;right:90px;width:900px;font-size:46px;font-weight:700;line-height:1.55;color:#e2d7f5}}
p b{{color:#c084fc;direction:ltr;unicode-bidi:isolate}}
.h{{position:absolute;bottom:380px;right:90px;font-size:40px}}
''')+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">آخر فرصة ⏳</div>
<h1>السحب<br><em>بكرة</em></h1>
<p>لسا فيك تشارك وتربح شهر <b>Gemini</b> أو <b>Claude</b>. روح على بوست المسابقة، اكتب أي واحد بدك ومنشن صاحب.</p>
<div class="h">@nexa.ryx</div>
</body></html>''',1080,1920)

# ---------- 4. True or false (Fri Nov 27) ----------
render('true-false',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.33;left:-300px;top:450px}}
.pill{{position:absolute;top:360px;right:80px}}
h1{{position:absolute;top:410px;right:80px;font-size:96px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
.box{{position:absolute;top:640px;right:80px;left:80px;display:flex;flex-direction:column;gap:26px}}
.row{{{card};padding:30px 30px;display:flex;gap:24px;align-items:center}}
.n{{width:60px;height:60px;border-radius:50%;flex:none;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900}}
.row b{{font-size:36px;font-weight:800;line-height:1.45}}
.q{{position:absolute;top:1095px;right:80px;font-size:38px;font-weight:800;color:#e2d7f5}}
.q i{{font-style:normal;color:#c084fc}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">اختبر حالك</div>
<h1>صح <em>ولا غلط؟</em></h1>
<div class="box">
<div class="row"><div class="n">1</div><b>الاشتراك الرسمي لازم يكون غالي</b></div>
<div class="row"><div class="n">2</div><b>بدون فيزا ما بتقدر تشترك بـ <span dir="ltr">Canva Pro</span></b></div>
<div class="row"><div class="n">3</div><b>الحساب المشترك آمن زي حسابك الخاص</b></div>
</div>
<div class="q">كم وحدة منهم <i>غلط</i>؟ جاوب بالكومنتات 👇</div>
<div class="foot"><div class="muted">الجواب بالكابشن</div><div class="h">@nexa.ryx</div></div>
</body></html>''')

# ---------- 5. Month thanks + what next (Sun Nov 29) ----------
render('month-thanks',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.36;left:-300px;top:450px}}
.pill{{position:absolute;top:360px;right:80px}}
h1{{position:absolute;top:445px;right:80px;font-size:92px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
h2{{position:absolute;top:705px;right:80px;font-size:40px;font-weight:700;color:#e2d7f5}}
.grid{{position:absolute;top:795px;right:80px;left:80px;display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.c{{{card};padding:24px 26px;display:flex;align-items:center;gap:20px}}
.n{{width:60px;height:60px;border-radius:50%;flex:none;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900}}
.c b{{font-size:34px;font-weight:800}}
.q{{position:absolute;top:1100px;right:80px;font-size:38px;font-weight:800;color:#e2d7f5}}
.q i{{font-style:normal;color:#c084fc}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">شهر كامل معكم 💜</div>
<h1>شكراً إلكم<br><em>والجاي أكبر</em></h1>
<h2>شو بدكم تشوفوا أكتر الشهر الجاي؟</h2>
<div class="grid">
<div class="c"><div class="n">1</div><b>عروض وخصومات</b></div>
<div class="c"><div class="n">2</div><b>مسابقات أكتر</b></div>
<div class="c"><div class="n">3</div><b>شروحات أدوات AI</b></div>
<div class="c"><div class="n">4</div><b>اشتراكات جديدة</b></div>
</div>
<div class="q">اكتب <i>الرقم</i> بالكومنتات 👇</div>
<div class="foot"><div class="muted">رأيكم بيفرق معنا</div><div class="h">@nexa.ryx</div></div>
</body></html>''')
