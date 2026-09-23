import asyncio
import os

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = "https://behruz702559.github.io/tashgo-mini-app/"
WELCOME_IMAGE = "welcome.jpg"

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable topilmadi!")

bot = Bot(token=TOKEN)
dp = Dispatcher()


def main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🛍️ Xaridni boshlash 🛍️",
                    web_app=WebAppInfo(url=WEB_APP_URL),
                )
            ]
        ]
    )


@dp.message(Command("start"))
async def start_handler(message: Message):
    text = (
        "🔥 <b>TASHGO</b> ga xush kelibsiz!\n\n"
        "🎮 O‘yinlar va Telegram xizmatlarini qulay xarid qiling.\n\n"
        "🛍️ Do‘konni ochish uchun quyidagi tugmani bosing:"
    )

    if os.path.exists(WELCOME_IMAGE):
        await message.answer_photo(
            photo=FSInputFile(WELCOME_IMAGE),
            caption=text,
            reply_markup=main_keyboard(),
        )
    else:
        await message.answer(text, reply_markup=main_keyboard())


@dp.message(Command("shop"))
async def shop_handler(message: Message):
    await message.answer(
        "🛒 <b>TASHGO Do‘kon</b>\n\nDo‘konni ochish uchun tugmani bosing:",
        reply_markup=main_keyboard(),
    )


@dp.message(Command("balance"))
async def balance_handler(message: Message):
    await message.answer("💰 <b>Balansim</b>\n\nBalans tizimi sozlanmoqda.")


@dp.message(Command("deposit"))
async def deposit_handler(message: Message):
    await message.answer("💳 <b>Balansni to‘ldirish</b>\n\nTo‘lov tizimi sozlanmoqda.")


@dp.message(Command("orders"))
async def orders_handler(message: Message):
    await message.answer("📦 <b>Buyurtmalarim</b>\n\nHozircha buyurtmalar yo‘q.")


@dp.message(Command("history"))
async def history_handler(message: Message):
    await message.answer("📜 <b>Xaridlar tarixi</b>\n\nHozircha xaridlar tarixi bo‘sh.")


@dp.message(Command("support"))
async def support_handler(message: Message):
    await message.answer("💬 <b>Qo‘llab-quvvatlash</b>\n\nAdministrator bilan bog‘laning.")


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "❓ <b>Yordam</b>\n\n"
        "/start — 🚀 TASHGO\n"
        "/shop — 🛒 Do‘kon\n"
        "/balance — 💰 Balansim\n"
        "/deposit — 💳 Balansni to‘ldirish\n"
        "/orders — 📦 Buyurtmalarim\n"
        "/history — 📜 Xaridlar tarixi\n"
        "/support — 💬 Qo‘llab-quvvatlash"
    )


async def health(request):
    return web.Response(text="TASHGO BOT ISHLAYAPTI!")


async def main():
    app = web.Application()
    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.getenv("PORT", "10000"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print("🔥 TASHGO BOT ISHLAYAPTI...")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
