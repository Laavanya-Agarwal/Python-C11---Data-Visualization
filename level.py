import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv('data.csv')
# print(df)
studentdf = df.groupby('level')['attempt'].mean()
print(studentdf)

# horizontal 
fig = go.Figure(go.Bar(
    x = studentdf, y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation = 'h'
))
fig.show()
# vertical
fig2 = go.Figure(go.Bar(
    x = ['Level 1', 'Level 2', 'Level 3', 'Level 4'], y = studentdf, orientation = 'v'
))
fig2.show()