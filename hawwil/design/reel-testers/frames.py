import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+sys.argv[1]); await pg.evaluate('document.fonts.ready')
        for t in sys.argv[2:]:
            await pg.evaluate(f'setT({t})'); await pg.screenshot(path=f'/tmp/claude-0/-home-claude/5b6814f7-63ed-5b01-a601-43ef71754e88/scratchpad/f{t}.png')
        await b.close()
asyncio.run(main())
