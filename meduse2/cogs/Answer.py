import json
import discord
from discord.ext import commands
from discord import app_commands
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Answer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="answer_book", description="解答之書")
    @app_commands.describe(question="有什麼貓餅")
    async def answer(self, interaction: discord.Interaction, question: str):
      await interaction.response.defer()
      
      #叫爬蟲
      async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        url = 'https://answersbook.iwhy.dev/'
        await page.goto(url)
        try:
          await page.click("button.z-0")
          print("pressed")
        except Exception as e:
          print("Cannot press the button")
        
        #等待回應然後取得網頁內容
        await page.wait_for_timeout(3000)
        response = await page.content()
        soup = BeautifulSoup(response, 'html.parser')
        answer = soup.select_one('h2.text-5xl')
        print(answer.text)
        
        #輸出
        embed=discord.Embed(title="解答之書σ ﾟ∀ ﾟ) ﾟ∀)σ", description=question, color=0xe570e7)
        embed.set_thumbnail(url=str(jdata["h"]))
        embed.add_field(name=f"解答:{answer.text}", value='', inline=False)
        embed.set_footer(text="答案僅供參考，請自行評估風險")
        await interaction.followup.send(embed=embed)

        browser.close()
        
async def setup(bot):
    await bot.add_cog(Answer(bot))