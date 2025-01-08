from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Переглянути товари')],
                                     [KeyboardButton(text='Додати товар'), KeyboardButton(text='Видалити товар')],
                                     ], resize_keyboard=True)

confirm = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Так')],
                                         [KeyboardButton(text='Ні')]], resize_keyboard=True)
