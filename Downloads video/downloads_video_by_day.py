from config import *


df_download_video = pd.read_sql(SELECT_DOWNLOAD_VIDEO, CONN)
base_chart_by_day(df_download_video)
