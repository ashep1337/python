#!/usr/bin/env python3
"""
terminal_weather_colored.py — 7-day Evansdale, IA weather with colors & icons
Requires: requests, colorama
"""

from datetime import datetime

import requests
from colorama import Fore, Style, init

# Init colorama
init(autoreset=True)

# Evansdale coordinates
LAT = 42.4678
LON = -92.2821

# Weather codes mapping (Open-Meteo WMO codes)
WEATHER_CODES = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫"),
    48: ("Rime fog", "🌫"),
    51: ("Light drizzle", "🌦"),
    53: ("Moderate drizzle", "🌦"),
    55: ("Dense drizzle", "🌧"),
    56: ("Freezing drizzle", "🌧"),
    57: ("Freezing drizzle heavy", "🌧"),
    61: ("Slight rain", "🌧"),
    63: ("Moderate rain", "🌧"),
    65: ("Heavy rain", "🌧"),
    66: ("Freezing rain", "🌧"),
    67: ("Freezing rain heavy", "🌧"),
    71: ("Slight snow", "🌨"),
    73: ("Moderate snow", "🌨"),
    75: ("Heavy snow", "❄️"),
    77: ("Snow grains", "🌨"),
    80: ("Slight rain showers", "🌦"),
    81: ("Moderate rain showers", "🌧"),
    82: ("Violent rain showers", "🌧"),
    85: ("Slight snow showers", "🌨"),
    86: ("Heavy snow showers", "❄️"),
    95: ("Thunderstorm", "⛈"),
    96: ("T-storm + slight hail", "⛈"),
    99: ("T-storm + heavy hail", "⛈"),
}


def fetch_forecast():
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,windspeed_10m_max,weathercode"
        f"&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch"
        f"&timezone=auto&forecast_days=7"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


def colorize(temp_max, temp_min, rain_chance, wind_speed, text):
    """Apply color based on conditions."""
    if temp_max >= 85:
        text = Fore.RED + text + Style.RESET_ALL
    elif temp_min <= 32:
        text = Fore.CYAN + text + Style.RESET_ALL
    if rain_chance >= 50:
        text = Fore.YELLOW + text + Style.RESET_ALL
    if wind_speed >= 15:
        text = Fore.MAGENTA + text + Style.RESET_ALL
    return text


def display_forecast(data):
    daily = data["daily"]
    print(f"\n{Fore.GREEN}Weather Forecast — Evansdale, IA{Style.RESET_ALL}\n")
    print(f"{'Date':<12} {'Cond':<30} {'High':>6} {'Low':>6} {'Rain%':>7} {'Wind':>7}")
    print("-" * 74)

    for i in range(len(daily["time"])):
        date_str = datetime.strptime(daily["time"][i], "%Y-%m-%d").strftime("%a %m/%d")
        code = daily["weathercode"][i]
        cond, icon = WEATHER_CODES.get(code, (f"Code {code}", ""))
        tmax = daily["temperature_2m_max"][i]
        tmin = daily["temperature_2m_min"][i]
        rain = daily["precipitation_probability_max"][i] or 0
        wind = daily["windspeed_10m_max"][i]

        cond_text = f"{icon} {cond}"
        colored_line = colorize(
            tmax,
            tmin,
            rain,
            wind,
            f"{date_str:<12} {cond_text:<30} {tmax:>6.0f} {tmin:>6.0f} {rain:>7.0f} {
                wind:>7.0f}",
        )
        print(colored_line)


def main():
    try:
        data = fetch_forecast()
        display_forecast(data)
    except Exception as e:
        print(Fore.RED + "Error fetching forecast:" + Style.RESET_ALL, e)


if __name__ == "__main__":
    main()
