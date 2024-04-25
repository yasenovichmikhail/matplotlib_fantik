from config import *


users_by_month = pd.read_sql(select_users_by_day, conn)
base_chart_by_day(users_by_month)
