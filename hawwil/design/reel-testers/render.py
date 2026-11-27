import asyncio,subprocess,sys
from playwright.async_api import async_playwright
FPS=30;DUR=17
async def main():
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart','reel_tmp.mp4'],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+sys.argv[1]); await pg.evaluate('document.fonts.ready')
        for i in range(FPS*DUR):
            await pg.evaluate(f'setT({i/FPS})')
            ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
        await b.close()
    ff.stdin.close(); assert ff.wait()==0
asyncio.run(main())
