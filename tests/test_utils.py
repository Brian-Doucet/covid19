
from datetime import datetime, timedelta
import pytest
import re
import utils
from freezegun import freeze_time

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
