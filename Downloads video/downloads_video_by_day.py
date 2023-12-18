from sqlite3 import OperationalError
import psycopg2 as db  
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

select_true_order_actions = """select date_trunc('day', server_date), count(*)
from tm_order_actions
where server_date between '2023-11-30 23:59:59' AND '2023-12-31 23:59:59'
and is_success = 'true'
and metrics_amount_before != '-1'
group by date_trunc('day', server_date)
order by date_trunc('day', server_date) desc"""

select_false_order_actions = """select date_trunc('day', server_date), count(*)
from tm_order_actions
where server_date between '2023-11-30 23:59:59' AND '2023-12-31 23:59:59'
and is_success = 'false'
group by date_trunc('day', server_date)
order by date_trunc('day', server_date) desc"""

select_unavailable_order_actions = """select date_trunc('day', server_date), count(*)
from tm_order_actions
where server_date between '2023-11-30 23:59:59' AND '2023-12-31 23:59:59'
and metrics_amount_before = '-1'
group by date_trunc('day', server_date)
order by date_trunc('day', server_date) desc;"""

select_skip_order_actions = """select date_trunc('day', server_date), count(*)
from tm_order_actions
where server_date between '2023-11-30 23:59:59' AND '2023-12-31 23:59:59'
and metrics_amount_before = '-2'
group by date_trunc('day', server_date)
order by date_trunc('day', server_date) desc;"""

true_order_actions_december = pd.read_sql(select_true_order_actions, conn)
false_order_actions_december = pd.read_sql(select_false_order_actions, conn)
unavailable_order_actions_december = pd.read_sql(select_unavailable_order_actions, conn)
skip_order_actions_december = pd.read_sql(select_skip_order_actions, conn)
timeFmt = mdates.DateFormatter('%d')

# months = mdates.MonthLocator()
# days = mdates.DayLocator()
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.yaxis.set_major_locator(ticker.AutoLocator())
plt.xlabel("December", fontsize=14, fontweight="bold")
plt.ylabel("Amount", fontsize=14, fontweight="bold")
plt.title("Order actions", fontsize=14, fontweight="bold")
plt.locator_params (axis='x', nbins= len(true_order_actions_december['date_trunc']))
plt.locator_params (axis='y', nbins= 20)
plt.grid(True)
plt.plot(true_order_actions_december['date_trunc'], true_order_actions_december['count'], '-.g', alpha=0.7, lw=1, mec='r', mew=3, ms=6, label='true')
plt.plot(false_order_actions_december['date_trunc'], false_order_actions_december['count'], '-.y', alpha=0.7, lw=1, mec='r', mew=3, ms=6, label='false')
plt.plot(unavailable_order_actions_december['date_trunc'], unavailable_order_actions_december['count'], '-.b', alpha=0.7, lw=1, mec='r', mew=3, ms=6, label='unavailable')
plt.plot(skip_order_actions_december['date_trunc'], skip_order_actions_december['count'], '-.r', alpha=0.7, lw=1, mec='r', mew=3, ms=6, label='skip')
plt.legend(loc='best')
plt.show()