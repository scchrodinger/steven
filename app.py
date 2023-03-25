#!/usr/bin/env python3
import requests
from cli_args_system import Args


args = Args(convert_numbers=False)

currency = args.flag_str('currency')
apikey = args.flag_str('api')
limit = args.flag_str('limit')
start = args.flag_str('start')


headers = {
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : apikey,
}

params = {
    'start' : start,
    'limit' : limit,
    'convert' : currency,
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

try:
    response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()

    json_data = response.json()

    if 'data' in json_data:
        coins = json_data['data']
        
        for x in coins:
            price = x['quote'][currency]['price']
            print(f"Coin: {x['symbol']}  Price: {price} {currency}")

    else:
        print('null')

except requests.exceptions.HTTPError as err:
    print(f'req failure: {err}')
