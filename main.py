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


bot.run(TOKEN)
