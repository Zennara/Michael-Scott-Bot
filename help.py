import os
import discord
from discord.ext import commands, tasks

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

#this will only work if theres a single command per cog

    @commands.command(name='help')
    async def help(self, ctx, cmd=''):
        description = ''
        if cmd == '':
            for key in self.bot.cogs.keys():
                description += f'{key}\n'

            description += "\nEnter '-help {command}' for more information on a command."

            helpEmbed = discord.Embed(
                title = "List of commands:",
                description = description, color=0x7289da
            )
            await ctx.channel.send(embed=helpEmbed)
        else:
            cog = self.bot.get_cog(cmd.lower())
            for c in cog.walk_commands():
                print(c.description)
                if str(c) == str(cmd.lower()):
                    description = c.description

            embed = discord.Embed(title=f'{cmd.title()} Command:',description=description, color=0x7289da)
            await ctx.channel.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(help(bot))
