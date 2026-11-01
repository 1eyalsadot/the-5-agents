#!/usr/bin/env python3.13
"""
Convert a Hebrew/RTL Markdown report (chen/Memory/*.md) to a branded PDF.
Usage: python3.13 md_to_pdf.py <input.md> <output.pdf> [title]

Requires: `pip install markdown` and the pre-installed Playwright/Chromium
(see repo session environment notes — PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers).
Used by Reuven (not Chen directly — she has no Bash) after every weekly
tender-scan report, per the standing user convention (added 01/11/2026):
every weekly scan also gets exported as PDF alongside the .md file.
"""
import sys
import os
import markdown

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
from playwright.sync_api import sync_playwright

def convert(md_path, pdf_path, title=None):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    body_html = markdown.markdown(text, extensions=["tables", "nl2br", "sane_lists"])

    if not title:
        title = os.path.splitext(os.path.basename(md_path))[0]

    html = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{
    font-family: "Segoe UI", "Arial", sans-serif;
    direction: rtl;
    text-align: right;
    color: #0B1F3A;
    line-height: 1.6;
    font-size: 13px;
    padding: 0 8px;
  }}
  h1 {{ color: #082D69; font-size: 22px; border-bottom: 3px solid #F8D325; padding-bottom: 8px; }}
  h2 {{ color: #082D69; font-size: 17px; margin-top: 26px; border-right: 4px solid #F8D325; padding-right: 10px; }}
  h3 {{ color: #1767A5; font-size: 14px; }}
  a {{ color: #1767A5; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 12px; }}
  th {{ background: #082D69; color: #fff; padding: 6px 8px; text-align: right; }}
  td {{ padding: 6px 8px; border-bottom: 1px solid #E6EBF3; vertical-align: top; }}
  tr:nth-child(even) td {{ background: #F5F8FC; }}
  strong {{ color: #082D69; }}
  hr {{ border: none; border-top: 1px solid #E6EBF3; margin: 20px 0; }}
  .footer-brand {{
    position: fixed; bottom: 0; right: 0; left: 0; text-align: center;
    font-size: 10px; color: #9AA7BC; padding: 6px 0;
  }}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    tmp_html = pdf_path + ".tmp.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium", headless=True)
        page = browser.new_page()
        page.goto("file://" + os.path.abspath(tmp_html))
        page.wait_for_timeout(200)
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "18mm", "bottom": "16mm", "right": "14mm", "left": "14mm"},
            display_header_footer=True,
            header_template="<div></div>",
            footer_template='<div style="font-size:9px;width:100%;text-align:center;color:#9AA7BC;">URIEL — <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
        )
        browser.close()

    os.remove(tmp_html)
    print("wrote", pdf_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: md_to_pdf.py <input.md> <output.pdf> [title]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
