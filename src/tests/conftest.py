import pytest
from services import geocoding, weather


@pytest.fixture(autouse=True)
def clear_all_caches():
    geocoding.get_city_coordinates.cache_clear()
    weather.get_weather.cache_clear()
    yield
