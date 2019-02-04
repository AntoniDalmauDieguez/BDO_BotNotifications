# Work with Python 3.6
import random
import asyncio
import aiohttp
import json
import discord
import time
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = ""
CHANNEL = ""

bot = Bot(command_prefix=BOT_PREFIX)

#Se ejecuta 1 vez al iniciar el bot
@bot.event
async def on_ready():
  await bot.change_presence(game=Game(name="with humans"))
  print("Logged in as " + bot.user.name)

@bot.command(name='8ball',
             description="Answers a yes/no question.",
             brief="Answers from the beyond.",
             aliases=['eight_ball', 'eightball', '8-ball'],
             pass_context=True)
async def eight_ball(context):
  possible_responses = [
    'That is a resounding no',
    'It is not looking likely',
    'Too hard to tell',
    'It is quite possible',
    'Definitely',
  ]
  await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@bot.command()
async def square(number):
  squared_value = int(number) * int(number)
  await bot.say(str(number) + " squared is " + str(squared_value))

@bot.command()
async def bitcoin():
  url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
  async with aiohttp.ClientSession() as session:  # Async HTTP request
    raw_response = await session.get(url)
    response = await raw_response.text()
    response = json.loads(response)
    await bot.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

hours = [00.15, 02.00, 05.00, 09.00, 12.00, 16.00, 19.00, 22.15]
monday = ["Kutum & Karanda", "Karanda", "Kzarka", "Kzarka", "Offin", "Kutum", "Nouver", "Kzarka"]
tuesday = ["Karanda", "Kutum", "Kzarka", "Nouver", "Kutum", "Nouver", "Karanda", "Garmoth"]
wednesday = ["Kutun & Kzarka", "Karanda", "Kzarka", "Karanda", "Maintenance", "Kutum", "Offin", "Karanda & Kzarka"]
thursday = ["Nouver", "Kutum", "Nouver", "Kutum", "Nouver", "Kzarka", "Kutum", "Garmoth"]
friday = ["Kzarka & Karanda", "Nouver", "Karanda", "Kutum", "Karanda", "Nouver", "Kzarka", "Kutum & Kzarka"]
saturday = ["Karanda", "Offin", "Nouver", "Kutum", "Nouver", "Quint & Muraka", "Karanda & Kzarka", "No boss"]
sunday = ["Nouver & Kutum", "Kzarka", "Kutum", "Nouver", "Kzarka", "Vell", "Garmoth", "Kzarka & Nouver"]

#Se ejecuta mientras el bot este encendido
async def my_background_task():
  await bot.wait_until_ready()
  channel = discord.Object(id=CHANNEL)

  while not bot.is_closed:
    diaActual = time.strftime("%w")
    horaActual = float(time.strftime("%H"))+1+float(time.strftime("%M"))/100
    check = 0

    if diaActual=="1":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, monday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="2":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, tuesday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="3":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, wednesday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="4":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, thursday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="5":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, friday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="6":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, saturday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1
    elif diaActual=="7":
      while check <= 7:
        if horaActual==hours[check]:
          await bot.send_message(channel, sunday[check]+" will spawn at "+str(hours[check])+"h")
          await asyncio.sleep(61)
        check+=1

    await asyncio.sleep(40)

bot.loop.create_task(my_background_task())
bot.run(TOKEN)
