from config import *


def ios_contracts_by_day(contracts_by_day):
    total_ios_contracts = contracts_by_day['cnt'].sum()
    total_money = total_ios_contracts * 10
    text_kwargs = dict(fontsize=12, fontweight='bold')
    time_format = mdates.DateFormatter('%d')
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    ax.xaxis.set_major_formatter(time_format)
    splot = sns.barplot(contracts_by_day, x='date', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=14)
    plt.title("iOS contracts", **text_kwargs)
    plt.grid(True)
    plt.text(-0.5, -0.8, f'Total amount of contracts: {total_ios_contracts}, ({total_money}$)', **text_kwargs)
    plt.text(-0.5, -2, ' ')
    plt.show()


df_ios_contracts_by_day = pd.read_sql(select_ios_contracts_by_day, conn)
ios_contracts_by_day(df_ios_contracts_by_day)
