from config import *


def type_of_orders(order_type_month):
    explode = []
    total_orders_month = order_type_month['amount'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(order_type_month)):
        explode.append(0.05)

    order_type_month['amount'].plot(
        kind='pie', labels=order_type_month['action_type'], textprops={"fontweight": "bold", "fontsize": "12"},
        shadow='true', autopct='%1.1f%%',
        cmap='Set3', figsize=(12, 8), explode=explode
    )
    plt.ylabel("%", fontsize=20, fontweight="bold")
    plt.legend(
        loc='upper right', labels=order_type_month['amount'], prop={'weight': 'bold'}
    )
    plt.text(-0.8, -1.1, f'Total orders: {total_orders_month}', **text_kwargs)
    plt.show()


orders_type = pd.read_sql(select_type_of_orders, conn)
type_of_orders(orders_type)
