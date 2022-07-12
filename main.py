import discord
from discord.ext import commands

import os
import re
from random import randrange

bot = commands.Bot(command_prefix='$')

@bot.command()
async def roll(ctx, dice_size):
    result = re.match('d(\d{1,2})', dice_size, flags=re.IGNORECASE)
    if result:
        dice_to_roll = int(result.group(1))
        rolled_number = randrange(dice_to_roll) + 1
        if rolled_number == dice_to_roll:
            await ctx.send('Oh baby, a natural {}'.format(rolled_number))
        else:
            await ctx.send('You rolled a {}'.format(rolled_number), file=discord.file('imgs/nat.gif'))
    else:
        await ctx.send('Syntax is: $roll d<number>', delete_after=5)

bot.run(os.environ['token'])