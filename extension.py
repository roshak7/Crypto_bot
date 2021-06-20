import requests
import json
from config import exchanger
from collections import defaultdict


class ConverterException(Exception):
    pass


class UserInfo:
    def __init__(self):
        self.f = "RUB"
        self.t = "USD"


class UserDB:
    def __init__(self):
        self.db = defaultdict(UserInfo)

    def change_from(self, user_id, val):
        self.db[user_id].f = val

    def change_to(self, user_id, val):
        self.db[user_id].t = val

    def get_pair(self, user_id):
        user = self.db[user_id]
        return user.f, user.t


class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise ConverterException("Неверное количество параметров")

        quote, base, amount = values
        quote_formatted = quote
        base_formatted = base

        if quote == base:
            raise ConverterException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={quote_formatted}_{base_formatted}&compact=ultra&apiKey=d36a50e14b5d1499e823')

        result = float(json.loads(r.content)[f"{quote_formatted}_{base_formatted}"]) * amount

        return round(result, 3)
