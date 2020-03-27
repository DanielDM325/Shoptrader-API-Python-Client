import requests
#import json


class ShoptraderAPIClient:
    API_URL = '.shoptrader.com/api/v2/'
    token = None
    status_code = None

    def __init__(self, API_URL, token):
        self.API_URL = 'http://' + API_URL + self.API_URL
        self.token = {'token': token}

    def products_get_product(self, code_type, product_code):
        API_URL = self.API_URL + 'products/' + str(product_code)
        headers = {'accept': 'application/json'}
        params = {'token': self.token['token'], 'search': code_type}
        response = requests.get(API_URL, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_post_product(self, model, sku, ean, name, quantity, price, purchase_price, status, images, images_alt, height, width, category_id, tax_rate, tax_class_id, meta_title, meta_keyword, meta_description, description, extra_description, intro_description):
        API_URL = self.API_URL + 'products'
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {
            'model': str(model),
            'sku': str(sku),
            'ean': str(ean),
            'name': name,
            'quantity': quantity,
            'price': price,
            'purchasePrice': purchase_price,
            'status': status,
            'images': images,
            'imagesAlt': images_alt,
            'height': height,
            'width': width,
            'categoryId': str(category_id),
            'taxRate': tax_rate,
            'taxClassId': tax_class_id,
            'metaTitle': meta_title,
            'metaKeyword': meta_keyword,
            'metaDescription': meta_description,
            'description': description,
            'extraDescription': extra_description,
            'introDescription': intro_description
        }
        response = requests.post(API_URL, params=self.token, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def currencies_get_currencies(self):
        API_URL = self.API_URL + 'currencies'
        headers = {'accept': 'aplication/json'}
        response = requests.get(API_URL, params=self.token, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
