import datetime


def date_generate(start_date, end_date):
    start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    next_dt = start_dt

    date_list = []
    while next_dt <= end_dt:
        next_dt_str = next_dt.date()
        date_list.append(next_dt_str)
        next_dt = next_dt + datetime.timedelta(days=1)

    return date_list