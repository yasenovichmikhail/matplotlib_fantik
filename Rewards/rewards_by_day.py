from config import *


df_rewards_by_day = pd.read_sql(select_rewards_by_day, conn)
base_chart_by_day(df_rewards_by_day)
