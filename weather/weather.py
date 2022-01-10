import pip._vendor.requests as req
import json

print("=====WEATHER=====")
print()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter city name: ")
API_KEY = "809c5980d2fae6cc3ab849d221faa4a2"
print()
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"

try:
    res = req.get(URL)
except:
    print('URL is not complete')

if res.status_code == 200:
   data = res.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}"+ u'\N{DEGREE SIGN}')
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   print("Error in the HTTP request")