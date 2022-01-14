import os
import discord
from discord.utils import get
from discord.ext import commands, tasks
import json

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="The profile command accepts a single user parameter.\nThis command is case insensitive.\nFor users with spaces in their username you must put the name in double quotation marks.\n\nExamples:\n`-profile elmocultist`\n`-profile \"elmo cultist\"`")
    async def profile(self, ctx, *person):
        description = ""
        person = ' '.join(str(p) for p  in person)
        title = f"{person} isn't in the database"
        async for member in ctx.guild.fetch_members(limit=None):
            if str(member)[:-5].lower() == str(person).lower():
                with open(r"data.json", 'r') as file:
                    data = json.load(file)

                    if str(member.id) in data["CharCountAllTime"]:
                        lltimechoroctercount = data["CharCountAllTime"][str(member.id)]
                    else:
                        lltimechoroctercount = 0

                    if str(member.id) in data["Bumps"]:
                        bumps = data["Bumps"][str(member.id)]
                    else:
                        bumps = "0"

                    description += f"All time character count: {lltimechoroctercount}\n"
                    description += f"All time bumps: {bumps}\n"
                    title=f"{person}'s Profile:"

                    try:
                        description += '\nAchievements:\n'
                        for achievement in data["Achievements"][str(member.id)]:
                            try:
                                if int(list(dict(achievement).values())[0]) != 1:
                                    description += f"{str(list(dict(achievement).keys())[0])} {str(list(dict(achievement).values())[0])} times."
                                else:
                                    description += f"{str(list(dict(achievement).keys())[0])} {str(list(dict(achievement).values())[0])} time."

                            except ValueError:
                                description += f'{achievement}\n'
                    except KeyError:
                        description += "No achievements."

        msg = discord.Embed(title=title,description=description,color=0x7289da)
        await ctx.channel.send(embed=msg)

def setup(bot: commands.Bot):
    bot.add_cog(profile(bot))
