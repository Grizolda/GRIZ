import discord
from discord.ext import commands


class Member(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief='returns the user\'s rank', description='returns the user\'s rank')
    async def rank(self, ctx, member : discord.Member=None):
        member = member or ctx.author

        if len(member.roles) == 1:
            emb_colour = discord.Colour.light_gray()
        else:
            emb_colour = member.colour

        card = discord.Embed(title=f'{member.name}', colour=emb_colour)
        card.add_field(name='rank', value='None', inline=True)
        card.add_field(name='level', value='0', inline=True)
        card.add_field(name='roles', value=f'{[role.mention for role in member.roles if not role.name == "@everyone"]}', inline=False)
        card.set_thumbnail(url=member.avatar_url)

        await ctx.channel.send(embed=card)
    
    @commands.has_permissions(administrator=True)
    @commands.command(brief='tags a member\\role', description='tags a member\\role')
    async def tag(self, ctx, tag : discord.Role):
        role_members = []
        for member in ctx.guild.members:
            for role in member.roles: 
                if role == tag:
                    role_members.append(member.mention)
        
        emb = discord.Embed(title=tag.name,
         description=f'{role_members}',
         colour=tag.colour)
        await ctx.channel.send(embed=emb)

def setup(client):
    client.add_cog(Member(client))
