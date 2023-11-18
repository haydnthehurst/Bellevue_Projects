#Final version of weather program

import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
API_KEY = "fe3b5a322005921d3177ffa0a88722d6"
CITY = input("What city would you like to know the weather of? ")
URL = BASE_URL + CITY + "&appid=" + API_KEY + "&units=imperial"

while True:
    try:
        response = requests.get (URL)
    except:
        print('Connection was unable to be established')
    else:
        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            temperature = main["temp"]
            humidity = main ["humidity"]
            pressure = main["pressure"]
            report = data["weather"]
            print(f"The weather in {CITY.title()} is: ")
            print(f"Temperature: {temperature}˚")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} inHg")
            print(f"Weather Report: {report[0]['description' ].title()}")
        else:
            print ("Invalid data entered or error in the HTTP request")
    runagain = input('Would you like to know the weather of another city? ("y" or "n")')
    if runagain == 'y':
        CITY = input('What city?')
    else:
        break
