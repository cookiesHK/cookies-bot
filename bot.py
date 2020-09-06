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
    await bot.change_presence(activity = discord.Game('Made By IAmcookies'))


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])

