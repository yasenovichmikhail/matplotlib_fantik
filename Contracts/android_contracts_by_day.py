from config import *


df_android_contracts_by_day = pd.read_sql(SELECT_ANDROID_CONTRACTS_BY_DAY, CONN)
contracts_by_day(df_android_contracts_by_day, 35)
