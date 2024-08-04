import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import router
from config import config


async def main():
    bot = Bot(
        token=config.token_mainbot.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)
    await bot.send_message(chat_id=config.admin_id.get_secret_value(), text="START")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
