import operator
from typing import Any

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window, StartMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import (
    Button,
    Multiselect,
    Back,
    Next,
    Start,
    Select,
    Radio,
    Row,
    Column,
)
from aiogram_dialog.widgets.text import Const, Format
from sqlalchemy.ext.asyncio import AsyncSession

from .getter import profession_getter, subjects_getter
from ...database.engine import session_maker
from ...database.orm_query import orm_add_user
from ...states.user_states import RegStates, StudentMenuState


async def finish_reg(
    callback: CallbackQuery, button: Button, manager: DialogManager
) -> None:
    async with session_maker() as session:
        username = callback.from_user.username
        user_id = callback.from_user.id
        profession_id = int(manager.find("profession").get_checked())
        subjects_ids = "_".join(manager.find("subject").get_checked())
        fullname = manager.find("name").get_value()
        role_id = 1
        print(username, user_id, profession_id, subjects_ids, fullname)
        await orm_add_user(
            session, user_id, username, fullname, role_id, profession_id, subjects_ids
        )


get_name_window = Window(
    Const("Введи своё ИМЯ и ФАМИЛИЮ"),
    TextInput(id="name", on_success=Next()),
    state=RegStates.name,
)

get_profession_window = Window(
    Const("Кто ты?"),
    Column(
        Radio(
            Format("✅{item[1]}"),
            Format("{item[1]}"),
            id="profession",
            item_id_getter=operator.itemgetter(0),
            items="professions",
        )
    ),
    Row(Back(), Next()),
    state=RegStates.profession,
    getter=profession_getter,
)

get_object_window = Window(
    Const("Выбери предметы"),
    Column(
        Multiselect(
            Format("{item[1]}✅"),
            Format("{item[1]}"),
            id="subject",
            item_id_getter=operator.itemgetter(0),
            items="subjects",
        )
    ),
    Back(),
    Next(on_click=finish_reg),
    state=RegStates.subjects,
    getter=subjects_getter,
)

finish_reg_window = Window(
    Const("Регистрация завершена"),
    Start(
        text=Const("В меню"),
        id="to_menu_btn",
        state=StudentMenuState.menu,
        mode=StartMode.RESET_STACK,
    ),
    state=RegStates.finish,
)

reg_dialog = Dialog(
    get_name_window, get_profession_window, get_object_window, finish_reg_window
)
