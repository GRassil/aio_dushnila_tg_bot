from aiogram_dialog import DialogManager
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.engine import session_maker
from app.database.orm_query import orm_get_subjects, orm_get_professions


async def profession_getter(dialog_manager: DialogManager, **middleware_data):
    session: AsyncSession = middleware_data.get("session")
    db_professions = await orm_get_professions(session)
    data = {
        "professions": [(profs.id, profs.name) for profs in db_professions],
    }
    return data


async def subjects_getter(dialog_manager: DialogManager, **middleware_data):
    session: AsyncSession = middleware_data.get("session")
    async with session_maker() as session:
        db_subjects = await orm_get_subjects(session)
    data = {"subjects": [(subject.id, subject.name) for subject in db_subjects]}
    return data
