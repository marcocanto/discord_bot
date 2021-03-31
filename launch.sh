#!/bin/sh

printf '%s\n' "$SPOTIPY_CACHE" > .cache-marcocanto
python3 bot/main.py