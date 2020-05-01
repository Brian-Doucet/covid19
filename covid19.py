from datetime import datetime

import requests
import pandas as pd

from utils import get_valid_end_date, get_formatted_datetime


def get_case_data(start, end=None, country_or_region=None):

    end_range = end or datetime.today()

    if get_valid_end_date(end_range):
        list_of_dates = [get_formatted_datetime(d) for d in pd.date_range(
            start=start, end=end_range).to_pydatetime()]
    else:
        print(f'{end_range} is not a valid date!\n')
        print('Please enter a date that less than or equal to yesterday')

    if len(list_of_dates) == 0:
        print('No dates to search. Enter valid dates')
    else:
        all_data = pd.DataFrame()
        for d in list_of_dates:
            base_url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{d}.csv'
            data = pd.read_csv(
                base_url, header=0, parse_dates=['Last_Update'])
            all_data = pd.concat(objs=[all_data, data])

        if not country_or_region:
            return all_data
        else:
            return all_data[all_data['Country_Region'] == country_or_region]


test = get_case_data('04-20-2020', '04-20-2020')
print(test)
# print(test.Last_Update.unique())
# print(test.head())
#print(test.groupby(['Province_State', 'Admin2'])['Confirmed'].sum())
# print(test.info())
