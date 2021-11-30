from pprint import pprint

# for greater simplicity install our package
# https://github.com/twelvedata/twelvedata-python

import requests

response = requests.get(
    "https://api.twelvedata.com/time_series?apikey=d47b661071de40f18a6d2cc8fd7ba710&interval=1day&start_date=2021-11-15 19:21:00&end_date=2021-11-22 19:21:00&format=JSON&country=US&exchange=NYSE&type=none&symbol=EUR/USD")

pprint(response.text)

