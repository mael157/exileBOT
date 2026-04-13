import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 7912213850  # depois você muda

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    text = message.text

    if text == "/start":
        await message.answer(
            "👋 Bem-vindo!\n\nEscolha:\n1 - Produto A\n2 - Produto B"
        )

    elif text == "1":
        await message.answer("✅ Pedido recebido! Aguarde...")

        await bot.send_message(
            ADMIN_ID,
            f"🛒 Novo pedido!\nCliente: {message.from_user.id}\nProduto: A"
        )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
