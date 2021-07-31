# importing discord.py and cogs
import discord
import os
from discord.ext import commands


# Command prefix
client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print("Bot is online.")
# Welcome message
@client.event
async def on_member_join(member,ctx):
    print(f'{member} has joined the server.')
    await ctx.send(f'{member} has joined the server')

# Leave message
@client.event
async def on_member_removed(member,ctx):
    print(f'{member} has left the server')
    await ctx.send(f'{member} has left the server')

# Ping pong command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

# Bot status
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Among us'))

# Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    

# Running the client
client.run('ODY5MzQ3MTUzNzA3OTQxOTI4.YP84oQ.JZ2XfCbANqKRXxAz1VqunxhA87g')