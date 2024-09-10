from config import *


def users_by_country_month(number_of_countries):

    select_users_by_country = f"""select country_iso, count(*) cnt
        from tm_users
        where actual_date between '{DATE1}' and '{DATE2}'
        group by country_iso
        order by cnt desc
        limit {number_of_countries}"""

    all_users_by_country = pd.read_sql(select_users_by_country, CONN)

    fig = plt.figure(figsize=(14, 10))
    splot = sns.barplot(all_users_by_country, x='country_iso', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=number_of_countries - 1)
    text_kwargs = dict(ha='center', va='center', fontsize=12, fontweight='bold')

    top_countries_list = []
    for i in all_users_by_country['country_iso']:
        for key, value in COUNTRIES.items():
            if i == key:
                top_countries_list.append(value)

    plt.xlabel("Country", **text_kwargs)
    plt.ylabel("Number of users", **text_kwargs)
    plt.title(f"Top {number_of_countries} countries", **text_kwargs)
    plt.grid(True)
    plt.legend(
        loc='upper right', labels=top_countries_list, prop={'weight': 'bold'}
    )
    plt.show()


if __name__ == '__main__':
    users_by_country_month(10)
