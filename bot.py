import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        embeds = message.embeds
        for embed in embeds:
            url =embed.url
            print(embed.url)
        await message.channel.send(url)

client.run('ODI1MDQ1OTMzNjE1MDg3NjM2.YF4N5w.9468dwHGDTrc8C3mC0bocMnej2E')