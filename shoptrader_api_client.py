import requests


class ShoptraderAPIClient:
    API_URL = '/api/v2/'
    token = None
    status_code = None

    def __init__(self, API_URL, token, credentials=None):
        self.API_URL = API_URL + self.API_URL
        self.token = {'token': token}
        self.credentials = credentials

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

    def products_post_product(self, model, sku, ean, name, quantity, price, purchase_price, status, images, images_alt, height, width, category_id, tax_rate, tax_class_id, manufacturer_id, meta_title, meta_keyword, meta_description, description, extra_description, intro_description, supplier_id):
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
            'width': width,
            'height': height,
            'categoryId': str(category_id),
            'taxRate': tax_rate,
            'taxClassId': tax_class_id,
            'manufacturerId': manufacturer_id,
            'metaTitle': meta_title,
            'metaKeyword': meta_keyword,
            'metaDescription': meta_description,
            'description': description,
            'introDescription': intro_description,
            'extraDescription': extra_description,
            'supplier_id': str(supplier_id)
        }
        response = requests.post(API_URL, params=self.token, headers=headers, json=data, auth=self.credentials)
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
