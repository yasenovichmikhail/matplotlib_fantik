from main_import import *

def users_by_day(users_month):
    timeFmt = mdates.DateFormatter('%d')
    # months = mdates.MonthLocator()
    #days = mdates.DayLocator()
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    ax.xaxis.set_major_formatter(timeFmt)
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    plt.ylabel("Users", fontsize=14, fontweight="bold")
    plt.title("New Users by day", fontsize=14, fontweight="bold")
    plt.locator_params (axis='x', nbins= len(users_month['date_trunc']))
    plt.locator_params (axis='y', nbins= 20)
    plt.grid(True)
    plt.plot(users_month['date_trunc'], users_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
    plt.show()

select_users_by_day = """select date_trunc('day', actual_date), count(distinct user_name)
from tm_users
where date_trunc('day', actual_date) between '2023-08-31 23:59:59' and '2023-09-30 23:59:59'
group by date_trunc('day', actual_date)
order by date_trunc('day', actual_date) desc"""

users_by_day_february = pd.read_sql(select_users_by_day, conn)
users_by_day(users_by_day_february)
users_by_day_february.describe().round()