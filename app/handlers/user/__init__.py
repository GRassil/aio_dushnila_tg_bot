__call__ = ("router",)

from aiogram import Router

from .command_start import router as start_router
from .do_variants_menu import router as variants_router
from .main_menu import router as main_menu_router
from .registration import router as registration_router
from .student_practice import router as practice_router
from .student_profile import router as profile_router
from .write_support import router as support_router
from .course import router as course_router

router = Router()
router.include_routers(
    start_router,
    registration_router,
    main_menu_router,
    variants_router,
    support_router,
    profile_router,
    practice_router,
    course_router,
)
