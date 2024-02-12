import wolframalpha
import wikipedia
import requests


### Place various functions used by all of ISAAC in this file ###

def weather_main() -> str:
    with open('weatherapi.txt', 'r') as f:
        contents = f.read().split("\n")
        api_key = contents[0]
        city_name = contents[1]
        f.close()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = int(((float(y["temp"]) - 273) * 9 / 5) + 32)
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return current_temperature
    else:
        return "Weather is currently unavailable"

def init_alpha():
    global client
    with open("waid.txt", 'r') as f:
        id = f.read()
    client = wolframalpha.Client(id)
    return client

def alpha_response(question):
    res = client.query(question)
    return next(res.results).text

def info_response(query):
    try:
        return alpha_response(query)
    except StopIteration:
        return "According to wikipedia: " + wikipedia.summary(query, sentences=3)
        