import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    
    # @skladovishebot
    bot = Bot(token='7633240986:AAEwzDMo0y7UkoMVvot0sBWWB4XXLkKkce0')
    dp = Dispatcher()
    
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
        
    except KeyboardInterrupt:
        print('byebye')