import logging
import sqlite3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig( level = logging.INFO)

b = Bot(token="5222453708:AAGfRhUyIjYaWSXaH7rEWbDGU2omoAAraws")
bot = Dispatcher(b)
ADMIN = 738052033

@bot.message_handler(commands="start")
async def st(message):
    await message.reply(f'Salom <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b> men ishlayabman😉', parse_mode='HTML')


@bot.message_handler(commands="test")
async def st(message):
    await message.reply("Meni kodimni Asadbek yozgan")

@bot.message_handler(commands="link")
async def link_name(message: types.Message):
    if message.chat.id == ADMIN:
        with open("link.txt", "w+") as p:
            p.write(message.text.replace("/link ", "").strip())
        await message.reply("Havola nomi uchun text saqlandi!")
    else:
        await message.reply("Bot admini emassiz!")


@bot.channel_post_handler(content_types=["text"])
async def podpis(message):
    if message.chat.type == 'channel':
        with open("link.txt", "r") as l:
            link = l.read()
        await message.edit_text(f'{message.text}\n\n© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">{link}</a>', parse_mode='HTML', disable_web_page_preview=True)


@bot.channel_post_handler(content_types=["photo", "video", "animation", "voice", "audio", "document"])
async def photopodpis(message):
    if message.chat.type == 'channel':
        with open("link.txt", "r") as l:
            link = l.read()
        if message.caption is not None:
            await message.edit_caption(f'{message.caption}\n\n© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">{link}</a>', parse_mode='HTML')
        else:
            await message.edit_caption(f'© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">{link}</a>', parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)