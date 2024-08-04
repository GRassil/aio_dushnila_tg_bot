from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.user import go_student_menu_kb

router = Router()


@router.callback_query(F.data == "student profile menu")
async def student_profile_menu(callback: CallbackQuery):
    # TODO: Добавить подгрузку статистики
    await callback.message.edit_text(
        text=f"Профиль пользователя {callback.from_user.full_name}",
        reply_markup=go_student_menu_kb,
    )
