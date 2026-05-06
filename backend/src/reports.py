from __future__ import annotations

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = BASE_DIR / "reports"


def export_daily_report(location_name: str, hourly: list[dict], daily: list[dict], alerts: list[dict]) -> str:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    safe = location_name.replace(" ", "_")
    path = REPORTS_DIR / f"{safe}_weather_report.csv"
    rows = []
    for row in daily:
        rows.append({
            "city": location_name,
            "date": row.get("date"),
            "max_temp_c": row.get("tmax_c"),
            "min_temp_c": row.get("tmin_c"),
            "rain_mm": row.get("rain_mm"),
            "rain_probability": row.get("rain_prob"),
            "wind_max_ms": row.get("wind_max_ms"),
            "uv_max": row.get("uv_max"),
            "alerts": "; ".join(a["label"] for a in alerts),
        })
    pd.DataFrame(rows).to_csv(path, index=False)
    return str(path)
