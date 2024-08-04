from aiogram import Router, F
from aiogram.types import Message

from app.keyboards.user import buy_course_kb
from app.texts.user import buy_course_text

router = Router()


@router.message(F.data == "course")
async def buy_course(message: Message):
    await message.edit_text(text=buy_course_text, reply_markup=buy_course_kb)
