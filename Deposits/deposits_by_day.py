from config import *


def deposits_by_day(deposit_by_day):
    time_format = mdates.DateFormatter('%d')
    fig, ax = plt.subplots(figsize=(14, 10), layout='constrained')
    ax.xaxis.set_major_formatter(time_format)
    splot = sns.barplot(deposit_by_day, x='date', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=14)
    plt.xlabel("Date", fontsize=14, fontweight="bold")
    plt.ylabel("Number of deposits", fontsize=14, fontweight="bold")
    plt.title("Deposits by day", fontsize=14, fontweight="bold")
    plt.grid(True)
    plt.show()


df_deposits_by_day = pd.read_sql(select_deposits_by_day, conn)
deposits_by_day(df_deposits_by_day)
