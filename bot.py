# bot.py
import os
import random
import json
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

with open('cook_times.json') as f:
    data = json.loads(f.read())

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='cook', help='Replies when your food is cooked. Example:  !cook fish')
async def cook(ctx, food_type):
    if food_type == 'fish':
        response = "Fish cooked!"
        print("Waiting on fish to cook.")
        await asyncio.sleep(int(data['food']['fish'][0]['cooktime']))
        await ctx.send(response)
    elif food_type == 'meat':
        print("Waiting on meat to cook.")
        response = "Meat cooked!"
        await asyncio.sleep(int(data['food']['meat'][0]['cooktime']))
        await ctx.send(response)
    elif food_type == 'trophyfish':
        print("Waiting on trophy fish to cook.")
        response = "Trophy fish cooked!"
        await asyncio.sleep(int(data['food']['trophyfish'][0]['cooktime']))
        await ctx.send(response)
    elif food_type == 'kraken':
        print("Waiting on kraken to cook.")
        response = "Kraken cooked!"
        await asyncio.sleep(int(data['food']['kraken'][0]['cooktime']))
        await ctx.send(response)
    elif food_type == 'megalodon':
        print("Waiting on megalodon to cook.")
        response = "Megalodon cooked!"
        await asyncio.sleep(int(data['food']['megalodon'][0]['cooktime']))
        await ctx.send(response)
    else:
        response = "Something broke..."
        print("Else statement reached. Something broke...")

bot.run(token)
