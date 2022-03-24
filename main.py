import discord, os
from discord.ext import commands
from colorama import Fore, init

init()

PREFIX = '' # The bot commands prefix. Unless you add commands this is useless
TOKEN = '' # Should be a USER token not a normal bot token

bot = commands.Bot(
    command_prefix = PREFIX,
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot = True,
)
bot.help_command = None
bot._BotBase__cogs = commands.core._CaseInsensitiveDict()


def error(text):
  print(f"{Fore.RED}[!] {text}{Fore.RESET}")

def success(text):
  print(f"{Fore.GREEN}[!] {text}{Fore.RESET}")



@bot.listen('on_ready')
async def on_ready():
  if os.name == 'nt': 
    os.system('cls')
  print("""██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗      █████╗ ███╗   ██╗████████╗██╗      ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗████╗  ██║╚══██╔══╝██║      ██╔══██╗██║████╗  ██║██╔════╝ 
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ███████║██╔██╗ ██║   ██║   ██║█████╗██████╔╝██║██╔██╗ ██║██║  ███╗
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██║██║╚██╗██║   ██║   ██║╚════╝██╔═══╝ ██║██║╚██╗██║██║   ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║██║ ╚████║   ██║   ██║      ██║     ██║██║ ╚████║╚██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝      ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝                            
                                                                                                                          """)
  print(f"{Fore.MAGENTA}An easy tool used to mark pings as read by Sxvxge.{Fore.RESET}")
  print(f"{Fore.CYAN}Github: https://github.com/Sxvxgee{Fore.RESET}")


@bot.listen("on_message")
async def antiping(message):
  if bot.user.mentioned_in(message):
    try:
      await message.ack()
    except:
      error(f"Couldn't mark a message as read.\nMessage Jump URL: {message.jump_url}\nMessage ID: {message.id}")
    else:
      success(f"Marked a message as read.\nMessage Jump URL: {message.jump_url}\nMessage ID: {message.id}")


bot.run(TOKEN)
