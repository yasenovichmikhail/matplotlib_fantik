from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter


def get_all_purchases_by_country(date_from, date_to, pattern, package_name, conn):
    select_all_purchases = f"""with all_users as (select user_id
                   from tm_logons
                   where install_referrer
                       like '%%{pattern}%%'
                     and logon_date between '{date_from}' AND '{date_to}')
select currency_iso, sum(price) sum
from tm_consumable_purchases tcp
         join all_users on all_users.user_id = tcp.user_id
where transaction_date between '{date_from}' AND '{CURRENT_TIME}'
  and payment_status_id = 2
  and bundle_identifier = '{package_name}'
  and tcp.consumable_product_id not in (62, 63, 64, 65, 66, 67, 68)
  and currency_iso != 'HUF'
 group by currency_iso"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue(date_from, date_to, pattern, package_name, conn):
    total = 0
    df_dict = get_all_purchases_by_country(date_from=date_from,
                                           date_to=date_to,
                                           pattern=pattern,
                                           package_name=package_name,
                                           conn=conn).to_dict(orient='list')
    currency_lst = df_dict['currency_iso']
    all_sum_lst = df_dict['sum']
    all_sum_dict = dict(zip(currency_lst, all_sum_lst))
    for key, value in all_sum_dict.items():
        if key != 'USD':
            price = get_exchange(usd_converter(key, value))
            print(f'{value} {key} = {price}$')
            total += price
        else:
            price = round(float(value), 2)
            total += price
            print(f'{price} USD = {price}$')
    total = round(total, 2)
    print(f'Total amount: {total}$')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                pattern='E_C_P',
                package_name=PACKAGE_NAME_FANTIK,
                conn=DB_PROD_CONNECTION)
