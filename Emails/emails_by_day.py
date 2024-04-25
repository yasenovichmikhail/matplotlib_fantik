from config import *


df_confirmed_emails = pd.read_sql(select_confirm_emails, conn)
base_chart_by_day(df_confirmed_emails)
