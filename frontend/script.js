const form = document.getElementById("weather-form");
const input = document.getElementById("city-input");
const countryInput = document.getElementById("country-input");
const output = document.getElementById("weather-output");

let currentUnit = "C";
let lastData = null;

const unitButton = document.getElementById("toggle-unit");

const darkButton = document.getElementById("toggle-dark");

unitButton.addEventListener("click", () => {
  currentUnit = currentUnit === "C" ? "F" : "C";
  unitButton.textContent = `Switch to °${currentUnit === "C" ? "F" : "C"}`;
  if (lastData) {
    renderWeather(lastData);
  }
});

function convertTemp(tempC) {
  return currentUnit === "C" ? tempC : Math.round(tempC * 9 / 5 + 32);
}

function renderWeather(data) {
  lastData = data;
  const cards = data.forecast
  .map(
    (day) => `
    <div class="forecast-card">
      <div class="forecast-date">${day.date}</div>
      <img src="https://openweathermap.org/img/wn/${day.icon}@2x.png" alt="${day.description}" />
      <div class="forecast-temp">${convertTemp(day.temperature)}°${currentUnit}</div>
      <div class="forecast-details">
        Humidity: ${day.humidity}%<br>
        Wind: ${day.wind_speed} m/s<br>
        Pressure: ${day.pressure} hPa
      </div>
    </div>
  `
  )
  .join("");

  output.innerHTML = `
    <h2>${data.location}</h2>
    <div class="forecast-grid">${cards}</div>
  `;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const city = input.value.trim();
  const country = countryInput.value.trim().toUpperCase();

  if (!city) return;

  output.innerHTML = "Loading...";
  lastData = null;
  unitButton.classList.add("hidden");

  try {
    const query = country ? `${city},${country}` : city;

    const res = await fetch(`http://127.0.0.1:8000/weather?city=${encodeURIComponent(query)}`);
    if (!res.ok) throw new Error("City not found");

    const data = await res.json();
    if (!data.forecast || data.forecast.length === 0) {
      throw new Error("No forecast data available.");
    }

    renderWeather(data);
    unitButton.classList.remove("hidden");
  } catch (err) {
    output.innerHTML = `<p class="error">Error: ${err.message}</p>`;
  }
});

if (localStorage.getItem("darkMode") === "true") {
  document.body.classList.add("dark-mode");
  darkButton.textContent = "Light Mode";
}

darkButton.addEventListener("click", () => {
  const isDark = document.body.classList.toggle("dark-mode");
  darkButton.textContent = isDark ? "Light Mode" : "Dark Mode";
  localStorage.setItem("darkMode", isDark);
});