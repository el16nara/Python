import asyncio
import logging
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO)

API_TOKEN = "8282041255:AAHCD_Cib3pRQZfD2IgQS0qKGVxNZ5Sf7xQ"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

BASE_DIR = Path(__file__).parent
MEDIA_DIR = BASE_DIR / "media"

QUIZ = [
    {"question": "1️⃣ Какой тип данных в Python является неизменяемым?", "options": ["list", "dict", "set", "tuple"], "correct": 3, "image": "p1.png"},
    {"question": "2️⃣ Что выведет код: print(type([]) is list)?", "options": ["True", "False", "list", "Ошибка"], "correct": 0, "image": "p2.jpg"},
    {"question": "3️⃣ Какой результат выполнения: len({1, 2, 2, 3})?", "options": ["4", "3", "2", "Ошибка"], "correct": 1, "image": "p3.jpg"},
    {"question": "4️⃣ Что делает ключевое слово yield?", "options": ["Возвращает значение и завершает функцию", "Создаёт генератор", "Вызывает исключение", "Останавливает программу"], "correct": 1, "image": "p4.jpg"},
    {"question": "5️⃣ Что такое GIL в Python?", "options": ["Модуль для графики", "Глобальная блокировка интерпретатора", "Тип данных", "Система сборки мусора"], "correct": 1, "image": "p5.jpg"},
    {"question": "6️⃣ Какой результат: bool([])?", "options": ["True", "False", "None", "Ошибка"], "correct": 1, "image": "p6.webp"},
    {"question": "7️⃣ Как правильно обработать исключение?", "options": ["if error:", "catch Exception:", "try / except", "error handling"], "correct": 2, "image": "p7.webp"},
    {"question": "8️⃣ Что делает async def?", "options": ["Создаёт поток", "Создаёт асинхронную функцию", "Запускает цикл", "Оптимизирует код"], "correct": 1, "image": "p8.jpg"},
    {"question": "9️⃣ Какой результат: [x*x for x in range(3)]?", "options": ["[1, 4, 9]", "[0, 1, 4]", "[0, 1, 2]", "[1, 2, 3]"], "correct": 1, "image": "p9.jpg"},
    {"question": "🔟 Что делает функция enumerate()?", "options": ["Сортирует список", "Возвращает индекс и значение", "Копирует коллекцию", "Удаляет элементы"], "correct": 1, "image": "p10.jpg"}
]

user_data = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Здравствуйте! 👋\nЭто викторина по Python (повышенный уровень).\nДля начала введите /quiz")

@dp.message(Command("quiz"))
async def quiz(message: types.Message):
    user_data[message.from_user.id] = 0
    await send_question(message.from_user.id, message.chat.id)

async def send_question(user_id: int, chat_id: int):
    index = user_data[user_id]
    if index >= len(QUIZ):
        await bot.send_message(chat_id, "Викторина завершена! 🎉 Спасибо за участие.")
        user_data.pop(user_id)
        return
    q = QUIZ[index]
    img_path = MEDIA_DIR / q["image"]
    if img_path.exists():
        await bot.send_photo(chat_id, FSInputFile(str(img_path)))
    buttons = [InlineKeyboardButton(text=opt, callback_data=str(i)) for i, opt in enumerate(q["options"])]
    inline_keyboard = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    progress = f"Вопрос {index+1} из {len(QUIZ)} 📚"
    await bot.send_message(chat_id, f"{progress}\n\n{q['question']}", reply_markup=keyboard)

@dp.callback_query()
async def answer_handler(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id not in user_data:
        await callback.answer("Начните викторину командой /quiz")
        return
    index = user_data[user_id]
    q = QUIZ[index]
    selected = int(callback.data)
    if selected == q["correct"]:
        text = "✅ Верно!"
    else:
        text = f"❌ Неверно! Правильный ответ: {q['options'][q['correct']]}"
    await callback.message.answer(text)
    user_data[user_id] += 1
    await send_question(user_id, callback.message.chat.id)

async def main():
    logging.info("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())