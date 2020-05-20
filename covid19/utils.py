#!/usr/bin/env python

"""Methods for validating parameters and ensuring proper formatting for dates"""


from datetime import datetime, timedelta

import pandas as pd

DATETIME_FORMAT = "%m-%d-%Y"


def file_to_list(file: str) -> list:
    """Convert a column from a file into a list of values

    Arguments:
        file {str} -- file name
        
    Raises:
        Exception: If no values in column specified then file is considered empty

    Returns:
        list -- A list with all values from the column given
    """
    list_of_values = pd.read_csv(file, squeeze=True).tolist()

    if not list_of_values:  # no data in file
        raise Exception("File is empty")

    return list_of_values


def state_parameter_validator(state_name):
    """Check to make sure the state name is valid

    Arguments:
        state_name {str} -- State name, case sensitive

    Raises:
        Exception: If the state name is invalid or does not exist

    Returns:
        None -- If state given is valid
    """
    valid_states = file_to_list("covid19/data/state_province.csv")
    is_valid_state = state_name in valid_states

    if not is_valid_state:
        raise Exception(
            "{} is not valid. Use one of the following values:{}".format(
                state_name, valid_states
            )
        )
    else:
        return


def country_region_parameter_validator(country_region):
    """Check to make sure country or region name is valid

    Arguments:
        country_region {str} -- country/region name, case sensitive

    Raises:
        Exception: If the country/region given is invalid or does not exist
    """
    valid_country_region = file_to_list("covid19/data/country_region.csv")
    is_valid_country_region = country_region in valid_country_region

    if not is_valid_country_region:
        raise Exception(
            "{} is not valid. Use one of the following values:{}".format(
                country_region, valid_country_region
            )
        )
    else:
        return


def get_formatted_datetime(date_to_format: datetime) -> str:
    """Convert a datetime object to a different string format

    Arguments:
        date_to_format {datetime} -- A datetime object

    Returns:
        str -- A date in the format of mm-dd-yyyy (e.g. 01-01-2020)
    """

    return date_to_format.strftime(DATETIME_FORMAT)


def is_valid_end_date(end_date):
    """Check that date is prior to (or inclusive of) yesterday

    Arguments:
        end_date {datetime} -- The date to check

    Returns:
        None -- True if date entered is not greater than yesterday
    """
    yesterday = datetime.today() - timedelta(days=1)
    end_date_formatted = datetime.strptime(end_date, DATETIME_FORMAT)

    return end_date_formatted <= yesterday
