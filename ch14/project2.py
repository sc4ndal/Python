# OpenWeather icon 처리 : https://openweathermap.org/weather-conditions#How-to-get-icon-URL

from tkinter import *
import requests
import json
from datetime import datetime

win = Tk()
win.geometry("400x400")
win.resizable(0,0)
win.title("Weather App")

api_key = "e6556117f5b050ff93999b87d6de170b"
city_name = 'Busan'
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='  \
              + city_name + '&appid=' + api_key
print(weather_url)

# # Get the response from fetched url
response = requests.get(weather_url)
print('response = ', response)
#
# # changing response from json to python readable
weather_info = response.json()
print(weather_info)
print(json.dumps(weather_info,  indent="\t"))
#
print(weather_info['weather'])
print(weather_info['weather'][0]['description'])
print(weather_info['sys']['sunrise'])
print('humidity : ', weather_info['main']['humidity'], '%')
#
# win.mainloop()