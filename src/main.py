from src.api_clients.nbp_client import NBPClient

nbp_client = NBPClient()
gold_price = nbp_client.get_exchange_rate('A','USD')


test2 = nbp_client.get_gold_price_for_range('2021-12-01','2021-12-13')
print(test2)