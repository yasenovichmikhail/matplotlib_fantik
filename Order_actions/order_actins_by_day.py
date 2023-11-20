select_order_actions = """select 'True' as activities, count(*)
from tm_order_actions
where start_date between '2023-11-18 23:59:59' AND '2023-11-19 23:59:59'
  and is_success = 'true'
  and metrics_amount_after != '-1'
union
select 'False', count(*)
from tm_order_actions
where start_date between '2023-11-18 23:59:59' AND '2023-11-19 23:59:59'
  and is_success = 'false'
union
select 'Unavailable', count(*)
from tm_order_actions
where start_date between '2023-11-18 23:59:59' AND '2023-11-19 23:59:59'
  and is_success = 'true'
  and metrics_amount_after = '-1';"""

order_actions = pd.read_sql(select_order_actions, conn)
  
fig = plt.figure(figsize = (12, 8))
#plots = plt.bar(users_by_country_april['country_iso'], users_by_country_april['cnt'], color ='c', width = 0.8)
splot = sns.barplot(order_actions, x='activities', y='count', color ='c', width = 0.8)
plt.bar_label(splot.containers[0],size=14)
            
plt.xlabel("Activities", fontsize=14, fontweight="bold")
plt.ylabel("Number of activities", fontsize=14, fontweight="bold")
plt.title("Order actions", fontsize=14, fontweight="bold")
plt.grid(True)
plt.show()