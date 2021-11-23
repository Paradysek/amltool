import pprint

from src.api_clients.nbp_client import NBPClient


def test_nbp_client_get_exchagne_rate():
    client = NBPClient()
    res = client.get_exchange_rate('A', 'USD')
    pprint.pprint(res)


def test_nbp_client_get_gold_price():
    client = NBPClient()
    res = client.get_gold_price()
    pprint.pprint(res)
