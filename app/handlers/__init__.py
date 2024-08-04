__call__ = ("router",)

from aiogram import Router

from .admin import router as admin_router
from .user import router as user_router
from .common import router as common_router

router = Router(name="admin")
router.include_router(user_router)
router.include_router(admin_router)
router.include_router(common_router)
