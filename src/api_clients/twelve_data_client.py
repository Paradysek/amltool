from dataclasses import dataclass
import requests
import json


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


@dataclass
class AvgPriceRecord:
    datetime: str
    avgprice: float


@dataclass
class AvgPriceModel:
    symbol: str
    interval: str
    currency_base: str
    currency_quote: str
    type: str
    values: list[AvgPriceRecord]


class TwelveDataClient:

    def __init__(self):
        self.base_url = 'https://api.twelvedata.com'
        self.token = self._get_token()

    def get_exchange_rate_list(self,
                               interval: str,
                               start_date: str,
                               end_date: str,
                               country: str,
                               exchange: str,
                               symbol: str) -> TwelveDataModel:
        res = requests.get(
            f'{self.base_url}/time_series'
            f'?apikey={self.token}'
            f'&interval={interval}'
            f'&start_date={start_date}'
            f'&end_date={end_date}'
            f'&format=JSON'
            f'&country={country}'
            f'&exchange={exchange}'
            f'&type=none'
            f'&symbol={symbol}'
        )

        return self._map_to_twelvedata_model(res.json())

    def get_avgpricelist(self,
                         interval: str,
                         symbol: str,
                         start_date: str,
                         end_date: str) -> AvgPriceModel:
        res = requests.get(
            f'{self.base_url}/avgprice'
            f'?apikey={self.token}'
            f'&interval={interval}'
            f'&symbol={symbol}'
            f'&start_date={start_date}'
            f'&end_date={end_date}'
            f'&format=JSON'
        )

        return self._map_to_avgpricemodel(res.json())

    def _map_to_twelvedata_model(self, response: dict) -> TwelveDataModel:
        meta = response['meta']
        values = response['values']
        records = []
        for value in values:
            record = TwelveDataRecord(
                datetime=value['datetime'],
                open=value['open'],
                high=value['high'],
                low=value['low'],
                close=value['close']
            )

            records.append(record)

        return TwelveDataModel(
            symbol=meta['symbol'],
            interval=meta['interval'],
            currency_base=meta['currency_base'],
            currency_quote=meta['currency_quote'],
            values=records

        )

    def _map_to_avgpricemodel(self, response: dict) -> AvgPriceModel:
        meta = response['meta']
        values = response['values']
        records = []
        for value in values:
            record = AvgPriceRecord(
                datetime=value['datetime'],
                avgprice=value['avgprice']
            )

            records.append(record)

        return AvgPriceModel(
            symbol=meta['symbol'],
            interval=meta['interval'],
            currency_base=meta['currency_base'],
            currency_quote=meta['currency_quote'],
            type=meta['type'],
            values=records
        )

    def _get_token(self):
        with open('api_clients/token.json') as json_file:
            data = json.load(json_file)

        return data['token']
