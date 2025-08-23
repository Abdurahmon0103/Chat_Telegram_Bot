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

load_dotenv()
TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("""
Salom!!!
Bu bot sizga video, audio va rasm yuboradi.
va AI kabi xususiyatlari ham mavjud.
Sizga yordam kerak bo'lsa /help buyrug'ini bosing.
""")

@dp.message(Command("help"))
async def send_help(message: Message):
    await message.answer("""
Bo't Commands:
/video = Video
/audio = Audio
/photo = Rasm
/project = Admin tomonidan yaratilgan web loyihalar
""")

@dp.message(Command("project"))
async def project_send(message: Message):
    await message.answer(
        """
        Admin tomonidan yaratilgan web loyihalar:
        1. https://project-admin-panel-with-vue.netlify.app/DataTable
        2. https://olmamarket.netlify.app/Home
        """
    )

@dp.message(Command("video"))
async def vd_send(message: Message):
    await message.answer_video(
        video="BAACAgIAAxkBAANPaKlKldZOoSx1EONA676AAz1CmoAAAo19AAJ_uFFJtM7okO3jjhM2BA", 
        caption="Bu Video"
    )

@dp.message(Command("photo"))
async def image_send(message: Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMiaKk0bnqelv2co7LdrdFg3X-JwBUAAqn1MRt_uFFJahdUjesiohsBAAMCAANzAAM2BA", 
        caption="Bu Rasm"
    )

@dp.message(Command("audio"))
async def audio_send(message: Message):
    await message.answer_audio(
        audio="CQACAgIAAxkBAAM_aKlHd8y_ccjw1eFghP0OIcjlxMcAAmZkAAKKHplL80sYiYBnsh42BA", 
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
