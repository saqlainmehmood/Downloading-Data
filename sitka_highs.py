from pathlib import Path
import csv

import matplotlib.pyplot as plt
from datetime import datetime

# first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')

path = Path('weather_data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# extract the high tempratures
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[5])
    dates.append(current_date)
    highs.append(high)

# print(highs)


# plot the high tempratures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# format plot
ax.set_title("Daily High Temprature")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
