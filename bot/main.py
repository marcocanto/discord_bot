import discord
import os
import requests
import json
import re
from dotenv import load_dotenv

client_id = '28753b42e9824af2a5b5277b6dbf3865'
client_secret = '34eaa15829f04f3ba13b439f61a6d1d4'

load_dotenv()
client = discord.Client()
code='AQD-ORMrz71z-HwlT36QL79ElnFw6oIQ9JRnacrtZINBMkDk210f35_gwolauJz-HpL2UI4LKV6V1oeOibWc-8jqXfglwEalnTXfKpOCOH-LNmmE08Oy2h9q9g7ecp_372oicBdl7P023gM5bckJ7iPPnI43UjRdWaItU4yEMVV5lU3KPu1uT0Hb83R5SUXONQ'

refresh_token = os.getenv('REFRESH_TOKEN')
API_URL = 'https://accounts.spotify.com/api/token'
params = {'grant_type': 'refresh_token', 'refresh_token': refresh_token,
'client_id':client_id, 'client_secret': client_secret}
PLAYLIST_URL = 'https://api.spotify.com/v1/playlists/spotify:playlist:4uzB4Xdaa3xBEqef3FzF0o/tracks'
SONG_URL = 'https://api.spotify.com/v1/tracks/'

r = requests.post(API_URL, params)
access_token = r.json().get("access_token")

headers = {
    "Authorization": 'Bearer ' + access_token,
    "Content-Type": "application/json"
    }

def get_song(track_id):
    r = requests.post(PLAYLIST_URL, headers=headers, params=params)
    song = requests.get(SONG_URL + track_id, headers = headers)
    song_json = song.json()
    artist = song_json["artists"][0]["name"]
    name = song_json["name"]
    return name, artist

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'spotify' in message.content:
        embeds = message.embeds
        if len(embeds) == 1:
            url = embeds[0].url
            x = re.findall(r"^(https:\/\/open.spotify.com\/track\/|spotify:user:spotify:playlist:)([a-zA-Z0-9]+)(.*)$",url)
            track_id = x[0][1]
            uri = ["spotify:track:" + track_id]
            params = {"uris": uri}
            try:
                r = requests.post(PLAYLIST_URL, headers=headers, params=params)
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)

            name, artist = get_song(track_id)
            added_msg = "added **{}** by **{}** to playlist.".format(name, artist)
            await message.channel.send(added_msg)
            print("Added {} by {} to playlist.".format(name, artist))

client.run(os.getenv('TOKEN'))