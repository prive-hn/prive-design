#!/usr/bin/env python3
"""Render banner HTML to Shopify-ready JPG images using Playwright."""

import asyncio
import base64
import os
import zipfile
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent
BANNERS_HTML = ROOT / "banners.html"
SVG_PATH = ROOT / "assets" / "logo-wordmark-v4.svg"
OUTPUT_DIR = ROOT / "dist"
ZIP_PATH = ROOT / "prive-banners-shopify.zip"

# Shopify recommended banner dimensions.
DESKTOP_W, DESKTOP_H = 2000, 980
MOBILE_W, MOBILE_H = 750, 735

BANNERS = [
    (1, "hero"),
    (2, "nuevos"),
    (3, "coleccion-regalos"),
    (4, "ofertas"),
    (5, "genero"),
    (6, "mas-vendido"),
    (7, "exclusivos"),
    (9, "dia-madre"),
    (10, "san-valentin"),
    (11, "navidad"),
]


async def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    svg_b64 = base64.b64encode(SVG_PATH.read_bytes()).decode()
    data_uri = f"data:image/svg+xml;base64,{svg_b64}"

    html = BANNERS_HTML.read_text(encoding="utf-8").replace(
        "assets/logo-wordmark-v4.svg", data_uri
    )

    tmp_html = Path("/tmp/prive-banners-inline.html")
    tmp_html.write_text(html, encoding="utf-8")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 2400, "height": 1200},
            device_scale_factor=1,
        )
        page = await context.new_page()
        await page.goto(f"file://{tmp_html}", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)

        exported: list[Path] = []

        for bid, name in BANNERS:
            print(f"Banner {bid}: {name}")

            for variant, selector, width, height in [
                ("desktop", f"#banner-{bid} .banner-frame", DESKTOP_W, DESKTOP_H),
                ("mobile", f"#banner-{bid} .mobile-frame", MOBILE_W, MOBILE_H),
            ]:
                try:
                    element = await page.query_selector(selector)
                    if not element:
                        print(f"  ✗ {variant}: {selector} not found")
                        continue

                    await page.evaluate(
                        """
                        ({ selector, width, height }) => {
                            const frame = document.querySelector(selector);
                            if (frame) {
                                frame.style.width = `${width}px`;
                                frame.style.height = `${height}px`;
                                frame.style.overflow = 'hidden';
                            }
                        }
                        """,
                        {"selector": selector, "width": width, "height": height},
                    )
                    await page.wait_for_timeout(300)

                    output = OUTPUT_DIR / f"prive-{name}-{variant}.jpg"
                    await element.screenshot(path=str(output), quality=92)
                    exported.append(output)
                    print(f"  ✓ {variant}: {output} ({output.stat().st_size / 1024:.0f}KB)")
                except Exception as exc:
                    print(f"  ✗ {variant}: {exc}")

        await browser.close()

    print(f"\nCreating zip: {ZIP_PATH}")
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in exported:
            if file_path.exists():
                zf.write(file_path, file_path.name)
                print(f"  {file_path.name} ({file_path.stat().st_size / 1024:.0f}KB)")

    print(f"\n✓ Done! {len(exported)} files → {ZIP_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
