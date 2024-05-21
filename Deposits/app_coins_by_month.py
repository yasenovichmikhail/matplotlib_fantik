from config import *


def app_coins_month(app_deposit_month, text_value):
    explode = []
    total_app_deposits_month = app_deposit_month['amount'].sum()
    text_kwargs = dict(ha='right', va='center', fontsize=12, fontweight='bold')

    for i in range(len(app_deposit_month)):
        explode.append(0.05)

    app_deposit_month['amount'].plot(
        kind='pie',
        labels=app_deposit_month['amount'],
        textprops={"fontweight": "bold", "fontsize": "12"},
        shadow='true',
        autopct='%1.1f%%',
        cmap='Set3',
        figsize=(12, 8),
        explode=explode,
        startangle=45
    )
    plt.ylabel("%", fontsize=20, fontweight="bold")
    plt.legend(
        loc='upper right',
        labels=app_deposit_month['app_name'],
        prop={'weight': 'bold'}
    )
    plt.text(-1.5, -1.1, f'Total {text_value}: {total_app_deposits_month}', **text_kwargs)
    plt.show()


app_coins = pd.read_sql(SELECT_APP_COINS_MONTH, CONN)
app_coins_month(app_coins, 'coins')
# print(app_coins)