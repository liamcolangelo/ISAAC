### Place various functions used by all of JARVIS in this file ###

import python_weather

async def get_weather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get("Marmora, NJ")
        return str(weather.current.temperature)