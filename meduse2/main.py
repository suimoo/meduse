import os
import discord
from discord.ext import commands
from discord import app_commands
import json
import asyncio
import datetime

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)


@bot.event
async def on_ready():
    channel1 = bot.get_channel(1222577229830295582)
    channel2 = bot.get_channel(1026831620159848458)
    slash = await bot.tree.sync()
    print(f"{bot.user} 起床囉")
    print(f"已載入 {len(slash)} 個斜線指令")
    now=int(datetime.datetime.now().strftime("%H"))
    if now+8 > 24:
      now-=24
    now+=8
    greeting=""
    if 6 < now < 18:
      greeting="Bonjour,"
    else:
      greeting="Bonsoir,"
    embed = discord.Embed(title = (f"{greeting} Méduse上線了喔喔喔喔喔喔"))
    await channel1.send("早安")
    await channel2.send(embed = embed)

    #清空籤筒(詳見Draw.py)
    with open('setting.json', 'r', encoding='utf8') as jfile:
        jdata["draw_option_num"]=0
        for i in range(15):
            jdata["draw_options"][i]="-1"
    with open('setting.json', 'w', encoding='utf8') as jfile:
        json.dump(jdata,jfile,indent=4)

@bot.command()
async def hi(ctx):
    await ctx.send("hi")
    
@bot.tree.command(name = "hello", description = "早安")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("嗨")
    
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"就在剛剛 Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'就在剛剛 UnLoaded {extension} done!')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'就在剛剛 ReLoaded {extension} done!')

async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"loaded {filename[:-3]} success")
            
bot.setup_hook = setup_hook
    
async def main():
    async with bot:
        await bot.start(jdata['token'])

asyncio.run(main())