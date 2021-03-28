import discord
import os
import requests
import json
from dotenv import load_dotenv

client_id = '28753b42e9824af2a5b5277b6dbf3865'
client_secret = '34eaa15829f04f3ba13b439f61a6d1d4'
# URL = "https://accounts.spotify.com/authorize"
# params = {'client_id': '28753b42e9824af2a5b5277b6dbf3865', 'response_type': 'code', "redirect_uri": 'https://example.com/', 'scope': 'playlist-modify-private'}
load_dotenv()
client = discord.Client()
code='AQD-ORMrz71z-HwlT36QL79ElnFw6oIQ9JRnacrtZINBMkDk210f35_gwolauJz-HpL2UI4LKV6V1oeOibWc-8jqXfglwEalnTXfKpOCOH-LNmmE08Oy2h9q9g7ecp_372oicBdl7P023gM5bckJ7iPPnI43UjRdWaItU4yEMVV5lU3KPu1uT0Hb83R5SUXONQ'
# r = requests.get(URL, params=params)
# print(r.url)
# json = json.loads(r.text)
TOKEN=ODI1MDQ1OTMzNjE1MDg3NjM2.YF4N5w.bxvoRFK8E3gxEtHiOFIFzf-b8cA
REFRESH_TOKEN=AQBzTuijm17rcYm69X7O0tauUj0TMPOYhdjkzIeaQ3iUHGKdSZaTu5JiZdV0AAJxTarVoGBDZ2TDedoy_lI2WWxGuSLTaZxSeo4UkC8JJCmqJuVT3XN37O8skvJ-lL1wZuA
refresh_token = os.getenv('REFRESH_TOKEN')
API_URL = 'https://accounts.spotify.com/api/token'
params = {'grant_type': 'refresh_token', 'refresh_token': refresh_token,
'client_id':client_id, 'client_secret': client_secret}

r = requests.post(API_URL, params)

print(r.text)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'spotify' in message.content:
        embeds = message.embeds
        for embed in embeds:
            url =embed.url
            print(embed.url)

        await message.channel.send(url)

client.run(os.getenv('TOKEN'))