"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem

from datetime import datetime

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_constellation(update, context):
    user_text = update.message.text
    planet = user_text.split()[1]
    print(planet)
    dt_now = datetime.now()
    dt_now = dt_now.strftime('%Y/%m/%d')
    print(dt_now)
    planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun']
    if planet in planet_list:
        if planet == 'Mercury':
            ephem_planet = ephem.Mercury(dt_now)           
        elif planet == 'Venus':
            ephem_planet = ephem.Venus(dt_now)
        elif planet == 'Mars':
            ephem_planet = ephem.Mars(dt_now)
        elif planet == 'Jupiter':
            ephem_planet = ephem.Jupiter(dt_now)
        elif planet == 'Saturn':
            ephem_planet = ephem.Saturn(dt_now)
        elif planet == 'Uranus':
            ephem_planet = ephem.Uranus(dt_now)
        elif planet == 'Neptune':
            ephem_planet = ephem.Neptune(dt_now)
        elif planet == 'Pluto':
            ephem_planet = ephem.Pluto(dt_now)
        elif planet == 'Sun':
            ephem_planet = ephem.Sun(dt_now)
        constellation = ephem.constellation(ephem_planet)
        print(constellation)
        update.message.reply_text(f'Планета {planet} находится в созвездии {constellation[1]}')
    else:
        update.message.reply_text(f'Не знаю планеты {planet}')        

def main():
    mybot = Updater("5356104752:AAE0vTxK0mFBoW-j3Z_cc6lWOzEuAkloPDo", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
