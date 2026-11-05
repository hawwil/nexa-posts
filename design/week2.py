import subprocess, os, sys
D='/home/claude/nexa-posts/design'
O=sys.argv[1]
os.makedirs(O+'/html',exist_ok=True)
def render(name,html,w=1080,h=1350):
    f=f'{D}/_tmp_'+name.replace('/','_')+'.html'; open(f,'w').write(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files',f'--screenshot={O}/{name}.png',f'--window-size={w},{h}','file://'+f],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    os.rename(f,f'{O}/html/'+name.replace('/','_')+'.html')
head='<html dir="rtl" lang="ar"><head><link rel="stylesheet" href="base2.css"><style>%s</style></head><body>'
grad='background:linear-gradient(90deg,#e9d5ff,#a855f7);-webkit-background-clip:text;color:transparent;display:inline-block;padding-bottom:14px'

# ---------- Carousel: Canva free vs Pro ----------
cc='''
.glow.a{width:700px;height:700px;background:#6d28d9;opacity:.33;left:-320px;bottom:80px}
.mini{position:absolute;top:70px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center}
.mini .brand{font-weight:900;font-size:34px;letter-spacing:6px;direction:ltr;color:#fff}
.mini .brand i{font-style:normal;color:#a855f7}
.mini .pg{font-size:26px;color:#a99bc7;font-weight:700;direction:ltr}
.num{position:absolute;top:190px;right:70px;font-size:220px;font-weight:900;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(192,132,252,.55);direction:ltr}
.name{position:absolute;top:440px;right:80px;width:920px;font-size:84px;font-weight:900;line-height:1.3}
.cmp{position:absolute;top:690px;right:80px;left:80px;display:flex;flex-direction:column;gap:24px}
.row{border-radius:24px;padding:26px 34px;display:flex;gap:26px;align-items:center}
.row.f{background:rgba(255,255,255,.035);border:1px solid rgba(169,155,199,.22)}
.row.p{background:linear-gradient(160deg,rgba(124,58,237,.30),rgba(168,85,247,.10));border:1.5px solid rgba(192,132,252,.6)}
.ic{width:62px;height:62px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900}
.f .ic{background:rgba(169,155,199,.15);color:#a99bc7}
.p .ic{background:linear-gradient(135deg,#7c3aed,#a855f7);color:#fff}
.row small{display:block;font-size:24px;font-weight:800;margin-bottom:2px}
.f small{color:#a99bc7}.p small{color:#d8b4fe}
.row p{font-size:34px;font-weight:700;line-height:1.45}
.f p{color:#bdb2d6}.p p{color:#f5f0ff}
.swipe{font-size:28px;font-weight:700;color:#a99bc7}
'''
def cpage(n,T,body,mini=True):
    m='<div class="mini"><div class="brand">NE<i>X</i>A</div><div class="pg">%d / %d</div></div>'%(n,T) if mini else ''
    return head%cc+'<div class="glow a"></div>'+m+body+'</body></html>'
items=[("قوالب وعناصر بريميوم","قسم كبير من القوالب والصور والعناصر مقفول عليك","أكتر من 100 مليون صورة وفيديو وعنصر وقالب بريميوم"),
("إزالة الخلفية بضغطة","مش متوفرة، بدك برنامج تاني أو موقع خارجي","شيل خلفية أي صورة أو فيديو بثانية"),
("تغيير المقاس السحري","بتعيد التصميم من أول وجديد لكل منصة","حوّل بوست لستوري أو غلاف يوتيوب بضغطة وحدة"),
("هويتك البصرية جاهزة","ألوانك وخطوطك بتدخلها يدوي كل مرة","شعارك وألوانك وخطوطك جاهزين بكل تصميم"),
("مساحة التخزين","5GB بس","1TB، يعني 200 ضعف")]
T=len(items)+2
pages=[cpage(1,T,f'''<div class="logo" style="opacity:.55;top:-40px"></div>
<div class="pill" style="position:absolute;top:400px;right:80px">Canva</div>
<h1 style="position:absolute;top:470px;right:80px;font-size:104px;font-weight:900;line-height:1.3">المجاني ولا<br><span style="{grad}">Canva Pro؟</span></h1>
<p style="position:absolute;top:860px;right:80px;width:900px;font-size:44px;font-weight:700;line-height:1.5;color:#d6cbec">5 أشياء بتخسرها لما تضل على النسخة المجانية</p>
<div class="foot"><div class="swipe">اسحب ←</div><div class="h">@nexa.ryx</div></div>''',mini=False)]
for i,(t,f,p) in enumerate(items):
    pages.append(cpage(i+2,T,f'''<div class="num">0{i+1}</div><div class="name">{t}</div>
<div class="cmp"><div class="row f"><div class="ic">✕</div><div><small>المجاني</small><p>{f}</p></div></div>
<div class="row p"><div class="ic">✓</div><div><small>Canva Pro</small><p>{p}</p></div></div></div>
<div class="foot"><div class="swipe">اسحب ←</div><div class="h">@nexa.ryx</div></div>'''))
pages.append(cpage(T,T,'''<div class="logo" style="top:-20px"></div>
<h1 style="position:absolute;top:470px;right:80px;font-size:84px;font-weight:900;line-height:1.3">جاهز تنقل تصاميمك<br>لمستوى تاني؟</h1>
<p style="position:absolute;top:720px;right:80px;width:900px;font-size:38px;font-weight:600;line-height:1.6;color:#d6cbec">اشتراك Canva Pro رسمي على إيميلك، بضمان كامل وبأحسن سعر.</p>
<div style="position:absolute;top:920px;right:80px;background:linear-gradient(90deg,#7c3aed,#a855f7);padding:20px 54px;border-radius:60px;font-size:40px;font-weight:800">راسلنا بالخاص</div>
<div class="foot"><div class="muted">Visa · PayPal · USDT</div><div class="h">@nexa.ryx</div></div>''',mini=False))
os.makedirs(O+'/canva',exist_ok=True)
for i,p in enumerate(pages): render(f'canva/s{i+1}',p)

# ---------- Post: how to order ----------
howto='''
.glow.a{width:700px;height:700px;background:#7c3aed;opacity:.33;left:-300px;top:420px}
.pill{position:absolute;top:370px;right:80px}
h1{position:absolute;top:425px;right:80px;font-size:88px;font-weight:900;line-height:1.3}
h1 em{font-style:normal;%s}
.box{position:absolute;top:690px;right:80px;left:80px;border-radius:26px;background:linear-gradient(160deg,rgba(124,58,237,.16),rgba(255,255,255,.03));border:1px solid rgba(192,132,252,.22);padding:8px 36px}
.st{display:flex;align-items:center;gap:26px;padding:17px 0}
.st+.st{border-top:1px solid rgba(192,132,252,.15)}
.n{width:64px;height:64px;border-radius:50%%;background:linear-gradient(135deg,#7c3aed,#a855f7);display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;flex:none}
.st b{display:block;font-size:38px;font-weight:800}
.st span{display:block;font-size:26px;font-weight:600;color:#a99bc7}
.cta{background:linear-gradient(90deg,#7c3aed,#a855f7);padding:14px 40px;border-radius:50px;font-size:30px;font-weight:800;color:#fff}
'''%grad
render('howto',head%howto+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">كيف تطلب</div>
<h1>طلبك من NEXA<br><em>بـ 3 خطوات بس</em></h1>
<div class="box">
<div class="st"><div class="n">1</div><div><b>ابعتلنا شو بدك</b><span>اسم الاشتراك أو رابط المنتج، بالخاص</span></div></div>
<div class="st"><div class="n">2</div><div><b>ادفع بالطريقة اللي بتناسبك</b><span dir="rtl">Visa · PayPal · USDT</span></div></div>
<div class="st"><div class="n">3</div><div><b>استلم التفعيل</b><span>اشتراك رسمي بضمان كامل</span></div></div>
</div>
<div class="foot"><div class="cta">اطلب بالخاص</div><div class="h">@nexa.ryx</div></div></body></html>''')

# ---------- Post: we pay for you ----------
pay='''
.glow.a{width:620px;height:620px;background:#6d28d9;opacity:.35;left:-260px;bottom:120px}
.pill{position:absolute;top:380px;right:80px}
h1{position:absolute;top:435px;right:80px;font-size:90px;font-weight:900;line-height:1.28}
h1 em{font-style:normal;%s}
.sub{position:absolute;top:690px;right:80px;width:900px;font-size:34px;font-weight:600;line-height:1.6;color:#c9bde4}
.grid{position:absolute;top:830px;right:80px;left:80px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.card{border-radius:22px;padding:24px 28px;background:linear-gradient(160deg,rgba(124,58,237,.18),rgba(255,255,255,.03));border:1px solid rgba(192,132,252,.22);font-size:32px;font-weight:800}
.card span{display:block;font-size:24px;color:#a99bc7;font-weight:600;margin-top:2px}
.cta{background:linear-gradient(90deg,#7c3aed,#a855f7);padding:14px 40px;border-radius:50px;font-size:30px;font-weight:800;color:#fff}
'''%grad
render('pay-for-you',head%pay+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">خدمة ندفع عنك</div>
<h1>ما عندك فيزا؟<br><em>إحنا بندفع عنك</em></h1>
<p class="sub">ابعتلنا رابط أي منتج رقمي، وإحنا بنشتريه وبنوصّلك إياه مفعّل.</p>
<div class="grid">
<div class="card">تطبيقات مدفوعة<span>آيفون وأندرويد</span></div>
<div class="card">اشتراكات<span>شهرية أو سنوية</span></div>
<div class="card">كورسات أونلاين<span>من أي منصة</span></div>
<div class="card">أدوات وبرامج<span>تصميم، AI، مونتاج</span></div>
</div>
<div class="foot"><div class="cta">ابعتلنا الرابط</div><div class="h">@nexa.ryx</div></div></body></html>''')

# ---------- Stories ----------
sc='''html,body{width:1080px;height:1920px}
.glow.a{width:900px;height:900px;background:#7c3aed;opacity:.4;left:-300px;top:700px}
.logo{top:250px;-webkit-mask-image:linear-gradient(transparent,#000 20%,#000 70%,transparent)}
.pill{position:absolute;top:720px;right:90px;font-size:34px}
h1{position:absolute;top:790px;right:90px;font-size:140px;font-weight:900;line-height:1.2}
h1 span{background:linear-gradient(90deg,#e9d5ff,#a855f7);-webkit-background-clip:text;color:transparent;display:inline-block;padding-bottom:16px}
p{position:absolute;top:1160px;right:90px;width:900px;font-size:46px;font-weight:700;line-height:1.55;color:#e2d7f5}
p b{color:#c084fc;direction:ltr;unicode-bidi:isolate}
.h{position:absolute;bottom:380px;right:90px;font-size:40px}
.chips{position:absolute;top:1330px;right:90px;left:90px;display:flex;flex-wrap:wrap;gap:18px;direction:ltr;justify-content:flex-end}
.chip{border-radius:40px;padding:12px 30px;font-size:36px;font-weight:800;background:linear-gradient(160deg,rgba(124,58,237,.28),rgba(255,255,255,.04));border:1px solid rgba(192,132,252,.45)}
'''
render('draw-story',head%sc+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">مسابقة NEXA الأولى</div>
<h1>اليوم<br><span>السحب!</span></h1>
<p>مين رح يربح شهر <b>Canva Pro</b>؟ اسم الفائز بينزل على الصفحة، خليك قريب 👀</p>
<div class="h">@nexa.ryx</div></body></html>''',1080,1920)
render('ask-story',head%sc.replace('top:1160px','top:1180px').replace('top:1330px','top:1360px').replace('bottom:380px','bottom:240px')+'''<div class="glow a"></div><div class="logo"></div>
<div class="pill">سؤال الأسبوع</div>
<h1>شو الاشتراك<br><span>اللي بدك ياه؟</span></h1>
<p>ردّ على الستوري باسمه، وبنشتغل نوفّر الأكثر طلباً.</p>
<div class="chips"><div class="chip">ChatGPT</div><div class="chip">Gemini</div><div class="chip">Claude</div><div class="chip">Adobe</div><div class="chip">Canva Pro</div><div class="chip">...</div></div>
<div class="h">@nexa.ryx</div></body></html>''',1080,1920)
