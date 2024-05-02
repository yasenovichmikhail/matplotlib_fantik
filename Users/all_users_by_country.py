from config import *


def users_by_country_month(users_top_country_month):
    fig = plt.figure(figsize=(14, 10))
    splot = sns.barplot(users_top_country_month, x='country_iso', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=14)
    text_kwargs = dict(ha='center', va='center', fontsize=12, fontweight='bold')

    top_countries_list = []
    for i in users_top_country_month['country_iso']:
        for key, value in COUNTRIES.items():
            if i == key:
                top_countries_list.append(value)

    plt.xlabel("Country", **text_kwargs)
    plt.ylabel("Number of users", **text_kwargs)
    plt.title("Top 15 countries", **text_kwargs)
    plt.grid(True)
    plt.legend(
        loc='upper right', labels=top_countries_list, prop={'weight': 'bold'}
    )
    plt.show()


if __name__ == '__main__':
    all_users_by_country = pd.read_sql(SELECT_USERS_BY_COUNTRY, CONN)
    users_by_country_month(all_users_by_country)
