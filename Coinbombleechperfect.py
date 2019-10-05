import discord
from random import randint
from time import sleep
from discord import ext
from discord.ext import commands
import asyncio
import sys
import datetime

client = discord.Client()
token = "urtokenhere"

@client.event
async def on_ready():
    print ("Logged in")
    print ("--------------------------")

@client.event
async def on_message(message):
    if "<:coinbomb:573152290374942720> ***" == message.content[:34] and "Type `I WANT MONEY` into the chat now if you want to collect coins from their coin bomb!" in message.content and "has thrown a coin bomb!***" in message.content and message.author.id == 270904126974590976:
        date = datetime.datetime.now()
        if randint(1,3) == 3:
            print ("[Collected] Found a coin bomb at " + str(date.hour) + "h" + str(date.minute))
            time = str(randint(1000,5000))
            timefinal = str(time[0]) + "." + str(time[0:])
            sleep(float(timefinal))
            await message.channel.send("i want money")
        else:
            print ("[Not collected] Found a coin bomb at " + str(date.hour) + "h" + str(date.minute))

client.run(token, bot=False)
