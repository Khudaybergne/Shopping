from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from my_buttons import *
from datas import *

# 'start_bot' funksiyasiga 'dispatcher' argumentini qo'shildi
async def start_bot(dp):
    await start_db()

api = '7978912786:AAHC89BZLiiZRK43YgHdXLPXV0qkPtTqamE'
bot = Bot(api)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class RegStete(StatesGroup):
    name=State()
    phone_namber=State()
    #name,phone_number,id,username---> bazaga saqlaw


class FoodState(StatesGroup):
    type_of_food = State()
    price = State()
    name = State()
    photo = State()
    ingridients = State()

class zakaz_def(StatesGroup):
    food_type=State()
    food_name=State()
    phone_number=State()
    location=State()


admin_id = 5859365433


@dp.message_handler(commands=['start'])
async def send_hi(sms: types.Message):
    if admin_id == sms.from_user.id:
        await sms.answer(text='Salem Admin', reply_markup=admins_menu)
    else:
        await sms.answer(text='Assalamu aleykum', reply_markup=registrasiya)
@dp.message_handler(text="📖Menu📖")
async def klendt_menu(sms: types.Message):
    await sms.answer(" Hi!",reply_markup=menu1)
@dp.message_handler(text="Registrasiya")
async def registratsiya(sms: types.Message):
    await sms.answer("Assalamu Aleykum!\n Name:")
   
    await RegStete.name.set()
@dp.message_handler(state=RegStete.name)
async def name2(sms: types.Message,state:FSMContext):
    user_id = sms.from_user.id
    username = sms.from_user.username
    async with state.proxy() as Reg:
        Reg['Name']=sms.text
    await sms.answer("Tel:",reply_markup=next)
    await RegStete.phone_namber.set()
@dp.message_handler(state=RegStete.phone_namber)
async def telefonn2(sms:types.Message,state:FSMContext):
    user_id = sms.from_user.id
    username = sms.from_user.username
    async with state.proxy() as Reg:
        Reg['Tel']=sms.text
    await sms.answer(f"Atiniz: {Reg['Name']}\nTel: {Reg['Tel']}")
    await updatereg(name=Reg['Name'],telefon=Reg['Tel'],user_id=user_id,user_name=username)
    await state.finish()

@dp.message_handler(text='NEXT')
async def ok(sms:types.Message):
    await sms.answer("Assalamu Aleykum Xosh Kelinsiz!",reply_markup=menu)



# for admin
@dp.message_handler(text='Zat qosiw')
async def start_adding(sms: types.Message):
    await sms.answer('Hello \n\n Awqat Turi', reply_markup=zat_qosiw_menu)
    await FoodState.type_of_food.set()

@dp.message_handler(content_types="text", state=FoodState.type_of_food)
async def senddd(sms: types.Message, state: FSMContext):
    async with state.proxy() as foods:
        foods['Type'] = sms.text
    await sms.answer("Sena:")
    await FoodState.price.set()

@dp.message_handler(state=FoodState.price)
async def send2(sms: types.Message, state: FSMContext):
    async with state.proxy() as foods:
        foods['Price'] = sms.text
    await sms.answer("Name:")
    await FoodState.name.set()

@dp.message_handler(state=FoodState.name)
async def send3(sms: types.Message, state: FSMContext):
    async with state.proxy() as foods:
        foods['Name'] = sms.text
    await sms.answer("Masalliq:")
    await FoodState.ingridients.set()

@dp.message_handler(state=FoodState.ingridients)
async def send4(sms: types.Message, state: FSMContext):
    async with state.proxy() as foods:
        foods['Masalliq'] = sms.text
    await sms.answer("Photo:")
    await FoodState.photo.set()

@dp.message_handler(state=FoodState.photo, content_types="photo")
async def send5(sms: types.Message, state: FSMContext):
    async with state.proxy() as foods:
        foods['photo'] = sms.photo[0]['file_id']
    await sms.answer_photo(
        photo=foods['photo'],
        caption=f"""
1. Turi: {foods['Type']}
2. Sena: {foods['Price']} uzs
3. Ati: {foods['Name']}
4. Ingridiens: {foods['Masalliq']}""",
        reply_markup=admins_menu
    )
    # Ma'lumotlarni qo'shish
    await add_to_db(types_to=foods['Type'], price=foods['Price'], name=foods['Name'], photo=foods['photo'], ingri=foods['Masalliq'])
    await state.finish()
   
#Klent
@dp.message_handler(text="🌭Fast Food🍔")
async def menua(sms:types.Message):
    foods = await show_foods()
    for i in foods:
        if i[0]=='Fast Food':
            await sms.answer_photo(caption=f"""
🍽 Ati: {i[2]}
💵 Sena: {i[1]}
🍲 Ingridients: {i[4]}""",photo=i[3])

@dp.message_handler(text="🥘Awqatlar🍜")
async def menua(sms:types.Message):
    foods = await show_foods()
    for i in foods:
        if i[0]=='Awqatlar':
            await sms.answer_photo(caption=f"""
🍽 Ati: {i[2]}
💵 Sena: {i[1]}
🍲 Ingridients: {i[4]}""",photo=i[3])

@dp.message_handler(text="🍸Suwlar🍹")
async def menua(sms:types.Message):
    foods = await show_foods()
    for i in foods:
        if i[0]=='Suwlar':
            await sms.answer_photo(caption=f"""
🍽 Ati: {i[2]}
💵 Sena: {i[1]}
🍲 Ingridients: {i[4]}""",photo=i[3])


@dp.message_handler(text="📞Contacts📞")
async def menua(sms:types.Message):
    await sms.answer(f"TG: t.me//evos_admin_fake\nINSTA: @EvocNukus\nTEL: +998999999999")

@dp.message_handler(text="🔚")
async def menua(sms:types.Message):
    await sms.answer("Bas Bolim!",reply_markup=menu)

# @dp.message_handler(text="⚜️Zakaz Beriw⚜️")
# async def menua(sms:types.Message):
#     await sms.answer("1.Awqat Turi:",reply_markup=zakaz_awqat)
#     await zakaz_def.food_type.set()
# @dp.message_handler(state=zakaz_def.food_type)
# async def foodname(sms:types.Message,state:FSMContext):
#     async with  state.proxy() as Zakaz:
#         Zakaz['Turi']=sms.text
#     await sms.answer("2.Ati:")
#     await zakaz_def.food_name.set()
# @dp.message_handler(state=zakaz_def.food_name)
# async def namee(sms:types.Message,state:FSMContext):
#     async with state.proxy() as Zakaz:
#         Zakaz["Ati"]=sms.text
#     await sms.answer("3.Lakatsiya:")
#     await zakaz_def.location.set()
# @dp.message_handler(state=zakaz_def.location)
# async def location(sms:types.Message,state:FSMContext):
#     async with state.proxy() as Zakaz:
#         Zakaz["Location"]=sms.text
#         Zakaz["Telefon_nomer"]=docx
#     await sms.answer(f"1.Turi: {Zakaz['Turi']}\n2.Ati:{Zakaz['Ati']}\n3.Loc: {Zakaz['Location']}\n4.Tel: {Zakaz['Telefon_nomer']}")
#     await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
