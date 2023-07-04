import hikari
import lightbulb

from aceaebot import STDOUT_CHANNEL_ID

plugin = lightbulb.Plugin('logger')

def load(bot):
    bot.add_plugin(plugin)

@plugin.listener(hikari.StartedEvent)
async def on_started(event: hikari.StartingEvent) -> None:
    channel = await plugin.bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
    await channel.send("Aceae is online.")

