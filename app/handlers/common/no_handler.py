from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message(F.data)
async def btn_not_work(callback: CallbackQuery):
    await callback.answer("Эта функция пока в разработке")


@router.message()
async def no_handler(message: Message):
    await message.answer("Я не понимаю, воспользуйся кнопками, пожалуйста")
