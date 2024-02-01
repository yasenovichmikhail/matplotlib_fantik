from main_import import *

def emails_by_day(emails_month):
    timeFmt = mdates.DateFormatter('%d')
    # months = mdates.MonthLocator()
    days = mdates.DayLocator()
    fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')
    # ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(timeFmt)
    ax.xaxis.set_major_locator(days)
    plt.ylabel("Confirmed Emails", fontsize=14, fontweight="bold")
    plt.title("Emails by day", fontsize=14, fontweight="bold")
    # plt.locator_params (axis='x', nbins= 30 )
    plt.locator_params (axis='y', nbins= 20 )
    plt.grid(True)
    plt.plot(emails_month['date_trunc'], emails_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
    plt.show()

select_confirm_emails = """select date_trunc('day', actual_date), count(*)
    from tm_users
    where date_trunc('day', actual_date) between '2023-12-31 23:59:59' and '2024-01-31 23:59:59'
    and email is not null
    group by date_trunc('day', actual_date)
    order by date_trunc('day', actual_date) desc;"""

emails_january = pd.read_sql(select_confirm_emails, conn)
emails_by_day(emails_january)