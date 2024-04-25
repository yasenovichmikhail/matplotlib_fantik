from config import *


def rewards_by_day(rewards_month):
    time_format = mdates.DateFormatter('%d')
    # months = mdates.MonthLocator()
    days = mdates.DayLocator()
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    # ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(time_format)
    ax.xaxis.set_major_locator(days)
    plt.ylabel("Rewards", fontsize=14, fontweight="bold")
    plt.title("Rewards by day", fontsize=14, fontweight="bold")
    # plt.locator_params (axis='x', nbins= 30 )
    plt.locator_params(axis='y', nbins=20)
    plt.grid(True)
    plt.plot(rewards_month['date_trunc'], rewards_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
    plt.show()


df_rewards_by_day = pd.read_sql(select_rewards_by_day, conn)
rewards_by_day(df_rewards_by_day)
