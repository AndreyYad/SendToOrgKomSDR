from aiogram.dispatcher.dispatcher import Dispatcher

from handlers import generic

dp = Dispatcher()

dp.include_routers(
    generic.router
)