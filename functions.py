import asyncio
import wolframalpha
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
        return "No answer"

def query_handler(query):
    print("Received " + query)
    print(alpha_response(query))