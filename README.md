# Shoptrader API Python Client
 
The Shoptrader API Python Client is a wrapper developed to interface with the REST API provided by the Shoptrader platform. It greatly helps to develop applications using Python code instead of calling numerous url's using cURL. To get a complete view of all available calls visit their [API documentation page] (http://apidocs.shoptrader.com/).

## Getting Started

### Token Creation
Start out by creating an API token in the back office. This token will grant access to the API and define which rights a certain token might have or not have: read, write and delete.

```
Configuratie --> Api --> Add new token by providing a description and rights
```

Keep the token safe. If it ends up in malicous hands they will be able to abuse it. The token will be used when creating an API client object.

### Installing

Use the package manager pip to install this package.
```bash
pip install shoptrader_api_client
```