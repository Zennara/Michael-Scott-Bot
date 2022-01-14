import discord
from discord.utils import get
import os
from discord.ext import commands, tasks
import json
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='-',intents=intents)

#-----On Ready-----#
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    activity = discord.Streaming(name="Best Boss in the World",url='https://www.youtube.com/watch?v=vaNpcgmj5qI')
    await bot.change_presence(activity=activity)
    OneMinuteLoop.start()
    #fiveMinLoop.start()
    bot.remove_command('help')

    bot.load_extension("cogs.leaderboard")
    bot.load_extension("cogs.addchannel")
    bot.load_extension("cogs.removechannel")
    bot.load_extension("cogs.profile")
    bot.load_extension("cogs.throw")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.info")
    bot.load_extension("cogs.previouswinners")

@tasks.loop(seconds=300)
async def fiveMinLoop():
    redrumlogchannel = bot.get_channel(928831956953751592)

    with open("data.json", "r") as file:
        data = str(json.load(file))
    while len(data) > 0:
        if len(data) > 2000:
            await redrumlogchannel.send(data[:2000])
            data = data[2000:]
        else:
            await redrumlogchannel.send(data[:2000])
            data = ''

@tasks.loop(seconds=60)
async def OneMinuteLoop():
    day = str(datetime.utcnow())[8:11]
    with open(r"data.json", "r") as file:
        data = json.load(file)
        alltimeleaderboard = data['CharCountAllTime']
        ResettingCounters = data['ResettingCounters']

        genchnl = bot.get_channel(923413542303055935)

        for typ in ResettingCounters:
            for item in ResettingCounters[typ].items():
                ThisVariableWasntNeeded, resetDay = item

                if int(day) == int(resetDay):
                    rewritten = data['AlreadyReset'][typ] == 'True'

                    if typ == "Daily":
                        msg=discord.Embed(title=f"Resetting the {typ} leaderboard.", color=0x7289da)
                        await genchnl.send(embed=msg)
                        mychnl = bot.get_channel(906780579872272424)
                        await mychnl.send(embed=msg)

                        #top achievement
                        leaderboard = data["ResettingCharCounts"][f'CharCount{typ.title()}']
                        lst = []
                        lst = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

                        if len(lst) != 0:
                            winner = await bot.fetch_user(str(lst[0][0]))
                            msg=discord.Embed(title=f"{winner.name} got the Top {typ.title()} Character Count achievement!",color=0x7289da)
                            await genchnl.send(embed=msg)
                            await genchnl.send(f"{winner.mention}")

                            #this adds
                            data['Winners'][str(typ.title())].append(lst[0][0])

                            if str(lst[0][0]) in data["Achievements"]:
                                addedToCounter = False
                                count = 0
                                #adds to the counter if the counter already exists
                                for item in data["Achievements"][str(lst[0][0])]:
                                    try:
                                        if list(dict(item).keys())[0] == f"Achieved Top {typ.title()} Character Count":
                                            data["Achievements"][str(lst[0][0])][count][f"Achieved Top {typ.title()} Character Count"] += 1
                                            addedToCounter = True
                                    except ValueError:
                                        pass
                                    count += 1

                                if not addedToCounter:
                                    #adds to the counter if it doesnt exist but the person has other achievements
                                    dic = {f"Achieved Top {typ.title()} Character Count":1}
                                    data["Achievements"][str(lst[0][0])].append(dic)

                            else:
                                dic = {str(lst[0][0]):[]}
                                data['Achievements'].update(dic)
                                dic = {f"Achieved Top {typ.title()} Character Count":1}
                                data["Achievements"][str(lst[0][0])].append(dic)

                        nextDate = str(datetime.utcnow() + timedelta(days = 1))[8:10]
                        data['ResettingCounters'][typ]['start'] = nextDate


                    if typ == "Weekly":
                        msg=discord.Embed(title=f"Resetting the {typ} leaderboard.", color=0x7289da)
                        await genchnl.send(embed=msg)
                        mychnl = bot.get_channel(906780579872272424)
                        await mychnl.send(embed=msg)

                        #top achievement
                        leaderboard = data["ResettingCharCounts"][f'CharCount{typ.title()}']
                        lst = []
                        lst = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

                        if len(lst) != 0:
                            winner = await bot.fetch_user(str(lst[0][0]))
                            msg=discord.Embed(title=f"{winner.name} got the Top {typ.title()} Character Count achievement!",color=0x7289da)
                            await genchnl.send(embed=msg)
                            await genchnl.send(f"{winner.mention}")

                            #this adds
                            data['Winners'][str(typ.title())].append(lst[0][0])

                            if str(lst[0][0]) in data["Achievements"]:
                                addedToCounter = False
                                count = 0
                                #adds to the counter if the counter already exists
                                for item in data["Achievements"][str(lst[0][0])]:
                                    try:
                                        if list(dict(item).keys())[0] == f"Achieved Top {typ.title()} Character Count":
                                            data["Achievements"][str(lst[0][0])][count][f"Achieved Top {typ.title()} Character Count"] += 1
                                            addedToCounter = True
                                    except ValueError:
                                        pass
                                    count += 1

                                if not addedToCounter:
                                    #adds to the counter if it doesnt exist but the person has other achievements
                                    dic = {f"Achieved Top {typ.title()} Character Count":1}
                                    data["Achievements"][str(lst[0][0])].append(dic)

                            else:
                                dic = {str(lst[0][0]):[]}
                                data['Achievements'].update(dic)
                                dic = {f"Achieved Top {typ.title()} Character Count":1}
                                data["Achievements"][str(lst[0][0])].append(dic)

                        nextDate = str(datetime.utcnow() + timedelta(days = 7))[8:10]
                        data['ResettingCounters'][typ]['start'] = nextDate

                    if typ == "Monthly":
                        msg=discord.Embed(title=f"Resetting the {typ} leaderboard.", color=0x7289da)
                        await genchnl.send(embed=msg)
                        mychnl = bot.get_channel(906780579872272424)
                        await mychnl.send(embed=msg)

                        #top achievement
                        leaderboard = data["ResettingCharCounts"][f'CharCount{typ.title()}']
                        lst = []
                        lst = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

                        if len(lst) != 0:
                            winner = await bot.fetch_user(str(lst[0][0]))
                            msg=discord.Embed(title=f"{winner.name} got the Top {typ.title()} Character Count achievement!",color=0x7289da)
                            await genchnl.send(embed=msg)
                            await genchnl.send(f"{winner.mention}")

                            #this adds
                            data['Winners'][str(typ.title())].append(lst[0][0])

                            if str(lst[0][0]) in data["Achievements"]:
                                addedToCounter = False
                                count = 0
                                #adds to the counter if the counter already exists
                                for item in data["Achievements"][str(lst[0][0])]:
                                    try:
                                        if list(dict(item).keys())[0] == f"Achieved Top {typ.title()} Character Count":
                                            data["Achievements"][str(lst[0][0])][count][f"Achieved Top {typ.title()} Character Count"] += 1
                                            addedToCounter = True
                                    except ValueError:
                                        pass
                                    count += 1

                                if not addedToCounter:
                                    #adds to the counter if it doesnt exist but the person has other achievements
                                    dic = {f"Achieved Top {typ.title()} Character Count":1}
                                    data["Achievements"][str(lst[0][0])].append(dic)

                            else:
                                dic = {str(lst[0][0]):[]}
                                data['Achievements'].update(dic)
                                dic = {f"Achieved Top {typ.title()} Character Count":1}
                                data["Achievements"][str(lst[0][0])].append(dic)

                        nextDate = str(datetime.utcnow() + timedelta(days = 30))[8:10]
                        data['ResettingCounters'][typ]['start'] = nextDate

                    if bool(data['ResettingCharCounts'][f'CharCount{typ}']):
                        for item in data['ResettingCharCounts'][f'CharCount{typ}'].copy().items():
                            key, value = item

                            del data['ResettingCharCounts'][f'CharCount{typ}'][key]
                            del data['AlreadyReset'][typ]
                            data['AlreadyReset'][typ] = 'True'
                else:
                    data['AlreadyReset'][typ] = 'False'

    with open(r"data.json","w+") as file:
        json.dump(data, file, indent=4)

    #>----THIS PART SENDS THE ALLTIME LIST TO MY CHANNEL----<#
        description = ""
        allTimeList = []
        allcount = 0
        allTimeList = sorted(alltimeleaderboard.items(), key=lambda x: x[1], reverse=True)
        for i in allTimeList:
            if allcount < 5:
                allcount += 1
                person = await bot.fetch_user(i[0])
                description += f"{allcount}. {person.name}: {i[1]}\n"


        msg = discord.Embed(title="All Time Leaderboard",description=description,color=0x7289da)
        redrumMonitorChannel = bot.get_channel(928113571995467776)
        await redrumMonitorChannel.send(embed=msg)
        description = ""
        #>----THIS PART SENDS THE ALLTIME LIST TO MY CHANNEL----<#

