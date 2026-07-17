import requests


def fetch_live_weather(latitude: float, longitude: float) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation"
        "&timezone=auto"
    )
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    current = response.json()["current"]

    return {
        "temperature": float(current["temperature_2m"]),
        "humidity": float(current["relative_humidity_2m"]),
        "wind_speed": float(current["wind_speed_10m"]),
        "rainfall": float(current["precipitation"]),
    }
