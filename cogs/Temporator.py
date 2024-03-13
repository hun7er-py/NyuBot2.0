import nextcord 
from nextcord.ext import commands
import sys
import config
from config import *

class Temporator(commands.Cog):
    

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setupcat(self,ctx):
        try : 
            if ctx.author.guild_permissions.administrator == True and ctx.channel == config.get_MODERATION_CHANNEL() :
                if config.get_TEMP_CAT == None :
                    config.set_TEMP_CAT(await ctx.guild.create_category(ctx.message.content[10:]))
                else:
                    await ctx.send("You have already configured a category, silly!")
            else : 
                await ctx.send("You do not have sufficient permissions to do that")
        except:
            await ctx.send("We need a name for the category! Try !setupcat <name> ")
    
    @commands.command()
    async def setupvc(self,ctx):
        try : 
            if ctx.author.guild_permissions.administrator == True and ctx.channel == config.get_MODERATION_CHANNEL() :
                if config.get_CREATION_CHANNEL == None:
                    config.set_CREATION_CHANNEL_NAME(ctx.message.content[9:])
                    config.set_CREATION_CHANNEL(await ctx.guild.create_voice_channel(config.get_CREATION_CHANNEL_NAME(), category=config.get_TEMP_CAT()))
                else:
                    await ctx.send("You do not have sufficient permissions to do that")
            else:
                await ctx.send("You do not have sufficient permissions to do that")
        
        except:
            await ctx.send("We need a name for the category! Try !setupvc <name> ")
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        
        if after.channel is not None:
            if after.channel.name == config.get_CREATION_CHANNEL_NAME():
              if member.nick != None:
                channel = await after.channel.guild.create_voice_channel(f'{member.nick}''\'s VC', category=config.get_TEMP_CAT())
              else :   
                channel = await after.channel.guild.create_voice_channel(f'{member.name}''\'s VC', category=config.get_TEMP_CAT())
              await member.move_to(channel)
        
        if before.channel is not None and  before.channel != config.get_CREATION_CHANNEL() and before.channel.category == config.get_TEMP_CAT():
            if len(before.channel.members)==0:
                await before.channel.delete()

def setup(bot):
    bot.add_cog(Temporator(bot))

#@commands.command()
#async def nyuhelp(self, ctx):
#    embed = nextcord.Embed(title = "How to setup temporary channels",description="", color = 0x000ff)
#    embed.add_field(name="Help", value="To setup temporary channels, you have to first create a new category where the temporary channels will be created. After that, setup a channel where people can join to create a new channel\n 1 - type \"!setupcat\" followed by a name to setup category \n 2 - type \"!setupvc\" to setup the creation channel", inline = False)
#    await ctx.send(embed=embed)