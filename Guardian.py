import discord
from discord.ext import commands
import random

prefix = "this_is_useless_dont_touch_that"
client = commands.Bot(command_prefix = prefix, help_command=None)
txt = open("bot_token.txt", "r")
bot_token = txt.readline()

@client.event
async def on_message(message):
    yesemoji = "<:yes:809571059941769247>"
    noemoji = "<:no:809571073531183144>"
    maybeemoji = "<:maybe:809572355533701131>"
    wrongchannelerror = "You are asking for help in the wrong channel. Go to <#743037416947974165>"
    helpchannel = 743037416947974165

    pingmsglist = ["https://tenor.com/view/pinged-sargent-who-pinged-me-gif-15913755",
                  "https://tenor.com/view/ping-slap-dog-doggo-punch-gif-17672413",
                  "Don't you dare ping me again.",
                  "Just stop...",
                  "Why?",
                  "Go away.",
                  "Ping me again and i will curse you for the rest of your life.",
                  "I hate you... STOP PING!!!!",
                  "I will ban you next time.",
                  "For real can you please stop pinging me?",
                  "What do you want???",
                  "<:ping:746467200453574799>"]

    # Suggestions channels reactions
    if (message.channel.id == 745331693396820090 or # suggestions
        message.channel.id == 797968735632752660 or # stats-bot-suggestion
        message.channel.id == 793552899983540254 or # manager-suggestion
        message.channel.id == 803693527917658122 or # giveaway-suggestion
        message.channel.id == 751105161191096340): # faq-suggestion
        await message.add_reaction(yesemoji)
        await message.add_reaction(noemoji)
        await message.add_reaction(maybeemoji)
    # Ping messages
    elif "765571424903233577" in message.content:
        await message.channel.send("".join([pingmsglist[random.randrange(0, len(pingmsglist))] for i in range(1)]))
    # Ping mathieu message
    elif "195598321501470720" in message.content:
        await message.channel.send("I hope you had a good reason to ping the owner..")
    # !c in non verified chat message
    elif "!c" in message.content:
        if message.channel.id == 803605671580270623: # non-verified-chat
            await message.channel.send("You need to be verified first before doing that command.")
    # Get mod message
    elif ("get mod" in message.content or
         "give mod" in message.content or
         "myself mod" in message.content ):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("You can look in <#743030590005051434> if you want to put yourself as owner or look in <#746464567734829168> to give someone a role.")
    # Change chest message
    elif ("change chest" in message.content or
         "change reward" in message.content or
         "modify chest" in message.content or
         "modify the chest" in message.content or
         "chest reward" in message.content or
         "rewards of chest" in message.content or
         "rewards of the chest" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To change your chests rewards go on your gdps tools (http://gdps.mathieuar.fr/<yourgdps>/tools/changeChestRewards.php) and just fill up the informations.")
    # Create gauntlet message
    elif ("create gauntlet" in message.content or
         "create a gauntlet" in message.content or
         "make gauntlet" in message.content or
         "make a gauntlet" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("You can look in <#743027678046846999>.")
    # Create map pack message
    elif ("create map pack" in message.content or
         "create a map pack" in message.content or
         "make map pack" in message.content or
         "make a map pack" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("You can look in <#743027631968223284>.")
    # Create gdps message
    elif ("create gdps" in message.content or
         "create a gdps" in message.content or
         "make gdps" in message.content or
         "make a gdps" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To create a gdps you need to be level 1+ and type !c in <#748238238736711761>")
    # Delete gdps message
    elif ("delete gdps" in message.content or
         "delete my gdps" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To delete your gdps you can look at the pinned messages in <#743037447218397215>.")
    # Account disabled message
    elif ("account disabled" in message.content):
        if message.channel.id != helpchannel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("That means that you got **auto banned**, to unban yourself __delete everything__ in the \"Actions\" Table > click your database > click on the actions table > operations button on top > at the bottom click __<Clear table (TRUNCATE)>__.")
    # Lost account password message
    elif ("lost my password" in message.content or
         "lost my account password" in message.content or
         "forgot my password" in message.content or
         "forgot my account password" in message.content):
        if message.channel.id == helpchannel:
            await message.channel.send("If you lost your password login in your database then go in the accounts table, look for your account and replace whats in password by **$2y$10$NcGFx6QGceNBdWWigg9A2.z9NfY5czyhEb0y0GijRurPI7rv71Liu**\n\nThis will change your password to 123456 but be sure to change it again in your gdps tools.")

@client.event
async def on_ready():
    print("Bot pret")

client.run(bot_token)