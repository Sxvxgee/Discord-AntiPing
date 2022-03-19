import discord, os
from discord.ext import commands
from colorama import Fore, init

init()


bot = commands.Bot(
    command_prefix = PREFIX,
    case_insensitive=True,
    strip_after_prefix=True,
)


bot._BotBase__cogs = commands.core._CaseInsensitiveDict()

bot.run(TOKEN)
