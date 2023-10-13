select_orders = """select date_trunc('day', start_date), count(*)
from tm_user_orders
where date_trunc('day', start_date) > to_date('2023/08/31', 'yyyy/mm/dd')
and is_fictive = 'false'
group by date_trunc('day', start_date)
order by date_trunc('day', start_date) desc"""
orders = pd.read_sql(select_orders, conn)
timeFmt = mdates.DateFormatter('%d %m')
# months = mdates.MonthLocator()
days = mdates.DayLocator()
fig, ax = plt.subplots()
plt.plot(orders['date_trunc'], orders['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.xlabel("Date")
plt.ylabel("Orders")
plt.grid(True)