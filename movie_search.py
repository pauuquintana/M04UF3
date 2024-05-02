#!/usr/bin/python3


import requests
from colorama import Fore

title = "Buscador de peliculas"

print (Fore.YELLOW + title)
print ("-" * len(title))


name = input(Fore.GREEN + "\nIntroduce una pelicula: " + Fore.CYAN)
url="https://search.imdbot.workers.dev/?q="+name

movie = requests.get(url)
data = movie.json()

if not data['description']:
	print(Fore.RED + "Error: No se han encontrado resultados.")
else:
	title = data ['description'][0]['#TITLE']
	year = data ['description'][0]['#YEAR']
	actors = data ['description'][0]['#ACTORS']

	
	print(Fore.GREEN + "Titulo:" + Fore.CYAN + f" {title}" + Fore.GREEN)
	print(Fore.GREEN + "Año:" + Fore.CYAN + f" {year}" + Fore.GREEN)
	print(Fore.GREEN + "Actores:" + Fore.CYAN + f" {actors}" + Fore.GREEN)







