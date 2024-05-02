from config import *


users_by_month = pd.read_sql(SELECT_USERS_BY_DAY, CONN)
base_chart_by_day(users_by_month)
