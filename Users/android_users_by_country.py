from Users.all_users_by_country import users_by_country_month
from config import *

android_users_by_country = pd.read_sql(SELECT_ANDROID_USERS, CONN)
users_by_country_month(android_users_by_country)
