# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 00:56:38 2021

@author: kalt9
"""

import requests
import json

# Connecting to the Nutritionix API, the largest verified database of nutrition
# information; contains nutritional info on 1000s of grocery, restaurant and 
# common foods

nutriHEADERS = {
    'app-id':"INSERT ID HERE",
    'app-key':"INSERT KEY HERE",
    'Content-Type': "application/json"
    }


#### Pulling down Lipton tea product data
url = 'https://trackapi.nutritionix.com/v2/search/instant?query=<lipton tea>'

nutriresponse = requests.get(url, headers=nutriHEADERS)
nutriresponse.status_code
nutriresponseJson = nutriresponse.json()

#### Pulling down nutritional data
nutrientsurl = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
query = {'query':'dark chocolate'}
nutrientresponse = requests.post(nutrientsurl, headers=nutriHEADERS, json=query)
nutrientresponse.status_code
nutrientresponseJson = nutrientresponse.json()