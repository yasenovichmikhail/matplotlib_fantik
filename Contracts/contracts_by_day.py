select_user_contracts_month = """select date_trunc('day', tuc.actual_date), count(*)
from tm_user_contracts tuc
         join tm_subscription ts on ts.subscription_id = tuc.subscription_id
where user_contract_id > 42
  and user_id != 30
  and tuc.period_end_date::date - tuc.actual_date::date > 3
  and tuc.actual_date between '2023-11-30 23:59:59' AND '2023-12-31 23:59:59'
group by date_trunc('day', tuc.actual_date)
order by date_trunc('day', tuc.actual_date) asc"""

user_contracts_december = pd.read_sql(select_user_contracts_month, conn)
total_contracts_december = user_contracts_december['count'].sum()
total_sum_december = contracts_price * total_contracts_december

fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
timeFmt = mdates.DateFormatter('%d')
ax.xaxis.set_major_formatter(timeFmt)
plt.xlabel("December", fontsize=14, fontweight="bold")
plt.ylabel("Amount", fontsize=14, fontweight="bold")
plt.title("Contracts by day", fontsize=14, fontweight="bold")
#plt.locator_params (axis='x', nbins= 30 )
plt.locator_params (axis='y', nbins=user_contracts_december['count'].max() )
plt.locator_params (axis='x', nbins= len(user_contracts_december['date_trunc']))
plt.grid(True)
plt.plot(user_contracts_december['date_trunc'], user_contracts_december['count'], '-*b', alpha=0.7, lw=1, mec='r', mew=2, ms=6)
plt.bar_label(splot.containers[0],size=14)
plt.show()