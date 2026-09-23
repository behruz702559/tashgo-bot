import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


# =========================
# TASHGO BOT
# =========================

TOKEN = os.getenv("8814995862:AAEMe3lMVD09S6f8MaZErGFwgM2o2lsaXJU")

bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================
# /start
# =========================

@dp.message(Command("start"))
async def start(message: Message):

    # Tugma
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛍️ Xaridni boshlash 🛍️",
                web_app=WebAppInfo(
                    url="https://behruz702559.github.io/tashgo-mini-app/"
                )
            )
        ]
    ]
)
    # Foydalanuvchi ismi
    name = message.from_user.first_name

    # Matn
    caption = (
        f"👋 Xush kelibsiz, {name}!\n\n"
        "🔥 TASHGO'ga xush kelibsiz!\n\n"
        "Bizning xizmatlarimizdan foydalaning, "
        "vaqtingizni va pulingizni tejang.\n\n"

        "🎮 PUBG Mobile\n"
        "🔥 Free Fire\n"
        "⚔️ Mobile Legends\n"
        "🎯 Standoff 2\n"
        "⭐ Telegram Stars\n"
        "💎 Telegram Premium\n"
        "🎁 Telegram Gifts\n"
        "🎮 Steam\n"
        "💬 Discord Nitro\n\n"

        "⚡ Tezkor xizmat\n"
        "💰 Qulay narxlar\n"
        "🛡️ Ishonchli xizmat\n\n"

        "🙏 TASHGO xizmatlaridan "
        "foydalanganingiz uchun rahmat!"
    )

    # Rasm
    photo = FSInputFile("welcome.jpg")

    # Rasm + matn + tugma
    await message.answer_photo(
        photo=photo,
        caption=caption,
        reply_markup=keyboard
    )


# =========================
# 🛍️ XARIDNI BOSHLASH
# =========================

@dp.callback_query(lambda call: call.data == "start_shop")
async def start_shop(call: CallbackQuery):

    await call.answer()

    await call.message.answer(
        "🛒 TASHGO DO‘KONIGA XUSH KELIBSIZ!\n\n"
        "🎮 PUBG Mobile\n"
        "🔥 Free Fire\n"
        "⚔️ Mobile Legends\n"
        "🎯 Standoff 2\n"
        "⭐ Telegram Stars\n"
        "💎 Telegram Premium\n"
        "🎁 Telegram Gifts\n"
        "🎮 Steam\n"
        "💬 Discord Nitro\n\n"
        "👇 Kerakli mahsulotni tanlang."
    )


# =========================
# BOTNI ISHGA TUSHIRISH
# =========================

async def main():

    print("🔥 TASHGO BOT ISHLAYAPTI...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
