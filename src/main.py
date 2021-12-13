from src.api_clients.nbp_client import NBPClient
from src.api_clients.twelve_data_client import TwelveDataClient

nbp_client = NBPClient()
twelvedata_client = TwelveDataClient()
gold_price = nbp_client.get_exchange_rate('A','USD')


test = twelvedata_client.get_exchange_rate_list('1day','2021-11-11 00:00:00','2021-11-18 00:00:00','US','NYSE','EUR/USD')
print(test)