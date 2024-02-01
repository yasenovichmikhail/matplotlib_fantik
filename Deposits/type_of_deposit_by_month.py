from main_import import *

def type_of_deposits(deposits_month):
    explode = []
    total_deposits_month = deposits_month['count'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(deposits_month)):
        explode.append(0.03)

    deposits_month['count'].plot(
        kind='pie', labels=deposits_month['hearts_count'], textprops = {"fontweight":"bold", "fontsize":"12"}, autopct='%1.1f%%', cmap='Set3', figsize=(12,8),
        explode = explode, shadow = 'True'
    )

    hearts_month = []
    count_month = []

    total_price_month = deposits_month.sort_values(by='hearts_count')

    for j in total_price_month['hearts_count']:
        hearts_month.append(j)
    for k in total_price_month['count']:
        count_month.append(k)
    total_dict_month = dict(zip(hearts_month, count_month))

    total_price_month = 0
    for key, value in total_dict_month.items():
        for coin, price in prices.items():
            if int(key) == int(coin):
                total_price_month += int(value) * float(price)

    total_price_month = round(total_price_month, 2)

    plt.title('Type of deposits', fontsize=14, fontweight="bold")
    plt.ylabel("%", fontsize=12, fontweight="bold")
    plt.legend(
        loc = 'upper right', fontsize = 14, edgecolor = 'gray', title = 'Amount', title_fontsize = '12', labels = deposits_month['count'],
        prop = {'weight':'bold'}
    )
    plt.text(-0.95, -1.1, f'Total deposits: {total_deposits_month}', **text_kwargs)
    plt.text(-1.08, -1.2, f'Total: {total_price_month}$', **text_kwargs)
    plt.show()

select_type_deposits_by_month = """select t.hearts_count, count(*)
    from tm_consumable_purchases tcp
             join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
    where transaction_date between '2023-12-31 23:59:59' AND '2024-01-31 23:59:59'
      and tcp.user_id not in (25, 30, 5685, 34, 136397, 216573)
    group by t.hearts_count
    order by count(*) desc;"""

type_deposit_january = pd.read_sql(select_type_deposits_by_month, conn)
type_of_deposits(type_deposit_january)