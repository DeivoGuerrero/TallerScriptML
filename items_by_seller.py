#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import os
import time

find_site = False
mi_lista = []

print ("Programa que identifica todos los items de un vendedor...")
in_site = raw_input("Ingrese el ID del Site: ")

# Cargamos los Sites Disponibles
url = 'https://api.mercadolibre.com/sites/' + in_site.upper()
r_site = requests.get (url)
if r_site.ok:
    find_site = True
else:
    print ('Site no encontrado')

if find_site:
    url = 'https://api.mercadolibre.com/users/'
    in_seller = raw_input("Ingrese el ID del vendedor: ")

    r_seller = requests.get(url + in_seller)
    if r_seller.ok:
        url = 'https://api.mercadolibre.com/sites/' + in_site.upper() + '/search?seller_id=' + in_seller 
        args = { 'attributes': 'results' }
        r = requests.get (url, params=args)
        if r.ok:
            result = json.loads(r.text)
            for result in result['results']:
                n_id = result['id']
                n_title = result['title']
                n_category_id = result['category_id']

                url = 'https://api.mercadolibre.com/categories/' + n_category_id.upper()
                r = requests.get(url)
                if r.ok:
                    result = json.loads(r.text)
                    n_name_category = result['name'] 
                    mi_lista.append('id=' + n_id + '::title=' + n_title + '::category_id=' + n_category_id + '::name_category=' + n_name_category)
            for item in mi_lista:
                file = open("items_" + in_site.upper() + in_seller.upper() + "_" + time.strftime("%c") + ".log", "w")
                file.write( item + os.linesep)
                file.close()
    else:
        print ('Vendedor no encontrado')