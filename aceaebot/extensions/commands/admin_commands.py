import lightbulb
plugin = lightbulb.Plugin('admin_commands')

def load(bot):
    bot.add_plugin(plugin)

@plugin.command() # Registers command
@lightbulb.add_cooldown(10.0, 1, lightbulb.UserBucket) # Cooldown. User/Guild Bucket: cooldown applies to user / guild
@lightbulb.add_checks(lightbulb.owner_only) # Permissions
@lightbulb.option("text", "The thing to say.") # Options (Arguments)
@lightbulb.command("say", "Make the bot say something.") # Turns function into command object
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
    # All option values get stored in ctx.options
    await ctx.respond(ctx.options.text)