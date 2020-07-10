"""Tests for DarkSky API response and parsing response elements."""

from datetime import datetime

from freezegun import freeze_time
import pytest

from covid19.weather import get_weather_data
from covid19.config import API_KEY
from covid19.utils import get_formatted_datetime


# Set up testing constants
COORDINATES = [42.768089, -78.621017]


@freeze_time('05-25-2020')
def test_response_has_daily_key():
    """Test that the request does not fail"""

    sample_date = get_formatted_datetime(datetime.today())
    response = get_weather_data(
        api_token=API_KEY,
        lat=COORDINATES[0],
        lon=COORDINATES[1],
        date=sample_date)

    assert response['daily'] is not None


@freeze_time('05-25-2020')
def test_invalid_api_key():
    """Test that the request does not fail"""

    sample_date = get_formatted_datetime(datetime.today())
    response = get_weather_data(
        api_token='1234wetdgfgr45678',
        lat=COORDINATES[0],
        lon=COORDINATES[1],
        date=sample_date)

    assert response.get('code') == 403
