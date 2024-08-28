import datetime

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def get_date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)
