from dataclasses import dataclass

import requests


@dataclass
class TwelveDataRecord:
    datetime: str
    open: float
    high: float
    low: float
    close: float


@dataclass
class TwelveDataModel:
    symbol: str
    interval: str
    currency_base: str
    currency_quote: str
    values: list[TwelveDataRecord]


class TwelveDataClient:
    def __init__(self):

        self.base_url = 'https://api.twelvedata.com'
        self.token = 'd47b661071de40f18a6d2cc8fd7ba710'

    def get_exchange_rate_list(self,
                          interval: str,
                          start_date: str,
                          end_date: str,
                          country: str,
                          exchange: str,
                          symbol: str) -> TwelveDataModel:
        res = requests.get(f'{self.base_url}/time_series?apikey={self.token}&interval={interval}&start_date={start_date}&end_date={end_date}&format=JSON&country={country}&exchange={exchange}&type=none&symbol={symbol}')

        return self._map_to_twelvedata_model(res.json())

    def _map_to_twelvedata_model(self, response: dict) -> TwelveDataModel:
        meta = response['meta']
        values = response['values']

        return TwelveDataModel(
            symbol=meta['symbol'],
            interval=meta['interval'],
            currency_base=meta['currency_base'],
            currency_quote=meta['currency_quote'],
            values=values

        )






