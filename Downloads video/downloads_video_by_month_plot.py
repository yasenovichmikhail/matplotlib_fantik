select_video_download = """select date_trunc('month', download_date), count(*)
from tm_video_downloads
where date_trunc('month', download_date) > to_date('2023/04/01', 'yyyy/mm/dd')
group by date_trunc('month', download_date)
order by date_trunc('month', download_date) desc"""

video = pd.read_sql(select_video_download, conn)
timeFmt = mdates.DateFormatter('%B')

#months = mdates.MonthLocator()
# days = mdates.DayLocator()
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.yaxis.set_major_locator(ticker.AutoLocator())
#ax.xaxis.set_minor_locator(days)
plt.xlabel("Month", fontsize=14, fontweight="bold")
plt.ylabel("Amount", fontsize=14, fontweight="bold")
plt.title("Video Downloads by months", fontsize=14, fontweight="bold")
# plt.locator_params (axis='x', nbins= 7)
plt.locator_params (axis='y', nbins= 20 )
plt.grid(True)
plt.plot(video['date_trunc'], video['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
plt.show()