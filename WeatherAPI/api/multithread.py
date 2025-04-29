import time
import openmeteo_requests

from queue import Queue
from threading import Thread
from openmeteo_requests import Client

from WeatherAPI.config import URL, PARAMS, COUNT

q = Queue()

def get_response(meteo: Client, url: str, params: dict):
	responses = meteo.weather_api(url, params=params)
	q.put(responses[0])


def get_weather_with_threading():
	threads = []
	open_meteo: Client = openmeteo_requests.Client()

	time_start = time.time()
	for _ in range(COUNT):
		thread = Thread(target=get_response, args=(open_meteo, URL, PARAMS))
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()
	print(f"Time taken: {time.time() - time_start:.2f} seconds")


if __name__ == '__main__':
	get_weather_with_threading()
	while not q.empty():
		result = q.get()
		print(f"Coordinates {result.Latitude()}°N {result.Longitude()}°E")
		current = result.Current()
		current_temperature_2m = current.Variables(0).Value()
		print(f"Current temperature {current_temperature_2m:.1f}°C\n")