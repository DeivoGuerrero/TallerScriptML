#! /usr/bin/python
import requests
import json
import os

print ("Programa que identifica todos los items de un vendedor...")
in_site = raw_input("Ingrese el ID del Site: ")
find_site = False

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
    # BORRAR ESTO
    in_seller = "81644614"
    r_seller = requests.get(url + in_seller)
    if r_seller.ok:
        url = 'https://api.mercadolibre.com/sites/' + in_site.upper() + '/search?seller_id=' + in_seller 
        args = { 'attributes': 'results' }
        r = requests.get (url, params=args)
        if r.ok:
            result = json.loads(r.text)
            for result in result['results']:
                #mi_json = result.json()
                print "KEY: "
                n_id = result['id']
                n_title = result['title']
                n_category_id = result['category_id']

                url = 'https://api.mercadolibre.com/categories/' + n_category_id.upper()
                r = requests.get(url)
                if r.ok:
                    result = json.loads(r.text)
                    n_name_category = result['name'] 
                    print "ID: " + n_id + " - TITLE: " + n_title + " - ID_CATEGORY: " + n_category_id + " - NAME_CATEGORY: " + n_name_category
                #print result
                #print mi_json['id']
            mi_json = r.json()
            #print mi_json


            """
            mi_json = json.loads(r.text)
            for m_results in mi_json:
                print m_results.content
            """
    else:
        print ('Vendedor no encontrado')