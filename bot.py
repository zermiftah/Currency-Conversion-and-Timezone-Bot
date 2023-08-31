import discord
from discord.ext import commands
import pytz
from datetime import datetime
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I'm your bot!")

@bot.command()
async def convert(ctx, amount: float, source_currency: str, target_currency: str):
    source_currency = source_currency.upper()
    target_currency = target_currency.upper()

    if source_currency != 'IDR':
        await ctx.send("Sumber mata uang harus dalam IDR (Rupiah).")
        return

    available_target_currencies = ['USD', 'RUB', 'BRL', 'KRW']

    if target_currency not in available_target_currencies:
        await ctx.send("Mata uang tujuan tidak dikenal.")
        return

    conversion_rates = requests.get('https://api.exchangeratesapi.io/latest?base=IDR').json()['rates']
    converted_amount = amount * conversion_rates[target_currency]
    await ctx.send(f"{amount} IDR is approximately {converted_amount:.2f} {target_currency}.")

@bot.command()
async def time(ctx, location: str):
    location = location.lower()

    if location == 'inggris':
        timezone = pytz.timezone('Europe/London')
    elif location == 'rusia':
        timezone = pytz.timezone('Europe/Moscow')
    elif location == 'dubai':
        timezone = pytz.timezone('Asia/Dubai')
    elif location == 'korea':
        timezone = pytz.timezone('Asia/Seoul')
    else:
        await ctx.send('Zona waktu tidak dikenal.')
        return

    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'Waktu saat ini di {location.capitalize()}: {formatted_time}')

bot.run('MTE0NjY4NjczMjQ1MzAyMzgxNA.GIh6Ep.gi3-2JxwbW5AhesJZrtnp1idX9Q5H6yVto8_Y0')
