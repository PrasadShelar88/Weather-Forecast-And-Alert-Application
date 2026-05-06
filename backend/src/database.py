from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]
DB_DIR = BASE_DIR / "db"
DB_PATH = DB_DIR / "weather.db"

DEFAULT_LOCATIONS = [
    (1, "Pune", 18.5204, 73.8567, "Asia/Kolkata"),
    (2, "Mumbai", 19.0760, 72.8777, "Asia/Kolkata"),
    (3, "Delhi", 28.6139, 77.2090, "Asia/Kolkata"),
    (4, "Chhatrapati Sambhajinagar", 19.8762, 75.3433, "Asia/Kolkata"),
    (5, "Bengaluru", 12.9716, 77.5946, "Asia/Kolkata"),
    (6, "Hyderabad", 17.3850, 78.4867, "Asia/Kolkata"),
]


def get_connection() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db() -> None:
    con = get_connection()
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS locations(
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          lat REAL NOT NULL,
          lon REAL NOT NULL,
          tz TEXT DEFAULT 'Asia/Kolkata',
          UNIQUE(lat, lon)
        );

        CREATE TABLE IF NOT EXISTS weather_hourly(
          location_id INTEGER,
          ts TEXT,
          temp_c REAL,
          feels_c REAL,
          humidity REAL,
          wind_ms REAL,
          wind_gust_ms REAL,
          precip_mm REAL,
          precip_prob REAL,
          cloud_pct REAL,
          uv REAL,
          pressure_hpa REAL,
          visibility_km REAL,
          weather_code INTEGER,
          PRIMARY KEY(location_id, ts)
        );

        CREATE TABLE IF NOT EXISTS weather_daily(
          location_id INTEGER,
          date TEXT,
          tmax_c REAL,
          tmin_c REAL,
          rain_mm REAL,
          rain_prob REAL,
          wind_max_ms REAL,
          uv_max REAL,
          sunrise TEXT,
          sunset TEXT,
          PRIMARY KEY(location_id, date)
        );

        CREATE TABLE IF NOT EXISTS alert_log(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          location_id INTEGER,
          code TEXT,
          label TEXT,
          severity TEXT,
          created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
    )
    cur.executemany(
        "INSERT OR IGNORE INTO locations(id, name, lat, lon, tz) VALUES (?, ?, ?, ?, ?)",
        DEFAULT_LOCATIONS,
    )
    con.commit()
    con.close()


def query(sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    con = get_connection()
    rows = con.execute(sql, params).fetchall()
    con.close()
    return [dict(row) for row in rows]
