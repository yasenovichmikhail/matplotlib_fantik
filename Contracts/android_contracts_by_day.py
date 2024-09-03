from config import *


def get_android_contracts_per_day(product_id, price):
    select_android_contracts_by_day = f"""with dates as (
        SELECT *
        FROM generate_series('{GENERATE_DATE1}'::timestamp,
                             '{GENERATE_DATE2}'::timestamp, '1 day') as date
    ),
         contracts as (
             SELECT tuc.create_date::date
             FROM tm_user_contracts tuc
                      join tm_subscription ts on ts.subscription_id = tuc.subscription_id
             where tuc.period_end_date::date - tuc.create_date::date > 3
               and ts.subscription_product_id = {product_id}
         )

    select dates.date, count(contracts.create_date) cnt
    from dates
             left join contracts on contracts.create_date = dates.date
    group by dates.date
    order by dates.date """
    df_android_contracts_by_day = pd.read_sql(select_android_contracts_by_day, CONN)
    contracts_by_day(df_android_contracts_by_day, price)


if __name__ == '__main__':
    get_android_contracts_per_day(product_id=FANTIK_ANDROID_PRODUCT_ID,
                                  price=CONTRACTS_PRICE_FANTIK)

