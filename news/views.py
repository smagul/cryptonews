import requests
import json

from django.shortcuts import render


def home(request):
    # Grab Crypto Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,XLM,LTC,USDT,XMR,ADA,MIOTA&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        return render(request, 'prices.html', {'quote': quote})

    return render(request, 'prices.html', {})
