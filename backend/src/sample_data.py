from __future__ import annotations

import math
import random
from datetime import datetime, timedelta

from .database import get_connection, init_db


def seed_sample_weather() -> None:
    """Create deterministic sample forecast data so the project works without internet."""
    init_db()
    con = get_connection()
    locations = con.execute("SELECT id, name FROM locations ORDER BY id").fetchall()
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    today = now.date()

    for loc in locations:
        location_id = loc["id"]
        random.seed(location_id)
        base_temp = 27 + location_id
        for i in range(72):
            ts = now + timedelta(hours=i)
            hour = ts.hour
            temp = base_temp + 5 * math.sin((hour - 6) / 24 * 2 * math.pi) + random.uniform(-1.0, 1.0)
            humidity = max(35, min(95, 65 + random.uniform(-12, 18)))
            rain_boost = 45 if location_id in (1, 2, 4) and 6 <= i <= 18 else 10
            precip_prob = max(0, min(100, rain_boost + random.randint(-10, 25)))
            precip_mm = round(max(0, (precip_prob - 55) / 30), 2)
            wind_ms = round(3 + random.random() * 4, 2)
            gust_ms = round(wind_ms + random.random() * 4, 2)
            uv = max(0, round(9 * math.sin(max(0, (hour - 6)) / 12 * math.pi), 1)) if 6 <= hour <= 18 else 0
            con.execute(
                """
                INSERT OR REPLACE INTO weather_hourly
                (location_id, ts, temp_c, feels_c, humidity, wind_ms, wind_gust_ms,
                 precip_mm, precip_prob, cloud_pct, uv, pressure_hpa, visibility_km, weather_code)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    location_id,
                    ts.isoformat(timespec="minutes"),
                    round(temp, 1),
                    round(temp + 1.2, 1),
                    round(humidity, 1),
                    wind_ms,
                    gust_ms,
                    precip_mm,
                    precip_prob,
                    random.randint(20, 95),
                    uv,
                    round(1008 + random.random() * 8, 1),
                    round(5 + random.random() * 5, 1),
                    61 if precip_prob >= 60 else 2,
                ),
            )

        for d in range(7):
            date = today + timedelta(days=d)
            tmax = base_temp + 5 + random.uniform(-1, 4)
            if location_id == 3 and d in (1, 2):
                tmax = 41.5
            tmin = base_temp - 3 + random.uniform(-2, 1)
            rain_prob = 70 if location_id in (1, 2, 4) and d in (0, 1) else random.randint(15, 55)
            con.execute(
                """
                INSERT OR REPLACE INTO weather_daily
                (location_id, date, tmax_c, tmin_c, rain_mm, rain_prob, wind_max_ms, uv_max, sunrise, sunset)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    location_id,
                    date.isoformat(),
                    round(tmax, 1),
                    round(tmin, 1),
                    round(max(0, (rain_prob - 50) / 10), 1),
                    rain_prob,
                    round(8 + random.random() * 8, 1),
                    round(6 + random.random() * 4, 1),
                    f"{date.isoformat()}T06:15",
                    f"{date.isoformat()}T18:45",
                ),
            )
    con.commit()
    con.close()


if __name__ == "__main__":
    seed_sample_weather()
    print("Sample weather data created successfully.")
