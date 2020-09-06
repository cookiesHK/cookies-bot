import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='c!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(752024081850826854)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(752024081850826854)
    await channel.send(F'{member} leave!')
    
bot.run('NzUyMDE3MjcwNDA1ODU3Mzkz.X1RgqQ.a6FQSEbGlATLE-Tcfra_ydPGtx0')
