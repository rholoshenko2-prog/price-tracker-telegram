from dotenv import load_dotenv
import os

load_dotenv()  # загружает .env

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", "0"))  # если нет — 0

# Позже сюда добавим ссылки на товары, интервал проверки и т.д.
