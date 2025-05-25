import pytest
import requests
import requests_mock

from services import weather


def test_get_weather_success():
    lat, lon = 59.3293, 18.0686
    mock_response = {
        "properties": {
            "timeseries": [
                {
                    "time": "2024-05-24T12:00:00Z",
                    "data": {
                        "instant": {"details": {"air_temperature": 15.0}},
                        "next_1_hours": {
                            "summary": {"symbol_code": "partlycloudy_day"}
                        },
                    },
                }
            ]
        }
    }
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, json=mock_response)
        result = weather.get_weather(lat, lon)
        assert result["temperature"] == 15.0
        assert result["description"] == "partlycloudy_day"


def test_get_weather_no_data():
    lat, lon = 0, 0
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, json={})
        result = weather.get_weather(lat, lon)
        assert result is None
