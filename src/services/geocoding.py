import requests
from functools import lru_cache

API_URL = "https://nominatim.openstreetmap.org/search"


@lru_cache(maxsize=128)
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
            if item.get("type") in ["city", "town", "village"]:
                suggestions.append(
                    {
                        "name": item["display_name"],
                        "lat": float(item["lat"]),
                        "lon": float(item["lon"]),
                    }
                )
    return suggestions
