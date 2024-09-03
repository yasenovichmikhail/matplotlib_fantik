from config import *


def top_countries_of_deposit(number_of_countries):

    select_top_country_deposits_month = f"""select tu.country_iso, count(*) cnt
        from tm_consumable_purchases tcp
                 join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
                 join tm_users tu on tcp.user_id = tu.user_id
        where tcp.user_id not in (30, 25, 2283, 5685, 34, 136397, 216573, 279730, 281654, 293956, 426712, 439174, 403206,
                              397059, 271432, 258060, 330567, 332798, 530747, 619549, 962017, 961999, 961842, 961842)
          and transaction_date between '{DATE1}' and '{DATE2}'
          and payment_status_id = 2
        group by tu.country_iso
        order by cnt desc
        limit {number_of_countries}"""

    top_country_deposit = pd.read_sql(select_top_country_deposits_month, CONN)

    fig = plt.figure(figsize=(12, 8))
    splot = sns.barplot(top_country_deposit, x='country_iso', y='cnt', color='c', width=0.8)
    plt.bar_label(splot.containers[0], size=number_of_countries - 1)

    top_countries_list = []
    for i in top_country_deposit['country_iso']:
        for key, value in COUNTRIES.items():
            if i == key:
                top_countries_list.append(value)

    plt.xlabel("Country", fontsize=14, fontweight="bold")
    plt.ylabel("Deposits", fontsize=14, fontweight="bold")
    plt.title(f"Top {number_of_countries} countries", fontsize=14, fontweight="bold")
    plt.grid(True)
    plt.legend(
        loc='upper right', labels=top_countries_list, prop={'weight': 'bold'}
    )
    plt.show()


if __name__ == '__main__':
    top_countries_of_deposit(10)

