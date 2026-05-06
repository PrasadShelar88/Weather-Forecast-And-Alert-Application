# Weather Forecast & Alert Application - Backend

FastAPI backend for a Weather Forecast & Alert Application. It uses a seeded SQLite database so the project works immediately without an API key. The backend exposes weather forecasts, alert logic, and report generation.

## Features

- FastAPI REST API
- SQLite database auto-created on startup
- Sample weather data for Indian cities
- Weather alerts for rain, heat, wind, and UV index
- CSV report export
- No API key required for demo mode

## Folder Structure

```text
backend/
├── api/
│   └── app.py
├── src/
│   ├── alerts.py
│   ├── database.py
│   ├── live_weather.py
│   ├── reports.py
│   └── sample_data.py
├── db/
├── reports/
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Run Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Important Endpoints

- `GET /locations`
- `GET /forecast/hourly?location_id=1&hours=24`
- `GET /forecast/daily?location_id=1&days=7`
- `GET /alerts?location_id=1`
- `GET /summary/1`
- `POST /reports/1`

## Notes

This project is for educational use. The sample forecast is generated for demonstration. You can extend `src/live_weather.py` to fetch live data from Open-Meteo.
