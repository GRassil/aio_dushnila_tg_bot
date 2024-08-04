__call__ = ("router",)

from aiogram import Router

from .no_handler import router as no_handler_router

router = Router()
router.include_router(no_handler_router)
