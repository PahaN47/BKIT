import telebot
from telebot.types import ReplyKeyboardRemove
import os
from custom_filter import CurrentState
from values import state
import values
from pics import get_pic 
import plotter

kovyrshinbot = telebot.TeleBot('5077381184:AAE5d6etfiLN8K7SbPwabfuGAXYG6xuPla4')

@kovyrshinbot.message_handler(commands=['state'])
def start(message):
    kovyrshinbot.send_message(message.chat.id, text= str(values.current_state))

@kovyrshinbot.message_handler(commands=['start'])
def start(message):
    values.current_state = state.DEFAULT
    remove_markup = ReplyKeyboardRemove()
    kovyrshinbot.send_message(message.chat.id, text= 'Я завелся, чтобы строить графики или делать еще что-то', reply_markup= remove_markup)

@kovyrshinbot.message_handler(commands=['help'])
def help(message):
    values.current_state = state.DEFAULT
    remove_markup = ReplyKeyboardRemove()
    kovyrshinbot.send_message(message.chat.id, text= '/start - старт\n/options - варианты\n/pics - картинки\n/help - помощь', reply_markup= remove_markup)

@kovyrshinbot.message_handler(commands=['options'])
def options(message):
    values.current_state = state.DEFAULT
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True)
    plot_button = telebot.types.KeyboardButton('Построй график')
    extra_button = telebot.types.KeyboardButton('Картинки')
    markup.add(plot_button)
    markup.add(extra_button)
    kovyrshinbot.send_message(message.chat.id, text='Ну вот варианты', reply_markup= markup)

@kovyrshinbot.message_handler(commands=['pics'])
def pics_command(message):
    pics(message)

@kovyrshinbot.message_handler(current_state= [state.DEFAULT], content_types= ['text'], regexp= values.pics_r)
def pics_text(message):
    pics(message)

def pics(message):
    values.current_state = state.PICTURE
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True)
    pic1_button = telebot.types.KeyboardButton('Первая картинка')
    pic2_button = telebot.types.KeyboardButton('Вторая картинка')
    markup.add(pic1_button)
    markup.add(pic2_button)
    kovyrshinbot.send_message(message.chat.id, text='Какую тебе картинку', reply_markup= markup)

@kovyrshinbot.message_handler(current_state= [state.PICTURE], content_types= ['text'])
def send_pic(message):
    if (message.text.lower() == values.first_pic):
        pic = get_pic(values.pic1_url)
    elif (message.text.lower() == values.second_pic):
        pic = get_pic(values.pic2_url)
    else:
        remove_markup = ReplyKeyboardRemove()
        values.current_state = state.DEFAULT
        kovyrshinbot.send_message(message.chat.id, text= 'Че?', reply_markup= remove_markup)
    remove_markup = ReplyKeyboardRemove()
    values.current_state = state.DEFAULT
    kovyrshinbot.send_photo(message.chat.id, photo= pic, reply_markup= remove_markup)

@kovyrshinbot.message_handler(content_types= ['text'], regexp= values.plot_r)
def plot(message):
    values.current_state = state.PLOT
    remove_markup = ReplyKeyboardRemove()
    kovyrshinbot.send_message(message.chat.id, text= 'Введи функцию с переменной x в синтаксисе python.\nКое-как построю график в пределах \n[-10, 10] или меньше', reply_markup= remove_markup)

@kovyrshinbot.message_handler(current_state= [state.PLOT], content_types= ['text'])
def plot_picture(message):
    values.current_state = state.DEFAULT
    remove_markup = ReplyKeyboardRemove()
    plot_path = plotter.plot(message.text)
    plot_img = open(plot_path, 'rb')
    kovyrshinbot.send_photo(message.chat.id, photo= plot_img, reply_markup= remove_markup)
    plot_img.close()
    os.remove(plot_path)

kovyrshinbot.add_custom_filter(CurrentState())
kovyrshinbot.infinity_polling()
