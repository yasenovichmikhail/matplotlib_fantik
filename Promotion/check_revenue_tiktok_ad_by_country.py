from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter


def get_all_purchases_by_country(date_from, date_to, pattern, package_name, conn):
    select_all_purchases = f"""with all_users as (select user_id
                           from tm_logons
                           where install_referrer
                               like '%%{pattern}%%'
                             and logon_date between '{date_from}' AND '{date_to}')
        select case
                   when tu.country_iso = 'AT' then 'Austria'
                   when tu.country_iso = 'DE' then 'Germany'
                   when tu.country_iso = 'FR' then 'France'
                   when tu.country_iso = 'PT' then 'Portugal'
                   when tu.country_iso = 'GB' then 'Great Britain'
                   when tu.country_iso = 'NO' then 'Norway'
                   when tu.country_iso = 'AE' then 'United Arab Emirates'
                   end as country_iso,
               currency_iso,
               SUM(price) sum
        from tm_consumable_purchases tcp
                 join tm_users tu on tcp.user_id = tu.user_id
                 join all_users on all_users.user_id = tcp.user_id
        where transaction_date between '{date_from}' AND '{CURRENT_TIME}'
          and bundle_identifier = '{package_name}'
          and payment_status_id = 2
          and currency_iso != 'HUF'
          and tcp.consumable_product_id not in (62, 63, 64, 65, 66, 67, 68)
        group by country_iso, currency_iso
        order by sum desc"""

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
    all_country_lst = df_dict['country_iso']
    new_dict = {}
    for i in range(len(all_country_lst)):
        new_dict[all_country_lst[i]] = currency_lst[i], all_sum_lst[i]
    for key, value in new_dict.items():
        price = get_exchange(usd_converter(*value))
        price = round(float(price), 2)
        print(f'{key} - {price}$')
        total += price
    total = round(total, 2)
    print(f'Total amount: {total}$')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                pattern='E_C_P',
                package_name=PACKAGE_NAME_FANTIK,
                conn=DB_PROD_CONNECTION)
