from sqlalchemy import text
from config import *
import pandas as pd
from Deposits.type_of_deposit_by_month import type_of_deposits


def get_tiktok_users(date_from, date_to, conn):
    select_purchase_tiktok_users = f"""select t.hearts_count, count(*)
        from tm_consumable_purchases tcp
         join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
        where transaction_date between '{date_from}' and '{date_to}'
          and tcp.user_id in (select user_id
                      from tm_logons
                      where install_referrer
                          like '%%20set%%'
                        and package_name = 'com.tikboost.fantik')
        and payment_status_id = 2
        group by t.hearts_count
        order by t.hearts_count;"""

    get_all_tiktok_users = f"""select user_id
        from tm_logons
        where install_referrer
        like '%%ref=tiktok%%'
        order by logon_date desc;"""

    try:
        result = pd.read_sql(select_purchase_tiktok_users, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def main(date1, date2, conn):
    type_of_deposits(get_tiktok_users(date1, date2, conn))


if __name__ == '__main__':
    main(DATE1, DATE2, DB_PROD_CONNECTION)
