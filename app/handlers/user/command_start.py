from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.user import start_kb
from app.texts.user import start_message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(start_message, reply_markup=start_kb)
