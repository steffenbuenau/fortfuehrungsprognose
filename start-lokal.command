#!/bin/bash
# Startet die Seite lokal unter http://localhost:8765 und öffnet den Browser (Mac).
cd "$(dirname "$0")/docs" || exit 1
PORT=8765
echo "Seite läuft unter http://localhost:$PORT  –  Fenster schließen oder Ctrl+C zum Beenden."
( sleep 1; open "http://localhost:$PORT" ) &
python3 -m http.server "$PORT" --bind 127.0.0.1
