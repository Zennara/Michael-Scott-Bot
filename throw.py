import discord
from discord.utils import get
from discord.ext import commands, tasks


class throw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(description="The throw command accepts three parameters.\nThis command is case insensitive.\nIt needs at, a user, and something to throw.\nFor usernames with spaces use double quotation marks. \n\nExamples:\n`-throw at elmocultist a bag of kittens`\n`-throw at \"elmo cultist\" a bag of kittens`")
    async def throw(self, ctx, at, person, *items):
        personIs = False
        async for member in ctx.guild.fetch_members(limit=None):
            #dont try to change this trust me it doesnt work
            if str(member)[:-5].lower() == str(person).lower():
                personIs = True
                items = ' '.join(str(item) for item in items)
                msg = discord.Embed(title=f'{ctx.author.name} threw {items} at {member.name}!',color=0x7289da)
                await ctx.channel.send(embed=msg)
                await ctx.channel.send(f"{member.mention}")

        if not personIs:
            msg = discord.Embed(title=f"{person} isn't in the database.",color=0x7289da)
            await ctx.channel.send(embed=msg)

def setup(bot: commands.Bot):
    bot.add_cog(throw(bot))
