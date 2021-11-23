from dataclasses import dataclass
import requests


@dataclass
class NBPModel:
    currency: str
    exchange_rate: float
    date: str


class NBPClient:

    def __init__(self):
        self.base_url = 'http://api.nbp.pl/api'

    def get_exchange_rate(self, table: str, currency: str) -> NBPModel:
        res = requests.get(f'{self.base_url}/exchangerates/rates/{table}/{currency}/')

        return self._map_to_nbp_model(res.json())

    def get_gold_price(self) -> float:
        res = requests.get(f'{self.base_url}/cenyzlota')

        return float(res.json()[0]['cena'])

    def _map_to_nbp_model(self, response: dict) -> NBPModel:
        currency = response['code']
        rate = response['rates'][0]

        return NBPModel(
            currency=currency,
            exchange_rate=rate['mid'],
            date=rate['effectiveDate']
        )
