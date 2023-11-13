select_country_deposits_by_month = """select tu.country_iso, count(*)
from tm_consumable_purchases tcp
    join tm_users tu on tu.user_id = tcp.user_id 
  where transaction_date between '2023-10-31 23:59:59' AND '2023-11-30 23:59:59'
group by tu.country_iso
order by count(*) desc
limit 10
"""

country_deposit_by_month = pd.read_sql(select_country_deposits_by_month, conn)
explode = []

for i in range(len(country_deposit_by_month)):
    explode.append(0.03)

country_deposit_by_month['count'].plot(
    kind='pie', labels=country_deposit_by_month['country_iso'], textprops = {"fontweight":"bold", "fontsize":"12"}, autopct='%1.1f%%', cmap='Set3', figsize=(12,8),
    explode = explode, shadow = 'True'
    )
plt.title('Country of deposits', fontsize=13, fontweight="bold")
plt.ylabel("%", fontsize=12, fontweight="bold")
plt.legend(
    loc = 'upper right', fontsize = 14, edgecolor = 'gray', title = 'Amount', title_fontsize = '12', labels = country_deposit_by_month['count']
)
plt.show()