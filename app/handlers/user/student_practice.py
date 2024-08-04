from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.user import student_practice_menu_kb

router = Router()


@router.callback_query(F.data == "student practice menu")
async def practice_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Что будем ботать?", reply_markup=student_practice_menu_kb
    )
