import requests


class ShoptraderAPIClient:
    API_URL = 'shoptrader.nl/api/v2/'
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

    def products_post_product(model, sku, ean, name, quantity, price, purchase_price, status, images, images_alt, height, width, category_id, tax_rate, tax_class_id, meta_title, meta_keyword, meta_description, description, extra_description, intro_description):
        API_URL = self.API_URL + 'products/'
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = {
            'model': model,
            'sku': str(sku),
            'ean': str(ean),
            'name': name,
            'quantity': str(quantity),
            'price': str(price),
            'purchasePrice': str(purchase_price),
            'images': images,
            'imagesAlt': images_alt,
            'height': str(height),
            'width': str(width),
            'categoryId': str(category_id),
            'taxRate': str(tax_rate),
            'taxClassId': str(tax_class_id),
            'metaTitle': meta_title,
            'metaKeyword': meta_keyword,
            'metaDescription': meta_description,
            'description': description,
            'extraDescription': extra_description,
            'introDescription': intro_description
        }
        response = requests.post(API_URL, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            return None
