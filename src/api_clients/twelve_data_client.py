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
        self.token = ''

    def get_exchange_rate(self,
                          interval: str,
                          start_date: str,
                          end_date: str,
                          country: str,
                          exchange: str,
                          symbol: str):
        res = requests.get(f'{self.base_url}/time_series?apikey={self.token}&interval={interval}&start_date={start_date}&end_date={end_date}&format=JSON&country={country}&exchange={exchange}&type=none&symbol={symbol}')