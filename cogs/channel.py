import discord
from discord.ext import commands

class Channel(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # Commands
    @commands.command(brief='clears an amount of messages', description='clears an amount of messages')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int=5):
        await ctx.channel.purge(limit=amount + 1)
    
    @commands.command(pass_context=True, brief='invites an user to a channel', description='clears an amount of messages')
    async def invite(self, ctx, member : discord.Member, *, invite_message=''):
        await member.send(f'> `{str(ctx.message.author)[:-5]}` invited you to `{ctx.message.channel}` channel in `{ctx.message.guild.name}`!\
        \n{invite_message}')
    
    @commands.has_permissions(administrator=True)
    @commands.command(brief='sends a poll message to a channel', description='sends a poll message to a channel')
    async def poll(self, ctx, *, message):
        reaction1 = '👍'
        reaction2 = '👎'
        poll = discord.Embed(title='poll',
        description=f'{message}',
        colour=discord.Colour.purple())
        embed = await ctx.channel.send(embed=poll)
        await embed.add_reaction(reaction1)
        await embed.add_reaction(reaction2)

    @commands.command(brief='locks a channel', description='locks a channel')
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.channel.send("the channel was locked by an admin.")
    
    @commands.command(brief='unlocks a channel', description='unlocks a channel')
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.channel.send("the channel was unlocked by an admin.")

def setup(client):
    client.add_cog(Channel(client))
