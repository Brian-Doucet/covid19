import requests
import pandas as pd
from datetime import datetime


def get_formatted_datetime(date_to_format: datetime) -> str:
    datetime_format = '%m-%d-%Y'

    return date_to_format.strftime(datetime_format)


def get_case_data(start, end=None):

    end_range = end or datetime.today()

    list_of_dates = [d for d in pd.date_range(
        start=start, end=end_range).to_pydatetime()]

    all_data = pd.DataFrame()

    for d in list_of_dates:
        base_url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{get_formatted_datetime(d)}.csv'
        data = pd.read_csv(
            base_url, header=0, parse_dates=['Last_Update'])

    all_data = pd.concat(objs=[all_data, data])

    return all_data


test = get_case_data('04-20-2020', '04-21-2020')

print(test.head())
print(test.Country_Region.value_counts)
print(test.info())
