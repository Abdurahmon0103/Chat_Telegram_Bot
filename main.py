import asyncio
import logging
import sys
import os
from google import genai
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# .env dagi o‘zgaruvchilarni yuklash
load_dotenv()
TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("""
Salom!!!
Bu bot sizga video, audio va rasm yuboradi.
Ai va Calculator kabi xususiyatlari ham mavjud.
Sizga yordam kerak bo'lsa /help buyrug'ini bosing.
""")

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("""
Bo't Commands:
/video = Video
/audio = Audio
/photo = Rasm
""")

@dp.message(Command("video"))
async def vd_send(message: Message):
    await message.answer_video(
        video="BAACAgIAAxkBAAOUaKcDM5MByJA3lwdE_BKnI5T3Z2MAAiR1AAL7pClJDBj2kOheFyc2BA", 
        caption="Bu Video"
    )

@dp.message(Command("photo"))
async def image_send(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAObaKcEf8rfQs0KGIEtMRLPjhj3aF4AAoP0MRvl4fFIrDOYuqPSfJgBAAMCAANzAAM2BA", 
        caption="Bu Rasm"
    )

@dp.message(Command("audio"))
async def audio_send(message: Message):
    await message.answer_audio(
        audio="CQACAgIAAxkBAAOhaKcFa0V12ejGJE0fOW6v3ESwbYcAAv1yAAKOeaBJLMunSiJ1Lpc2BA", 
        caption="Bu Audio"
    )

@dp.message()
async def echo_handler(message: Message) -> None:
    client = genai.Client(api_key=GEMINI_API_KEY)

    def ai():
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=message.text
        )
        return response.text

    await message.reply(ai())

async def main() -> None:
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
