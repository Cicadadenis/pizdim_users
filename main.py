import sqlite3
import requests, os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telethon.tl.functions.account import UpdateUsernameRequest
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio, time
import config
from pyrogram import Client
from telethon.sync import TelegramClient
from requests_html import HTMLSession
from time import sleep
from func import *
from rich.console import Console
from telethon.sessions import StringSession
console = Console()

def logo():
	console.print("[blink blue]      _             __         ___       __[/]", justify="center")
	console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
	console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
	console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
	console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
	time.sleep(2)


loop = asyncio.get_event_loop()
tk="5485562654:AAFP6jU-_JsPrrgZRctLpY3wkXdJbmMFQTs"
bot = Bot(token=tk, loop=loop)
dp = Dispatcher(bot)
MethodGetMe = (f'''https://api.telegram.org/bot{tk}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
	id_us = (tttm['result']['id'])
	first_name = (tttm['result']['first_name'])
	username = (tttm['result']['username'])
	os.system('cls')
	logo()

	console.print(f"""[bold blue italic]
				---------------------------------
				🆔 Bot id: {id_us}
				---------------------------------
				👤 Имя Бота: {first_name}
				---------------------------------
				🗣 username: {username}
				---------------------------------
				🌐 https://t.me/{username}
				---------------------------------
				******* Suport: @Satanasat ******[/]
	""", justify="center")
cli = "1ApWapzMBu01UPf1jlTyrl24AgHltecw25G8bP-_xXwRbeROtHg0VqDOo3R6-LCXIa-ODklfVb9OHzaB35AvsOEFKy9KKdwQ5v2Djn7r-wqWh7xne0qIvzVqhUXXlwG8OG43PLiJ5UTZEaHnASD9WHkAjf-HzOgdcnMOdRWR2znwHlu3ErQXyvRT1FMAmJvB5cPadJpcu68AGk4FJQ6gMH1Egu524i7Tx6k-aMgMu-mgiZrgYo_foIesLirWZO4MYR2_gkUpxtj0ZhJGtlFJbHqRUCNM1LVzo4EaWwmsWuDHH5AmlLR4ufT6xlvbd0258mbDp4OcAzY7MImUHWAeiywdvMRV3buY="
client = TelegramClient(StringSession(cli), config.api_id, config.api_hash)
client.connect()
me = client.get_me()


async def get_channels():
	while True:
		await asyncio.sleep(1)
		session = HTMLSession()
		for _ in get_m():
			_ = _[0]
			r = session.get(f'https://t.me/{_}')
			if '<i class="tgme_icon_user"></i>' in r.text:
				
				try:
	
					gaga = await client(UpdateUsernameRequest(username=_))
					detele_monitoring(_)
					for i in config.admins:
						await bot.send_message(i, f"👑 <b>Бот обнаружил пустой юзик [@{_}] и успешно его занял.</b>", parse_mode="HTML")
				except:
					pass
				#await client.update_chat_username(channel.id, _)

			else:
				pass
				#print('Ничего не найдено', _)

@dp.message_handler(text="cicada")
async def cicada(m: types.Message):
	keyboard = InlineKeyboardMarkup()
	xx = get_m()
	for x in xx:
		keyboard.add(InlineKeyboardButton(text=f"{x[0]}", callback_data=f"{x[0]}"))
		msg = "Cлежка За Ними"
	await m.answer(msg, reply_markup=keyboard)
@dp.message_handler(commands=['start'])
async def process_start_command(m: types.Message):
	if m.chat.id in config.admins:
		text = "💾 <b>Стилер логинов в телегам:</b>\n\n"\
				f"👀 Просматривается каналов: <b>{len(get_m())}шт.</b>\n"
		button = KeyboardButton('➕ Добавить каналы')
		button1 = KeyboardButton('🏰 Главная')
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(button)
		keyboard.add(button1)
		await bot.send_message(m.chat.id, text,reply_markup=keyboard, parse_mode="HTML")
	else:
		await bot.send_message(m.chat.id, "<b>❌ Вам запрещенно использовать данного бота.</b>", parse_mode="HTML")

@dp.message_handler()
async def echo_message(m: types.Message):
	if m.text == '➕ Добавить каналы':
		await bot.send_message(m.chat.id, '👾 <b>Введите каналы построчно, каждая строка - новый канал. (С @)</b>', parse_mode="HTML")
	elif m.text == '🏰 Главная':
		await process_start_command(m)
	elif "@" in m.text:
		for _ in m.text.split('\n'):
				if "@" in _:
					add_m(_.split("@")[1])
					await bot.send_message(m.chat.id, f'✅ <b>Канал "{_}" был успешно добавлен.</b>', parse_mode="HTML")
				else:
					pass
				

if __name__ == '__main__':
	loop.create_task(get_channels())
	#dp.loop.create_task(get_channels())
	executor.start_polling(dp)
