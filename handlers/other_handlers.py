from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ua import LEXICON_UA

# Ініціалізуємо роутер рівня модуля
router: Router = Router()

# Цей хэндлер спрацьовуватиме на будь-які ваші повідомлення,
# крім команд "/start" і "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_UA['no_echo'])