from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.onboarding.static_text import github_button_text, secret_level_button_text
from users.models import CategoryModel, MenuModel, DetailMenuModel
from tgbot.language import get_language, get_language_menu, get_language_detail_menu

def make_keyboard_for_start_command():
    buttons = []
    but = CategoryModel.objects.all().order_by('order')
    k = 1
    but1 = []
    for i in but:
        # but1 = []
        if i.two_column:
            if k%2 != 0:
                # print("ISHLADI")
                # print(get_language(f"{i.code}", "uz"))
                but1.append(get_language(i.code, "uz"))
            else:
                but1.append(get_language(i.code, "uz"))
                buttons.append(but1)
                but1 = []
            k+=1
        else:
            but1.append(get_language(i.code, "uz"))
            buttons.append(but1)
    print(buttons)
    return ReplyKeyboardMarkup(buttons, )

def make_keyboard_for_menu_command():
    buttons = []
    but = MenuModel.objects.all().order_by('order')
    k = 1
    but1 = []
    for i in but:
        if i.two_column:
            if k%2 != 0:
                but1.append(get_language_menu(i.title, "uz"))
            else:
                but1.append(get_language_menu(i.title, "uz"))
                buttons.append(but1)
                but1 = []
            k+=1
        else:
            but1.append(get_language_menu(i.title, "uz"))
            buttons.append(but1)
            but1 = []
    return ReplyKeyboardMarkup(buttons, )

def make_keyboard_for_menu_pasta():
    buttons = []
    but = DetailMenuModel.objects.all().order_by('order')
    k = 1
    but1 = []
    for i in but:
        if i.two_column:
            if k%2 != 0:
                but1.append(get_language_detail_menu(i.title, "uz"))
            else:
                but1.append(get_language_detail_menu(i.title, "uz"))
                buttons.append(but1)
                but1 = []
            k+=1
        else:
            but1.append(get_language_detail_menu(i.title, "uz"))
            buttons.append(but1)
            but1 = []
    return ReplyKeyboardMarkup(buttons, )


def make_keyboard_button() -> ReplyKeyboardMarkup:
    # key = CategoryModel.objects.get(code="welcome")
    # print(key)
    buttons = [
        [get_language("settings", "uz")],
        [get_language("welcome")]
    ]
    return ReplyKeyboardMarkup(buttons)