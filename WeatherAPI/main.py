import asyncio

if __name__ == '__main__':
    from WeatherAPI.api.sequential import get_weather_sequential
    print(f"Starting the weather API request sequentially...")
    get_weather_sequential()

    from WeatherAPI.api.multiproc import get_weather_with_multiprocessing
    print(f"Starting the weather API request with multiprocessing...")
    get_weather_with_multiprocessing()

    from WeatherAPI.api.multithread import get_weather_with_threading
    print(f"Starting the weather API request with multithreading...")
    get_weather_with_threading()

    from WeatherAPI.api.coroutine import get_weather_with_asyncio
    print(f"Starting the weather API request with asyncio...")
    asyncio.run(get_weather_with_asyncio())