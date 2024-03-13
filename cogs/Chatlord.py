import nextcord
from nextcord.ext import commands
import string
import sys
import config

class Chatlord(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.author != self.bot.user and ctx != None and ctx.channel == config.get_MODERATION_CHANNEL():
            await ctx.delete()

    @commands.command()
    async def clear(self, ctx):
        await ctx.channel.purge(limit = 100000)

    @commands.command()
    async def testcog(self,ctx):
        await ctx.send(f"{config.get_TEST()}")

    @commands.command()
    async def uninstall(self,ctx):
      if config.get_DJ_CHANNEL() != None:
        await config.get_DJ_CHANNEL().delete()
        print("Dj channel deleted")
      if config.get_MODERATION_CHANNEL() != None:
        await config.get_MODERATION_CHANNEL().delete()
        print("Mod channel deleted")
      if config.get_CREATION_CHANNEL() != None:
        await config.get_CREATION_CHANNEL().delete()
        print("Creation channel deleted")
      if config.get_TEMP_CAT() != None:
        await config.get_TEMP_CAT().delete()
        print("Temporary cat deleted")
      if config.get_DJ_ROLE() != None:
        await config.get_DJ_ROLE().delete()
        print("DJ Role deleted")
      if config.get_TICKETING_CAT() != None:
        await config.get_TICKETING_CAT().delete()
        print("Ticketing cat deleted")
      if config.get_TICKETING_CHANNEL() != None:
        await config.get_TICKETING_CHANNEL().delete()
        print("Ticketing channel deleted")
      if config.get_SUPPORT_ROLE() != None:
        await config.get_SUPPORT_ROLE().delete()
        print("Support Role Deleted")

      embed = nextcord.Embed(title = "Uninstall",description="Why don't I remember anything", color = 0x000ff)
      embed.add_field(name = "KILL KILL KILL",\
            value = "While it pains me to bring destruction, Lucy has destroyed everything I've ever created",\
                      inline = False)
      embed.set_thumbnail(url="https://i.imgur.com/UthjWPD.jpg")
      await ctx.author.send(embed=embed)
      

def setup(bot):
    bot.add_cog(Chatlord(bot))