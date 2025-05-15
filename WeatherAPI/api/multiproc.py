import time
import requests

from multiprocessing import Pool

from WeatherAPI.config import URL, PARAMS, COUNT


def get_response(url: str, params: dict) -> dict:
	responses = requests.get(url, params=params, timeout=10)
	if responses.status_code != 200:
		raise Exception(f"Error: {responses.status_code}")
	return responses.json()


def get_weather_with_multiprocessing() -> list[dict]:
	time_start = time.time()
	with Pool(processes=4) as p:
		responses = p.starmap(get_response, [(open_meteo, URL, PARAMS) for _ in range(COUNT)])
	print(f"Time taken: {time.time() - time_start:.2f} seconds")
	return responses

if __name__ == '__main__':
	results = get_weather_with_multiprocessing()
	for i, result in enumerate(results):
		print(f"Coordinates {result.Latitude()}°N {result.Longitude()}°E")
		current = result.Current()
		current_temperature_2m = current.Variables(0).Value()
		print(f"Current temperature {current_temperature_2m:.1f}°C\n")