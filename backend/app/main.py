from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.alerts import evaluate_alerts
from src.database import init_db, query
from src.reports import export_daily_report
from src.sample_data import seed_sample_weather

app = FastAPI(
    title="Weather Forecast & Alert Application",
    description="FastAPI backend for weather forecast visualization and rule-based alerts.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    init_db()
    seed_sample_weather()


@app.get("/")
def root() -> dict:
    return {
        "message": "Weather Forecast & Alert API is running",
        "docs": "/docs",
        "endpoints": ["/locations", "/forecast/hourly", "/forecast/daily", "/alerts", "/summary/{location_id}"],
    }


@app.get("/locations")
def locations() -> list[dict]:
    return query("SELECT * FROM locations ORDER BY name")


@app.get("/forecast/hourly")
def hourly(location_id: int, hours: int = 24) -> list[dict]:
    rows = query(
        """
        SELECT * FROM weather_hourly
        WHERE location_id = ?
        ORDER BY ts
        LIMIT ?
        """,
        (location_id, hours),
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No hourly forecast found for this location")
    return rows


@app.get("/forecast/daily")
def daily(location_id: int, days: int = 7) -> list[dict]:
    rows = query(
        """
        SELECT * FROM weather_daily
        WHERE location_id = ?
        ORDER BY date
        LIMIT ?
        """,
        (location_id, days),
    )
    if not rows:
        raise HTTPException(status_code=404, detail="No daily forecast found for this location")
    return rows


@app.get("/alerts")
def alerts(location_id: int) -> dict:
    hourly_rows = hourly(location_id, 48)
    daily_rows = daily(location_id, 7)
    return {"location_id": location_id, "alerts": evaluate_alerts(hourly_rows, daily_rows)}


@app.get("/summary/{location_id}")
def summary(location_id: int) -> dict:
    locs = query("SELECT * FROM locations WHERE id = ?", (location_id,))
    if not locs:
        raise HTTPException(status_code=404, detail="Location not found")
    hourly_rows = hourly(location_id, 24)
    daily_rows = daily(location_id, 7)
    alert_rows = evaluate_alerts(hourly_rows, daily_rows)
    current = hourly_rows[0]
    return {
        "location": locs[0],
        "current": current,
        "daily": daily_rows,
        "hourly": hourly_rows,
        "alerts": alert_rows,
    }


@app.post("/reports/{location_id}")
def create_report(location_id: int) -> dict:
    locs = query("SELECT * FROM locations WHERE id = ?", (location_id,))
    if not locs:
        raise HTTPException(status_code=404, detail="Location not found")
    hourly_rows = hourly(location_id, 24)
    daily_rows = daily(location_id, 7)
    alert_rows = evaluate_alerts(hourly_rows, daily_rows)
    path = export_daily_report(locs[0]["name"], hourly_rows, daily_rows, alert_rows)
    return {"ok": True, "report_path": path}
