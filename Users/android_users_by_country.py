from Users.all_users_by_country import users_by_country_month
from config import *

android_users_by_country = pd.read_sql(select_android_users, conn)
users_by_country_month(android_users_by_country)
