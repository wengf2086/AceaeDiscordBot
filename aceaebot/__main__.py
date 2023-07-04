import hikari
import lightbulb

from aceaebot import GUILD_ID

if __name__ == "__main__":
    with open("./secrets/token") as f:
        _token = f.read().strip()
        bot = lightbulb.BotApp(
            token=_token,
            prefix="@",
            intents=hikari.Intents.ALL,
            default_enabled_guilds=GUILD_ID
        )

    bot.load_extensions_from("./aceaebot/extensions", recursive=True)
    bot.run() # Type 'python -m aceaebot -O' in the terminal to start the bot
