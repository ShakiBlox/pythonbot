import discord
from discord.ext import commands

class clearcmd(commands.Cog):

    def __init__(self, client):
        self.client = client

    commands.command()
    async def clear(ctx ,amount=0):
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(clearcmd(client))