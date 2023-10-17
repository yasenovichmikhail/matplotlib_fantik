from sqlite3 import OperationalError
import psycopg2 as db  
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

select_video_download = """select date_trunc('day', download_date), count(*)
from tm_video_downloads
where date_trunc('day', download_date) between '2023-03-31 23:59:59' and '2023-04-30 23:59:59'
group by date_trunc('day', download_date)
order by date_trunc('day', download_date) desc"""

video_april = pd.read_sql(select_video_download, conn)
timeFmt = mdates.DateFormatter('%d')

# months = mdates.MonthLocator()
# days = mdates.DayLocator()
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.yaxis.set_major_locator(ticker.AutoLocator())
plt.xlabel("April", fontsize=14, fontweight="bold")
plt.ylabel("Amount", fontsize=14, fontweight="bold")
plt.title("Video Downloads by day", fontsize=14, fontweight="bold")
plt.locator_params (axis='x', nbins= 30 )
plt.locator_params (axis='y', nbins= 20 )
plt.grid(True)
plt.plot(video_april['date_trunc'], video_april['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=3, ms=6)
d = video_april.describe()
plt.show()