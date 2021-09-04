import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv('data.csv')
# print(df)
studentdf = df.groupby('student_id')['attempt'].mean()
print(studentdf)

fig = go.Figure(go.Bar(
    x = ['TRL_123', 'TRL_987', 'TRL_abc', 'TRL_imb', 'TRL_mda', 'TRL_mno', 'TRL_rst', 'TRL_xsl', 'TRL_xyz', 'TRL_zet', 'TRL_zny'],
    y = studentdf,
    orientation = 'v'
))
fig.show()