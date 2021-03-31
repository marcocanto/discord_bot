#!/bin/sh
export SPOTIPY_CACHE='{"access_token": "BQD66fSfV-6fVM3M1RdkkWOgC7hOWXnzeA7PjRos7rtRL34T2DznLGxbEc-I7hxhvKuJkvo-5S9xM-6qR3kc7R5Gu6vfCKoznPIjFwi2N-9IkKdG2LwSVitvRljZFljZx9su8bXGoFIGWEI0K3ZDigi4XC_XtQJDqfSKAoApLlmn0D3D6Q", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQB3i7wJ4cKDBaRxb_-oe2K__5qmrYtiQynoQqH0yv2Mr_mZ0Va6M5c6n-p94l0cLoYx9sqd6j0h-bRvfKgn1IAp8JKK-IRs_dn-YWfI6bCl73ml6kt6kUBW8voM0xB4aIw", "scope": "playlist-modify-private", "expires_at": 1617224429}'

printf '%s\n' "$SPOTIPY_CACHE" > .cache-marcocanto
python3 bot/main.py