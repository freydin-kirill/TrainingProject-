import time
import asyncio
import openmeteo_requests

from openmeteo_requests import Client
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse

from WeatherAPI.config import URL, PARAMS, COUNT


async def get_response(meteo: Client, url: str, params: dict) -> WeatherApiResponse:
	responses = await asyncio.to_thread(meteo.weather_api, url, params=params)
	return responses[0]


async def get_weather_with_asyncio() -> list[WeatherApiResponse]:
	open_meteo: Client = openmeteo_requests.Client()

	time_start = time.time()
	tasks = [get_response(open_meteo, URL, PARAMS) for _ in range(COUNT)]
	responses = await asyncio.gather(*tasks)
	print(f"Time taken: {time.time() - time_start:.2f} seconds")
	return responses

if __name__ == '__main__':
	results = asyncio.run(get_weather_with_asyncio())
	for i, result in enumerate(results):
		print(f"Coordinates {result.Latitude()}°N {result.Longitude()}°E")
		current = result.Current()
		current_temperature_2m = current.Variables(0).Value()
		print(f"Current temperature {current_temperature_2m:.1f}°C\n")