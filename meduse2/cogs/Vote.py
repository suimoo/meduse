import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
from typing import Optional
import datetime
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polls = {}

    class ModalClass(discord.ui.Modal, title = "投票選項"):
        def __init__(self, title, count):
            super().__init__(title=title)
            for i in range(count):
                self.add_item(discord.ui.TextInput(label=f"選項{i+1}"))
        
            #self.endtime=now+mins
    #@app_commands.command()
    #async def on_interaction(self, interaction: discord.Interaction):
        #if interaction.type == discord.InteractionType.component:
            #if interaction.custom_id == "button1":
                #await interaction.response.send_message(content="Button clicked!", ephemeral=False)
            #elif interaction.custom_id == "button3":
                #await interaction.response.send_message(content="Button smashed!", ephemeral=False)
    
        async def on_submit(self, interaction: discord.Interaction):
            #await interaction.response.send_message("88")
            #options = [self.children[i].value for i in range(len(self.children))]
            reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
            arr=[0, 0, 0, 0, 0]
            embed=discord.Embed(title=self.title, description="請踴躍投票", color=0xe570e7)
            embed.set_thumbnail(url=str(jdata["h"]))
            embed.add_field(name="選項1:",value=f"{self.children[0].value}",  inline=False)
            embed.add_field(name="選項2:",value=f"{self.children[1].value}",  inline=False)
            for j in range(3,len(self.children)+1):
                embed.add_field(name=f"選項{j}:",value=f"{self.children[j-1].value}",  inline=False)
            embed.set_footer(text=f"投票一定有風險，事前請先詳閱根本沒有的公開說明書")
            await interaction.response.send_message(embed = embed)
            msg = await interaction.original_response()
            for j in range(len(self.children)):
                await msg.add_reaction(reactions[j])
            """
            @commands.Cog.listener
            async def on_reaction_add(self, reaction, user):
                for i in range(len(self.children)):
                    if reaction.emoji==reactions[i]:
                        arr[i]+=1
                for i in range(len(self.children)):
                    await reaction.message.delete(reactions[i])
            """
            #view = ViewClass(timeout = 30)
            #view = discord.ui.View()
            #for k in range (1, len(self.children)+1):
                #button = discord.ui.Button(discord.ui.Button(label = f"選項{k}", style = discord.ButtonStyle.primary, custom_id=f"button{k}"))
                #view.add_item(button)
            #view=ViewClass()
            #await interaction.response.send_message(embed = embed)
            #button = await bot.wait_for("button_click", check = lambda i: i.custom_id in ["button1", "button3"]
            
            """
            class ViewClass(discord.ui.View):
                def __init__(self, timeout: float | None = 180):
                    super().__init__(timeout = timeout)
                    for i in range (1, len(self.children)+1):
                        self.add_item(discord.ui.Button(label = f"選項{i}", style = discord.ButtonStyle.primary, custom_id=f"button{i}")) #添加一個Button到ViewClass中

                async def callback(self, interaction: discord.Interaction):
                    if interaction.type == discord.InteractionType.component:
                        if interaction.custom_id == "button1":
                            await interaction.response.send_message(content="1")
                        elif interaction.custom_id == "button2":
                            await interaction.response.send_message(content="2")
                        elif interaction.custom_id == "button3":
                            await interaction.response.send_message(content="3")
                        elif interaction.custom_id == "button4":
                            await interaction.response.send_message(content="4")
                        elif interaction.custom_id == "button5":
                            await interaction.response.send_message(content="5")
                    
                    embed=discord.Embed(title=self.title, description="請踴躍投票", color=0xe570e7)
                    embed.set_thumbnail(url=str(jdata["h"]))
                    embed.add_field(name="選項1:",value=f"{self.children[0].value}_目前票數:{arr[0]}",  inline=False)
                    embed.add_field(name="選項2:",value=f"{self.children[1].value}_目前票數:{arr[1]}",  inline=False)
                    for j in range(3,len(self.children)+1):
                        embed.add_field(name=f"選項{j}:",value=f"{self.children[j-1].value}_目前票數:{arr[j-1]}",  inline=False)
                    embed.set_footer(text="投票一定有風險，事前請先詳閱根本沒有的公開說明書")
                    await interaction.response.edit_message(embed = embed, view = view)
                    """


    @app_commands.command(name = "vote", description="創建一個投票")
    @app_commands.describe(title="投票標題", count="選項數量(最多5)", time="什麼時候結束(例.18:30)")
    #async def vote(self, interaction: discord.Interaction, count: int, option: Optional[str]=None):
    async def vote(self, interaction: discord.Interaction, title: str, count: int, time: Optional[str]=None):
        if count>5:
            await interaction.response.send_message("太多了啦")
            return
        elif count<2:
            await interaction.response.send_message("辦投票幹嘛")
            return
        modal = self.ModalClass(title, count, time)
        #now=datetime.datetime.now().strftime("%H%M")
        await interaction.response.send_modal(modal)
        if time!=None:
          await interaction.followup.send(f"即將開始投票，預計結束時間`{time}`")


async def setup(bot):
    await bot.add_cog(Vote(bot))