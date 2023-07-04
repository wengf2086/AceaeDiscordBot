import hikari, lightbulb
plugin = lightbulb.Plugin('info_commands')

def load(bot):
    bot.add_plugin(plugin)

@plugin.command 
@lightbulb.app_command_permissions(dm_enabled=True)
@lightbulb.command("info", "Get info on a user or server.")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def info() -> None:
    pass

@info.child
@lightbulb.option("user", "Select the user you'd like to inspect or input their User ID.", type = hikari.User)
@lightbulb.command("user", "Get info on a user.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_user_info(ctx: lightbulb.SlashContext) -> None:
    pass

@info.child
@lightbulb.command("server", "Get info on the current server.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_server_info(ctx):
    pass

@info.child
@lightbulb.option("user", "Select the user you want the avatar of or input their User ID.", type = hikari.User, required = False)
@lightbulb.command("avatar", "Get a user's profile picture.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_avatar(ctx):
    pass

@info.child
@lightbulb.command("help", "Learn more about me.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_help(ctx):
    pass