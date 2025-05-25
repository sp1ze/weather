import requests
from functools import lru_cache


@lru_cache(maxsize=128)
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
                "description": now["data"]
                .get("next_1_hours", {})
                .get("summary", {})
                .get("symbol_code"),
            }
            return summary
    return None
