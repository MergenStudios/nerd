# Imports
import discord
from discord.ext import commands

# Credentials
TOKEN = "OTg3ODI2MzE2Mzk1MDIwMzcw.GXfPsA.3THhN_arAvragM1Vu-67iqIsoQhsu3AfsWMTcI"

# Create bot
client = commands.Bot(command_prefix='!')

# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.fomat(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

# Command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
