
from datetime import datetime, timedelta
import pytest
import re
import utils

# Test to confirm formatted date is a string


def test_get_formatted_datetime_is_string():
    sample_datetime = datetime.today()
    formatted_date = utils.get_formatted_datetime(sample_datetime)
    assert type(formatted_date) == str

# Test to confirm formatted date is in proper format (mm-dd-yyyy)


def test_get_formatted_datetime_proper_format():
    pattern = re.compile(r'(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-([12]\d{3})')
    sample_datetime = datetime.today()
    formatted_date = utils.get_formatted_datetime(sample_datetime)
    assert bool(pattern.match(formatted_date)) == True


def test_get_valid_end_pass():
    valid_date = '05-01-2020'
    today = datetime.today().strftime('%m-%d-%Y')

    assert bool(utils.get_valid_end_date(valid_date)) == True


def test_get_valid_end_date_fail():
    today = datetime.today().strftime('%m-%d-%Y')

    assert bool(utils.get_valid_end_date(today)) == False
