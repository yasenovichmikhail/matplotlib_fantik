from config import *
import pandas as pd
from Promotion.currency_converter import get_exchange, usd_converter


def get_all_ios_purchases_by_country(date_from, date_to, package_name, conn):
    select_all_purchases = f"""select case
               when tu.country_iso = 'AT' then 'Austria'
               when tu.country_iso = 'DE' then 'Germany'
               when tu.country_iso = 'FR' then 'France'
               when tu.country_iso = 'PT' then 'Portugal'
               when tu.country_iso = 'GB' then 'Great Britain'
               when tu.country_iso = 'NO' then 'Norway'
               when tu.country_iso = 'AE' then 'United Arab Emirates'
               when tu.country_iso = 'IE' then 'Ireland'
               when tu.country_iso = 'BE' then 'Belgium'
               when tu.country_iso = 'NL' then 'Netherlands'
               when tu.country_iso = 'US' then 'USA'
               when tu.country_iso = 'IL' then 'Israel'
               end as country_iso,
           tcp.currency_iso,
           SUM(price) sum
    from tm_consumable_purchases tcp
             join tm_users tu on tcp.user_id = tu.user_id
    where transaction_date between '2024-12-31 23:59:59' AND '2025-01-31 23:59:59'
      and tcp.bundle_identifier = 'com.fametok.viral'
      and payment_status_id = 2
    --   and country_iso in ('AT', 'DE', 'FR', 'PT', 'GB', 'NO', 'AE')
    group by tu.country_iso, tcp.currency_iso
    order by sum desc"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue(date_from, date_to, package_name, conn):
    total_dict = {'Great Britain': 0, 'Germany': 0, 'France': 0, 'Austria': 0,
                  'Portugal': 0, 'Norway': 0, 'United Arab Emirates': 0}
    germany = 0
    great_britain = 0
    austria = 0
    france = 0
    portugal = 0
    norway = 0
    uae = 0
    ireland = 0
    belgium = 0
    netherlands = 0
    usa = 0
    israel = 0
    df_dict = get_all_ios_purchases_by_country(date_from=date_from,
                                               date_to=date_to,
                                               package_name=package_name,
                                               conn=conn).to_dict(orient='list')
    currency_lst = df_dict['currency_iso']
    all_sum_lst = df_dict['sum']
    all_country_lst = df_dict['country_iso']
    print(all_country_lst)
    print(currency_lst)
    print(all_sum_lst)
    new_list_of_tuples = []
    exchange_prices = []
    for i in range(len(currency_lst)):
        tmp_tuple = (currency_lst[i], all_sum_lst[i])
        new_list_of_tuples.append(tmp_tuple)
    for pair in new_list_of_tuples:
        price = get_exchange(usd_converter(*pair))
        price = round(price, 2)
        exchange_prices.append(price)
    print(exchange_prices)

    # for i in range(len(all_country_lst)):
    #     for key, value in total_dict.items():
    #         if key == all_country_lst[i]:
    #             print(all_country_lst[i])
    #             value += exchange_prices[i]
    #             print(exchange_prices[i])
    # print(total_dict)
    for i in range(len(all_country_lst)):
        if all_country_lst[i] == 'Germany':
            germany += exchange_prices[i]
        elif all_country_lst[i] == 'Great Britain':
            great_britain += exchange_prices[i]
        elif all_country_lst[i] == 'Austria':
            austria += exchange_prices[i]
        elif all_country_lst[i] == 'France':
            france += exchange_prices[i]
        elif all_country_lst[i] == 'Portugal':
            portugal += exchange_prices[i]
        elif all_country_lst[i] == 'Norway':
            norway += exchange_prices[i]
        elif all_country_lst[i] == 'United Arab Emirates':
            uae += exchange_prices[i]
        elif all_country_lst[i] == 'Ireland':
            ireland += exchange_prices[i]
        elif all_country_lst[i] == 'Belgium':
            belgium += exchange_prices[i]
        elif all_country_lst[i] == 'Netherlands':
            netherlands += exchange_prices[i]
        elif all_country_lst[i] == 'USA':
            usa += exchange_prices[i]
        elif all_country_lst[i] == 'Israel':
            israel += exchange_prices[i]
    # for i in range(len(all_country_lst)):
    #     if all_country_lst[i] == 'Germany':
    #         germany += exchange_prices[i]
    #     elif all_country_lst[i] == 'Great Britain':
    #         great_britain += exchange_prices[i]
    #     elif all_country_lst[i] == 'Austria':
    #         austria += exchange_prices[i]
    #     elif all_country_lst[i] == 'France':
    #         france += exchange_prices[i]
    #     elif all_country_lst[i] == 'Portugal':
    #         portugal += exchange_prices[i]
    #     elif all_country_lst[i] == 'Norway':
    #         norway += exchange_prices[i]
    #     elif all_country_lst[i] == 'United Arab Emirates':
    #         uae += exchange_prices[i]
    print(f" Germany - {germany}$\n Great Britain = {round(great_britain, 2)}$\n Austria - {austria}$\n France"
          f" - {france}$\n Portugal - {portugal}$\n Ireland - {ireland}\n Belgium - {belgium}\n"
          f" Netherlands - {netherlands}\n USA - {usa}\n Israel - {israel}")
    total = round(sum(exchange_prices), 2)
    print(f' Total amount: {total}$')
    # new_dict = {}United Arab Emirates
    # for i in range(len(all_country_lst)):
    #     new_dict[all_country_lst[i]] = currency_lst[i], all_sum_lst[i]
    # print(new_dict)
    # for key, value in new_dict.items():
    #     price = get_exchange(usd_converter(*value))
    #     price = round(float(price), 2)
    #     print(f'{key} - {price}$')
    #     total += price


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                package_name=PACKAGE_NAME_FAMETOK,
                conn=DB_PROD_CONNECTION)







