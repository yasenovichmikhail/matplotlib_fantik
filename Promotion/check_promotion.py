from sqlalchemy import text
from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter
from pprint import pprint


def get_all_purchases_by_country(date_from, date_to, pattern, conn):
    select_all_purchases = f"""select tcp.currency_iso, SUM(price)
    from tm_consumable_purchases tcp
         join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
    where transaction_date between '{date_from}' AND '{date_to}'
    and tcp.user_id in (select user_id
                      from tm_logons
                      where install_referrer
                          like '%%{pattern}%%'
                        and package_name = 'com.tikboost.fantik')
    and payment_status_id = 2
    group by tcp.currency_iso"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue():
    total = 0
    df_dict = get_all_purchases_by_country(date_from=DATE1,
                                           date_to=DATE2,
                                           pattern='CONN).to_dict(orient='list')
    currency_lst = df_dict['currency_iso']
    all_sum_lst = df_dict['sum']
    all_sum_dict = dict(zip(currency_lst, all_sum_lst))
    for key, value in all_sum_dict.items():
        if key != 'USD':
            price = get_exchange(usd_converter(key, round(value)))
            print(price)
            total += price
        else:
            total += int(value)
    print(total)


get_all_revenue()

