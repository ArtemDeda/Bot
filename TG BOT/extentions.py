import requests
import json
from cfg import keys


class Convertexception (Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float ):

        if quote == base:
            raise Convertexception(f"Нельзя конвертировать одинаковые валюты{base}!")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise Convertexception(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Convertexception(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise Convertexception(f'Количество "{amount}" не действительно! Введите количество ещё раз!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = r.json()[keys[base]]

        return total_base
