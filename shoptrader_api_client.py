import requests


class ShoptraderAPIClient:
    API_URL = 'shoptrader.nl/'
    API_key = None
    status_code = None

    def __init__(self, API_URL, API_key):
        self.API_URL = API_URL + self.API_URL
        self.API_key = API_key

    def products_get_product(code_type, product_code):
        API_URL = self.API_URL + 'products/' + str(product_code)
        headers = {'accept': 'application/json'}
        params = {'search', code_type}
        response = requests.get(API_URL, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
