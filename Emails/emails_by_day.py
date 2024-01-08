select_confirm_emails = """select date_trunc('day', actual_date), count(*)
from tm_users
where date_trunc('day', actual_date) > to_date('2023/11/30', 'yyyy/mm/dd')
and date_trunc('day', actual_date) < to_date('2024/01/01', 'yyyy/mm/dd')
and email is not null
group by date_trunc('day', actual_date)
order by date_trunc('day', actual_date) desc;"""

emails_december = pd.read_sql(select_confirm_emails, conn)
timeFmt = mdates.DateFormatter('%d')
# months = mdates.MonthLocator()
days = mdates.DayLocator()
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
# ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_major_locator(days)
plt.xlabel("December", fontsize=14, fontweight="bold")
plt.ylabel("Confirm Emails", fontsize=14, fontweight="bold")
plt.title("Emails by day", fontsize=14, fontweight="bold")
# plt.locator_params (axis='x', nbins= 30 )
plt.locator_params (axis='y', nbins= 20 )
plt.grid(True)
plt.plot(emails_december['date_trunc'], emails_december['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
plt.show()