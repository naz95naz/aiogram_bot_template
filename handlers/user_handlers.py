from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ua import LEXICON_UA

# Ініціалізуємо роутер рівня модуля
router: Router = Router()

# Цей хендлер спрацьовує на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_UA['/start'])


# Цей хендлер спрацьовує на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_UA['/help'])