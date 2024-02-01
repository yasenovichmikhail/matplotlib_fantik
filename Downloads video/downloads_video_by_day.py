from main_import import *

def video_downloads(video_month):
    timeFmt = mdates.DateFormatter('%d')
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    ax.xaxis.set_major_formatter(timeFmt)
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    plt.ylabel("Amount", fontsize=14, fontweight="bold")
    plt.title("Video Downloads by day", fontsize=14, fontweight="bold")
    plt.locator_params (axis='x', nbins= len(video_month['date_trunc']))
    plt.locator_params (axis='y', nbins= 20)
    plt.grid(True)
    plt.plot(video_month['date_trunc'], video_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=3, ms=6)
    plt.show()

select_video_download = """select date_trunc('day', download_date), count(*)
    from tm_video_downloads
    where date_trunc('day', download_date) between '2023-12-31 23:59:59' and '2024-01-31 23:59:59'
    group by date_trunc('day', download_date)
    order by date_trunc('day', download_date) desc"""

video_january = pd.read_sql(select_video_download, conn)
video_downloads(video_january)