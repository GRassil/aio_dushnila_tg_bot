from aiogram import Router

from app.filters.IsAdminFilter import IsAdminFilter

from .main_menu import router as main_menu_router

router = Router(name="admin")
router.message.filter(IsAdminFilter)
router.include_router(main_menu_router)
