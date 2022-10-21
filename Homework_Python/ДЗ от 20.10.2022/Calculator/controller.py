import user_interface as ui
import data_provider as dp
import telebot
import json
from telebot import types

def button_click(mark):
    number_one, number_second, number_action = ui.menu_amount(mark)
    res = dp.calculation(number_one, number_second, number_action)
    ui.rec_result(mark, res)
