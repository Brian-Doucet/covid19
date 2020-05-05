from datetime import datetime
import pandas as pd

from utils import is_valid_end_date, get_formatted_datetime


def get_case_data(start, end=None):
    """Get global COVID-19 case reports from the Data Repository by the Center 
    for Systems Science and Engineering at Johns Hopkins University.

    Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

    Arguments:
        start {str} -- Date to begin searching for cases

    Keyword Arguments:
        end {str} -- Date to end search on, inclusive (default: {None})
    Returns:
        pd.DataFrame -- A pandas DataFrame

        Data values include:
        =============   ========================================================
        FIPS            US only. Uniquely identifies counties within the USA
        Admin2          County name. US only.
        Province_State  Province, state or dependency name.
        Country_Region  Country, region, or sovereignty name. Official designations 
                        used by the U.S. Department of State.
        Last_Update     Date the most recent file was pushed to the project repo
                        (24 hour format, UTC).
        Lat and Long    Geographic centroids, not based on a specific address.
        Confirmed       Confirmed cases (includes presumptive positive and 
                        probable cases).
        Deaths          Number of deaths. US deaths include confirmed and probable.
        Recovered       Number of recovered cases. Recovered cases outside of China 
                        are based on estimates from local media, state and local
                        reporting (when available).
        Active          Derived; total confirmed - total recovered - total deaths
        Combined        Derived; combination of [Province_State],[Country_Region].
    """

    end_range = end or datetime.today()

    if is_valid_end_date(end_range):
        list_of_dates = [
            get_formatted_datetime(d)
            for d in pd.date_range(start=start, end=end_range).to_pydatetime()
        ]
    else:
        print(f"{end_range} is not a valid date!\n")
        print("Please enter a date that is less than or equal to yesterday ")

    if not list_of_dates:
        print("No dates to search. Enter valid dates")
    else:
        all_data = pd.DataFrame()
        for d in list_of_dates:
            base_url = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{d}.csv"
            data = pd.read_csv(base_url, header=0, parse_dates=["Last_Update"])
            all_data = pd.concat(objs=[all_data, data])

        return all_data


def filter_cases_by_country_region(df, country_or_region):
    """Filter cases by country specified

    Arguments:
        df {pd.DataFrame} -- A pandas DataFrame
        country {str} -- Name of country or region to filter results

    Returns:
        pd.DataFrame -- A filtered DataFrame
    """

    return df[df.Country_Region == country_or_region]


def filter_cases_by_province_state(df, province_or_state):
    """Filter cases by province or state specified

    Arguments:
        df {pd.DataFrame} -- A pandas DataFrame
        country {str} -- Name of province or state to filter results

    Returns:
        pd.DataFrame -- A filtered DataFrame
    """

    return df[df.Province_State == province_or_state]


def get_case_data_by_country(start, end, country_or_region):
    all_cases = get_case_data(start, end)
    filtered_cases = filter_cases_by_country_region(all_cases, country_or_region)

    return filtered_cases


def get_case_data_by_province_state(start, end, province_or_state):
    all_cases = get_case_data(start, end)
    filtered_cases = filter_cases_by_province_state(all_cases, province_or_state)

    return filtered_cases


test_country = get_case_data_by_country("04-20-2020", "04-21-2020", "US")
test_province_state = get_case_data_by_province_state(
    "04-20-2020", "04-21-2020", "New Hampshire"
)
print(test_country.head())
print(test_province_state.head())
