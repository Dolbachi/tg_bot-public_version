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
from routers.states.states import Rejim
base_router=Router()
class Rejim_dobavleniua_Restor(StatesGroup):
    id_table=State()
    name=State()
    address=State()
    contact=State()
    working_hours=State()
    description=State()
    rating=State()
    feedback=State()
    delivery=State()
    special=State()

@base_router.message(Command('rejim_on',prefix='!/'))
async def rejim_on(message:types.Message,state: FSMContext):
    await state.set_state(Rejim.full_name)
    await message.answer('Режим включен')

@base_router.message(Command('rejim_of',prefix='!/'))
async def rejim_on(message:types.Message,state: FSMContext):
    await state.clear()
    await message.answer('Режим выключен')

@base_router.message(Rejim.full_name,F.text)
async def rejim_on(message:types.Message,state: FSMContext):
    await message.reply('Пластмассовый мир победил')
    

    
@base_router.message(lambda message: message.text == "Добавить")
async def reg_dobav_start(message: types.Message, state: FSMContext):
    await message.answer("Введите ID ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.id_table)

@base_router.message(Rejim_dobavleniua_Restor.id_table)
async def add_id_table(message: types.Message, state: FSMContext):
    await state.update_data(id_table=message.text)
    await message.answer("Введите имя ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.name)

@base_router.message(Rejim_dobavleniua_Restor.name)
async def add_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите адрес ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.address)

@base_router.message(Rejim_dobavleniua_Restor.address)
async def add_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer("Введите контакт ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.contact)

@base_router.message(Rejim_dobavleniua_Restor.contact)
async def add_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer("Введите часы работы ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.working_hours)

@base_router.message(Rejim_dobavleniua_Restor.working_hours)
async def add_working_hours(message: types.Message, state: FSMContext):
    await state.update_data(working_hours=message.text)
    await message.answer("Доставка есть? (Да/Нет):")
    await state.set_state(Rejim_dobavleniua_Restor.delivery)

@base_router.message(Rejim_dobavleniua_Restor.delivery)
async def add_delivery(message: types.Message, state: FSMContext):
    await state.update_data(delivery=message.text)
    await message.answer("Введите описание ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.description)

@base_router.message(Rejim_dobavleniua_Restor.description)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите специальное предложение:")
    await state.set_state(Rejim_dobavleniua_Restor.special)

@base_router.message(Rejim_dobavleniua_Restor.special)
async def add_special(message: types.Message, state: FSMContext):
    await state.update_data(special=message.text)
    await message.answer("Введите рейтинг ресторана:")
    await state.set_state(Rejim_dobavleniua_Restor.rating)

@base_router.message(Rejim_dobavleniua_Restor.rating)
async def add_rating(message: types.Message, state: FSMContext):
    await state.update_data(rating=message.text)
    await message.answer("Введите отзывы о ресторане:")
    await state.set_state(Rejim_dobavleniua_Restor.feedback)

@base_router.message(Rejim_dobavleniua_Restor.feedback)
async def add_feedback(message: types.Message, state: FSMContext):
    await state.update_data(feedback=message.text)
    data = await state.get_data()
    restaurant = Restaurant(
        id_table=data["id_table"],
        name=data["name"],
        address=data["address"],
        contact=data["contact"],
        working_hours=data["working_hours"],
        delivery=data["delivery"],
        description=data["description"],
        special=data["special"],
        rating=data["rating"],
        feedback=data["feedback"]
    )
    dobav_zav(restaurant)
    await message.answer(f"Ресторан '{restaurant.name}' успешно добавлен в базу данных!")
    await state.clear()

