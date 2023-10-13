users_by_country = """select country_iso, count(*) cnt
from tm_users
where actual_date between '2023-09-30 23:59:59' AND '2023-10-31 23:59:59'
group by country_iso
order by cnt desc
limit 15"""

users_by_country_october = pd.read_sql(users_by_country, conn)

  
fig = plt.figure(figsize = (12, 8))
#plots = plt.bar(users_by_country_april['country_iso'], users_by_country_april['cnt'], color ='c', width = 0.8)
splot = sns.barplot(users_by_country_october, x='country_iso', y='cnt', color ='c', width = 0.8)
plt.bar_label(splot.containers[0],size=14)

top_countries_list = []
for i in users_by_country_october['country_iso']:
    for key, value in countries.items():
        if i == key:
            top_countries_list.append(value)
            
plt.xlabel("Country", fontsize=14, fontweight="bold")
plt.ylabel("Number of users", fontsize=14, fontweight="bold")
plt.title("Top 15 countries, October", fontsize=14, fontweight="bold")
plt.grid(True)
plt.legend(
    loc = 'upper right', labels = top_countries_list, prop = {'weight':'bold'}
)