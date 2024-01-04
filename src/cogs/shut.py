import nextcord
from nextcord.ext import commands

TESTING_GUILD_ID = 1192420850993999923
class Shut(commands.Cog):
    """A cog for testing the bot's functionality in a specific server.

    Args:
        commands (_type_): _description_
    """
    def __init__(self,bot:commands.Bot):
        """Initializes the Testing class with the Bot instance.

        Args:
            bot (commands.Bot): _description_
        """
        self.bot = bot

    @nextcord.slash_command(name="shut",description="Shutdown the bot",guild_ids=[TESTING_GUILD_ID])
    async def shut(self, interaction:nextcord.Interaction):
        """A command to initiate a bot shutdown sequence.

        Args:
            interaction (nextcord.Interaction): _description_
        """
        print("The bot is shutting")
        await interaction.response.send_message(content="Shutting down the bot ")
        await self.bot.close()


def setup(bot:commands.Bot) -> None:
    """A function that adds the Testing Cog to the bot. This should be called upon startup.

    Args:
        bot (commands.Bot): _description_
    """
    bot.add_cog(Shut(bot))