from config import *


def confirmed_emails(emails_month):
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
    plt.locator_params(axis='y', nbins=20)
    plt.grid(True)
    plt.plot(emails_month['date_trunc'], emails_month['count'], '*-.g', alpha=0.7, lw=1, mec='r', mew=2, ms=5)
    plt.show()


df_confirmed_emails = pd.read_sql(select_confirm_emails, conn)
confirmed_emails(df_confirmed_emails)
