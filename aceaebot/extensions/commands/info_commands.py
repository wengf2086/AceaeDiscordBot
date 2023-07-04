import hikari, lightbulb, time
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
    user = ctx.options.user

    # If user is not a Member, display only User information
    if not isinstance(user, hikari.Member):
        # Accent color
        # Avatar URL
        # Banner URL
        # Display Avatar URL (?)
        # Flags
        # Global Name
        # is bot / is system
        # Mention
        # Username
        pass

    # If user is a Member, display Member information
    elif isinstance(user, hikari.Member):
        # Display name
        # Guild Avatar URL
        # Join Date
        # Nickname
        # Server Boost since
        # Timeout until
        # Roles
        # Presence
        pass

@info.child
@lightbulb.command("server", "Get info on the current server.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_server_info(ctx: lightbulb.SlashContext) -> None:
    pass

@info.child
@lightbulb.option("user", "Select the user you want the avatar of or input their User ID.", type = hikari.User, required = False)
@lightbulb.command("avatar", "Get a user's avatar.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_avatar(ctx: lightbulb.SlashContext) -> None:
    _user = ctx.options.user or ctx.member or ctx.user
    if isinstance(_user, hikari.Member) and _user.guild_avatar_url:
        _avatar = _user.guild_avatar_url
    else:
        _avatar = _user.display_avatar_url

    _banner = (await plugin.bot.rest.fetch_user(_user)).banner_url # No way to get user's guild banner URL?
    _embed = hikari.Embed(
    title = "Your Profile Picture" if _user == ctx.author or _user == ctx.member else f"{_user.display_name}'s Profile Picture",
    description = f"{_user.mention}",
    url = str(_avatar),
    color = _user.accent_color)\
    .set_author(name="author", url = str(_avatar), icon = ctx.get_guild().icon_url)\
    .set_footer("footer")\
    .set_image(_avatar)\

    await ctx.respond(embed = _embed)




@info.child
@lightbulb.command("help", "Learn more about me.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_help(ctx: lightbulb.SlashContext) -> None:
    pass