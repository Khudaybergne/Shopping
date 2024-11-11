from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

admins_menu = ReplyKeyboardMarkup(resize_keyboard=True)

admins_menu.add(KeyboardButton('Zat qosiw'),
                KeyboardButton(text='Zakazlar'),
                KeyboardButton(text='Xabar jiberiw'),
                )
registrasiya=ReplyKeyboardMarkup(resize_keyboard=True)
registrasiya.add(KeyboardButton("Registrasiya"),
                 KeyboardButton("Kiriw"))
next=ReplyKeyboardMarkup(resize_keyboard=True)
next.add(KeyboardButton('NEXT'))
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='📖Menu📖'),KeyboardButton(text='📞Contacts📞'))
menu.add(  KeyboardButton("⚜️Zakaz Beriw⚜️"),KeyboardButton(text='📍Manzil'))

menu1=ReplyKeyboardMarkup(resize_keyboard=True)
menu1.add(KeyboardButton(text="🌭Fast Food🍔"),
          KeyboardButton(text="🥘Awqatlar🍜"),
          KeyboardButton(text="🍸Suwlar🍹"),
          KeyboardButton(text="🔚"))
zakaz_awqat=ReplyKeyboardMarkup(resize_keyboard=True)
zakaz_awqat.add(KeyboardButton("fast food"),
                KeyboardButton("drinks"),
                KeyboardButton("foods"))


menu_zakaz=ReplyKeyboardMarkup(resize_keyboard=True)
menu_zakaz.add(KeyboardButton("📌Location"),
               KeyboardButton("💎To'lem💎"))



zat_qosiw_menu = ReplyKeyboardMarkup(resize_keyboard=True)
zat_qosiw_menu.add(KeyboardButton("Fast Food"),
                   KeyboardButton("Suwlar"),
                   KeyboardButton("Awqatlar"))

