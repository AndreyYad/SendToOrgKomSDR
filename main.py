from asyncio import run

from bot.dispatcher import dp
from bot.bot import bot
from modules.register_handlers import register_handlers

async def main():
    await register_handlers()
    print('Бот запущен!')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        run(main())
    except KeyboardInterrupt:
        pass