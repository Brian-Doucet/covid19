#!/usr/bin/env python3

"""Script to extract and transform weather data using the DarkSky API"""
from typing import Optional

import pandas as pd
import requests

from covid19 import utils
from covid19.config import API_KEY


def get_weather_data(api_token: str, lat: float, lon: float, date: str) -> dict:
    """Returns historical weather conditions using the DarkSky API

    Args:
        api_token (str): DarkSky API key
        lat (float): The latitude of a location
        lon (float): The longitude of a location
        date (str): Date of weather request

    Returns:
        dict: API response in JSON data format
    """
    # API requires date in ISO 8601 format
    time = utils.get_iso_date(date)

    url = f"https://api.darksky.net/forecast/{api_token}/{lat},{lon},{time}?exclude=currently,hourly,flags"
    response = requests.get(url)
    json_data = response.json()

    return json_data


def extract_weather_data(weather_json: dict) -> Optional[pd.DataFrame]:
    """Extracts data from the API response

    Args:
        weather_json (dict): [description]

    Returns:
        Optional[pd.DataFrame]: [description]
    """
    lat = weather_json.get('latitude', None)
    lon = weather_json.get('longitude', None)
    tz = weather_json.get('timezone', None)

    # Data block containing weather conditions by day
    daily_block = weather_json['daily'].get('data', [])

    if len(daily_block) > 0:
        time = daily_block[0].get('time')
        if not time:
            print("No value for time")
        dew_point = daily_block[0].get('dewPoint')
        if not dew_point:
            print("No value for dew point")
        humidity = daily_block[0].get('humidity')
        if not humidity:
            print("No value for humidity")
        pressure = daily_block[0].get('pressure')
        if not pressure:
            print("No value for pressure")
        ozone = daily_block[0].get('ozone')
        if not ozone:
            print("No value for ozone")
        uv_index = daily_block[0].get('uvIndex')
        if not uv_index:
            print("No value for uv index")
        temp_high = daily_block[0].get('temperatureHigh')
        if not temp_high:
            print("No value for temperature high")
        temp_low = daily_block[0].get('temperatureLow')
        if not temp_low:
            print("No value for temperature low")
        temp_max = daily_block[0].get('temperatureMax')
        if not temp_max:
            print("No value for temperature max")
        temp_min = daily_block[0].get('temperatureMin')
        if not temp_min:
            print("No value for temperature min")

    else:
        print("No data returned for daily block")

        return

    list_of_values = [[
        lat, lon, tz, time,
        dew_point, humidity, pressure, ozone,
        uv_index, temp_high, temp_low, temp_max, temp_min
    ]]
    col_names = [
        'latitude', 'longitude', 'timezone', 'time',
        'dew_point', 'humidity', 'pressure', 'ozone',
        'uv_index', 'temperature_high', 'temperature_low',
        'temperature_max', 'temperature_min'
    ]

    all_data = pd.DataFrame(data=list_of_values,
                            columns=col_names)

    return all_data


list_of_coordinates = [(42.768089, -78.621017), (42.36008, -71.058884)]

daily_weather = pd.DataFrame()

for coords in list_of_coordinates:
    api_response = get_weather_data(
        api_token=API_KEY,
        lat=coords[0],
        lon=coords[1],
        date='05-28-2020'
    )
    raw_data = extract_weather_data(api_response)
    daily_weather = pd.concat(objs=[daily_weather, raw_data])

return daily_weather