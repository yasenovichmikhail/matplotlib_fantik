from config import *


df_orders_month = pd.read_sql(select_orders, conn)
base_chart_by_day(df_orders_month)
