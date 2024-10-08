from aiogram.fsm.state import State, StatesGroup


class RegStates(StatesGroup):
    name = State()
    profession = State()
    subjects = State()
    finish = State()


class StudentMenuState(StatesGroup):
    menu = State()


class SupportStates(StatesGroup):
    sup_mes = State()


class DoExercisesStates(StatesGroup):
    subject = State()
    num_in_kim = State()


class SendVariantStates(StatesGroup):
    variant_id = State()
    first_part_answers = State()
    second_part_answers = State()
