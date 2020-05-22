import pandas as pd
import pytest
import datatest as dt

import covid19.cases as cases

# Set of tests to confirm specific attributes within the raw data being returned
def test_get_case_data_column_count():
    # call function
    actual = cases.get_case_data(start="04-29-2020", end="04-30-2020")
    actual_col_count = actual.shape[1]

    # set expectations
    expected_col_count = 12

    assert actual_col_count == expected_col_count


# Test for column names and column order
def test_get_case_data_column_names_and_order():
    # call function
    actual = cases.get_case_data(start="05-01-2020", end="05-02-2020")
    actual_col_names_list = list(actual.columns)

    # set expectations
    expected_col_names = [
        "FIPS",
        "Admin2",
        "Province_State",
        "Country_Region",
        "Last_Update",
        "Lat",
        "Long_",
        "Confirmed",
        "Deaths",
        "Recovered",
        "Active",
        "Combined_Key",
    ]
    # assertion
    dt.validate(actual.columns, expected_col_names)


# Set of tests for DataFrame filtering on Country/Region and Province/State

# Set up test data
@pytest.fixture(scope="module")
def test_data():
    return pd.read_csv("tests/covid19_all_cases_04072020.csv", sep=",")


def test_filter_cases_by_country_region(test_data):
    # call function
    actual = cases.filter_cases_by_country_region(test_data, "US")
    actual_country_region_value = actual["Country_Region"].unique()

    # set expectations
    expected_value = "US"

    # assertion
    actual_country_region_value[0] == expected_value


def test_filter_cases_by_province_state(test_data):
    # call function
    actual = cases.filter_cases_by_province_state(test_data, "Texas")
    actual_country_region_value = actual["Country_Region"].unique()

    # set expectations
    expected_value = "Texas"

    # assertion
    actual_country_region_value[0] == expected_value


# Tests to check for correct datatypes
def test_get_case_data_by_country():
    actual = cases.get_case_data_by_country(
        start="05-01-2020", end="05-02-2020", country_or_region="US"
    )
    actual_dtypes = actual.dtypes.astype("str").to_dict()
    # set expectations
    expected_dtypes = {
        "FIPS": "float64",
        "Admin2": "object",
        "Province_State": "object",
        "Country_Region": "object",
        "Last_Update": "datetime64[ns]",
        "Lat": "float64",
        "Long_": "float64",
        "Confirmed": "int64",
        "Deaths": "int64",
        "Recovered": "int64",
        "Active": "int64",
        "Combined_Key": "object",
    }
    assert actual_dtypes == expected_dtypes
