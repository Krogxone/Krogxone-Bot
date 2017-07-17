#Lowkey Lokiii's id
#<@150766748818341888>
import discord
import logging
import asyncio
from discord.ext import commands

client = discord.Client()
logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='with myself'))

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}! Be sure to follow the rules and enjoy your stay!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    if message.content.startswith('.test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#    elif message.content.startswith('.rip'):
#        client.kick(discord.Object(id='150766748818341888')
    elif message.content.startswith('.info'):
        print('This bot is in Alpha stage.')
        print('---------------------------')
        print("You can find basically all my info by clicking on Krogxone's profile")
#    elif message.content.startswith('.voice'):
#        client.join_voice_channel
    elif message.content.startswith('.help'):
        await client.send_message(message.channel, 'Currently there is no help section, will be added soon.')
    elif message.content.startswith('.getav'):
        await client.send_message(discord.Object(id='329845405737025537'), discord.User.avatar_url)
    elif message.content.startswith('.cp'):
        await client.send_file(discord.Object(id='329845405737025537'), 'cp.png')
    elif message.content.startswith('.tp'):
        await client.send_file(discord.Object(id='329845405737025537'), 'tracer.jpg')
        

client.run('MjEyMTI4MTE5NzYxNDAzOTA0.DE5YTw.6ipTmDluf1U5v326QKXv4HcaWig')
