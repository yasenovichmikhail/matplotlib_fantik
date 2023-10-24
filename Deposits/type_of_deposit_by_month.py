select_type_deposits_by_month = """select t.hearts_count, count(*)
from tm_consumable_purchases tcp
         join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
  and transaction_date between '2023-09-30 23:59:59' AND '2023-10-31 23:59:59'
group by t.hearts_count
order by count(*) desc"""

type_deposit_by_month = pd.read_sql(select_type_deposits_by_month, conn)
explode = []

for i in range(len(type_deposit_by_month)):
    explode.append(0.05)

type_deposit_by_month['count'].plot(
    kind='pie', labels=type_deposit_by_month['hearts_count'], textprops = {"fontweight":"bold", "fontsize":"12"}, autopct='%1.1f%%', cmap='Set3', figsize=(12,8),
    explode = explode, shadow = 'True'
    )
plt.title('Type of deposits', fontsize=13, fontweight="bold")
plt.ylabel("%", fontsize=12, fontweight="bold")
plt.legend(
    loc = 'upper right', fontsize = 14, edgecolor = 'gray', title = 'Amount', title_fontsize = '12', labels = type_deposit_by_month['count']
)
plt.show()