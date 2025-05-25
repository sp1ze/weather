## Demo
Try the cloud run demo [here](https://weather-app-726246433940.europe-west1.run.app/)


## How the Application Works

**Flow:**
1. User types a city name on the homepage.
2. Frontend JavaScript sends autocomplete requests to the backend, which queries OpenStreetMap’s API for matching cities.
3. Once a city is chosen, the backend requests its coordinates from OpenStreetMap.
4. The backend then fetches live weather data for those coordinates from the yr.no weather API.
5. The weather results are returned and rendered on the page.

**API Structure:**
- `/api/city_suggestions` — Returns city autocomplete results.
- `/api/weather` — Returns weather info for a requested city.

## Developer Quickstart

### Requirements

- Python 3.8+
- pip

### Installation & Running

```bash
# Clone this repo or copy files locally
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install Python dependencies
pip install -r requirements.txt

# Run the app
python app.py

### Run tests
```bash
python -m pytest
```