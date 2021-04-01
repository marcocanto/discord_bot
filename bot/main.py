import discord
import os
import requests
import json
import re
import spotipy
import spotipy.util as util
# from dotenv import load_dotenv

# load_dotenv()

client = discord.Client()

username = 'marcocanto'
scope = 'playlist-modify-private'

cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path='.cache-marcocanto')
auth_manager = spotipy.oauth2.SpotifyOAuth(scope='playlist-modify-private',
                                            cache_handler=cache_handler, 
                                            show_dialog=True)

spotify = spotipy.Spotify(auth_manager=auth_manager)

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
    
    print("Message Content:")
    print(message.content)

    if 'spotify' in message.content:
        msg = message.content
        x = re.findall(r"(https:\/\/open.spotify.com\/track\/|spotify:user:spotify:playlist:)([a-zA-Z0-9]+)(.*)",msg)
        print(x)
        track_id = x[0][1]
        track_ids = [track_id]
        results = spotify.user_playlist_add_tracks(username, '4uzB4Xdaa3xBEqef3FzF0o',  track_ids)
        print(results)
        name, artist = get_song(track_id)
        
        added_msg = "Added **{}** by **{}** to the amalgamation.".format(name, artist)
        print(added_msg)
        await message.channel.send(added_msg)
            
# test

client.run(os.getenv('TOKEN'))