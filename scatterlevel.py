import plotly.express as px
import pandas as pd
import csv

df = pd.read_csv("data.csv")
studentdf = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(studentdf, x="student_id", y="level", size="attempt", color="attempt")
fig.show()