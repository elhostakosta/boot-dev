def sort_dates(dates):
    return sorted(dates, key=sort_on)

def sort_on(date):
    new_date_format = date.split("-")
    return (new_date_format[2], new_date_format[0], new_date_format[1])
