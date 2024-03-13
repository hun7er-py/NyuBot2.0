import nextcord
from nextcord.ext import commands
import config
import string



class Welcome(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print("MEMBER JOINED!!!")
        embed = nextcord.Embed(title = str(config.get_WELCOME_TITLE()),description="", color = 0x000ff)
        embed.add_field(name=str(config.get_WELCOME_TITLE()), value=str(config.get_WELCOME_MESSAGE()), inline = False)
        embed.set_thumbnail(url="https://i.imgur.com/UthjWPD.jpg")
        await member.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcome(bot))