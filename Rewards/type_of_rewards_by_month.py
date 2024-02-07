from main_import import *

def type_of_reward(reward_type_month):
    explode = []
    total_rewards_month = reward_type_month['amount'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(reward_type_month)):
        explode.append(0.05)
    
    reward_type_month['amount'].plot(
        kind='pie', labels=reward_type_month['reward_type'], textprops = {"fontweight":"bold", "fontsize":"12"}, shadow = 'true', autopct='%1.1f%%',
        cmap='Set3', figsize=(12,8), explode=explode
    )
    plt.ylabel("%", fontsize=20, fontweight="bold")
    plt.legend(
        loc = 'upper right', labels = reward_type_month['amount'], prop = {'weight':'bold'}
    )
    plt.text(-0.8, -1.1, f'Total rewards: {total_rewards_month}', **text_kwargs)
    plt.show()

select_type_rewards = """select case
               when reward_id = 1 then 'Hearts'
               when reward_id = 2 then 'Boost x2'
               when reward_id = 3 then 'Bonus discount'
               when reward_id = 4 then 'View'
               end  reward_type,
           count(*) amount
    from tm_user_rewards
    where actual_date between '2023-12-31 23:59:59' AND '2024-01-31 23:59:59'
    group by reward_id
    order by reward_id asc"""

type_of_reward_january = pd.read_sql(select_type_rewards, conn)
type_of_reward(type_of_reward_january)