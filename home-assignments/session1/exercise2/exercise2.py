# 1.
# Write a python program, that checks your location according to your IP.
# Then checks the current weather at your location and writes the result to a file in a regular text format.
import requests
import pyowm
import re

lines = []
end = '"'
city = re.compile('"city": "', re.IGNORECASE)
country = re.compile('"country": "', re.IGNORECASE)
r = requests.get('https://ipinfo.io/')
r.text
print(r.text, file=open("location", "w"))
file = open("location", "r")
with open('location', 'rt') as in_file:
    for line in in_file:
        if city.search(line) !=None:
            lines.append(line.rstrip('\n'))
            city_name = (line[(line.find(': "')+3):(line.rfind('",'))])
        if country.search(line) != None:
            lines.append(line.rstrip('\n'))
            country_name = (line[(line.find(': "')+3):(line.rfind('",'))])
owm = pyowm.OWM('65acef8a6dcd9d337fcc6a181b132552')
check_w = owm.weather_at_place(city_name+","+country_name)
my_city_w = check_w.get_weather()
print(my_city_w, file=open("my_city_w.txt", "w"))

# 2.
# In that same program, create a list with at least 10 cities,
# And print their current weather in the following format:
# “The weather in <city>, <country>(full country name) is XX degrees.

with open('cities_list', 'rt') as in_file:
    for i in in_file:
        city_list_name = (i[0:i.find(',')])
        city_list_country = (i[i.find(',')+1:i.rfind(',')])
        city_list_country_full = (i[i.rfind(',')+1:])
        city_list_country_full = city_list_country_full.rstrip('\n')
        api = pyowm.OWM('65acef8a6dcd9d337fcc6a181b132552')
        collectinfo = api.weather_at_place(city_list_name+","+city_list_country)
        short = collectinfo.get_weather()
        temperature = short.get_temperature('celsius')
        temperature = str(temperature)
        v_temp = (temperature[temperature.find("': ")+3:temperature.find(",")])
        print('The weather in '+city_list_name+', '+city_list_country_full+' is '+v_temp+' degrees.')