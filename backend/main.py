from src.sample_data import seed_sample_weather
from src.database import query
from src.alerts import evaluate_alerts


def main() -> None:
    seed_sample_weather()
    locations = query("SELECT * FROM locations ORDER BY name")
    print("Weather Forecast & Alert Application")
    print("Available locations:")
    for loc in locations:
        print(f"{loc['id']}. {loc['name']}")
    location_id = locations[0]["id"]
    hourly = query("SELECT * FROM weather_hourly WHERE location_id=? ORDER BY ts LIMIT 24", (location_id,))
    daily = query("SELECT * FROM weather_daily WHERE location_id=? ORDER BY date LIMIT 7", (location_id,))
    alerts = evaluate_alerts(hourly, daily)
    print("\nDemo city:", locations[0]["name"])
    print("Current temp:", hourly[0]["temp_c"], "°C")
    print("Alerts:")
    for alert in alerts:
        print("-", alert["label"], "|", alert["severity"])


if __name__ == "__main__":
    main()
