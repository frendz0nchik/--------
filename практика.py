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

