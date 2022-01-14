import os
import discord
from discord.utils import get
from discord.ext import commands, tasks
import json

class removechannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="Removes the channel the command was sent in from the list of monitored channels.")
    @commands.has_role("mod")
    async def removechannel(self, ctx):
        with open(r"data.json", "r") as file:
            data = json.load(file)
            channels = data['channels']

            if ctx.channel.id in channels:
                data['channels'].remove(ctx.channel.id)
                msg = discord.Embed(title="Removed!", color=0x7289da)
                await ctx.channel.send(embed=msg)
            else:
                msg = discord.Embed(title="This channel isn\'t in the list.", color=0x7289da)
                await ctx.channel.send(embed=msg)

        with open(r"data.json", 'w') as f:
            json.dump(data, f, indent=4)

def setup(bot: commands.Bot):
    bot.add_cog(removechannel(bot))
