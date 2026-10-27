import asyncio, sys
from playwright.async_api import async_playwright
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/work/preview/out12"
JOBS = [
    ("index", "light", 820, ["__top__", "__mid__"], "home"),
    ("concepts/index", "dark", 820, ["__top__"], "topics"),
    ("1-electrostatics/index", "light", 820, ["__top__"], "u1"),
    ("1-electrostatics/06-circulation-and-boundary-conditions", "light", 820, ["__top__", "__bottom__"], "l06"),
    ("3-maxwell-and-waves/22-phasor-maxwell-equations-and-damped-waves", "dark", 820, ["__top__"], "l22"),
    ("concepts/boundary-conditions", "light", 820, ["__top__", "__mid__"], "bc"),
    ("concepts/skin-depth", "dark", 820, ["__top__"], "sd"),
    ("concepts/motional-emf", "light", 380, ["__top__"], "memf-phone"),
    ("index", "dark", 380, ["__top__"], "home-phone"),
]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for page, theme, width, targets, label in JOBS:
            pg = await b.new_page(viewport={"width": width, "height": 1000}, device_scale_factor=1)
            await pg.goto(f"file://{OUT}/{page}.html")
            if theme == "dark":
                await pg.evaluate("document.documentElement.setAttribute('saved-theme','dark')")
            await pg.wait_for_timeout(300)
            w = await pg.evaluate("document.documentElement.scrollWidth")
            ov = await pg.evaluate("""()=>[...document.querySelectorAll('.katex-display')].map(e=>e.scrollWidth-e.clientWidth).filter(x=>x>2).length""")
            for i, t in enumerate(targets):
                if t == "__bottom__":
                    await pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                if t == "__mid__":
                    await pg.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")
                await pg.wait_for_timeout(150)
                out = f"/home/claude/work/preview/b12-{label}-{theme}-{i}.png"
                await pg.screenshot(path=out)
                print(out.split('/')[-1], "scrollWidth", w, "overflow", ov)
            await pg.close()
        await b.close()
asyncio.run(main())
