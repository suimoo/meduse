import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add", description="算")
    async def add(self, interaction: discord.Interaction, a: int, b: int):
        await interaction.response.send_message("{} + {} = {}".format(a, b, a+b))
        
    @app_commands.command(name="say", description="要讓Méduse說什麼")
    async def say(self, interaction: discord.Interaction, text: str):
        await interaction.channel.send(text)
        
    @app_commands.command(name="croissant", description="Croissant")
    async def croissant(self, interaction: discord.Interaction):
        await interaction.response.send_message("Quaso!")
        
    @app_commands.command(name="wakeup", description="起床重睡")
    @app_commands.describe(member = "要@誰", count = "幾次(不要太多)")
    async def wakeup(self, interaction: discord.Interaction, member: discord.Member, count: int): 
        if count>20:
            await interaction.response.send_message("太多了..要滿出來了...")
        else:
            await interaction.response.defer()
            for i in range(count):
                await interaction.followup.send(f'{member.mention} 起床')
                #await interaction.channel.send(f'{member.mention} 起床')

    @commands.command()
    async def u(self, ctx):
        await ctx.send("u")

async def setup(bot):
    await bot.add_cog(Cmds(bot))