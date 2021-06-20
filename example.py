from collections import defaultdict
from extension import Convertor, ConverterException


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


class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise ConverterExceprion("Неверное название параметров")
        quote, base , amount = values