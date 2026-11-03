import subprocess, sys
S=sys.argv[1]
head='<html dir="rtl" lang="ar"><head><link rel="stylesheet" href="base2.css"><style>%s</style></head><body>'
common='''
.glow.a{width:700px;height:700px;background:#6d28d9;opacity:.33;left:-320px;bottom:80px}
.mini{position:absolute;top:70px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center}
.mini .brand{font-weight:900;font-size:34px;letter-spacing:6px;direction:ltr;color:#fff}
.mini .brand i{font-style:normal;color:#a855f7}
.mini .pg{font-size:26px;color:#a99bc7;font-weight:700;direction:ltr}
.num{position:absolute;top:220px;right:70px;font-size:300px;font-weight:900;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(192,132,252,.55);direction:ltr}
.name{position:absolute;top:560px;right:80px;font-size:108px;font-weight:900;direction:ltr;line-height:1.2}
.what{position:absolute;top:720px;right:80px;width:900px;font-size:44px;font-weight:700;line-height:1.5;color:#e9ddff}
.ex{position:absolute;top:930px;right:80px;left:80px;border-radius:24px;padding:28px 34px;background:linear-gradient(160deg,rgba(124,58,237,.18),rgba(255,255,255,.03));border:1px solid rgba(192,132,252,.25)}
.ex small{display:block;font-size:24px;color:#c084fc;font-weight:800;margin-bottom:6px}
.ex p{font-size:32px;font-weight:600;line-height:1.55;color:#d6cbec}
.swipe{font-size:28px;font-weight:700;color:#a99bc7}
'''
def page(n,total,body,extra='',mini=True):
    m='<div class="mini"><div class="brand">NE<i>X</i>A</div><div class="pg">%d / %d</div></div>'%(n,total) if mini else ''
    return head%(common+extra)+'<div class="glow a"></div>'+m+body+'</body></html>'
tools=[("Gemini","بحث وكتابة وتلخيص بسرعة، ومربوط بخدمات جوجل","اطلب منه يكتبلك سيرة ذاتية احترافية أو يلخصلك ملف PDF طويل"),
("Claude","كتابة وتحليل وبرمجة بمستوى عالي، وبيفهم الملفات الطويلة","اعطيه أفكارك وخليه يرتبلك خطة شغل أو رسالة رسمية"),
("Canva Pro","تصميم بوستات وفيديوهات بقوالب جاهزة وأدوات ذكية","صمم بوست كامل بدقيقة، وشيل خلفية أي صورة بضغطة"),
("Adobe Firefly","توليد صور وتعديلها بالكتابة بس","اكتب وصف الصورة اللي بدك إياها وبتطلعلك بثواني"),
("ChatGPT","مساعد شامل للأسئلة والكتابة والترجمة","ترجم إيميل أو صحح نص بالإنجليزي قبل ما تبعته")]
T=len(tools)+2
pages=[]
pages.append(page(1,T,'''<div class="logo" style="opacity:.55;top:-40px"></div>
<div class="pill" style="position:absolute;top:400px;right:80px">احفظ البوست</div>
<h1 style="position:absolute;top:470px;right:80px;font-size:118px;font-weight:900;line-height:1.25">5 أدوات<br><span style="background:linear-gradient(90deg,#e9d5ff,#a855f7);-webkit-background-clip:text;color:transparent;display:inline-block;padding-bottom:12px">ذكاء اصطناعي</span></h1>
<p style="position:absolute;top:830px;right:80px;font-size:46px;font-weight:700;color:#d6cbec">بتوفرلك ساعات من الشغل</p>
<div class="foot"><div class="swipe">اسحب ←</div><div class="h">@nexa.ryx</div></div>''',mini=False))
for i,(n,w,e) in enumerate(tools):
    pages.append(page(i+2,T,f'''<div class="num">0{i+1}</div><div class="name">{n}</div><div class="what">{w}</div>
<div class="ex"><small>جرّبها هيك</small><p>{e}</p></div>
<div class="foot"><div class="swipe">اسحب ←</div><div class="h">@nexa.ryx</div></div>'''))
pages.append(page(T,T,'''<div class="logo" style="top:-20px"></div>
<h1 style="position:absolute;top:470px;right:80px;font-size:92px;font-weight:900;line-height:1.3">بدك اشتراك<br>بأي وحدة منهم؟</h1>
<p style="position:absolute;top:740px;right:80px;width:900px;font-size:38px;font-weight:600;line-height:1.6;color:#d6cbec">اشتراكات رسمية بضمان كامل وبأحسن سعر، والدفع بالطريقة اللي بتناسبك.</p>
<div style="position:absolute;top:930px;right:80px;background:linear-gradient(90deg,#7c3aed,#a855f7);padding:20px 54px;border-radius:60px;font-size:40px;font-weight:800">راسلنا بالخاص</div>
<div class="foot"><div class="muted">Visa · PayPal · USDT</div><div class="h">@nexa.ryx</div></div>''',mini=False))
for i,p in enumerate(pages):
    f=f'{S}/car/s{i+1}.html'; open(f,'w').write(p)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--allow-file-access-from-files','--hide-scrollbars',f'--screenshot={S}/car/s{i+1}.png','--window-size=1080,1350','file://'+f],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
from PIL import Image
ims=[Image.open(f'{S}/car/s{i+1}.png') for i in range(T)]
c=Image.new('RGB',(1080*4,1350*2),'#000')
for i,im in enumerate(ims): c.paste(im,((i%4)*1080,(i//4)*1350))
c.resize((1440,900)).save(f'{S}/car/sheet.png')
