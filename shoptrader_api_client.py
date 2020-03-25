import requests


class ShoptraderAPIClient:
    API_URL = 'shoptrader.nl/'
    API_key = None
    status_code = None

    def __init__(self, API_URL, API_key):
        self.API_URL = API_URL + self.API_URL
        self.API_key = API_key
