import asyncio
from aiogram import Bot, Dispatcher
from config import TELEGRAM_TOKEN, CHAT_ID

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()

    print("Бот запущен и готов к работе!")

    # Отправляем тебе тестовое сообщение прямо сейчас
    await bot.send_message(
        chat_id=CHAT_ID,
        text="Привет! Это твой бот мониторинга цен. Я запустился и готов работать! 🚀"
    )

    # Запускаем прослушку сообщений (бесконечно)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
