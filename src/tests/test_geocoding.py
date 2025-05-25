import pytest
import requests
import requests_mock

from services import geocoding


def test_get_city_coordinates_success():
    city_name = "Stockholm"
    mock_data = [{"lat": "59.3293", "lon": "18.0686"}]
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, json=mock_data)
        coords = geocoding.get_city_coordinates(city_name)
        assert coords["lat"] == pytest.approx(59.3293)
        assert coords["lon"] == pytest.approx(18.0686)


def test_get_city_coordinates_not_found():
    city_name = "NoSuchCity"
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, json=[])
        coords = geocoding.get_city_coordinates(city_name)
        assert coords is None


def test_search_city_hints_returns_cities():
    partial_city = "Stock"
    mock_data = [
        {
            "display_name": "Stockholm, Sweden",
            "lat": "59.3293",
            "lon": "18.0686",
            "type": "city",
        },
        {
            "display_name": "Kalmar, Sweden",
            "lat": "56.6616",
            "lon": "16.3616",
            "type": "city",
        },
    ]
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, json=mock_data)
        suggestions = geocoding.search_city_hints(partial_city)
        assert len(suggestions) == 2
        assert suggestions[0]["name"] == "Stockholm, Sweden"
        assert suggestions[1]["name"] == "Kalmar, Sweden"
