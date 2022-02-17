#!/opt/homebrew/bin/python3
import requests
import json


user_currency = input().lower() # user_currency
currency_cache = {} # empty currency in cache


# add currency of USD and EUR in cache
r = requests.get(f'http://www.floatrates.com/daily/{user_currency}.json')

r_str = r.text
r_python = json.loads(r_str)

for i, j in r_python.items():
  if i == 'usd':
    currency_cache['usd'] = j
  elif i == 'eur':
    currency_cache['eur'] = j


# function - check if user_inputs are in cache
def compare_user_input_and_cache():

  while True:
    exchange_currency = input()

    if not exchange_currency:
      break

    exchange_amount = float(input())

    print(f'Checking the cache...')

    if exchange_currency.lower() in currency_cache:
      print(f'Oh! It is in the cache!')
    else:
      print(f'Sorry, but it is not in the cache!')
      add_users_exchange_currency_in_cache(exchange_currency)

    users_exchange_amount(exchange_currency, exchange_amount)


# function - get the exchange amount
def users_exchange_amount(currency, amount):
  user_exchange_rate = r_python[f'{currency.lower()}']['rate']

  print(f'You received {user_exchange_rate * amount} {currency.upper()}')


# function - add new queried user input to cache
def add_users_exchange_currency_in_cache(currency):

  for i, j in r_python.items():
    if i == currency.lower():
      currency_cache[f'{currency.lower()}'] = j

# execute
compare_user_input_and_cache()
