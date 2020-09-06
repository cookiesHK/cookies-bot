import discord
from discord.ext import commands
import json
import os

with open('setting.json', 'r') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} leave!')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
