from config import *
import pandas as pd


def select_all_orders_id(action_type, action_amount, limit, conn=DB_PROD_CONNECTION):
    select_all_orders = f"""
        select order_id
        from tm_user_orders
        where action_type_id = {action_type}
            and order_status_id = 2
            and actions_amount = {action_amount}
        order by order_id desc
        limit {limit};
    """

    try:
        result = pd.read_sql(select_all_orders, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_order_id(action_type, action_amount, limit, conn):
    order_list = []
    orders_dict = select_all_orders_id(action_type=action_type,
                                       action_amount=action_amount,
                                       limit=limit,
                                       conn=conn).to_dict()
    orders = orders_dict['order_id']
    for key, value in orders.items():
        order_list.append(value)
    return order_list


def fetch_metrics_before(order_id, conn=DB_PROD_CONNECTION):
    select_metrics_before = f"""
        select metrics_amount_before
        from tm_order_actions
        where order_id = {order_id}
            and is_success = 'true'
            and metrics_amount_before != '-1'
            and metrics_amount_before != '-2'
        order by start_date
        limit 1
    """
    df_metrics_before = pd.read_sql(select_metrics_before, conn)
    return int(df_metrics_before.iloc[0]['metrics_amount_before'])


def fetch_metrics_after(order_id, conn=DB_PROD_CONNECTION):
    select_metrics_after = f"""
        select metrics_amount_after
        from tm_order_actions
        where order_id = {order_id}
            and is_success = 'true'
            and metrics_amount_after != '-1'
            and metrics_amount_after != '-2'
        order by start_date desc
        limit 1
    """
    df_metrics_after = pd.read_sql(select_metrics_after, conn)
    return int(df_metrics_after.iloc[0]['metrics_amount_after'])


def get_difference(metrics_before, metrics_after):
    diff = metrics_after - metrics_before
    return diff


def calculate_execution_percent(diff, action_amount):
    execution_percent = (diff / action_amount) * 100
    return round(float(execution_percent), 2)


def main(action_type, action_amount, limit, conn):
    percent_list = []
    all_orders_id = get_all_order_id(action_type=action_type,
                                     action_amount=action_amount,
                                     limit=limit,
                                     conn=conn)
    for order_id in all_orders_id:
        diff = get_difference(metrics_before=fetch_metrics_before(order_id=order_id,
                                                                  conn=conn),
                              metrics_after=fetch_metrics_after(order_id=order_id,
                                                                conn=conn))
        execution_percent = calculate_execution_percent(diff=diff,
                                                        action_amount=action_amount)
        percent_list.append(execution_percent)
        print(f'order_id: {order_id}: ordered - {action_amount}, completed - {diff}. '
              f'The execution percent is {execution_percent}%')
    average_percent = sum(percent_list) / len(percent_list)
    print(f'The average percent is {round(average_percent, 2)}')


if __name__ == '__main__':
    main(action_type=1,
         action_amount=200,
         limit=50,
         conn=DB_PROD_CONNECTION)
