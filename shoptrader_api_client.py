import requests


class ShoptraderAPIClient:
    API_URL = '/api/v2/'
    token = None
    status_code = None

    def __init__(self, API_URL, token, credentials=None):
        self.API_URL = API_URL + self.API_URL
        self.token = {'token': token}
        self.credentials = credentials

    def orders_post_order(self, basket_key=None, currency_type=None, language_id=None, comment=None, payment_status=None, payment_transaction_id=None, payment_comment=None):
        API_URL = self.API_URL + 'orders'
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {}
        if basket_key is not None:
            data['baskeyKey'] = str(basket_key)
        if currency_type is not None:
            data['currencyType'] = currency_type
        if language_id is not None:
            data['languageId'] = language_id
        if comment is not None:
            data['comment'] = comment
        if payment_status is not None:
            data['paymentStatus'] = payment_status
        if payment_transaction_id is not None:
            data['paymentTransactionId'] = str(payment_transaction_id)
        if payment_comment is not None:
            data['paymentComment'] = payment_comment
        response = requests.post(API_URL, params=self.token, headers=headers, json=data, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_get_product(self, code_type, product_code):
        API_URL = self.API_URL + 'products/' + str(product_code)
        headers = {'accept': 'application/json'}
        params = {'search': code_type, 'token': self.token['token']}
        response = requests.get(API_URL, params=params, headers=headers, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_patch_product(self, product_code, model, sku, ean, name, description, intro_description, extra_description, meta_title, meta_keyword, meta_description, quantity, category_id, price, purchase_price, status, tax_rate, manufacturer_id, images, images_alt):
        API_URL = self.API_URL + 'products/' + str(product_code)
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {}
        if model is not None:
            data['model'] = str(model)
        if sku is not None:
            data['sku'] = str(sku)
        if ean is not None:
            data['ean'] = str(ean)
        if name is not None:
            data['name'] = name
        if description is not None:
            data['description'] = description
        if intro_description is not None:
            data['introDescription'] = intro_description
        if extra_description is not None:
            data['extraDescription'] = extra_description
        if meta_title is not None:
            data['metaTitle'] = meta_title
        if meta_keyword is not None:
            data['metaKeyword'] = meta_keyword
        if meta_description is not None:
            data['metaDescription'] = meta_description
        if quantity is not None:
            data['quantity'] = quantity
        if category_id is not None:
            data['categoryId'] = category_id
        if price is not None:
            data['price'] = price
        if purchase_price is not None:
            data['purchasePrice'] = purchase_price
        if status is not None:
            data['status'] = status
        if tax_rate is not None:
            data['taxRate'] = tax_rate
        if manufacturer_id is not None:
            data['manufacturerId'] = manufacturer_id
        if images is not None:
            data['images'] = images
        if images_alt is not None:
            data['imagesAlt'] = images_alt
        response = requests.patch(API_URL, params=self.token, headers=headers, json=data, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_get_products_range(self, only_main_products, offset):
        API_URL = self.API_URL + 'products'
        headers = {'accept': 'application/json'}
        params = {
            'filter[only_main_products]': 'true' if only_main_products else 'false',
            'offset': str(offset),
            'token': self.token['token']
        }
        response = requests.get(API_URL, params=params, headers=headers, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_get_number_of_products(self):
        response = self.products_get_products_range(True, 0)
        if response is None:
            return None
        else:
            return int(response['numRows'])

    def products_post_product(self, model=None, sku=None, ean=None, name=None, seo_name=None, quantity=None, price=None, purchase_price=None, status=None, images=None,
                              images_alt=None, height=None, width=None, category_id=None, tax_rate=None, tax_class_id=None, manufacturer_id=None, meta_title=None, meta_keyword=None,
                              meta_description=None, description=None, extra_description=None, intro_description=None, supplier_id=None):
        API_URL = self.API_URL + 'products'
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {}
        if model is not None:
            data['model'] = str(model)
        if sku is not None:
            data['sku'] = str(sku)
        if ean is not None:
            data['ean'] = str(ean)
        if name is not None:
            data['name'] = name
        if seo_name is not None:
            data['seoName'] = seo_name
        if quantity is not None:
            data['quantity'] = quantity
        if price is not None:
            data['price'] = price
        if purchase_price is not None:
            data['purchasePrice'] = purchase_price
        if status is not None:
            data['status'] = status
        if images is not None:
            data['images'] = images
        if images_alt is not None:
            data['imagesAlt'] = images_alt
        if width is not None:
            data['width'] = width
        if height is not None:
            data['height'] = height
        if category_id is not None:
            data['categoryId'] = str(category_id)
        if tax_rate is not None:
            data['taxRate'] = tax_rate
        if tax_class_id is not None:
            data['taxClassId'] = tax_class_id
        if manufacturer_id is not None:
            data['manufacturerId'] = manufacturer_id
        if meta_title is not None:
            data['metaTitle'] = meta_title
        if meta_keyword is not None:
            data['metaKeyword'] = meta_keyword
        if meta_description is not None:
            data['metaDescription'] = meta_description
        if description is not None:
            data['description'] = description
        if intro_description is not None:
            data['introDescription'] = intro_description
        if extra_description is not None:
            data['extraDescription'] = extra_description
        if supplier_id is not None:
            data['supplierId'] = supplier_id
        response = requests.post(API_URL, params=self.token, headers=headers, json=data, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def products_delete_product(self, product_code):
        API_URL = self.API_URL + 'products/' + str(product_code)
        headers = {'accept': 'aplication/json'}
        response = requests.delete(API_URL, params=self.token, headers=headers, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def currencies_get_currencies(self):
        API_URL = self.API_URL + 'currencies'
        headers = {'accept': 'aplication/json'}
        response = requests.get(API_URL, params=self.token, headers=headers, auth=self.credentials)
        if response.status_code == 200:
            return response.json()
        else:
            return None
