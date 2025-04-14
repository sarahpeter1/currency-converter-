# currency convrter system in python
import requests

api_key = "6f4ecc619f302998b156695e"
base_url =  f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"


def convert_currency(from_currency,to_currency,amount):
    response = requests.get(base_url)
    if response.status_code != 200:
        return 'Error getting the exhange rates'
    data = response.json()
    rates = data.get('conversion_rates', {})

    if from_currency not in rates or to_currency not in rates:
        return 'Wrong currency code'
    
    # target currency / from from_currency or base to_currency rates['CAD']
    
    convert = amount * (rates[to_currency] / rates[from_currency])
    
    #2usd = 3000 ngn
    return f"{amount} {from_currency} = {convert}{to_currency}"
    # return f"The conversion of {amount}{from_currency} is {convert}{to_currency}"



# we need to collect user inputs which are the base currency, target currency and amount, 4.6, 2.0
from_currency = input('Enter the base currency e.g usd,gbp: ').upper()
to_currency = input('Enter the target currency e.g usd,gbp: ').upper()
amount = float(input('Enter the amount: '))

our_result = convert_currency(from_currency,to_currency,amount)
print(our_result)


