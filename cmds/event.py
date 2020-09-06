import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener() 
    async def on_member_join(self, member):
         channel = self.bot.get_channel(int(jdata['Welcome_channel']))
         await channel.send(F'Welcome {member.mention} join us server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F'{member} leave!')

    @commands.Cog.listener()      
    async def on_message(self, msg):
        if msg.content == 'fuck' and msg.author != self.bot.user:
            await msg.channel.send('Hey!Dont say bad words!')

    

def setup(bot):
    bot.add_cog(Event(bot))