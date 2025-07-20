from typing import Dict
from collections import defaultdict
from datetime import datetime, timedelta


def format_forcast(data: Dict) -> Dict:
    city = data.get("city", {}).get("name")
    country = data.get("city", {}).get("country")

    forecasts = data.get("list", [])
    grouped_by_day = defaultdict(list)

    for entry in forecasts:
        date_string, time_string = entry["dt_txt"].split()
        grouped_by_day[date_string].append((time_string, entry))

    formatted = []
    preferred_times = ["12:00:00", "15:00:00", "09:00:00", "18:00:00"]

    today = datetime.utcnow().date()
    days = [today + timedelta(days=i) for i in range(6)]

    available_dates = sorted(grouped_by_day.keys())
    for date in available_dates:
        dt = datetime.strptime(date, "%Y-%m-%d").date()
        if dt not in days and dt > today:
            days.append(dt)
        if len(days) == 6:
            break

    for day in days:
        date_string = day.strftime("%Y-%m-%d")
        entries = grouped_by_day.get(date_string)
        if not entries:
            continue

        selected = None
        for pref_time in preferred_times:
            for time_string, entry in entries:
                if time_string == pref_time:
                    selected = entry
                    break
            if selected:
                break

        if not selected:
            selected = entries[0][1]

        if day == today:
            day_label = "Today"
        elif day == today + timedelta(days=1):
            day_label = "Tomorrow"
        else:
            day_label = day.strftime("%A")

        date_label = f"{day_label}<br>({date_string})"

        formatted.append({
            "date": date_label,
            "temperature": round(selected["main"]["temp"]),
            "description": selected["weather"][0]["description"],
            "icon": selected["weather"][0]["icon"],
            "humidity": selected["main"]["humidity"],
            "pressure": selected["main"]["pressure"],
            "wind_speed": selected["wind"]["speed"]
        })

    return {
        "location": f"{city}, {country}",
        "forecast": formatted
    }
