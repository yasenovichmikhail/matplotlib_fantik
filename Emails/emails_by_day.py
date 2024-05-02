from config import *


df_confirmed_emails = pd.read_sql(SELECT_CONFIRM_EMAILS, CONN)
base_chart_by_day(df_confirmed_emails)
