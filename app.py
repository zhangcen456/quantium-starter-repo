from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app=Dash()

df=pd.read_csv("./data/processed.csv")
df['sales']=df['sales'].str.replace("$","",regex=False)
df['sales']=pd.to_numeric(df['sales'])
df['date']=pd.to_datetime(df['date'])

app.layout=[
    html.H1("Sales for pink morsels"),
    dcc.Graph(figure=px.line(df,x='date',y='sales',line_group='region',color='region'))
]

if __name__=="__main__":
    app.run(debug=True)