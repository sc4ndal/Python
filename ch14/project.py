import json
from tkinter import *

import requests
import urlopen
from pyowm import owm
from requests import *
from json import *
from datetime import datetime
from io import BytesIO
from PIL import Image
import threading
import urllib.request
import cv2
from PIL import ImageTk, Image

win = Tk()
win.geometry('600x300')
win.resizable(0,0)
win.title('wheather app')

dt=datetime.now()
dt=dt.strftime('%Y-%m-%d %H:%M:%S')
print("현재시간 : "+dt)
city_name = "busan"
api_key = 'e6556117f5b050ff93999b87d6de170b'
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
response = requests.get(weather_url)
weather_info = response.json()
json.dumps(weather_info, indent="\t")

print(weather_info)
print(weather_info['weather'][0]['icon'])
print(weather_info['weather'][0]['main'])

def searchCity():
    city_name=entry.get()
    kelvin=273
    api_key = 'e6556117f5b050ff93999b87d6de170b'
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    json.dumps(weather_info, indent="\t")
    temp2.configure(text=""+str(round(weather_info['main']['temp']-kelvin,2))+"ºc")
    hum2.configure(text=""+str(weather_info['main']['humidity'])+"%")
    ws2.configure(text=""+str(weather_info['wind']['speed'])+"m/s")
    ndtest = str(weather_info['weather'][0]['icon'])
    if("n" in ndtest):
        dn.configure(text="저녁입니다.")
    else:
        dn.configure(text="낮입니다.")
    # img1.configure(image=img11)

    if(weather_info['weather'][0]['main']=="Clouds"):
        img1.configure(image=clody)
    if(weather_info['weather'][0]['main']=="Clear"):
        img1.configure(image=clear)
    if(weather_info['weather'][0]['main']=="Rain"):
        img1.configure(image=rain)





# owm = OWM(API_key)
# city_name='Busan'

# print(weather_url)

# kelvin = 273

# print('response = ', response)

# if response == 200:

# print(weather_info)

# print(json.dumps(weather_info, indent="\t"))
# print("날씨")
# print(weather_info['weather'])
# print("날씨정보")
# print(weather_info['weather'][0]['description'])
# print("온도")
# print(str(round(weather_info['main']['temp']-kelvin,2))+"ºc") #round로 상수만 반환,2로 소수점 두자리까지 반환
# print("습도")
# print(str(weather_info['main']['humidity'])+"%")
# print("바람")
# print(str(weather_info['wind']['speed'])+"m/s")
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  날씨 아이콘 받아오는 링크
# print(weather_info['sys']['sunrise'])
iconcode = weather_info['weather'][0]['icon']
iconurl = "http://openweathermap.org/img/w/"+iconcode+".png"
# img22 = ImageTk.PhotoImage(Image.open(iconurl))
# cv2.imshow("test",iconurl)
# print(img11)
# req = Image.open(BytesIO(res.content))
print(iconurl)
# ll = Label(win, image=req)
# ll.grid(row=0,column=5)
#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑링크는 만들었지만 링크로 이미지 붙이는건 미구현


clody = PhotoImage(file="cloudy.png")
clear = PhotoImage(file="day_clear.png")
suncloud = PhotoImage(file="day_partial_cloud.png")
rain = PhotoImage(file="day_rain.png")

elabel = Label(win,text="찾을 도시 : ")
elabel.grid(row=0, column=0)
entry = Entry(win)
entry.grid(row=0, column=1)
ebtn = Button(win,text="검색",command=searchCity)
ebtn.grid(row=0,column=2)

temp1 = Label(win,text="온도 : ")
temp1.grid(row=1,column=0)
temp2 = Label(win)
temp2.grid(row=1,column=1)

hum1 = Label(win,text="습도 : ")
hum1.grid(row=2,column=0)
hum2 = Label(win)
hum2.grid(row=2,column=1)

ws1 = Label(win,text="풍속 : ")
ws1.grid(row=3,column=0)
ws2 = Label(win)
ws2.grid(row=3,column=1)

nd = Label(win,text="현재 시간 : "+dt)
nd.grid(row=4,column=0)

dn = Label(win)
dn.grid(row=4,column=1)

img1 = Label(win)
img1.grid(row=5,column=0)
img2 = Label(win)
img2.grid(row=5,column=1)

exit = Button(win,text="종료",command=win.destroy)
exit.grid(row=5,column=3)




win.mainloop()

