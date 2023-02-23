import asyncio
import json
import os
from datetime import datetime

import discord
from discord.ext import commands

#-------------------------------------------------------------------------------
with open('config.json','r',encoding='utf8') as jfile:
    config = json.load(jfile)

Intents = discord.Intents.all()

bot = commands.Bot(command_prefix=config['prefix'],help_command=None,intents = Intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=config["game"]))
    print(">>機器人已啟動<<")

async def main():
    async with bot:
        for filename in os.listdir("./cogs"):
            if filename.endswith('.py'):
                await bot.load_extension(F"cogs.{filename[:-3]}")
                print(filename)
        await bot.start(config['token'])
asyncio.run(main())

