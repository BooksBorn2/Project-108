import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import scipy
df = pd.read_csv("P108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig.show()
