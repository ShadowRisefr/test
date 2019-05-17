import json
import requests
import sys

filename = "test.json"

maps = open(filename, mode = 'w', encoding="utf-8")

name1 = {
'Name': "Новокузнецк, зыряновская, 97",
}

name2 = {
'Name': "Новокузнецк, Доватора, 11",
}

name3 = {
'Name': "Новокузнецк, Клименко, 52а",
}

name4 = {
'Name': "Новокузнецк, Бардина, 27а",
}

name5 = {
'Name': "Новокузнецк, Дружбы, 2/1",
}

name6 = {
'Name': "Новокузнецк, Береговая, 134",
}

name7 = {
'Name': "Новокузнецк, Разведчиков, 3",
}

name8 = {
'Name': "Новокузнецк, Латугина, 20",
}

name9 = {
'Name': "Новокузнецк, Кутузова, 25",
}

mapsjs = []
mapsjs.append(name1)
mapsjs.append(name2)
mapsjs.append(name3)
mapsjs.append(name4)
mapsjs.append(name5)
mapsjs.append(name6)
mapsjs.append(name7)
mapsjs.append(name8)
mapsjs.append(name9)
json.dump(mapsjs,maps)

#---------------------load------------—

maps = open(filename, mode='r', encoding="utf-8")
maps_date = json.load(maps)

for x in maps_date:
    params = {

    'adress': x['Name'],
    'region': "russia",
    }
    print(params)
    YandexMapsUrl = "https://geocode-maps.yandex.ru/1.x/?apikey=82a32a7f-84a2-4eb0-bd73-fe49223472c7&format=json&geocode={}".format(x['Name'])
    print(YandexMapsUrl)
    req = requests.get(YandexMapsUrl)
    res = req.json()
    print(res)
    result = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

    print (str(result).split(' '))
