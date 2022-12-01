#import datetime as dt
#from email.policy import default
#from types import CoroutineType
#from urllib import response
#from pip import main
#import requests
#from app.controllers.default import city

#URL_BASE = "https://api.openweathermap.org/data/2.5/weather?"
#CHAVE_API = "4e57b56702d12e0263b188773495de82"

#url = URL_BASE + "&" + "units=metric" + "&" + "appid=" + CHAVE_API + "&q=" + city
#response = requests.get(url).json()

#temp = response['main']['temp']
#sens = response['main']['feels_like']
#temp_max = response['main']['temp_max']
#temp_min = response['main']['temp_min']
#teste= response['name']