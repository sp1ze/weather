from flask import Blueprint, request, jsonify
from services.geocoding import get_city_coordinates, search_city_hints
from services.weather import get_weather

api_bp = Blueprint("api", __name__)


@api_bp.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing city parameter"}), 400

    coords = get_city_coordinates(city)
    if not coords:
        return jsonify({"error": "City not found"}), 404

    weather = get_weather(coords["lat"], coords["lon"])
    if not weather:
        return jsonify({"error": "Weather not found"}), 500

    return jsonify({"city": city, "coordinates": coords, "weather": weather})


@api_bp.route("/city_suggestions", methods=["GET"])
def city_suggestions():
    query = request.args.get("q")
    if not query:
        return jsonify([])
    suggestions = search_city_hints(query)
    return jsonify(suggestions)
