from datetime import datetime, timedelta

def date_in_future(integer):
    if isinstance(integer, int):
        future_date = datetime.now() + timedelta(days=integer)
        return future_date.strftime("%d-%m-%Y %H:%M:%S")
    else:
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

print(date_in_future([]))
print(date_in_future(2))