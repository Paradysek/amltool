from dataclasses import dataclass
import requests


@dataclass
class NBPModel:
    currency: str
    exchange_rate: float
    date: str


@dataclass
class GoldPrice:
    date: str
    price: float


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

    def get_gold_price_for_range(self, start_date, end_date):
        res = requests.get(f'{self.base_url}/cenyzlota/{start_date}/{end_date}')
        values = res.json()
        records = []
        for value in values:
            record = GoldPrice(
                date=value['data'],
                price=value['cena']
            )

            records.append(record)
        return records



