import discord
from discord.ext import commands
from discord import app_commands
import json

#intents = discord.Intents.default()
#intents.message_content = True
#client = discord.Client(intents = intents)
#tree = app_commands.CommandTree(client) 沒用暫存

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)


@bot.event
async def on_ready():
    channel = bot.get_channel(1222577229830295582)
    slash = await bot.tree.sync()
    print(f"{bot.user} 起床囉")
    print(f"已載入 {len(slash)} 個斜線指令")
    await channel.send("早安")

@bot.command()
async def hi(ctx):
    await ctx.send("hi")
    
@bot.tree.command(name = "hello", description = "jojo")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("嗨")
        
bot.run(jdata['token'])