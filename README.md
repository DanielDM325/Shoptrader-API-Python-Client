![Node Development logo](https://www.nodedevelopment.net/wp-content/uploads/logo-Node-Development.png) ![Shoptader logo](https://www.myparcel.nl/app/uploads/2019/08/Logo_Shoptrader-180x0-c-default.png)
# Shoptrader API Python Client
> Developed by Node Development

The Shoptrader API Python Client is a wrapper developed to interface with the REST API provided by the Shoptrader platform. It greatly helps to develop applications using Python code instead of calling numerous url's using cURL. To get a complete view of all available calls visit their [API documentation page](http://apidocs.shoptrader.com/).

## Getting Started

### Token Creation
Start out by creating an API token in the back office. This token will grant access to the API and define which rights a certain token might have or not have: read, write and delete.

```
Back Office --> Configuratie --> Api --> Add new token by providing a description and rights
```

Keep the token safe. If it ends up in malicous hands they will be able to abuse it. The token will be used when creating an API client object.

### Installing

Use the package manager pip to install this package.
```bash
pip install shoptrader_api_client
```

## Usage

## Support
Need help developing an appliction? We at Node Development and Shoptrader can help you automate all kinds of functionality. Synchronizing products with an external database, keeping tab on your stock or importing orders into your accounting suite.

## Authors
This package is developed by Daniel Mizrahi from Node Development
[dmizrahi@nodedevelopment.net](mailto:dmizrahi@nodedevelopment.net)
[www.nodedevelopment.net](https://nodedevelopment.net)

Of course none of this would be possible without the help of Shoptrader.

## License
