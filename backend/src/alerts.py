from __future__ import annotations


def evaluate_alerts(hourly: list[dict], daily: list[dict]) -> list[dict]:
    alerts: list[dict] = []
    next_12 = hourly[:12]
    next_24 = hourly[:24]

    if any((row.get("precip_prob") or 0) >= 60 for row in next_12):
        alerts.append({
            "code": "RAIN_SOON",
            "label": "Rain likely in the next 12 hours",
            "severity": "warning",
            "recommendation": "Carry an umbrella and avoid outdoor plans if possible.",
        })

    if len(daily) > 1 and (daily[1].get("tmax_c") or 0) >= 40:
        alerts.append({
            "code": "HEAT_WAVE",
            "label": "High temperature risk tomorrow",
            "severity": "critical",
            "recommendation": "Stay hydrated and avoid afternoon outdoor activity.",
        })

    if any((row.get("wind_gust_ms") or 0) >= 12 for row in next_24):
        alerts.append({
            "code": "WIND_HIGH",
            "label": "Strong wind gusts possible within 24 hours",
            "severity": "warning",
            "recommendation": "Secure loose outdoor items and drive carefully.",
        })

    if daily and (daily[0].get("uv_max") or 0) >= 8:
        alerts.append({
            "code": "UV_HIGH",
            "label": "High UV index today",
            "severity": "info",
            "recommendation": "Use sunscreen and avoid direct sun exposure at noon.",
        })

    if not alerts:
        alerts.append({
            "code": "NORMAL",
            "label": "No major weather risk detected",
            "severity": "safe",
            "recommendation": "Weather looks manageable for normal activity.",
        })
    return alerts
