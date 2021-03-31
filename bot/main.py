import discord
import os
import requests
import json
import re
import spotipy
import spotipy.util as util
# from dotenv import load_dotenv

# load_dotenv()
client_id = '28753b42e9824af2a5b5277b6dbf3865'
client_secret = '34eaa15829f04f3ba13b439f61a6d1d4'
redirect_url = 'https://example.com/'
scope = 'playlist-modify-private'

client = discord.Client()
token = util.prompt_for_user_token(username='marcocanto', redirect_uri=redirect_url, scope=scope, client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth=token)
username = 'marcocanto'

spotify.trace = False

def get_song(track_id):
    song = spotify.track(track_id)
    artist = song["artists"][0]["name"]
    name = song["name"]
    return name, artist

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'spotify' in message.content:
        print("Message Content:")
        print(message.content)
        # refresh_token()
        embeds = message.embeds
        url = embeds[0].url
        x = re.findall(r"^(https:\/\/open.spotify.com\/track\/|spotify:user:spotify:playlist:)([a-zA-Z0-9]+)(.*)$",url)
        track_id = x[0][1]
        track_ids = [track_id]
        results = spotify.user_playlist_add_tracks(username, '4uzB4Xdaa3xBEqef3FzF0o',  track_ids)
        print(results)
        name, artist = get_song(track_id)
        
        added_msg = "added **{}** by **{}** to playlist.".format(name, artist)
        print(added_msg)
        await message.channel.send(added_msg)
            
# test

client.run(os.getenv('TOKEN'))