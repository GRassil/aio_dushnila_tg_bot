from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, Update, TelegramObject


class SubCheckMiddleware(BaseMiddleware):
    def __init__(self, channel_id) -> None:
        self.channel_id = channel_id

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any: ...
