import nextcord, time, string
from nextcord.ext import commands
from nextcord.ui import Button, View
import asyncio
import config

class Ticketing(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  
  async def ticket_setup(self, ctx):
    config.set_SUPPORT_ROLE(await ctx.guild.create_role(name = "NYU Support"))
    config.set_TICKETING_CAT(await ctx.guild.create_category(name = "Tickets"))
    config.set_TICKETING_CHANNEL(await ctx.guild.create_text_channel(name = "New ticket", category = config.get_TICKETING_CAT()))
    embed = nextcord.Embed(title = "Ticketing", description = "Click the button below to create a new ticket")
    
    async def button_callback(interaction):
      inter = interaction
      await new_ticket(inter)
      
    button = Button(style = nextcord.ButtonStyle.primary, label = "Create here", emoji = "🎟")
    button.callback = button_callback
    view = View()
    view.add_item(button)
    await config.get_TICKETING_CHANNEL().send(embed = embed, view= view)

  


async def new_ticket(interaction):
  support_role = config.get_SUPPORT_ROLE()
  guild = interaction.guild
  print(str(support_role))
  nr = config.get_TICKET_COUNTER()
  config.add_TICKET_COUNTER()
  overwrites = {
                guild.default_role : nextcord.PermissionOverwrite(view_channel = False),
                interaction.user: nextcord.PermissionOverwrite(read_messages=True),
                interaction.user: nextcord.PermissionOverwrite(send_messages=True),
                interaction.user: nextcord.PermissionOverwrite(view_channel = True),
    support_role : nextcord.PermissionOverwrite(view_channel=True),
    support_role: nextcord.PermissionOverwrite(read_messages=True),
    support_role: nextcord.PermissionOverwrite(send_messages=True)
            }
  chan = await guild.create_text_channel(f'ticket # {nr}', category =  config.get_TICKETING_CAT(), overwrites = overwrites)

  async def button_callback(interaction):
      inter = interaction
      await confirm(inter)
      
  button = Button(style = nextcord.ButtonStyle.primary, label = "Close ticket", emoji = "📕")
  button.callback = button_callback
  view = View()
  view.add_item(button)
  embed = nextcord.Embed(title = f"Ticket {nr}", description = "Please describe the problem")
  await chan.send(embed = embed, view = view)



async def confirm(interaction):
  async def button_yes_callback(interaction):
      inter = interaction
      await inter.channel.delete()
  async def button_no_callback(interaction):
      inter = interaction
      await inter.message.delete()
      
  button_yes = Button(style = nextcord.ButtonStyle.primary, label = "Yes", emoji = "👍")
  button_yes.callback = button_yes_callback
  button_no = Button(style = nextcord.ButtonStyle.red, label = "No", emoji = "⛔")
  button_no.callback = button_no_callback
  view = View()
  view.add_item(button_yes)
  view.add_item(button_no)
  nr = config.get_TICKET_COUNTER
  embed = nextcord.Embed(title = f"Delete ticket {nr}?", description = "Please confirm or cancel")
  inter = interaction
  await inter.channel.send(embed = embed, view = view)


  
def setup(bot):
      bot.add_cog(Ticketing(bot))