from src.api_clients.nbp_client import NBPClient
from src.api_clients.twelve_data_client import TwelveDataClient

nbp_client = NBPClient()
twelvedata_client = TwelveDataClient()
gold_price = nbp_client.get_exchange_rate('A','USD')
test = twelvedata_client.get_exchange_rate_list('1day','2021-11-11 00:00:00','2021-11-18 00:00:00','US','NYSE','EUR/USD')
test1 = twelvedata_client.get_avgpricelist('1day','EUR/USD','2021-11-17 00:00:00','2021-11-30 00:00:00')

print(test1)