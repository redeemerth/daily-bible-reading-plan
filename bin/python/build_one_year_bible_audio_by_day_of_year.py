import csv
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# Get all of 2016
start_dt = date(2018, 1, 1)
end_dt = date(2018, 12, 31)
i = 1

with open('oneyearbible_urls.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Day_Number', 'Month_Day'])
    for dt in daterange(start_dt, end_dt):
        month = str(dt.strftime("%m"))
        day = str(dt.strftime("%d"))
        month_day = f"{month}{day}"
        writer.writerow([i, month_day])
        i = i+1

print("Done executing program")