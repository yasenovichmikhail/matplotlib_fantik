from config import *


def apps_promotion(data_frame):
    text_kwargs = dict(ha='center', va='center', fontsize=12, fontweight='bold')
    fig, ax = plt.subplots(figsize=(14, 10), layout='constrained')
    splot = sns.barplot(data_frame, x='app_name', y='amount', color='c', width=0.5)
    plt.bar_label(splot.containers[0], size=12, fontweight="bold")
    plt.ylabel("Log In", **text_kwargs)
    plt.xlabel("App name", **text_kwargs)
    plt.title("Apps promotion", **text_kwargs)
    plt.grid(True)
    plt.show()


df_apps_promotion = pd.read_sql(SELECT_APP_PROMOTION, CONN)
apps_promotion(df_apps_promotion)
