import nextcord
import asyncio, time
from nextcord.ext import commands
from nextcord.ui import Button, View
import wavelink
import config

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(self.node_connect())
        print("init done, no errors")
    
    @commands.Cog.listener()
    async def on_wavelink_node_connect(node: wavelink.Node):
        print(f"node {node.identifier} is ready")

    @commands.command()
    async def play(self, ctx: commands.Context, *, search:wavelink.YouTubeTrack):
        config.set_CTX_MUSIC(ctx)
        play_para = False
        if ctx.author.voice.channel == None:
          ctx.send("Please connect to a voice channel")
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            await vc.play(search)
            play_para = True
        else:
            vc : wavelink.Player = ctx.voice_client
            print("Connected to voice chat")
        
        if (vc.is_playing == False) and vc.queue.is_empty:
            await vc.play(search)
            
        elif play_para == False:
            await vc.queue.put_wait(search)
            embed = nextcord.Embed(title="▶️ Song put in queue : ",
                                    description=f"📢 | `{search.title}` by {search.author} \n **LINK:** {search.uri}", color=0x91cd0e)
            embed.set_author(name="Nyu Music Bot",
                                icon_url=self.bot.user.display_avatar)
            msg = await ctx.send(embed = embed)
            print("added to queue")
            print(vc.queue)
        await ctx.message.delete()
        
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, player : wavelink.Player, track: wavelink.Track):
      await config.get_DJ_CHANNEL().purge(limit = 10000)
      if not player.queue.is_empty:
            for e in player.queue:
                qembed = nextcord.Embed(title="▶️ Song in queue : ",
                                        description=f"📢 |  `{e.title}` by {e.author} \n **LINK:** {e.uri}", color=0x91cd0e)
                qembed.set_author(name="Nyu Music Bot",
                                    icon_url=self.bot.user.display_avatar)
                messg = await config.get_DJ_CHANNEL().send(embed=qembed)
      embed = nextcord.Embed(title="▶️ Playing song : ",
                                  description=f"📢 | Now Playing `{track.title}` by {track.author} \n **LINK:** {track.uri}", color=0x91cd0e)
      embed.set_author(name="Nyu Music Bot",
                          icon_url=self.bot.user.display_avatar)
      
      msg = await config.get_DJ_CHANNEL().send(embed = embed)
      await msg.add_reaction("▶️")
      await msg.add_reaction("⏸")
      await msg.add_reaction("⏭")
      await msg.add_reaction("⏹")

        
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        re = str(payload.emoji)
        if payload.member != self.bot.user:
            if re == "▶️":
                print("play button pressed")
                await self.resume(config.get_CTX_MUSIC())
                await message.remove_reaction(payload.emoji, payload.member)
            elif re == "⏸":
                print("pause button pressed")
                await self.pause(config.get_CTX_MUSIC())
                await message.remove_reaction(payload.emoji, payload.member)
            elif re == "⏭":
                print("skip button pressed")
                await self.skip(config.get_CTX_MUSIC())
                await message.remove_reaction(payload.emoji, payload.member)
            elif re == "⏹":
                print("stop button pressed")
                await self.stop(config.get_CTX_MUSIC())
                await message.remove_reaction(payload.emoji, payload.member)
            elif re == None:
                print("nothing done")
        else:
            
            return
        await message.remove_reaction(payload.emoji, payload.member)

    @commands.Cog.listener()
    async def on_wavelink_track_end(self,player: wavelink.Player, track: wavelink.Track, reason):
        if player.queue.is_empty:
            await player.stop()
            time.sleep(180)
            await player.disconnect()
        
        next_song = await player.queue.get_wait()

        embed = nextcord.Embed(title="▶️ Playing next : ",
                               description=f"📢 | Now Playing `{next_song.title}` by {next_song.author} \n **LINK:** {next_song.uri}", color=0x91cd0e)
        embed.set_author(name="Nyu Music Bot",
                         icon_url=self.bot.user.display_avatar)

        embed.set_image(url=next_song.thumbnail)
        await player.stop()
        await player.play(next_song)

    
    @commands.command()
    async def pause(self, ctx):
        if ctx.channel == config.get_DJ_CHANNEL():
            vc: wavelink.Player = ctx.voice_client
            await vc.pause()

    @commands.command()
    async def resume(self, ctx: commands.Context):
        if ctx.channel == config.get_DJ_CHANNEL():
            vc: wavelink.Player = ctx.voice_client
            await vc.resume()

    @commands.command()
    async def skip(self, ctx: commands.Context):
        if ctx.channel == config.get_DJ_CHANNEL():
            vc: wavelink.Player = ctx.voice_client
            if vc.queue.is_empty:
                await ctx.send("There are no songs in queue")
            else : 
                await vc.stop()

    @commands.command()
    async def stop(self, ctx: commands.Context):
        if ctx.channel == config.get_DJ_CHANNEL():
            vc: wavelink.Player = ctx.voice_client
            await vc.disconnect()
    
    @commands.Cog.listener()
    async def on_waveink_node_ready(self, node: wavelink.Node):
        print(f"Node <{node.id}> is ready!")
    
    async def node_connect(self):
        await self.bot.wait_until_ready()
        await wavelink.NodePool.create_node(bot=self.bot, host="lavalink1.albinhakanson.se", port=1141, password="albinhakanson.se")

def setup(bot):
    bot.add_cog(Music(bot))

#https://lavalink.darrennathanael.com/ -------------- node list