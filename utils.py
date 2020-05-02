from datetime import datetime, timedelta

# Function to check valid end range


def get_formatted_datetime(date_to_format: datetime) -> str:
    datetime_format = '%m-%d-%Y'

    return date_to_format.strftime(datetime_format)


def get_valid_end_date(end_date: datetime) -> bool:
    yesterday = datetime.today() - timedelta(days=1)
    end_date_formatted = datetime.strptime(end_date, '%m-%d-%Y')

    return end_date_formatted <= yesterday
