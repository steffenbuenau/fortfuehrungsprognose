"""Kopiert docs/prompt.txt in den <pre id="prompt-text">-Block von docs/index.html.

Nach jeder Änderung am Prompt ausführen:  python3 tools/sync_prompt.py
"""
import html
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent / "docs"
prompt = (root / "prompt.txt").read_text(encoding="utf-8").rstrip("\n")
index_path = root / "index.html"
page = index_path.read_text(encoding="utf-8")
new_page, n = re.subn(
    r'(<pre id="prompt-text">)(.*?)(</pre>)',
    lambda m: m.group(1) + html.escape(prompt, quote=False) + m.group(3),
    page,
    flags=re.S,
)
if n != 1:
    raise SystemExit("Prompt-Block in index.html nicht gefunden.")
index_path.write_text(new_page, encoding="utf-8")
print("index.html aktualisiert.")
