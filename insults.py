#!/usr/bin/python3

import requests

url = "https://evilinsult.com/generate_insult.php?lang=pt&type=json"

insult  = requests.get(url)

i = insult.json()

print(i['insult'],"\n", i['comment'])




