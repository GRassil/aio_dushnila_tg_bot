from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message

from config import config


class IsAdminFilter(Filter):
    def __init__(self, bot: Bot):
        self.admins_list = None

    async def __call__(self, message: Message):
        admins_chat = await message.bot.get_chat_administrators(
            config.admin_chat_id.get_secret_value()
        )
        admins_list = [member.router.id for member in self.admins_list]
        return message.from_user.id in admins_list
