import telebot
from .file import readfiles

def sendMessage(website, details):
    chat_id, token = readfiles()
    bot = telebot.TeleBot(token)

    details = details.replace(",", "\n->")
    details = details.replace("[", "\n->")
    details = details.replace("]", "\n")
    message = f'****{website}****\n{details}'

    bot.send_message(chat_id=chat_id, text=message)
