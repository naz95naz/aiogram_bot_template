import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


# Функція конфігурування і запуску бота
async def main() -> None:

    # Завантажуємо конфіг у змінну config
    config: Config = load_config('.env')

    # Ініціалізуємо бот і диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Реєструємо роутери в диспетчері
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаємо накопичені апдейти і запускаємо polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())