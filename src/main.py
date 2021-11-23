from src.api_clients.nbp_client import NBPClient

nbp_client = NBPClient()
gold_price = nbp_client.get_gold_price()

print(gold_price)
