import webapi

print("Hello World!")
print('hello from mateurz')
print("O Dzień dobry")


# example of getting exchange rate from NBP

res = webapi.get_exchange_rate('A', 'CHF')
json_response = res.json()
print(json_response['rates'][0]['mid'])


