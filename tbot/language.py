import json
import os

from users.models import CategoryModel, MenuModel, DetailMenuModel
from django.utils import timezone, translation

def  get_language(word, lang=None) -> str:
    if lang:
        translation.activate(lang)
    try:
        lang, _ = CategoryModel.objects.get_or_create(code=word, defaults={'title': word})
    except CategoryModel.DoesNotExist:
        lang = CategoryModel.objects.create(code=word, title=word)
        print(lang)
    print(lang)
    return lang.title.replace(r'\n', '\n')


def get_language_menu(word, lang=None) -> str:
    if lang:
        translation.activate(lang)
    try:
        lang, _ = MenuModel.objects.get_or_create(code=word, defaults={'title': word})
    except MenuModel.DoesNotExist:
        lang = MenuModel.objects.create(code=word, title=word)
        print(lang)
    print(lang)
    return lang.title.replace(r'\n', '\n')

def get_language_detail_menu(word, lang=None) -> str:
    if lang:
        translation.activate(lang)
    try:
        lang, _ = DetailMenuModel.objects.get_or_create(code=word, defaults={'title': word})
    except DetailMenuModel.DoesNotExist:
        lang = DetailMenuModel.objects.create(code=word, title=word)
        print(lang)
    print(lang)
    return lang.title.replace(r'\n', '\n')