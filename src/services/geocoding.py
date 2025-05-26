import requests
from cachetools import TTLCache, cached

API_URL = "https://nominatim.openstreetmap.org/search"

city_cache = TTLCache(maxsize=1000, ttl=60 * 60)


@cached(city_cache)
def get_city_coordinates(city_name):
    params = {"q": city_name, "format": "json", "limit": 1}
    response = requests.get(
        API_URL, params=params, headers={"User-Agent": "weather-app"}
    )
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return {"lat": float(data["lat"]), "lon": float(data["lon"])}
    return None


def search_city_hints(partial_city):
    params = {
        "q": partial_city,
        "format": "json",
        "addressdetails": 1,
        "limit": 5,
        "extratags": 1,
        "dedupe": 1,
    }
    response = requests.get(
        API_URL, params=params, headers={"User-Agent": "weather-app"}
    )
    suggestions = []
    if response.status_code == 200:
        for item in response.json():
            suggestions.append(
                {
                    "name": item["display_name"],
                    "lat": float(item["lat"]),
                    "lon": float(item["lon"]),
                }
            )
    return suggestions
