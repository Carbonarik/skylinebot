import discord
from discord.ext import commands
import requests

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1aZ5OZaVTXYmPfliHZrH733wnKtY33iufFGfBI3EbWQ4/edit#gid=258091288'

@bot.event
async def on_message(message):
    try:
        if message.content.startswith("▶ Игровой ник:"):
            nick_names = message.content[len("▶ Игровой ник:"):].strip().split()
            result_message = ""

            for nick_name in nick_names:
                query_url = f'{spreadsheet_url}/gviz/tq?tq=SELECT%20A%20WHERE%20A%20%3D%20%27{nick_name}%27'
                response = requests.get(query_url)

                if response.status_code == 200 and nick_name in response.text:
                    result_message += f'**Игрок {nick_name} был найден в таблице ЧС.**\n'
                else:
                    result_message += f'Игрок {nick_name} не найден в таблице ЧС.\n'

            await message.channel.send(result_message)

    except Exception as e:
        await message.channel.send(f'Произошла ошибка: {str(e)}')

bot.run('MTE1NTkxMzUyMzM0ODY1NjEzOQ.GmfgLH.uI4G3jSdYDFZuVNLwj-4XGtmDT6T0GMCd9yN7U')
