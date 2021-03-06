
from datetime import datetime, timedelta

import pytest  # type: ignore

import covid19.utils as utils
from freezegun import freeze_time  # type: ignore

# Test to confirm formatted date is a string
@freeze_time('04-20-2020')
def test_get_formatted_datetime_is_string():
    sample_datetime = datetime.today()
    formatted_date = utils.get_formatted_datetime(sample_datetime)
    assert formatted_date == '04-20-2020'

# Test to confirm formatted date is in proper format (mm-dd-yyyy)
@freeze_time('01-02-2020')
def test_get_formatted_datetime_proper_format():
    sample_datetime = datetime.today()
    formatted_date = utils.get_formatted_datetime(sample_datetime)
    expected_format = '%m-%d-%Y'
    expected_datetime = datetime(year=2020, month=1, day=2)

    assert datetime.strptime(
        formatted_date, expected_format) == expected_datetime

# Tests to confirm valid end dates


def test_get_valid_end_date_pass():
    valid_date = '05-01-2020'

    assert utils.is_valid_end_date(valid_date) == True


def test_get_valid_end_date_fail():
    today = datetime.today().strftime('%m-%d-%Y')

    assert utils.is_valid_end_date(today) == False

# Set of tests for state/province


def test_state_parameter_validator_pass():
    assert utils.state_parameter_validator('Massachusetts') is None


def test_state_parameter_validator_fail():
    with pytest.raises(Exception) as info:
        utils.state_parameter_validator('The Shire')

    assert("The Shire is not valid") in str(info.value)

# Set of tests for country/region


def test_country_region_parameter_validator_pass():
    assert utils.country_region_parameter_validator('Canada') is None


def test_country_region_parameter_validator_fail():
    with pytest.raises(Exception) as info:
        utils.state_parameter_validator("Pandora")

    assert("Pandora is not valid") in str(info.value)
