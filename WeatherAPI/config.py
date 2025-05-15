URL = "https://api.open-meteo.com/v1/forecast"
LATITUDE = [55.7522, 32.8091, 52.5244, 40.7143]
LONGITUDE = [37.6156, 34.9971, 13.4105, -74.006]
PARAMS = {
	"hourly": ["temperature_2m", "dew_point_2m", "rain", "relative_humidity_2m", "precipitation_probability", "uv_index"],
	"models": "best_match",
	"current": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain"],
	"timezone": "GMT",
	"forecast_days": 3
}
COUNT = LONGITUDE.__len__()