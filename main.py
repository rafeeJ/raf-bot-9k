import discord
from discord.ext import commands

import os
import re
from random import randrange

bot = commands.Bot(command_prefix='$')

@bot.command()
async def roll(ctx, dice_size):
    result = re.match('d(\d{1,2})', dice_size, flags=re.IGNORECASE)
    n = randrange(int(result.group(1)))
    await ctx.send('You rolled a {}'.format(n + 1))

bot.run(os.environ['token'])