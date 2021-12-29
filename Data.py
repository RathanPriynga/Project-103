import pandas 
import plotly.express 
df = pandas.read_csv("line_chart.csv")
fig = plotly.express.scatter(df,x="date",y="cases",color="country",title='Covid-19 Cases')
fig.show()

