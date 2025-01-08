from aiogram import F, Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keybards as kb
import app.tovars as tovars

import random

router = Router()


class Add(StatesGroup):
    name = State()
    descr = State()
    price = State()
    

class Delete(StatesGroup):
    id = State()
    confirm = State()



def random_quote():
    list = []
    with open('app/quotes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            list.append(line)
    return random.choice(list)

@router.message(CommandStart())
async def start(message: Message):

    await message.answer(f'Привіт, новий користувач {message.from_user.full_name}')

    # await message.answer('Вітаю, це бот твого складу, щоб продовжити натисни на одну з кнопок нижче', reply_markup=kb.main)


@router.message(F.text == 'Переглянути товари')
async def view(message: Message):
    if not tovars.items:
        message.answer('На складі пусто')
    else:
        res = 'Список товарів:\n\n'
        
        for key, item in tovars.items.items():
            res += f'{key}.\nНазва: {item['name']}\nОпис: {item['descr']}\nЦіна: {item['price']}\n'
            
        await message.answer(res)
        
        
@router.message(F.text == 'Додати товар')
async def add_start(message: Message, state: FSMContext):
    await message.answer('Введіть назву товару')
    await state.set_state(Add.name)
    
@router.message(Add.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введіть опис')
    await state.set_state(Add.descr)
    
@router.message(Add.descr)
async def add_descr(message: Message, state: FSMContext):
    await state.update_data(descr=message.text)
    await message.answer('Введіть ціну')    
    await state.set_state(Add.price)
    
@router.message(Add.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=int(message.text))
    
    item = await state.get_data()
    item_key = len(tovars.items)
    tovars.items[item_key] = item
    with open('app/tovars.py', 'w', encoding='utf-8') as file:
        file.write(f'items = {tovars.items}\n')        
    
    await message.answer(
f'''
Товар Додано
Назва: {item['name']}
Опис: {item['descr']}
Ціна: {item['price']}
😎😎😎
''', reply_markup=kb.main)
    await state.clear()
    
    
@router.message(F.text == 'Видалити товар')
async def start_delete(message: Message, state: FSMContext):
    await view(message)
    await message.answer('Введіть номер товару:')
    await state.set_state(Delete.id)
    
@router.message(Delete.id)
async def delete(message: Message, state: FSMContext):
    await state.update_data(id=int(message.text))
    await message.answer('Впевнені що хочете видалити цей товар?', reply_markup=kb.confirm)
    await state.set_state(Delete.confirm)
    
@router.message(Delete.confirm)
async def delete_confirm(message: Message, state: FSMContext):
    await state.update_data(confirm=message.text)
    data = await state.get_data()
    
    
    if data['confirm'] == 'Так':
        poped = tovars.items.pop(data['id'])
        
        with open('app/tovars.py', 'w', encoding='utf-8') as file:
            file.write(f'items = {tovars.items}')
        
        await message.answer(f'Видалено:\n{poped}', reply_markup=kb.main)
        await state.clear()
        await view(message)
    elif data['confirm'] == 'Ні':
        await message.answer('Буває', reply_markup=kb.main)
        await state.clear()


@router.message(Command(commands=['help']))
async def help(message: Message):
    await message.answer('Чим можу допомогти?')



@router.message(Command(commands=['saysomething']))
async def quote(message: Message):
    quote = random_quote()
    await message.answer(quote)


@router.message(F.text == 'доброго ранку')
async def reply(message: Message):
    await message.reply('Доброго ранку, чим будеш снідати?')


@router.message()
async def echo(message: Message):
    await message.reply(message.text)