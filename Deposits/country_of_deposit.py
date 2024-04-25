from config import *


def countries_of_deposit(country_deposit_by_month):
    fig = plt.figure(figsize=(12, 8))
    splot = sns.barplot(country_deposit_by_month, x='country_iso', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=14)

    top_countries_list = []
    for i in country_deposit_by_month['country_iso']:
        for key, value in countries.items():
            if i == key:
                top_countries_list.append(value)

    plt.xlabel("Country", fontsize=14, fontweight="bold")
    plt.ylabel("Number of deposit", fontsize=14, fontweight="bold")
    plt.title("Top 15 countries", fontsize=14, fontweight="bold")
    plt.grid(True)
    plt.legend(
        loc='upper right', labels=top_countries_list, prop={'weight': 'bold'}
    )
    plt.show()


top_country_deposit = pd.read_sql(select_top_country_deposits_month, conn)
countries_of_deposit(top_country_deposit)
