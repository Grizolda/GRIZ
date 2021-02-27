import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.utils import get


filtered_message = "You are muted from the server for 5 minutes.\nNext time be nice!"

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Commands
    @commands.command(brief='kicks a member', description='kicks a member')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.send(f"{ctx.author.mention} kicked {member.mention} from the server.")

    @commands.command(brief='bans a member', description='bans a member')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.send(f"{ctx.author.mention} baned {member.mention}.")
    
    @commands.has_permissions(ban_members=True)
    @commands.command(brief='unbans a baned member', description='unbans a baned member')
    async def unban(self, ctx, *, member):
        pass
    
    @commands.command(brief='mutes a member', description='mutes a member')
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason=filtered_message):
        role = get(member.server.roles, name="muted")
        await member.add_roles(role)
        await member.send(reason)

    # Events
    @Cog.listener()
    async def on_message(self, message):
        filtered_words = ['cat', 'dog']
        for word in filtered_words:
            if word in message.content.lower().split():
                await message.delete()
                
        #await self.client.process_commands(message)
    


    # Errors
    @kick.error
    @ban.error
    async def unknown_member(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Member is not found.")

def setup(client):
    client.add_cog(Moderation(client))
