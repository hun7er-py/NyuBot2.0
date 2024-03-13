import nextcord
from nextcord.ext import commands
import os
import random
import string
import asyncio
from unicodedata import category
import config
from keep_alive import keep_alive
import flask

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
intents = nextcord.Intents.default()
intents.members = True
intents.reactions = True


@bot.event
async def on_ready():
    print("Bot connected to {0.user}".format(bot))
    await bot.change_presence(activity=nextcord.Game(name='with your heart'))


@bot.command()
async def hello(ctx):
    await ctx.send("Hi there")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.extension")
    await ctx.send("Loaded cog")


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.extension")
    await ctx.send("Reloaded cog")


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.extension")
    await ctx.send("Unloaded cog")


for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")
        print(f"Loaded {fn[:-3]}")

keep_alive()
try:
  bot.run(os.environ['TOKEN'])

except:
  os.system("kill 1")

