from datetime import datetime, timedelta

# Function to check valid end range


def get_formatted_datetime(date_to_format: datetime) -> str:
    """Convert a datetime object to a different string format

    Arguments:
        date_to_format {datetime} -- A datetime object

    Returns:
        str -- A date in the form of mm-dd-yyyy (e.g. 01-01-2020)
    """
    datetime_format = '%m-%d-%Y'

    return date_to_format.strftime(datetime_format)


def is_valid_end_date(end_date: datetime) -> bool:
    """Check that date is prior to (or inclusive of) yesterday

    Arguments:
        end_date {datetime} -- The date to check

    Returns:
        bool -- True if date entered is not greater than yesterday
    """
    yesterday = datetime.today() - timedelta(days=1)
    end_date_formatted = datetime.strptime(end_date, '%m-%d-%Y')

    return end_date_formatted <= yesterday
