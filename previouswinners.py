import os
import discord
from discord.utils import get
from discord.ext import commands, tasks
import json

class previouswinners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="The previouswinners command accepts two parameters, category and amount.\nThe accepted categories are monthly, weekly, and daily.\nFor amount you can enter a number or all.\n\nExamples:\n`-previouswinners daily all`\n`-previouswinners weekly 10`")
    async def previouswinners(self, ctx, category, specifics):
        with open(r"data.json", "r") as file:
                data = json.load(file)
                previousWinners = list(data['Winners'][str(category.title())])
                previousWinners = previousWinners[::-1]
                description = "(most recent to last)\n"
                counter = 0

                if str(specifics) == 'all':
                    for i in list(previousWinners):
                        counter += 1
                        person = await self.bot.fetch_user(i)
                        description += f"{counter}. {person.name}\n"
                else:
                    for i in list(previousWinners[:int(specifics)]):
                        counter += 1
                        person = await self.bot.fetch_user(i)
                        description += f"{counter}. {person.name}\n"

                if description == '':
                    description = "There are no previous winners."

                msg = discord.Embed(title=f"Previous {category.title()} Winners:",description=description,color=0x7289da)
                await ctx.channel.send(embed=msg)


def setup(bot: commands.Bot):
    bot.add_cog(previouswinners(bot))
