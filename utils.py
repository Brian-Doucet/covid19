from datetime import datetime, timedelta
import pandas as pd

DATETIME_FORMAT = "%m-%d-%Y"


def file_to_list(file: str, column: str) -> list:
    file_to_df = pd.read_csv(file, usecols=[column])
    list_of_values = file_to_df[column].tolist()

    if not list_of_values:  # no data in file
        raise Exception("File is empty")

    return list_of_values


def state_parameter_validator(state_name: str) -> bool:
    valid_states = file_to_list("tests/state_province.csv", "state")
    is_valid_state = state_name in valid_states

    if not is_valid_state:
        raise Exception(
            "{} is not valid. Use one of the following values:{}".format(
                state_name, valid_states
            )
        )
    else:
        return


def country_region_parameter_validator(country_region: str) -> bool:
    valid_country_region = file_to_list("tests/country_region.csv", "country_region")
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
        str -- A date in the form of mm-dd-yyyy (e.g. 01-01-2020)
    """

    return date_to_format.strftime(DATETIME_FORMAT)


def is_valid_end_date(end_date: datetime) -> bool:
    """Check that date is prior to (or inclusive of) yesterday

    Arguments:
        end_date {datetime} -- The date to check

    Returns:
        bool -- True if date entered is not greater than yesterday
    """
    yesterday = datetime.today() - timedelta(days=1)
    end_date_formatted = datetime.strptime(end_date, DATETIME_FORMAT)

    return end_date_formatted <= yesterday
