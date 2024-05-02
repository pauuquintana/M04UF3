#!/usr/bin/python3

import requests

url = "https://cataas.com/cat?json=true"

cataas = requests.get(url)

cat_data = cataas.json()


for fact in cat_data:
	print(fact.['text']+"\n")




