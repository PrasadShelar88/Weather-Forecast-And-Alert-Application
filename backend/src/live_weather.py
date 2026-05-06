from __future__ import annotations

import httpx

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_open_meteo(lat: float, lon: float, timezone: str = "Asia/Kolkata") -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": timezone,
        "current_weather": "true",
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,wind_speed_10m,wind_gusts_10m,cloud_cover,uv_index,pressure_msl,visibility",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,wind_speed_10m_max,uv_index_max,sunrise,sunset",
    }
    with httpx.Client(timeout=20) as client:
        response = client.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()
        return response.json()
