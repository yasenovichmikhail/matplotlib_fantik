from main_import import *

def type_of_orders(order_type_month):
    explode = []
    total_orders_month = order_type_month['amount'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(order_type_month)):
        explode.append(0.05)
    
    order_type_month['amount'].plot(
        kind='pie', labels=order_type_month['action_type'], textprops = {"fontweight":"bold", "fontsize":"12"}, shadow = 'true', autopct='%1.1f%%',
        cmap='Set3', figsize=(12,8), explode=explode
    )
    plt.ylabel("%", fontsize=20, fontweight="bold")
    plt.legend(
        loc = 'upper right', labels = order_type_month['amount'], prop = {'weight':'bold'}
    )
    plt.text(-0.8, -1.1, f'Total orders: {total_orders_month}', **text_kwargs)
    plt.show()

select_type_orders_month = """select count(*) amount,
       case
           when action_type_id = 1 then 'Likes'
           when action_type_id = 2 then 'Shares'
           when action_type_id = 3 then 'Comments'
           when action_type_id = 4 then 'Followers'
           when action_type_id = 5 then 'Views'
           end  action_type
from tm_user_orders
where is_fictive = 'false'
  and start_date between '2023-12-31 23:59:59' AND '2024-01-31 23:59:59'
  and order_sum != 0
group by action_type_id
order by action_type_id asc;"""

orders_type_january = pd.read_sql(select_type_orders_month, conn)
type_of_orders(orders_type_january)