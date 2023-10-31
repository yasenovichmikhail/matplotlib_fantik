select_deposit_october = """
select date_trunc('day', transaction_date), count(transaction_date)
from tm_consumable_purchases
where date_trunc('day', transaction_date) between '2023-09-30 23:59:59' and '2023-10-31 23:59:59'
  and user_id > 99
  and user_id not in (2222, 2297, 162, 2283)
group by date_trunc('day', transaction_date)
order by date_trunc('day', transaction_date) desc
"""

deposit_october = pd.read_sql(select_deposit_october, conn)
timeFmt = mdates.DateFormatter('%d')
# months = mdates.MonthLocator()
days = mdates.DayLocator()
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(days)
plt.xlabel("October", fontsize=14, fontweight="bold")
plt.ylabel("Deposit", fontsize=14, fontweight="bold")
plt.title("Deposits by day", fontsize=14, fontweight="bold")
# plt.locator_params (axis='x', nbins= 30 )
plt.locator_params (axis='y', nbins= deposit_october['count'].max())
plt.grid(True)
plt.plot(deposit_october['date_trunc'], deposit_october['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
plt.show()