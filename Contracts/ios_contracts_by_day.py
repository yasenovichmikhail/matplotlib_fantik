from config import *


df_ios_contracts_by_day = pd.read_sql(select_ios_contracts_by_day, conn)
contracts_by_day(df_ios_contracts_by_day, 10)
