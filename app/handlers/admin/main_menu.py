from aiogram import Router
from aiogram.filters import Filter, Command
from aiogram.types import Message

from app.filters.IsAdminFilter import IsAdminFilter

router = Router()


@router.message(Command("router"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в бот, администратор!")
