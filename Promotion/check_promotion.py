from sqlalchemy import text
from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter
from pprint import pprint


def get_all_purchases_by_country(date_from, date_to, pattern, package_name, conn):
    select_all_purchases = f"""select tcp.currency_iso, SUM(price)
    from tm_consumable_purchases tcp
    where transaction_date between '{date_from}' AND '{date_to}'
    and tcp.user_id in (select user_id
                      from tm_logons
                      where install_referrer
                          like '%%{pattern}%%'
                        and package_name = '{package_name}')
    and payment_status_id = 2
    and price != '0.0000'
    and currency_iso != 'RUB'
    group by tcp.currency_iso"""

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
            price = get_exchange(usd_converter(key, round(value, 0)))
            print(price)
            total += price
        else:
            print(int(round(value, 0)))
            total += int(round(value, 0))
    print(f'Total amount: {total}')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                pattern='google-play',
                package_name=PACKAGE_NAME_FANTIK,
                conn=CONN)
