# Assignment
# Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format 
# and returns a list of the dates sorted in ascending order.

# My solution is meh ...
# def sort_dates(dates):
    # dates_ymd = []

    # sorted_datesmdy = []

    # for date in dates:
        # ls = date.split('-')
        # desc = ls[2] + '-' + ls[0] + '-' + ls[1]
        # dates_ymd.append(desc)

    # sorted_dates = sorted(dates_ymd)

    # for sd in sorted_dates:
        # ls = sd.split('-')
        # asc = ls[1] + '-' + ls[2] + '-' + ls[0]
        # sorted_datesmdy.append(asc)

    # return sorted_datesmdy

def sort_dates(dates: list[str]) -> list[str]:
    return sorted(dates, key=format_date)


def format_date(date: str):
    month, day, year = date.split("-")
    return year + month + date