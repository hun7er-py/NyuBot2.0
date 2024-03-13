from typing import ValuesView
from unicodedata import category
import nextcord
from nextcord.ext import commands
import config
from cogs.Ticketing import *

class NyuSetup(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hellonyu(self,ctx):
        embed = nextcord.Embed(title = "Hello, I'm Nyu!",description="The ultra flexible wannabe all-in-one Discord bot", color = 0x000ff)
        embed.add_field(name = "Who am I?",\
            value = "I'm Nyu, your personal Discord DJ, organiser and janitor. I kind of try to do everything and anything. But let me show you what I can do right \
                now since my creator is still working on me : ", inline = False)
        embed.set_thumbnail(url="https://i.imgur.com/UthjWPD.jpg")
        await ctx.send(embed=embed)
        embed = nextcord.Embed(title = "What can i do?",description="The ultra flexible wannabe all-in-one Discord bot big flex", color = 0x000ff)
        embed.add_field(name="To put me to work, you can type the following commands : ",\
            value="First of all, we need to setup our cosy private moderation channel where all the admin commands are available,\nto do so, start with !setupmod",\
                inline = True)
        embed.set_thumbnail(url="https://i.imgur.com/UthjWPD.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def setupnyu(self,ctx):
        await temp_channels_setup(self,ctx)
        await setup_music(self, ctx)
        await Ticketing.ticket_setup(self,ctx)
        await ctx.message.delete()

    @commands.command()
    async def setupmod(self,ctx):
        await moderation_setup(self,ctx)

    @commands.command()
    async def setupmusic(self,ctx):
        await ctx.send("I'm currently looking for ways to share my favorite tunes, but I'm sure I'll figure it out soon")
        await setup_music(self, ctx)

        

async def moderation_setup(self,ctx):
    if ctx.author.guild_permissions.administrator == True:
            member = ctx.author
            overwrites = {
                ctx.guild.default_role : nextcord.PermissionOverwrite(view_channel = False),
                member : nextcord.PermissionOverwrite(read_messages=True),
                member : nextcord.PermissionOverwrite(send_messages=True)
            }
            #await ctx.send("We'll set you up with a basic configuration")
            if config.get_TEMP_CAT() == None:
                await member.send("I will now configure a moderation channel for the two of us")
                config.set_TEMP_CAT(await ctx.guild.create_category("Nyu Bot"))
                config.set_MODERATION_CHANNEL(await ctx.guild.create_text_channel("Nyu moderation", overwrites = overwrites, category = config.get_TEMP_CAT()))
                await config.get_MODERATION_CHANNEL().send("Hi there! From now on, just the two of us are in here and commands in other channels will be ignored :heart:")
                embed = nextcord.Embed(title = "What can i do?",description="The ultra flexible wannabe all-in-one Discord bot big flex", color = 0x000ff)
                embed.add_field(name="To put me to work, you can type the following commands : ",\
                value="***!setupnyu*** Sets up everything automatically\
                 \n***!setupmusic*** - Sets up and enables the music bot\
                 \n***!setupmod*** - Sets up the basic moderation channel, temp stuff etc\
                 \n***!clear*** - Purge the entire channel of all messages",\
                inline = True)
                embed.set_thumbnail(url="https://i.imgur.com/UthjWPD.jpg")
                await config.get_MODERATION_CHANNEL().send(embed=embed)
                
            else : 
                await config.get_MODERATION_CHANNEL().send("You have already set up the moderation :)!")

            
            
async def temp_channels_setup(self, ctx):
    if ctx.author.guild_permissions.administrator == True and ctx.channel == config.get_MODERATION_CHANNEL():
        config.set_CREATION_CHANNEL_NAME("Create new")
        config.set_CREATION_CHANNEL(await ctx.guild.create_voice_channel(config.get_CREATION_CHANNEL_NAME(), category=config.get_TEMP_CAT()))


async def setup_music(self,ctx):
    if ctx.author.guild_permissions.administrator == True and ctx.channel == config.get_MODERATION_CHANNEL():
        guild = ctx.guild
        print("entering music setup")
        rolename = "DJ Nyu"
        print("Trying to create role")
        djrole = await guild.create_role(name = "NYU Dj")
        config.set_DJ_ROLE(djrole)
        
        print("role created")
        await ctx.author.add_roles(djrole)
        overwrites = {
                ctx.guild.default_role : nextcord.PermissionOverwrite(view_channel = False),
                djrole: nextcord.PermissionOverwrite(read_messages=True),
                djrole: nextcord.PermissionOverwrite(send_messages=True),
                djrole: nextcord.PermissionOverwrite(view_channel = True)
            }
        config.set_DJ_CHANNEL(await ctx.guild.create_text_channel("DJ chat", overwrites = overwrites, category = config.get_TEMP_CAT()))
        
def setup(bot):
    bot.add_cog(NyuSetup(bot))
