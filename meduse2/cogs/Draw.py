import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from typing import Optional
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

#清空籤筒
def clear():
    with open('setting.json', 'r', encoding='utf8') as jfile:
        jdata["draw_option_num"]=0
        for i in range(15):
            jdata["draw_options"][i]="-1"
    with open('setting.json', 'w', encoding='utf8') as jfile:
        json.dump(jdata,jfile,indent=4)


class Draw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="draw_set", description="在籤筒中加入選項")
    @app_commands.describe(option="加入選項")
    async def draw_set(self, interaction: discord.Interaction, option: str):
        if int(jdata["draw_option_num"])>=15:
            await interaction.response.send_message("加入失敗，超過數量上限")
        
        else:
            with open('setting.json', 'r', encoding='utf8') as jfile:
                jdata["draw_options"][jdata["draw_option_num"]]=option
            with open('setting.json', 'w', encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)

            await interaction.response.send_message(f"已成功加入選項:{option}")
            
            with open('setting.json', 'r', encoding='utf8') as jfile:
                jdata["draw_option_num"]+=1
            with open('setting.json', 'w', encoding='utf8') as jfile:
                json.dump(jdata,jfile,indent=4)


    @app_commands.command(name="draw_reset", description="清空籤筒")
    async def draw_reset(self, interaction: discord.Interaction):
        clear()
        await interaction.response.send_message(f"已清空籤筒")


    @app_commands.command(name="draw_content", description="查看籤筒內容物")
    async def draw_content(self, interaction: discord.Interaction):
        if jdata["draw_options"][0]=="-1" :
            await interaction.response.send_message("籤筒是空的喔喔喔，可以使用/draw_set指令在籤筒中加入選項")
        else:
            embed=discord.Embed(title="Sui籤筒", description="以下是目前籤筒中已有的籤", color=0x00FFFF)
            for i in range(jdata["draw_option_num"]):
                embed.add_field(name=jdata["draw_options"][i],value=f"{i+1}號籤",  inline=True)
            embed.set_footer(text="抽籤一定有風險，事前請先詳閱根本沒有的公開說明書( ･ิω･ิ)")
            await interaction.response.send_message(embed=embed)
    
    
    @app_commands.command(name="draw", description="開始抽籤吧")
    async def draw(self, interaction: discord.Interaction):
        if jdata["draw_options"][0]=="-1" :
            await interaction.response.send_message("籤筒是空的，請先確定您已使用/draw_set指令在籤筒中加入選項")
        else:
        #發送抽籤結果
            embed=discord.Embed(title="Sui籤結果", description="見證奇蹟的時刻", color=0xF9F900)
            result=random.randint(1, jdata["draw_option_num"])
            embed.add_field(name=jdata["draw_options"][result-1],value=f"結果為{result}號籤",  inline=False)
            embed.set_footer(text="恭喜中獎d(`･∀･)b")
            await interaction.response.send_message(embed=embed)
        #清空籤筒
            clear()
        
    
async def setup(bot):
    await bot.add_cog(Draw(bot))