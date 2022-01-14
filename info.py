import discord
from discord.ext import commands, tasks

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="Information on the Micheal Scott bot.")
    async def info(self, ctx):
        embed = discord.Embed(
                title = "Micheal Scott Features:",
                description = "Keeps count of all the characters sent in channels Micheal Scott is set to monitor.\nHas daily, weekly, monthly, and alltime character count leaderboards.\nHas achievements like reaching 10k characters or being first on a leaderboard.",
                color=0x7289da
            )
        await ctx.channel.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(info(bot))
