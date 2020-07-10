#!/usr/bin/env python3

"""Script to extract and transform weather data using the DarkSky API"""

from typing import Optional, Dict

import pandas as pd
import requests

from covid19.utils import get_iso_date, get_multi_key_responses


def get_weather_data(api_token: str, lat: float, lon: float, date: str) -> Dict:
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
    time = get_iso_date(date)

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
        data_response = daily_block[0]
        data_fields = ['lat', 'lon', 'tz', 'time',
                       'dew_point', 'humidity', 'pressure', 'ozone',
                       'uv_index', 'temp_high', 'temp_low', 'temp_max', 'temp_min']

        results = [lat, lon, tz].extend(
            get_multi_key_responses(data_fields, data_response))
        list_of_values = [results]

        all_data = pd.DataFrame(data=list_of_values,
                                columns=data_fields)

        return all_data

    else:
        print("No data returned for daily block")
        return None
