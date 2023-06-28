import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv("master.csv")

df['sum_year'] = df.groupby('year')['suicides/100k pop'].transform('sum')



#Количество случаев суицида за год

fig = px.bar(df,
              x="year",
              y="sum_year",
              labels = {'year':'Год'},
              color = "sum_year",
              title="Количество случаев суицида за год")
fig.update_traces(width=0.6)
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

df = df.drop(columns = {'country-year', 'HDI for year'})
df = df.rename(columns = {'gdp_per_capita ($)' : 'gdp_per_capita', 'gdp_for_year ($)' : 'gdp_for_year'})
print(df)



#Количество случаев суицида в зависимости от поколения

df_2 = df.groupby('generation').mean(numeric_only=True)

print(df_2)

fig_2 = px.bar(df_2,
              x=df_2.index,
              y="suicides/100k pop",
              labels = {'generation':'Поколение'},
              color = "suicides/100k pop",
              title="Количество случаев суицида за год")
fig_2.update_traces(width=0.6)
fig_2.update_layout(barmode='group', xaxis_tickangle=-45)
fig_2.show()



#Количество случаев суицида в зависимости от пола

df_3 = df.groupby('sex').mean(numeric_only = True)

print(df_3)

fig = px.bar(df_3,
              x= df_3.index,
              y="suicides/100k pop",
              labels = {'sex':'Пол'},
              color = "suicides/100k pop",
              title="Количество случаев суицида в зависимости от пола")
fig.update_traces(width=0.6)
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()



#Распределение случаев суицида в зависимости от пола в каждом году 

trend_sex = df.groupby(['year', 'sex']).agg(
    population=('population', 'sum'),
    suicides=('suicides_no', 'sum')
).reset_index()

trend_sex['suicides_per_100k'] = (trend_sex['suicides'] / trend_sex['population']) * 100000

fig, ax = plt.subplots()
colors = {'male': 'blue', 'female': 'red'}

for sex, data in trend_sex.groupby('sex'):
    ax.plot(data['year'], data['suicides_per_100k'], color=colors[sex], linewidth=1)
    ax.scatter(data['year'], data['suicides_per_100k'], color=colors[sex], s=25)

# Настройка осей и заголовка
ax.set_xlabel('Year')
ax.set_ylabel('suicides/100k pop')
ax.set_title('Trends Over Time, by Sex')

# Настройка легенды
ax.legend(['Male', 'Female'])

# Настройка интервала значений по оси x
ax.set_xticks(range(1985, 2016, 5))
ax.set_xlim(1985, 2015)



#Распределение случаев суицида в зависимости от пола в каждом году 

df_country = df
df_country["sum_count"] = df.groupby('country')['suicides/100k pop'].transform('sum')
df_country = df.groupby('country').mean(numeric_only = True)

fig = px.bar(df_country,
              x= "sum_count",
              y= df_country.index,
              orientation='h',
              labels = {'country':'Страна'},
              color = "sum_count",
              title="Количество случаев суицида в зависимости от страны")
fig.update_traces(width=0.6)
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()
