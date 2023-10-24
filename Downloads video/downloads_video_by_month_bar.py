select_video_download = """select date_trunc('month', download_date), count(*)
from tm_video_downloads
where date_trunc('month', download_date) > to_date('2023/04/01', 'yyyy/mm/dd')
group by date_trunc('month', download_date)
order by date_trunc('month', download_date) asc"""

video_bar = pd.read_sql(select_video_download, conn)
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
video_bar['date_trunc'] = video_bar['date_trunc'].dt.strftime('%b')
#timeFmt = mdates.DateFormatter('%B')

ax = sns.barplot(video_bar, x="date_trunc", y="count")
ax.bar_label(ax.containers[0], fontsize=14, fontweight="bold")
ax.locator_params (axis='y', nbins= 20)
plt.xlabel("2023", fontsize=14, fontweight="bold")
plt.ylabel("Amount", fontsize=14, fontweight="bold")
plt.title("Video downloads by month", fontsize=14, fontweight="bold")

#ax.xaxis.set_major_formatter(timeFmt)

plt.grid(True)
plt.show()