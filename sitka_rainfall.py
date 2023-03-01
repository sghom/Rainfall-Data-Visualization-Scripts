import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'C:/Users/lazd/backup/career/python/data_visualization/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_rows = next(reader)

    dates, rains = [], []
    for row in reader:
        date = datetime.strptime(row[header_rows.index('DATE')],'%Y-%m-%d')
        rain = float(row[header_rows.index('PRCP')])
        dates.append(date)
        rains.append(rain)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, linewidth = 1, c='green')
    ax.set_title('Amount of Rainfall - 2018\nSitka, Alaska', fontsize = 20)
    ax.set_xlabel('',fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Percipitation (cm)', fontsize=16)
    ax.tick_params(axis='both',which='major',labelsize=16)

    plt.show()