#-----Message Listener-----#
@bot.event
async def on_message(message):
    if message.content == "!d bump":
        with open(r"data.json", "r") as file:
            data = json.load(file)
            if str(message.author.id) in data['Bumps']:
                data['Bumps'][str(message.author.id)] += 1
            else:
                data['Bumps'][str(message.author.id)] = 1
        with open(r"data.json", 'w') as f:
            json.dump(data, f, indent=4)

    if not message.author.bot:
        with open(r"data.json", "r") as file:
            data = json.load(file)
            channels = data['channels']

        if message.channel.id in channels:
            msgCount = len(message.clean_content)

            with open(r"data.json", "r") as file:
                data = json.load(file)
                charcountall = data['CharCountAllTime']
                charcountmonth = data['ResettingCharCounts']['CharCountMonthly']
                charcountweek = data['ResettingCharCounts']['CharCountWeekly']
                charcountdaily = data['ResettingCharCounts']['CharCountDaily']

            #<-----All Time Counter---->#
            async def alltimefunction():
                added = False
                for thing in list(charcountall.items()):
                    key, value = thing

                    if str(message.author.id) == str(key):
                        added = True
                        endkey = key
                        endvalue = value

                if added:
                    charcountalltime = endvalue
                    charcountalltime += msgCount
                    data['CharCountAllTime'][endkey] = charcountalltime

                    async def checkforachievement(threshold, achievement):
                        genchnl = bot.get_channel(923413542303055935)
                        with open(r"data.json", 'r+') as f:
                            if int(charcountalltime) >= threshold:
                                if str(message.author.id) in data["Achievements"]:
                                    if achievement in data["Achievements"][str(message.author.id)]:
                                        return
                                    else:
                                        data['Achievements'][str(message.author.id)].append(achievement)
                                        msg = discord.Embed(title=f"{message.author.name} {achievement}!", color=0x7289da)
                                        await genchnl.send(embed=msg)
                                        await genchnl.send(f"{message.author.mention}")
                                else:
                                    dic = {str(message.author.id):[]}
                                    data['Achievements'].update(dic)
                                    data['Achievements'][str(message.author.id)].append(achievement)

                                    msg = discord.Embed(title=f"{message.author.name} {achievement}!", color=0x7289da)
                                    await genchnl.send(embed=msg)
                                    msg = discord.Embed(title="This is your first achievement!", color=0x7289da)
                                    await genchnl.send(embed=msg)
                                    await genchnl.send(f"{message.author.mention}")

                    await checkforachievement(10_000,"Reached 10k Characters")
                    await checkforachievement(100_000,"Reached 100k Characters")
                    await checkforachievement(500_000,"Reached 500k Characters")
                    await checkforachievement(1_000_000,"Reached 1mil Characters")
                    await checkforachievement(10_000_000,"Reached 10mil Characters")
                else:
                    data['CharCountAllTime'][message.author.id] = msgCount

                with open(r"data.json", 'w') as f:
                    json.dump(data, f, indent=4)
            #<-----Count Function---->#
            def addtocounter(id, typ, info):
                added = False
                msgCount = len(message.clean_content)
                for thing in list(info.items()):
                    key, value = thing
                    if str(id) == str(key):
                        added = True
                        endkey = key
                        endvalue = value
                if added:
                    charcount = endvalue
                    charcount += msgCount
                    data['ResettingCharCounts'][f'CharCount{typ}'][endkey] = charcount
                    with open(r"data.json", 'w') as f:
                        json.dump(data, f, indent=4)
                else:
                    data['ResettingCharCounts'][f'CharCount{typ}'][id] = msgCount
                    with open(r"data.json", 'w') as f:
                        json.dump(data, f, indent=4)

            await alltimefunction()

            addtocounter(message.author.id, 'Daily', data['ResettingCharCounts']['CharCountDaily'])
            addtocounter(message.author.id, 'Monthly',data['ResettingCharCounts']['CharCountMonthly'])
            addtocounter(message.author.id, 'Weekly',data['ResettingCharCounts']['CharCountWeekly'])

            redrumchnl = bot.get_channel(928113571995467776)
            for thing in list(charcountall.items()):
                key, value = thing

                if str(message.author.id) == str(key):
                    endkey = key
                    endvalue = value
                    await redrumchnl.send(f"{message.author}\nAdded: {value}")

    await bot.process_commands(message)
