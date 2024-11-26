import asyncio

from aiogram import Bot, Dispatcher

from core.settings import settings
from telegram_bot.handlers import router as handlers_router

bot = Bot(token=settings.bot.token)
dp = Dispatcher()
dp.include_router(handlers_router)


async def start() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
