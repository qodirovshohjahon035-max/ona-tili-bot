import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from datetime import datetime
from tests import ALL_TESTS  # tests.py faylidan savollarni chaqirib oladi

# --- SOZLAMALAR ---
TOKEN = "9054380112:AAG9rxcDdQZilfKMLziS07pnJ_XG30AfkYw"
TARGET_GROUP_ID = -1003936831719  # Guruh ID raqamingiz

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def send_test_session():
    """Guruhga 30 ta testni 40 soniya oraliq bilan yuborish"""
    print("Test seansi boshlandi...")
    
    # Bazadan 30 ta testni tanlab olamiz
    session_tests = ALL_TESTS[:30]
    
    for index, test in enumerate(session_tests, start=1):
        try:
            await bot.send_poll(
                chat_id=TARGET_GROUP_ID,
                question=f"[{index}/30] {test['question']}",
                options=test['options'],
                type="quiz",
                correct_option_id=test['correct_option'],
                is_anonymous=False,
                explanation=test['explanation']
            )
        except Exception as e:
            logging.error(f"Test yuborishda xatolik: {e}")
        
        # Oxirgi test bo'lmasa, keyingi testgacha 40 soniya kutadi
        if index < len(session_tests):
            await asyncio.sleep(40)
            
    print("Test seansi yakunlandi!")

async def scheduler():
    """Yakshanbadan tashqari har kuni 09:00 va 15:00 da ishga tushirish"""
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.weekday()  # 0: Dushanba, ..., 6: Yakshanba
        
        # Yakshanba (6) bo'lmasa va vaqt 09:00 yoki 15:00 bo'lsa
        if current_day != 6 and current_time in ["09:00", "15:00"]:
            await send_test_session()
            await asyncio.sleep(61)  # Bir daqiqa kutish (takrorlanib qolmasligi uchun)
            
        await asyncio.sleep(30)

async def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.create_task(scheduler())
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())