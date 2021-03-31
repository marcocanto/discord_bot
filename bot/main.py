import discord
import os
import requests
import json
import re
from dotenv import load_dotenv

load_dotenv()
client_id = '28753b42e9824af2a5b5277b6dbf3865'
client_secret = '34eaa15829f04f3ba13b439f61a6d1d4'

client = discord.Client()

refresh_token = os.getenv('REFRESH_TOKEN')
API_URL = 'https://accounts.spotify.com/api/token'
r_params = {'grant_type': 'refresh_token', 'refresh_token': refresh_token,
'client_id':client_id, 'client_secret': client_secret}
PLAYLIST_URL = 'https://api.spotify.com/v1/playlists/4uzB4Xdaa3xBEqef3FzF0o/tracks'
SONG_URL = 'https://api.spotify.com/v1/tracks/'

r = requests.post(API_URL, r_params)
access_token = r.json().get("access_token") 
headers = {
    "Authorization": 'Bearer ' + access_token,
    "Content-Type": "application/json"
    }

def get_song(track_id):
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
                print(track_id)
                r = requests.post(PLAYLIST_URL, headers=headers, params=params)
                print(r.content)
            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                r = requests.post(API_URL, r_params)
                access_token = r.json().get("access_token") 
                r = requests.post(PLAYLIST_URL, headers=headers, params=params)
                

            name, artist = get_song(track_id)
            added_msg = "added **{}** by **{}** to playlist.".format(name, artist)
            await message.channel.send(added_msg)
            print(added_msg)
            
# test

client.run(os.getenv('TOKEN'))