from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter


def get_all_ios_purchases_by_country(date_from, date_to, package_name, conn):
    select_all_purchases = f"""with all_users as (select user_id
                           from tm_logons
                           where logon_date between '{date_from}' AND '{date_to}')
        select case
                   when tu.country_iso = 'AT' then 'Austria'
                   when tu.country_iso = 'DE' then 'Germany'
                   when tu.country_iso = 'FR' then 'France'
                   when tu.country_iso = 'PT' then 'Portugal'
                   when tu.country_iso = 'GB' then 'Great Britain'
                   when tu.country_iso = 'NO' then 'Norway'
                   when tu.country_iso = 'AE' then 'United Arab Emirates'
                   end as country_iso,
               tcp.currency_iso,
               SUM(price) sum
        from tm_consumable_purchases tcp
                 join tm_users tu on tcp.user_id = tu.user_id
                 join all_users on all_users.user_id = tcp.user_id
        where transaction_date between '{date_from}' AND '{CURRENT_TIME}'
          and tcp.bundle_identifier = '{package_name}'
          and payment_status_id = 2
          and country_iso in ('AT', 'DE', 'FR', 'PT', 'GB', 'NO', 'AE')
        group by tu.country_iso, tcp.currency_iso
        order by sum desc"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue(date_from, date_to, package_name, conn):
    df_dict = get_all_ios_purchases_by_country(date_from=date_from,
                                               date_to=date_to,
                                               package_name=package_name,
                                               conn=conn).to_dict(orient='list')
    currency_lst = df_dict['currency_iso']
    all_sum_lst = df_dict['sum']
    all_country_lst = df_dict['country_iso']
    total_dict = {}
    for country in all_country_lst:
        total_dict.setdefault(country, 0)
    new_list_of_tuples = []
    exchange_prices = []
    for i in range(len(currency_lst)):
        tmp_tuple = (currency_lst[i], all_sum_lst[i])
        new_list_of_tuples.append(tmp_tuple)
    for pair in new_list_of_tuples:
        price = get_exchange(usd_converter(*pair))
        price = round(price, 2)
        exchange_prices.append(price)
    for i in range(len(all_country_lst)):
        for key, value in total_dict.items():
            if key == all_country_lst[i]:
                total_dict[key] += exchange_prices[i]

    sorted_dict = sorted(total_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_total_dict = dict(sorted_dict)
    for key, value in sorted_total_dict.items():
        print(f"{key} - {round(value, 2)}$")

    total = round(sum(exchange_prices), 2)
    print(f'Total amount: {total}$')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                package_name=PACKAGE_NAME_FAMETOK,
                conn=DB_PROD_CONNECTION)
