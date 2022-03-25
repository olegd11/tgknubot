from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *

TOKEN = "5201437772:AAGkY3EFQrwMJpyYk1ChTiv2UGtKqCY07A4"
admin_id = -724676739

boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	if message['from'].id == admin_id:
		await message.answer(f"Привіт, адмін")
	else:
		await message.answer(f"Привіт, {message['from'].first_name}! Це бот звоторотнього зв'язку із Дирекцією Студентського містечка КНУ. Поставте Ваше запитання або залиште пропозицію")

@dp.message_handler()
async def process_start_command(message: types.Message):
	if message.reply_to_message == None:
		if '/start' not in message.text:
			await boty.forward_message(admin_id, message.from_user.id, message.message_id)
	else:
		if message['from'].id == admin_id:
			if message.reply_to_message.forward_from.id:
					await boty.send_message(message.reply_to_message.forward_from.id, message.text)
		else:
			await message.answer('Дайте відповідь на повідомлення в особистий чат користувача будь ласка.')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await boty.forward_message(admin_id, message.from_user.id, message.message_id)


@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message):
    await boty.forward_message(admin_id, message.from_user.id, message.message_id)

if __name__ == '__main__':
	print("starting")
	executor.start_polling(dp)

