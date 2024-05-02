from config import *


df_orders_month = pd.read_sql(SELECT_ORDERS, CONN)
base_chart_by_day(df_orders_month)
