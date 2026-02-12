import asyncio
from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()

    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
