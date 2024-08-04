from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

sub_to_channel_btn = InlineKeyboardButton(
    text="Подписаться", url="https://t.me/dushnilamath"
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            sub_to_channel_btn,
            InlineKeyboardButton(text="Начать регистрацию", callback_data="reg"),
        ]
    ]
)

social_type_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ученик")],
        [KeyboardButton(text="Преподаватель")],
        [KeyboardButton(text="Родитель")],
        [KeyboardButton(text="Другое")],
    ],
    input_field_placeholder="Нажми на кнопку",
)

subjects_kb = InlineKeyboardBuilder()
subjects_dict = {"math": "Матеша Профиль", "infa": "Инфа", "social": "Общага"}
for i in subjects_dict:
    subjects_kb.row(InlineKeyboardButton(text=subjects_dict[i], callback_data=i))

subjects_kb.row(InlineKeyboardButton(text="Готово", callback_data=f"finish_reg"))

go_student_menu_btn = InlineKeyboardButton(text="В меню", callback_data=f"student menu")

go_student_menu_kb = InlineKeyboardMarkup(inline_keyboard=[[go_student_menu_btn]])

teacher_menu_btn = InlineKeyboardButton(text="В меню", callback_data=f"teacher menu")

go_teacher_menu_kb = InlineKeyboardMarkup(inline_keyboard=[[teacher_menu_btn]])

student_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Мой профиль", callback_data="student profile menu"
            )
        ],
        [
            InlineKeyboardButton(text="Ботать", callback_data="student practice menu"),
            InlineKeyboardButton(text="Варианты", callback_data="student variant menu"),
        ],
        [InlineKeyboardButton(text="Курс", callback_data="student course menu")],
        [
            InlineKeyboardButton(
                text="Техподдержка", callback_data="student support menu"
            )
        ],
    ]
)
next_btn = InlineKeyboardButton(text="▶️", callback_data="next page")
prev_btn = InlineKeyboardButton(text="◀️", callback_data="prev page")

student_practice_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Теория", callback_data="get theory")],
        [InlineKeyboardButton(text="Банк задач", callback_data="get practice")],
        [go_student_menu_btn],
    ]
)

student_exam_variants_menu_kb = InlineKeyboardBuilder(markup=[[go_student_menu_btn]])

buy_course_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поступить на курс", callback_data="course")],
        [go_student_menu_btn],
    ]
)
