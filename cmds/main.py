import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'Network Delay:**{round(self.bot.latency*1000)}** (ms)')

    @commands.command()
    async def info(self, ctx):
       embed=discord.Embed(title="INFO", description="About the bot", color=0x0091ff)
       embed.set_author(name="Made by IAmcookies #0001")
       embed.add_field(name="Make in", value="Hong Kong", inline=True)
       embed.add_field(name="Learn code in", value="Proladon channel", inline=True)
       embed.set_footer(text="©IAmcookies 2020 All Rights Reserved")
       await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
  
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'> **BANNED** User {member}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f'> User **{member}** get kick')

def setup(bot):
    bot.add_cog(Main(bot))