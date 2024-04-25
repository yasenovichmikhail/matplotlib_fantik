from config import *


def android_contracts_by_day(contracts_by_day):
    total_android_contracts = contracts_by_day['cnt'].sum()
    total_money = total_android_contracts * 35
    text_kwargs = dict(fontsize=12, fontweight='bold')
    time_format = mdates.DateFormatter('%d')
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    ax.xaxis.set_major_formatter(time_format)
    splot = sns.barplot(contracts_by_day, x='date', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=14)
    plt.title("android contracts", **text_kwargs)
    plt.grid(True)
    plt.text(-0.5, -0.8, f'Total amount of contracts: {total_android_contracts}, ({total_money}$)', **text_kwargs)
    plt.text(-0.5, -2, ' ')
    plt.show()


df_android_contracts_by_day = pd.read_sql(select_android_contracts_by_day, conn)
android_contracts_by_day(df_android_contracts_by_day)
