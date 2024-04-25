from config import *


df_android_contracts_by_day = pd.read_sql(select_android_contracts_by_day, conn)
contracts_by_day(df_android_contracts_by_day, 35)
