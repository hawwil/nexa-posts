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

# ---------- 1. This or that (Nov 16) ----------
render('this-or-that',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.33;left:-300px;top:450px}}
.pill{{position:absolute;top:390px;right:80px}}
h1{{position:absolute;top:445px;right:80px;font-size:96px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
.vs{{position:absolute;top:720px;right:80px;left:80px;display:flex;gap:30px;align-items:stretch}}
.c{{flex:1;{card};padding:34px 30px;text-align:center}}
.c.b{{background:linear-gradient(160deg,rgba(124,58,237,.32),rgba(168,85,247,.10));border:1.5px solid rgba(192,132,252,.6)}}
.n{{width:84px;height:84px;margin:0 auto 14px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900}}
.c b{{display:block;font-size:52px;font-weight:900;direction:ltr}}
.c span{{display:block;font-size:28px;font-weight:600;color:#a99bc7;margin-top:6px}}
.or{{align-self:center;font-size:40px;font-weight:900;color:#c084fc}}
.q{{position:absolute;top:1060px;right:80px;font-size:40px;font-weight:800;color:#e2d7f5}}
.q i{{font-style:normal;color:#c084fc}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">سؤال سريع</div>
<h1>إنت مع مين؟<br><em>اختار رقم</em></h1>
<div class="vs"><div class="c"><div class="n">1</div><b>Canva</b><span>سريع وسهل وقوالب جاهزة</span></div>
<div class="or">ولا</div>
<div class="c b"><div class="n">2</div><b>Photoshop</b><span>تحكم كامل بكل بكسل</span></div></div>
<div class="q">اكتب <i>1</i> أو <i>2</i> بالكومنتات 👇</div>
<div class="foot"><div class="muted">بدك اشتراك رسمي بأي واحد؟ راسلنا</div><div class="h">@nexa.ryx</div></div>
</body></html>''')

# ---------- 2. FAQ story (Nov 17) ----------
render('faq-story',head%(story+f'''
.logo{{top:90px}}
.glow.a{{width:900px;height:900px;background:#7c3aed;opacity:.4;left:-300px;top:700px}}
.pill{{position:absolute;top:540px;right:90px;font-size:34px}}
h1{{position:absolute;top:600px;right:90px;font-size:110px;font-weight:900;line-height:1.25}}
h1 em{{font-style:normal;{grad}}}
.qa{{position:absolute;top:930px;right:90px;left:90px;display:flex;flex-direction:column;gap:18px}}
.it{{{card};padding:18px 36px}}
.it b{{display:block;font-size:38px;font-weight:800;color:#d8b4fe}}
.it span{{display:block;font-size:32px;font-weight:600;color:#f5f0ff;line-height:1.5;margin-top:4px}}
.h{{position:absolute;bottom:170px;right:90px;font-size:40px}}
''')+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">أسئلة بتوصلنا كتير</div>
<h1>قبل ما<br><em>تطلب</em></h1>
<div class="qa">
<div class="it"><b>الاشتراك رسمي؟</b><span>آه، رسمي ومفعّل على إيميلك إنت</span></div>
<div class="it"><b>في ضمان؟</b><span>ضمان كامل طول مدة الاشتراك</span></div>
<div class="it"><b>كيف بدفع؟</b><span dir="rtl">Visa · PayPal · USDT</span></div>
<div class="it"><b>كيف بطلب؟</b><span>ابعتلنا رسالة بالخاص وبنرد عليك بنفس اليوم</span></div>
</div>
<div class="h">@nexa.ryx</div>
</body></html>''',1080,1920)

# ---------- 3. Cheap subscription (Nov 18) ----------
render('cheap-subscription',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.33;left:-300px;top:450px}}
.pill{{position:absolute;top:350px;right:80px}}
h1{{position:absolute;top:400px;right:80px;width:940px;font-size:78px;font-weight:900;line-height:1.3}}
h1 em{{font-style:normal;{grad}}}
.box{{position:absolute;top:630px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px}}
.row{{border-radius:24px;padding:12px 30px;display:flex;gap:24px;align-items:center;background:rgba(255,255,255,.035);border:1px solid rgba(169,155,199,.22)}}
.row.p{{background:linear-gradient(160deg,rgba(124,58,237,.32),rgba(168,85,247,.10));border:1.5px solid rgba(192,132,252,.6)}}
.ic{{width:56px;height:56px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;background:rgba(169,155,199,.15);color:#a99bc7}}
.p .ic{{background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff}}
.row b{{display:block;font-size:32px;font-weight:800}}
.row span{{display:block;font-size:24px;font-weight:600;color:#a99bc7}}
.p span{{color:#d8b4fe}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">قبل ما تشتري</div>
<h1>ليش الاشتراك الرخيص<br><em>بينقطع بعد أسبوع؟</em></h1>
<div class="box">
<div class="row"><div class="ic">✕</div><div><b>حساب مشترك مع عشرات الناس</b><span>بيتسكّر أول ما المنصة تكتشفه</span></div></div>
<div class="row"><div class="ic">✕</div><div><b>تفعيل بطرق مش رسمية</b><span>بيشتغل يومين وبعدها بيوقف</span></div></div>
<div class="row"><div class="ic">✕</div><div><b>ما في ضمان ولا حدا يرد عليك</b><span>بتخسر مصاريك وبترجع من الأول</span></div></div>
<div class="row p"><div class="ic">✓</div><div><b>عند NEXA: رسمي على إيميلك</b><span>بضمان كامل طول مدة الاشتراك</span></div></div>
</div>
<div class="foot"><div class="muted">اسأل قبل ما تدفع، راسلنا</div><div class="h">@nexa.ryx</div></div>
</body></html>''')

# ---------- 4. Contest 2 (Nov 20) ----------
render('contest2',head%f'''
.glow.a{{width:700px;height:700px;background:#7c3aed;opacity:.38;left:-300px;top:380px}}
.pill{{position:absolute;top:390px;right:80px}}
h1{{position:absolute;top:465px;right:80px;font-size:104px;font-weight:900;line-height:1.25}}
h1 em{{font-style:normal;{grad}}}
h2{{position:absolute;top:740px;right:80px;width:920px;font-size:42px;font-weight:700;line-height:1.5;color:#e2d7f5}}
h2 b{{color:#c084fc;direction:ltr;unicode-bidi:isolate}}
.box{{position:absolute;top:900px;right:80px;left:80px;{card};padding:8px 36px}}
.st{{display:flex;align-items:center;gap:24px;padding:14px 0}}
.st+.st{{border-top:1px solid rgba(192,132,252,.15)}}
.n{{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800;flex:none}}
.st b{{font-size:34px;font-weight:800}}
.date{{font-size:30px;font-weight:800}}.date i{{font-style:normal;color:#a99bc7;font-weight:600}}
'''+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">مسابقة NEXA التانية</div>
<h1>اربح شهر<br><em>Gemini أو Claude</em></h1>
<h2>والفايز بيختار الاشتراك اللي بدو إياه 💜</h2>
<div class="box">
<div class="st"><div class="n">1</div><b>تابع <span dir="ltr" style="unicode-bidi:isolate">@nexa.ryx</span></b></div>
<div class="st"><div class="n">2</div><b>لايك للبوست</b></div>
<div class="st"><div class="n">3</div><b>اكتب بالكومنت أي واحد بدك ومنشن صاحب</b></div>
</div>
<div class="foot"><div class="date"><i>السحب: </i>الخميس 26 نوفمبر</div><div class="h">@nexa.ryx</div></div>
</body></html>''')

# ---------- 5. Contest 2 reminder story (Nov 21) ----------
render('contest2-story',head%(story+f'''
.glow.a{{width:900px;height:900px;background:#7c3aed;opacity:.4;left:-300px;top:700px}}
.pill{{position:absolute;top:700px;right:90px;font-size:34px}}
h1{{position:absolute;top:770px;right:90px;font-size:140px;font-weight:900;line-height:1.25}}
h1 em{{font-style:normal;{grad}}}
p{{position:absolute;top:1150px;right:90px;width:900px;font-size:46px;font-weight:700;line-height:1.55;color:#e2d7f5}}
p b{{color:#c084fc;direction:ltr;unicode-bidi:isolate}}
.h{{position:absolute;bottom:380px;right:90px;font-size:40px}}
''')+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">المسابقة التانية</div>
<h1>شهر مجاني<br><em>علينا</em></h1>
<p>اربح شهر <b>Gemini</b> أو <b>Claude</b>. تابع، لايك، واكتب بالكومنت أي واحد بدك ومنشن صاحب. السحب الخميس 26 نوفمبر.</p>
<div class="h">@nexa.ryx</div>
</body></html>''',1080,1920)
