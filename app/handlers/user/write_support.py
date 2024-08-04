from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from app.keyboards.user import go_student_menu_kb
from app.states.user_states import SupportStates

router = Router()


@router.callback_query(F.data == "student support menu")
async def support_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(SupportStates.sup_mes)
    await callback.message.edit_text(
        text="Что случилось, что Вас беспокоит?", reply_markup=go_student_menu_kb
    )


@router.message(SupportStates.sup_mes)
async def get_mes_to_support(message: Message, state: FSMContext):
    await state.clear()
    answer_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Ответить",
                    callback_data=f"answer_support {message.from_user.id}",
                )
            ]
        ]
    )
    await message.bot.send_message(
        chat_id="-1001835598101",
        text=f"Сообщение от {message.from_user.full_name}",
        reply_markup=answer_kb,
    )
    await message.bot.copy_message(
        chat_id="-1001835598101",
        from_chat_id=message.chat.id,
        message_id=message.message_id,
    )
    await message.answer(
        "Спасибо за сообщение. Мы обязательно ответим вам в течении 24 часов",
        reply_markup=go_student_menu_kb,
    )
