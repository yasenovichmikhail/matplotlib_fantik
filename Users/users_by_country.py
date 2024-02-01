from main_import import *

def users_by_country_month(users_country_month, users_top_country_month):
    fig = plt.figure(figsize = (12, 8))
    #plots = plt.bar(users_by_country_april['country_iso'], users_by_country_april['cnt'], color ='c', width = 0.8)
    splot = sns.barplot(users_top_country_month, x='country_iso', y='cnt', color ='c', width = 0.8)
    plt.bar_label(splot.containers[0],size=14)
    total_users = users_country_month['cnt'].sum()

    top_countries_list = []
    for i in users_top_country_month['country_iso']:
        for key, value in countries.items():
            if i == key:
                top_countries_list.append(value)
            
    plt.xlabel("Country", fontsize=14, fontweight="bold")
    plt.ylabel("Number of users", fontsize=14, fontweight="bold")
    plt.title("Top 15 countries", fontsize=14, fontweight="bold")
    plt.grid(True)
    plt.legend(
        loc = 'upper right', labels = top_countries_list, prop = {'weight':'bold'}
    )
    plt.show()

users_by_country_top =  """select country_iso, count(*) cnt
    from tm_users
    where actual_date between '2023-12-31 23:59:59' AND '2024-01-31 23:59:59'
    group by country_iso
    order by cnt desc
    limit 15"""

users_by_country =  """select country_iso, count(*) cnt
    from tm_users
    where actual_date between '2023-12-31 23:59:59' AND '2024-01-31 23:59:59'
    group by country_iso
    order by cnt desc"""

users_by_country_top_january = pd.read_sql(users_by_country_top, conn)
users_by_country_january = pd.read_sql(users_by_country, conn)
  
users_by_country_month(users_by_country_january, users_by_country_top_january)