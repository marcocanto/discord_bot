#!/bin/sh

# uncomment this line for local deployment
# export SPOTIPY_CACHE=(env spotify cache)

printf '%s\n' "$SPOTIPY_CACHE" > .cache-marcocanto
python3 bot/main.py