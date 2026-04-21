from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN, PROXY_URL
from calendar_api import create_event
from aiogram.client.session.aiohttp import AiohttpSession
import asyncio


async def main():
    session = AiohttpSession(proxy=PROXY_URL)

    # Передаем session в Bot
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def send_welcome(message: Message):
        await message.answer("Hi! I'm your Google Calendar assistant.")

    @dp.message(Command("create_event"))
    async def handle_create_event(message: Message):
        # Example input: /create_event Meeting 2026-04-21T10:00:00 2026-04-21T11:00:00
        try:
            _, summary, start, end = message.text.split(' ', 3)
            link = create_event(summary, start, end)
            await message.reply(f"✅ Event created!\n🔗 View it here: {link}")
        except Exception as e:
            await message.reply(f"❌ Failed to create event. {e}")

    try:
        # Запуск поллинга с прокси
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        await session.close()

if __name__ == '__main__':
    asyncio.run(main())
