select_type_orders_month = """select 'Likes' as action, count(*) as Amount
from tm_user_orders
where action_type_id = 1
and start_date between '2023-03-31 23:59:59' AND '2023-04-30 23:59:59'
and is_fictive = 'false'
union
select 'Shares' as Shares, count(*)
from tm_user_orders
where action_type_id = 2
and start_date between '2023-03-31 23:59:59' AND '2023-04-30 23:59:59'
and is_fictive = 'false'
union
select 'Comments' as Comments, count(*)
from tm_user_orders
where action_type_id = 3
and start_date between '2023-03-31 23:59:59' AND '2023-04-30 23:59:59'
and is_fictive = 'false'
union
select 'Followers' as Followers, count(*)
from tm_user_orders
where action_type_id = 4
and start_date between '2023-03-31 23:59:59' AND '2023-04-30 23:59:59'
and is_fictive = 'false'
order by Amount desc"""

orders_type_april = pd.read_sql(select_type_orders_month, conn)
explode = []

for i in range(len(orders_type_april)):
    explode.append(0.05)
    
orders_type_april['amount'].plot(
    kind='pie', labels=orders_type_may['action'], textprops = {"fontweight":"bold", "fontsize":"14"}, shadow = 'True', autopct='%1.1f%%', cmap='Set3', figsize=(12,8), explode=explode
)
plt.title('April, 2023', fontsize=14, fontweight="bold")
plt.ylabel("%", fontsize=20, fontweight="bold")
plt.legend(
    loc = 'lower left', labels = orders_type_april['amount'], prop = {'weight':'bold'}
)