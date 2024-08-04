from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.user import student_menu_kb
from app.texts.user import student_menu_text

router = Router()


@router.callback_query(F.data == "student menu")
async def student_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text=student_menu_text, reply_markup=student_menu_kb
    )
