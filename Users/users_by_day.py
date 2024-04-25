from config import *


def users_by_day(users_month):
    time_format = mdates.DateFormatter('%d')
    # months = mdates.MonthLocator()
    # days = mdates.DayLocator()
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    ax.xaxis.set_major_formatter(time_format)
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    plt.ylabel("Users", fontsize=14, fontweight="bold")
    plt.title("New Users by day", fontsize=14, fontweight="bold")
    plt.locator_params(axis='x', nbins=len(users_month['date_trunc']))
    plt.locator_params(axis='y', nbins=20)
    plt.grid(True)
    plt.plot(users_month['date_trunc'], users_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
    plt.show()


users_by_month = pd.read_sql(select_users_by_day, conn)
users_by_day(users_by_month)
