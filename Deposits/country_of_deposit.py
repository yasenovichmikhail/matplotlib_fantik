from config import *

def countries_of_deposit(country_deposit_by_month):
    fig = plt.figure(figsize = (12, 8))
    #plots = plt.bar(users_by_country_april['country_iso'], users_by_country_april['cnt'], color ='c', width = 0.8)
    splot = sns.barplot(country_deposit_by_month, x='country_iso', y='cnt', color ='c', width = 0.8)
    plt.bar_label(splot.containers[0],size=14)

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
        loc = 'upper right', labels = top_countries_list, prop = {'weight':'bold'}
    )
    plt.show()

select_top_country_deposits_month = """select tu.country_iso, count(*) cnt
from tm_consumable_purchases tcp
         join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
         join tm_users tu on tcp.user_id = tu.user_id
where tcp.user_id not in (30, 25, 5685, 34, 136397, 216573)
  and transaction_date between '2024-01-31 23:59:59' AND '2024-02-29 23:59:59'
group by tu.country_iso
order by cnt desc
limit 15"""

top_country_deposit_february = pd.read_sql(select_top_country_deposits_month, conn)
countries_of_deposit(top_country_deposit_february)