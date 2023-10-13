import asyncio
import wolframalpha
import wikipedia
import GUI
### Place various functions used by all of ISAAC in this file ###

import python_weather

async def get_weather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get("Marmora, NJ")
        return str(weather.current.temperature)

def weather_main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_weather())

def init_alpha():
    global client
    with open("waid.txt", 'r') as f:
        id = f.read()
    client = wolframalpha.Client(id)
    return client

def alpha_response(question):
    res = client.query(question)
    try:
        answer = next(res.results).text
        return answer
    except StopIteration:
        return None

def info_response(query):
    answer = alpha_response(query)
    if answer == None:
        answer = wikipedia.summary(query, sentences=3)
    return "xAccording to wikipedia: " + answer # The "x" is for formatting in java (I don't know why this is necessary)

def query_handler(query):
    asyncio.set_event_loop(asyncio.new_event_loop())
    asyncio.get_event_loop().run_until_complete((GUI.communicator.send_message("0002" + info_response(query))))

# TODO! Everything is being sent to wikipedia instead of WolframAlpha
# TODO! Add scroll bar to java GUI