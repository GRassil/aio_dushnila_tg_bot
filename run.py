import asyncio
import os
from dotenv import load_dotenv, find_dotenv

from app.middlewares.DBMiddleware import DBMiddleware

load_dotenv(find_dotenv())  # load .env file

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import router
from config import config

from app.database.engine import create_db, session_maker


async def on_startup():
    await create_db()


async def main():
    bot = Bot(
        token=config.token_mainbot.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_routers(router)
    dp.startup.register(on_startup)
    dp.update.middleware(DBMiddleware(session_pool=session_maker))
    await dp.start_polling(bot)
    await bot.send_message(chat_id=config.admin_id.get_secret_value(), text="START")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
