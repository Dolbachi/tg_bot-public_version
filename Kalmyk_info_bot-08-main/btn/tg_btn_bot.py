from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,WebAppInfo
# Основная клавиатура
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Старт')],
        [KeyboardButton(text='Помощь'), KeyboardButton(text='Показать')],
        [KeyboardButton(text='Показать страничку')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

# Клавиатура для админа
main_admin = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Панель админа')],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)
# Панель админа
admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить')],
        [KeyboardButton(text='Удалить')],
        [KeyboardButton(text='Изменить')],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)