import requests

def get_exchange_rate(table, currency):
    res = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/')
    return res
