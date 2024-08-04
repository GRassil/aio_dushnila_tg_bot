from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.keyboards.user import social_type_kb, subjects_kb, go_student_menu_kb
from app.states.user_states import RegStates

router = Router()


@router.callback_query(F.data == "reg")
async def get_name(callback: CallbackQuery, state: FSMContext):
    try:
        is_member = await callback.bot.get_chat_member(
            chat_id="@dushnilamath", user_id=callback.from_user.id
        )
        if is_member.status == "left":
            raise Exception
    except Exception:
        await callback.answer("Ну подпишись")
    else:
        await state.set_state(RegStates.name)
        await callback.message.answer("Введи свое Имя и Фамилию")


@router.message(RegStates.name)
async def get_social_type(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegStates.social_type)
    await message.answer("Кто ты?", reply_markup=social_type_kb)


@router.message(RegStates.social_type)
async def get_subjects(message: Message, state: FSMContext):
    await state.update_data(social_type=message.text)
    await state.set_state(RegStates.subjects)
    await message.answer("Выбери свой предмет", reply_markup=subjects_kb.as_markup())


@router.callback_query(RegStates.subjects)
async def finish_registration(callback: CallbackQuery, state: FSMContext):
    # TODO: Добить кнопки
    data = await state.get_data()
    await state.clear()
    if callback.data == "finish_reg":

        await callback.message.answer(
            "Регистрация завершена", reply_markup=go_student_menu_kb
        )
    else:
        await callback.message.edit_reply_markup(reply_markup=go_student_menu_kb)
