import asyncio
import logging
from aiogram import *
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from data_bot.config import tg_token
from routers.routers import *
from routers.base_routers import *

async def start_bot(bot:Bot):
    await bot.send_message(Admin_id[0], text='Бот запущен')

async def stop_bot(bot:Bot):
    await bot.send_message(Admin_id[0], text='Бот остановлен')

async def main():
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    dp.include_router(base_router)
    dp.include_router(router)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__=="__main__":
    asyncio.run(main())