#! /usr/bin/python
import requests
import json

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
    r_seller = requests.get(url + in_seller)
    if r_seller.ok:
        url = 'https://api.mercadolibre.com/sites/' + in_site.upper() + '/search?seller_id=' + in_seller 
        args = { 'attributes': 'results' }
        r = requests.get (url, params=args)
        if r.ok:
            mi_json = r.json()
            print mi_json
            """
            mi_json = json.loads(r.text)
            for m_results in mi_json:
                print m_results.content
            """
    else:
        print ('Vendedor no encontrado')