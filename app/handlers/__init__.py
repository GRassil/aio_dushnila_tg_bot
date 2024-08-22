__call__ = ("router",)

from aiogram import Router
from aiogram_dialog import setup_dialogs

from .admin import router as admin_router
from .user import router as user_router
from .common import router as common_router

from ..dialogs import all_dialogs

router = Router()

for dialog in all_dialogs:
    router.include_router(dialog)

router.include_router(user_router)
router.include_router(admin_router)
router.include_router(common_router)
setup_dialogs(router)
