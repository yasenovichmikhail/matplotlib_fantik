select_type_deposits_by_month = """select t.hearts_count, count(*)
from tm_consumable_purchases tcp
         join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
  and transaction_date between '2023-10-31 23:59:59' AND '2023-11-30 23:59:59'
group by t.hearts_count
order by count(*) desc"""

type_deposit_november = pd.read_sql(select_type_deposits_by_month, conn)
explode = []
total_deposits_november = type_deposit_november['count'].sum()
text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

for i in range(len(type_deposit_november)):
    explode.append(0.03)

type_deposit_november['count'].plot(
    kind='pie', labels=type_deposit_november['hearts_count'], textprops = {"fontweight":"bold", "fontsize":"12"}, autopct='%1.1f%%', cmap='Set3', figsize=(12,8),
    explode = explode, shadow = 'True'
    )

hearts_november = []
count_november = []

total_price_november = type_deposit_november.sort_values(by='hearts_count')

for j in total_price_november['hearts_count']:
    hearts_november.append(j)
for k in total_price_november['count']:
    count_november.append(k)
total_dict_november = dict(zip(hearts_november, count_november))

total_price_november = 0
for key, value in total_dict_november.items():
    for coin, price in prices.items():
        if int(key) == int(coin):
            total_price_november += int(value) * int(price)

total_price_november = round(total_price_november, 2)

plt.title('Type of deposits', fontsize=14, fontweight="bold")
plt.ylabel("%", fontsize=12, fontweight="bold")
plt.legend(
    loc = 'upper right', fontsize = 14, edgecolor = 'gray', title = 'Amount', title_fontsize = '12', labels = type_deposit_november['count'], prop = {'weight':'bold'}
)
plt.text(-0.83, -1.1, f'Total deposits: {total_deposits_november}', **text_kwargs)
plt.text(-1.08, -1.2, f'Total: {total_price_november}$', **text_kwargs)
plt.show()