import os
import discord
from discord.utils import get
from discord.ext import commands, tasks
import json

class leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="The leaderboard command accepts a single category parameter.\nThe categories are alltime, monthly, weekly, and daily.\n\nExample:\n`-leaderboard alltime`")
    async def leaderboard(self, ctx, category):

        if category == "alltime":
            with open(r"data.json", "r") as file:
                description = ""
                data = json.load(file)
                alltimeleaderboard = data['CharCountAllTime']
                allTimeList = []
                allcount = 0
                allTimeList = sorted(alltimeleaderboard.items(), key=lambda x: x[1], reverse=True)

                for i in allTimeList:
                    if allcount < 5:
                        allcount += 1
                        person = await self.bot.fetch_user(i[0])
                        description += f"{allcount}. {person.name}: {i[1]}\n"
                msg = discord.Embed(title="All Time Leaderboard",description=description,color=0x7289da)
                await ctx.channel.send(embed=msg)

        elif category == "daily":
            with open(r"data.json", "r") as file:
                description = ""
                data = json.load(file)
                dailyleaderboard = data["ResettingCharCounts"]['CharCountDaily']
                dailycount = 0
                dailyList = []
                dailyList = sorted(dailyleaderboard.items(), key=lambda x: x[1], reverse=True)

                for i in dailyList:
                    if dailycount < 5:
                        dailycount += 1
                        person = await self.bot.fetch_user(i[0])
                        description += f"{dailycount}. {person.name}: {i[1]}\n"
                msg = discord.Embed(title="Daily Leaderboard",description=description,color=0x7289da)
                await ctx.channel.send(embed=msg)

        elif category == "monthly":
            with open(r"data.json", "r") as file:
                description = ""
                data = json.load(file)
                monthlyleaderboard = data["ResettingCharCounts"]['CharCountMonthly']
                monthlyList = []
                monthlycount = 0

                monthlyList = sorted(monthlyleaderboard.items(), key=lambda x: x[1], reverse=True)
                for i in monthlyList:
                    if monthlycount < 5:
                        monthlycount += 1
                        person = await self.bot.fetch_user(i[0])
                        description += f"{monthlycount}. {person.name}: {i[1]}\n"
                msg = discord.Embed(title="Monthly Leaderboard",description=description,color=0x7289da)
                await ctx.channel.send(embed=msg)

        elif category == "weekly":
            with open(r"data.json", "r") as file:
                description = ""
                data = json.load(file)
                weeklyleaderboard = data["ResettingCharCounts"]['CharCountWeekly']
                weeklyList = []
                weeklycount = 0

                weeklyList = sorted(weeklyleaderboard.items(), key=lambda x: x[1], reverse=True)
                for i in weeklyList:
                    if weeklycount < 5:
                        weeklycount += 1
                        person = await self.bot.fetch_user(i[0])
                        description += f"{weeklycount}. {person.name}: {i[1]}\n"
                msg = discord.Embed(title="Weekly Leaderboard",description=description,color=0x7289da)
                await ctx.channel.send(embed=msg)

def setup(bot: commands.Bot):
    bot.add_cog(leaderboard(bot))
