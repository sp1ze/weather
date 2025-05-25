import requests
from cachetools import TTLCache, cached

weather_cache = TTLCache(maxsize=1000, ttl=60 * 10)


@cached(weather_cache)
def get_weather(lat, lon):
    print(f"Fetching weather for coordinates: lat={lat}, lon={lon}")
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    response = requests.get(url, headers={"User-Agent": "weather-app"})
    if response.status_code == 200:
        data = response.json()
        if "properties" in data and "timeseries" in data["properties"]:
            now = data["properties"]["timeseries"][0]
            summary = {
                "time": now["time"],
                "temperature": now["data"]["instant"]["details"].get("air_temperature"),
                "wind_speed": now["data"]["instant"]["details"].get("wind_speed"),
                "description": now["data"]
                .get("next_1_hours", {})
                .get("summary", {})
                .get("symbol_code"),
            }
            return summary
    return None
