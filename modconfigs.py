import discord
from discord.ext import commands

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
    # Kick command
    @commands.command()
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.send(f'{member.mention} has been kicked from this server')

    # Ban command
    @commands.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.send(f'{member.mention} has been banned from this server')

    # Unban command 
    @commands.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_descriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_descriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(moderation(client))