# Discord-AntiPing
A tool used to mark messages that have the discord account pinged as read.

## Required Packages
### Assuming you have Python installed and added to your PATH.
- Colorama: `pip install colorama`
- Discord.py-self rebase branch: `pip install git+https://github.com/dolfies/discord.py-self@rebase`
  - If you had any previous discord-related packages you need to uninstall them first.

## Usage
- Get your account token.
- Add the account token between the quotes next to `TOKEN =`  in `main.py`
- Add a prefix between the quotes next to `PREFIX =`  in `main.py`.
- Add a user ID to `bot.owner_ids = []`  as a number, as in without quotes.
  - You can copy a user ID by going to User Settings -> Advanced -> Enable Developer Mode.

## Warning
The usage of selfbots is NOT allowed by Discord; thus you might get banned. 
