from config import *


df_download_video = pd.read_sql(select_download_video, conn)
base_chart_by_day(df_download_video)
