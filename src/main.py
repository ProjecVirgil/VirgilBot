import os

from dotenv import load_dotenv

from src.logger import logging

load_dotenv()


DISCORD_API_TOKEN = os.getenv("DISCORD_API_TOKEN")


