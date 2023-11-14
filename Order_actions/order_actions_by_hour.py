import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.dates as mdates

select_order_actions_by_hour = """select date_trunc('hour', start_date), count(*)
from tm_order_actions
where start_date between '2023-11-12 23:59:59' AND '2023-11-13 23:59:59'
group by date_trunc('hour', start_date)
order by date_trunc('hour', start_date) desc
"""

order_actions_by_hour = pd.read_sql(select_order_actions_by_hour, conn)

fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
timeFmt = mdates.DateFormatter('%H')
hours = mdates.HourLocator()
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(hours)

x = order_actions_by_hour['date_trunc']
y = order_actions_by_hour['count']

plt.scatter(x, y)
plt.grid(True)
plt.show()