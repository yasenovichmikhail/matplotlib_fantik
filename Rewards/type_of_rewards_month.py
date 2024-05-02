from config import *


def type_of_rewards(reward_type_month):
    explode = []
    total_rewards_month = reward_type_month['amount'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(reward_type_month)):
        explode.append(0.05)

    reward_type_month['amount'].plot(
        kind='pie', labels=reward_type_month['reward_type'],
        textprops={"fontweight": "bold", "fontsize": "12"},
        shadow='true', autopct='%1.1f%%',
        cmap='Set3', figsize=(12, 8), explode=explode
    )
    plt.ylabel("%", fontsize=20, fontweight="bold")
    plt.legend(
        loc='upper right', labels=reward_type_month['amount'], prop={'weight': 'bold'}
    )
    plt.text(1.2, -1.2, f'Total rewards: {total_rewards_month}', **text_kwargs)
    plt.show()


df_type_of_reward = pd.read_sql(SELECT_TYPE_REWARDS, CONN)
type_of_rewards(df_type_of_reward)
