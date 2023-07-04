import hikari
import lightbulb

from aceaebot import GUILD_ID, STDOUT_CHANNEL_ID

if __name__ == "__main__":
    with open("./secrets/token") as f:
        _token = f.read().strip()
        bot = lightbulb.BotApp(
            token=_token,
            prefix="@",
            intents=hikari.Intents.ALL,
            default_enabled_guilds=GUILD_ID
        )

    @bot.listen(hikari.StartedEvent)
    async def on_started(event: hikari.StartingEvent) -> None:
        channel = await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
        await channel.send("Aceae is online.")

    @bot.command() # Registers command
    @lightbulb.add_cooldown(10.0, 1, lightbulb.UserBucket) # Cooldown. User/Guild Bucket: cooldown applies to user / guild
    @lightbulb.add_checks(lightbulb.owner_only) # Permissions
    @lightbulb.option("text", "The thing to say.") # Options (Arguments)
    @lightbulb.command("say", "Make the bot say something.") # Turns function into command object
    @lightbulb.implements(lightbulb.SlashCommand)
    async def cmd_say(ctx: lightbulb.SlashContext) -> None:
        # All option values get stored in ctx.options
        await ctx.respond(ctx.options.text)

    @bot.listen(lightbulb.CommandErrorEvent) # Error handler
    async def on_error(event: lightbulb.CommandErrorEvent) -> None:
        if isinstance(event.exception, lightbulb.CommandInvocationError):
            await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
            raise event.exception

        # Unwrap the exception to get the original cause
        exception = event.exception.__cause__ or event.exception

        if isinstance(exception, lightbulb.NotOwner):
            await event.context.respond("You are not the owner of this bot.")
        elif isinstance(exception, lightbulb.CommandIsOnCooldown):
            await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")

    bot.load_extensions_from("./aceaebot/extensions", recursive=True)
    bot.run() # Type 'python -m aceaebot -O' in the terminal to start the bot
