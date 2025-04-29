import time
import openmeteo_requests

from openmeteo_requests import Client
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse

from WeatherAPI.config import URL, PARAMS, COUNT

def get_response(meteo: Client, url: str, params: dict) -> WeatherApiResponse:
    responses = meteo.weather_api(url, params=params)
    return responses[0]

def get_weather_sequential() -> list[WeatherApiResponse]:
    results = []
    open_meteo: Client = openmeteo_requests.Client()

    time_start = time.time()
    for _ in range(COUNT):
        responses = open_meteo.weather_api(URL, params=PARAMS)
        results.append(responses[0])
    print(f"Time taken: {time.time() - time_start:.2f} seconds")
    return results

if __name__ == '__main__':
    results = get_weather_sequential()
    for i, result in enumerate(results):
        print(f"Coordinates {result.Latitude()}°N {result.Longitude()}°E")
        current = result.Current()
        current_temperature_2m = current.Variables(0).Value()
        print(f"Current temperature {current_temperature_2m:.1f}°C\n")

