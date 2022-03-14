from aiogram import Bot, types
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

b = Bot(token="5204482932:AAGsX5xQxiD0dBvw5On6qx72cGqtPU1Fwk4")
bot = Dispatcher(b)


@bot.message_handler(commands="start")
async def st(message):
    await message.reply("Salom men ishlayabman")


@bot.message_handler(commands="test")
async def st(message):
    await message.reply("Meni kodimni Asadbek yozgan")


@bot.channel_post_handler(content_types=["text"])
async def podpis(message):
    if message.chat.type == 'channel':
        t = message.text
        await message.edit_text(t+f'\n\n<a href="https://t.me/Teran_Pikrlar/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>',
                                parse_mode='HTML', disable_web_page_preview=True)


@bot.channel_post_handler(content_types=["photo", "video", "audio", "document"])
async def photopodpis(message):
    if message.chat.type == 'channel':
        if message.text is not None:
            t = message.caption
            await message.edit_caption(f'{t}\n\n<a href="https://t.me/Teran_Pikrlar/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>',
                                       parse_mode='HTML')
        else:
            await message.edit_caption(f'\n\n<a href="https://t.me/Teran_Pikrlar/{message.message_id}">Teran Pikrlaydiganlar Uchun</a>',
                                       parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(bot)
