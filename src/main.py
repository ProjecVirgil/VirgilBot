import platform

import nextcord
from nextcord.ext import commands
from pyfiglet import figlet_format

from config import DISCORD_API_TOKEN
from logger import logging

TESTING_GUILD_ID = 1192420850993999923

class VirgilBot(commands.Bot):
    """The main bot class for the Virgil Discord Bot.

    Args:
        commands (_type_): _description_
    """
    def __init__(self):
        """Initializes a new instance of the `VirgilBot` class."""
        super().__init__(command_prefix="!", intents=nextcord.Intents.all())

        self.ascii_art = figlet_format("Retr0", font="slant")
        self.cogs_list = ['shut']
        self.load_commands()
        self.load_cogs()
        self.synched = ""

    def load_cogs(self):
        """Load all cogs in the 'cogs' directory and add them to the bot."""
        for ext in self.cogs_list:
            try:
                self.load_extension(f'cogs.{ext}')
                logging.info(f"Cog {ext} loaded successfully")
            except Exception as e:
                logging.error(f"Error in the load of cog {ext}: {e}")

    async def on_ready(self):
        """Event handler that is called when the bot connects to Discord."""
        await self.change_presence(activity=nextcord.Game(name="writing poems"))
        print(self.ascii_art)
        logging.info("THE BOT IS ONLINE")
        logging.info(f"Logged in as {self.user.name}")
        logging.info(f"Bot ID {self.user.id}")
        logging.info(f"nextcord Version {nextcord.__version__}")
        logging.info(f"Python Version {platform.python_version()}")

    def load_commands(self):
        """Load all command functions from the 'bot/commands' module."""
        @self.slash_command(name="hello",description="My first slash command", guild_ids=[TESTING_GUILD_ID])
        async def hello(interaction: nextcord.Interaction):
            await interaction.response.send_message("Hello!")

if __name__ == '__main__':
    bot = VirgilBot()
    bot.run(DISCORD_API_TOKEN)
