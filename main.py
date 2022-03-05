from urllib import response
import requests
import json

"""
#Simple request

i = 1
while i < 11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status = j['status']
    print("El personaje {}.- {} tiene status: {}".format(i, name, status))
    i += 1
"""
#Request episodios
url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
personajes = (j['characters'])
list_names = list()
list_names_humans = list()
list_names_others = list()
humanosT = 0
NoHumanosT = 0

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    list_names.append(name)
    if js['species']== 'Human':
        list_names_humans.append(name)
    else:
        list_names_others.append(name)

        
print("El numero total de personajes es: ", len(list_names))
for list_name_human in list_names_humans:
    humanosT += 1
    print("El personaje humano {} es: {}".format(humanosT, list_name_human))

for list_name_other in list_names_others:
    NoHumanosT += 1
    print("El personaje no humano {} es: {}".format(NoHumanosT, list_name_other))
