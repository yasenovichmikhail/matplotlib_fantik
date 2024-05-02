from config import *


df_rewards_by_day = pd.read_sql(SELECT_REWARDS_BY_DAY, CONN)
base_chart_by_day(df_rewards_by_day)
