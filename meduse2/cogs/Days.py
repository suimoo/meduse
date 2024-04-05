import discord
from discord.ext import commands
import json,asyncio,datetime
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
  

class Days(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
        async def interval():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                now=datetime.datetime.now().strftime("%H%M")
                self.channel= self.bot.get_channel(1219982397244837898)
                if now == "0400":
                    random_member = random.sample(jdata["day"],6 )
                    f1=random_member[0]
                    f2=random_member[1]
                    f3=random_member[2]
                    f4=random_member[3]
                    f5=random_member[4]
                    f6=random_member[5]
                    embed=discord.Embed(title="原神日曆：", description="出事我不負責~~~", color=0xc800ff)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/917631875307147264/953142358206185493/IMG_2247.jpg")
                    embed.add_field(name="宜 : ", value="今天內在原神中\"可能\"適合做的事喔喔喔", inline=True)
                    embed.add_field(name=f1, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    embed.add_field(name=f2, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    embed.add_field(name=f3, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    embed.add_field(name="忌 : ", value="今天內在原神中\"可能\"不適合做的事喔喔喔", inline=False)
                    embed.add_field(name=f4, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    embed.add_field(name=f5, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    embed.add_field(name=f6, value="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", inline=False)
                    await self.channel.send(embed=embed)
                    
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(1)
                    pass
                     
        self.bg_task=self.bot.loop.create_task(interval())

async def setup(bot):
    await bot.add_cog(Days(bot))