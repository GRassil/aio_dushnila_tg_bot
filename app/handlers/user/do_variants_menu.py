from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.user import student_exam_variants_menu_kb

router = Router()


@router.callback_query(F.data == "student variant menu")
async def practice_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выбери варик для решения",
        reply_markup=student_exam_variants_menu_kb.as_markup(),
    )
