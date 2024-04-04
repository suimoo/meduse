import discord
from discord.ext import commands
from discord import app_commands
import json
import random
from discord.app_commands import Choice
from typing import Optional

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Luck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="luck", description="來看看今天運勢如何吧")
    @app_commands.describe(times="要抽幾次(可不選)")
    async def luck(self, interaction: discord.Interaction, times:Optional[int]=None):
        if times==None:
            lucknum=random.randint(1, 100)
            if lucknum<=50:
                random_luck="吉"
            elif lucknum<=60:
                random_luck="中吉"
            elif lucknum<=70:
                random_luck="小吉"
            elif lucknum<=80:
                random_luck="凶"
            elif lucknum<=85:
                random_luck="大吉"
            elif lucknum<=88:
                random_luck="大凶"
            elif lucknum<=90:
                random_luck="ㄔ ㄐ ㄐ"
            elif lucknum<=99:
                random_luck="末吉"
            elif lucknum==100:
                random_luck="太扯啦!!還不快去抽卡!!!"
            random_item = random.choice(jdata["lucky_item"])
            embed=discord.Embed(title="御Sui籤σ ﾟ∀ ﾟ) ﾟ∀)σ", description="看看你今日運勢如何吧", color=0xe570e7)
            embed.set_thumbnail(url=str(jdata["h"]))
            embed.add_field(name=f"今日運勢:{random_luck}",value="這是你的今日運勢",  inline=False)
            embed.add_field(name=f"幸運物:{random_item}",value="請務必拿到手",  inline=False)
            embed.set_footer(text="抽籤一定有風險，事前請先詳閱根本沒有的公開說明書")
            await interaction.response.send_message(embed=embed)
            
        a=b=c=d=e=f=g=h=i=0
        if times>=1000000:
            await interaction.response.send_message("ㄔㄐㄐ啦乾")
            return
        for x in range(times):
            #await interaction.response.defer()
            r = random.randint(1, 100)
            if r <=50:
                a+=1
            elif r <=60:
                d+=1
            elif r <=70:
                c+=1
            elif r <=80:
                g+=1
            elif r <=85:
                b+=1
            elif r <=88:
                f+=1
            elif r <=90:
                i+=1
            elif r <=99:
                e+=1
            elif r ==100:
                h+=1
        total = a + b + c + d + e + f + g + h + i
        embed=discord.Embed(title="sui便你抽", description="請不要輸入一百萬以上\n他可能會當掉，違者罰你吃窩ㄐㄐ", color=0xffdbdb)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/964132714812952596/986196214347354163/DF94DFC0-6058-4C53-907A-ADC2D4840ECB1.png?width=1358&height=1358&ex=6615064c&is=6602914c&hm=8036a36f994792a86dfc855bac169d14a88d8a4a2e2b2a4c3095d2d7616f48f6&")
        if h!=0:    
            embed.add_field(name="太扯啦!!還不快去抽卡!!!", value=h, inline=True)
        if i!=0:
            embed.add_field(name="ㄔㄐㄐ", value=i, inline=False)
        if b!=0:
            embed.add_field(name="大吉", value=b, inline=False)
        if a!=0:
            embed.add_field(name="吉", value=a, inline=False)
        if d!=0:
            embed.add_field(name="中吉", value=d, inline=False)
        if c!=0:
            embed.add_field(name="末吉", value=c, inline=False)
        if g!=0:
            embed.add_field(name="凶", value=g, inline=False)
        if f!=0:
            embed.add_field(name="大凶", value=f, inline=False)
        embed.set_footer(text=f"共計抽了{total}次，符合上限規定")
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="luck_rate", description="祈願機率")
    async def luck_rate(self, interaction: discord.Interaction):
        embed=discord.Embed(title="御Sui籤σ ﾟ∀ ﾟ) ﾟ∀)σ", description="詞條機率一覽", color=0xe570e7)
        embed.set_thumbnail(url=str(jdata["h"]))
        embed.add_field(name="太扯啦!!\n還不快去抽卡!!!:", value="1%", inline=False)
        embed.add_field(name="ㄔ ㄐ ㄐ:", value="2%", inline=False)
        embed.add_field(name="大吉:", value="5%", inline=False)
        embed.add_field(name="吉:", value="50%", inline=False)
        embed.add_field(name="中吉:", value="10%", inline=False)
        embed.add_field(name="小吉:", value="10%", inline=False)
        embed.add_field(name="末吉:", value="9%", inline=False)
        embed.add_field(name="凶:", value="10%", inline=False)
        embed.add_field(name="大凶:", value="3%", inline=False)
        embed.set_footer(text="每種幸運物出現機率一致")
        await interaction.response.send_message(embed=embed)
        

async def setup(bot):
    await bot.add_cog(Luck(bot))