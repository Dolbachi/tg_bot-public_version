import sqlite3
from aiogram import Bot, Dispatcher,  F, Router
from aiogram.filters import Command,Filter
import btn.tg_btn_bot as kb
from data_bot import config
from data_bot.config import Admin_id,path_db
from functions.function_for_data_baza import *
import pytz
from datetime import *
from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from test_class.classis import *
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
router=Router()

@router.message(Command('start'))  
async def cmd_start(message:types.Message):
    await message.answer(f'Привет {message.from_user.first_name} Чем я могу быть полезен ?')
    if message.from_user.id in list(map(int,Admin_id)):
        await message.answer('Вы авторизованы как админ !',reply_markup=kb.main_admin)
    else:
        await message.answer('Вы авторизованы как user',reply_markup=kb.main)

@router.message((lambda message: message.text == "Старт"))
async def start_button(message: types.Message):
    await cmd_start(message)
      
@router.message(Command('help'))
async def cmd_help(message:types.Message):
    help_html=""" 
<b>Список доступных команд:</b>\n
<b>/start</b> — начать работу с ботом\n
<b>/help</b> — показать список команд\n
<b>/save</b> — сохранить сообщение в базу\n
<b>/delete</b> — удалить сообщения из базы\n
<b>/show</b> — показать список ресторанов из базы\n
\n
Если у вас возникли вопросы, обратитесь к <a href="https://t.me/support_bot">поддержке</a>.
"""
    await message.reply(help_html, parse_mode="HTML")
    
@router.message((lambda message: message.text == "Помощь"))
async def help_button(message: types.Message):
    await cmd_help(message)  
        
@router.message(Command('del_zav'))
async def cmd_dobav_zav(message:types.Message):
    data = message.text[len("/del_zav"):].strip().split(',')
    restaurant = Restaurant(*data)
    if poisk_for_name(restaurant) == 'Yes':
        del_zav(restaurant)
        await message.reply(f"Ресторан '{restaurant.name}' удален из базы данных!")
    else:
        await message.reply("Неверный формат. Убедитесь, что вы ввели все 9 параметров.")
        
@router.message(Command('show'))
async def cmd_show(message:types.Message):
    mst=''
    rest=show_restaraunt(path=path_db)
    for i in rest:
        mst += i+ "\n"
    await message.answer(mst)

@router.message(lambda message: message.text.strip() == "Показать страничку")
async def show_button_sites(message: types.Message):
    doc=FSInputFile('C:/Users/leham/Documents/GitHub/Kalmyk_info_bot-08/imena.html')
    await message.answer_document(document=doc)

@router.message((lambda message: message.text == "Показать"))
async def show_button(message: types.Message):
    await cmd_show(message)  

@router.message(F.text =='Панель админа')
async def bla_bla(message:types.Message):
    await message.answer(f'Вы вошли в панель админа',reply_markup=kb.admin_panel)

@router.message(Command('id'))
async def id(message:types.Message):
    await message.answer(f'{message.from_user.id}') 

@router.message(lambda message: message.text == "Назад")
async def back_to_main_menu(message: types.Message):
    await message.answer("Вы вернулись в основное меню.", reply_markup=kb.main)

@router.message(Command('time'))
async def time(message:types.Message):
    Moscows_time=pytz.timezone("Europe/Moscow")
    Moscows_time = datetime.now(Moscows_time).strftime('%d.%m.%Y %H:%M:%S')  
    await message.reply(f"Текущее время по Москве: {Moscows_time}")

#@router.message(Command('open_zav'))
#async def open_zav(message:types.Message):




@router.message()
async def not_understand(message:types.Message):
    await message.reply('Я тебя не понимаю')

