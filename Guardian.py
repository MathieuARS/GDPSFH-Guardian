import random
import discord
import re
import os
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot_token = os.environ.get("bot_token")
prefix = "this_is_useless_dont_touch_that"
client = commands.Bot(command_prefix = prefix, help_command=None)

owner_id = 195598321501470720
owners_id = [195598321501470720, #Moi
             180790976128745472] #Rya

suggestions_channels = [745331693396820090, # suggestions
                        797968735632752660, # stats-bot-suggestion
                        793552899983540254, # manager-suggestion
                        803693527917658122, # giveaway-suggestion
                        751105161191096340] # faq-suggestion

@client.event
async def on_message(message):
    x = re.search(r"(s.{0,4}t.{0,4}e.{0,4}a.{0,4}r.{0,4}n.{0,4}c.{0,4}o.{0,4}m.{0,4}m.{0,4}i.{0,4}n.{0,4}u.{0,4}t.{0,4}y).*", message.content)
    if x is not None:
        await message.delete()

    ping_owner_message = False
    yesemoji = "<:yes:809571059941769247>"
    noemoji = "<:no:809571073531183144>"
    maybeemoji = "<:maybe:809572355533701131>"
    wrongchannelerror = "You are asking for help in the wrong channel. Go to <#743037416947974165>"
    help_channel = 743037416947974165
    bot_id_list = [798512290222833664, 765571424903233577]

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
    blacklisted_channels = [743030923678711808, #announcements
                            802655265366212698, #mod-announcements
                            765369648971382784, #down-time
                            809420779225350144] #presentations
    creategdps_wordlist = ["create gdps",
                           "create a gdps",
                           "make gdps",
                           "make a gdps"]

    # Suggestions channels reactions
    if message.channel.id in suggestions_channels:
        if message.author.id == owner_id or message.author.id in bot_id_list:
            pass
        else:
            await message.add_reaction(yesemoji)
            await message.add_reaction(noemoji)
            await message.add_reaction(maybeemoji)
    if message.channel.id in blacklisted_channels:
        return
    # Ping messages
    elif "765571424903233577" in message.content:
        await message.channel.send("".join([pingmsglist[random.randrange(0, len(pingmsglist))] for i in range(1)]))
    # Ping owner message
    elif str(owner_id) in message.content:
        if ping_owner_message is True:
            await message.channel.send("I hope you had a good reason to ping the owner..")
        else:
            pass
    # Get mod message
    elif ("get mod" in message.content or
         "give mod" in message.content or
         "myself mod" in message.content ):
        if message.channel.id != help_channel:
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
        if message.channel.id != help_channel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To change your chests rewards go on your gdps tools (http://gdps.mathieuar.fr/<yourgdps>/tools/changeChestRewards.php) and just fill up the informations.")
    # Create gauntlet message
    elif ("create gauntlet" in message.content or
         "create a gauntlet" in message.content or
         "make gauntlet" in message.content or
         "make a gauntlet" in message.content):
        if message.channel.id != help_channel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("You can look in <#743027678046846999>.")
    # Create map pack message
    elif ("create map pack" in message.content or
         "create a map pack" in message.content or
         "make map pack" in message.content or
         "make a map pack" in message.content):
        if message.channel.id != help_channel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("You can look in <#743027631968223284>.")
    # Create gdps message
    elif message.content in creategdps_wordlist:
        if message.channel.id != help_channel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To create a gdps you need to be level 1+ and type !c in <#748238238736711761>")
    # Delete gdps message
    elif ("delete gdps" in message.content or
         "delete my gdps" in message.content):
        if message.channel.id != help_channel:
            await message.channel.send(wrongchannelerror)
        else:
            await message.channel.send("To delete your gdps you can look at the pinned messages in <#743037447218397215>.")
    # Lost account password message
    elif ("lost my password" in message.content or
         "lost my account password" in message.content or
         "forgot my password" in message.content or
         "forgot my account password" in message.content):
        if message.channel.id == help_channel:
            await message.channel.send("If you lost your password login in your database then go in the accounts table, look for your account and replace whats in password by **$2y$10$NcGFx6QGceNBdWWigg9A2.z9NfY5czyhEb0y0GijRurPI7rv71Liu**\n\nThis will change your password to 123456 but be sure to change it again in your gdps tools.")

@client.event
async def on_message_edit(before, after):
    x = re.search(r"(s.{0,4}t.{0,4}e.{0,4}a.{0,4}r.{0,4}n.{0,4}c.{0,4}o.{0,4}m.{0,4}m.{0,4}i.{0,4}n.{0,4}u.{0,4}t.{0,4}y).*", after.content)
    if x is not None:
        await after.delete()

@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    authorid = str(msg.author.id)
    suggestion_content = msg.content
    yesemoji = client.get_emoji(809571059941769247)
    noemoji = client.get_emoji(809571073531183144)
    maybeemoji = client.get_emoji(809572355533701131)

    accepted = discord.Embed(title="Suggestion accepted!", description = "<@" + authorid + ">", color = discord.Colour.green())
    denied = discord.Embed(title="Suggestion denied.", description = "<@" + authorid + ">", color = discord.Colour.red())
    maybe = discord.Embed(title="Suggestion may be accepted.", description = "<@" + authorid + ">", color = discord.Colour.from_rgb(255, 128, 0))

    if payload.channel_id in suggestions_channels:
        if payload.user_id in owners_id:
            if payload.emoji == yesemoji:
                accepted.add_field(name = "Suggestion:", value = suggestion_content, inline = True)
                await channel.send(embed=accepted)
                await msg.delete()
            elif payload.emoji == noemoji:
                denied.add_field(name = "Suggestion:", value = suggestion_content, inline = True)
                await channel.send(embed=denied)
                await msg.delete()
            elif payload.emoji == maybeemoji:
                maybe.add_field(name = "Suggestion:", value = suggestion_content, inline = True)
                await channel.send(embed=maybe)
                await msg.delete()

@client.event
async def on_ready():
    print("Bot ready")

client.run(bot_token)
