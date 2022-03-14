from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import aiogram
from aiogram import Bot, types

b = Bot(token="5204482932:AAGsX5xQxiD0dBvw5On6qx72cGqtPU1Fwk4")
bot = Dispatcher(b)


@bot.message_handler(commands="start")
async def st(message):
    await message.reply(f'Salom <b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b> men ishlayabman😉', parse_mode='HTML')


@bot.message_handler(commands="test")
async def st(message):
    await message.reply("Meni kodimni Asadbek yozgan")


@bot.channel_post_handler(content_types=["text"])
async def podpis(message):
    if message.chat.type == 'channel':
        t = message.text
        await message.edit_text(f'{t}\n\n© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>', parse_mode='HTML', disable_web_page_preview=True)


@bot.channel_post_handler(content_types=["photo", "video", "animation", "voice", "audio", "document"])
async def photopodpis(message):
    if message.chat.type == 'channel':
        if message.caption is not None:
            await message.edit_caption(f'{message.caption}\n\n© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>', parse_mode='HTML')
        else:
            await message.edit_caption(f'© <b>{message.author_signature}</b>\n\n<a href="https://t.me/{message.chat.username}/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>', parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(bot, skip_updates=True)
