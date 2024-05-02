from config import *


df_ios_contracts_by_day = pd.read_sql(SELECT_IOS_CONTRACTS_BY_DAY, CONN)
contracts_by_day(df_ios_contracts_by_day, 10)
