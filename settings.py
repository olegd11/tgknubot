import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = "5201437772:AAGkY3EFQrwMJpyYk1ChTiv2UGtKqCY07A4"

TELEGRAM_SUPPORT_CHAT_ID = "-724676739"
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "Вас вітає Дирекція Студентського містечка КНУ. Поставте Ваше запитання або залиште пропозицію 👋")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")