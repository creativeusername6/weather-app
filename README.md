# Weather Web App

A simple weather forecast web application built with **Python (FastAPI)** on the backend and **HTML/CSS/JavaScript** on the frontend.

It fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/).

---

## Features

- Search by city (with optional country code)
- Displays current weather and 5-day forecast
- Toggle between Celsius and Fahrenheit
- Light and Dark mode switch
- Weather icons and forecasts displayed in styled cards

---

## How to Use

### 1. Get an API Key

Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get a free API key.

### 2. Create `.env` file

Inside the `backend/` directory, create a `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 3. Set up and run the backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- API available at: http://127.0.0.1:8000/weather?city=London
- Docs: http://127.0.0.1:8000/docs

### 4. Open the frontend

You can open frontend/index.html directly in a browser, or use a local server to avoid CORS issues.

---

## Disclaimer

This is a personal/learning project.
Weather data is provided by [OpenWeatherMap](https://openweathermap.org/).

Usage must comply with:
- [Terms and Conditions of Use](https://openweathermap.org/themes/openweathermap/assets/docs/OpenWeather_T%26C_of_sale.pdf)
- [Privacy Policy](https://openweather.co.uk/privacy-policy)

**Note:** This project does not include an API key. Users must obtain their own key and configure it in a local `.env` file.