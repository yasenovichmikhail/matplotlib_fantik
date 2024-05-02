from Users.all_users_by_country import users_by_country_month
from config import *

ios_users_by_country = pd.read_sql(SELECT_IOS_USERS, CONN)
users_by_country_month(ios_users_by_country)
