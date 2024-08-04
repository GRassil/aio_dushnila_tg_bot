from aiogram.fsm.state import StatesGroup, State


class BaseState(StatesGroup):
    subject = State()


class ExerciseState(BaseState):
    number_in_kim = State()
    photo = State()
    answer = State()


class VariantState(BaseState):
    name = State()
    description = State()
    file = State()
