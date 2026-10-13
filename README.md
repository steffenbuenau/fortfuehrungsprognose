# Fortführungsprognose selbst erstellen

Quelltext der Website **https://fortfuehrungsprognose-selbst-erstellen.de** – ein Leitfaden für Geschäftsführer zur Fortbestehensprognose nach § 19 InsO, mit Kostenübersicht und einem Prompt zum Selbermachen.

Betreiberin: von Bünau Operations GmbH, Berlin.

## Aufbau

- `docs/` – die Website (reines HTML und CSS, keine Abhängigkeiten, keine Cookies). GitHub Pages veröffentlicht diesen Ordner.
- `docs/prompt.txt` – der Prompt. Er ist zusätzlich in `docs/index.html` eingebettet.
- `tools/sync_prompt.py` – überträgt Änderungen aus `prompt.txt` in `index.html`.
- `start-lokal.command` – startet die Seite lokal auf dem Mac (Doppelklick).

## Ändern und veröffentlichen

1. Dateien in `docs/` bearbeiten. Nach Änderungen am Prompt: `python3 tools/sync_prompt.py`.
2. Lokal prüfen: Doppelklick auf `start-lokal.command` oder `docs/index.html` im Browser öffnen.
3. Committen und pushen. GitHub Pages veröffentlicht die neue Fassung nach etwa einer Minute.

## Regelmäßig prüfen

- Rechtsstand und Preise (Stand: Oktober 2026).
- Die BAFA-Förderung läuft nach aktuellem Stand Ende 2026 aus. Den Absatz in `docs/index.html` dann anpassen oder entfernen.

## Lizenz

Texte © von Bünau Operations GmbH. Den Prompt dürfen Sie für Ihr eigenes Unternehmen frei verwenden und anpassen.
