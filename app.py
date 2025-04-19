from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app=Dash()

df=pd.read_csv("./data/processed.csv")
df['sales']=df['sales'].str.replace("$","",regex=False)
df['sales']=pd.to_numeric(df['sales'])
df['date']=pd.to_datetime(df['date'])

app.layout=[
    html.H1("Sales for pink morsels"),
    dcc.RadioItems(
        options=["north", "east", "south", "west", "all"],
        value="north",
        id="region-radio",
        inline=True,
        labelStyle={'padding-right':"10px"}
    ),
    dcc.Graph(id="graph")
]

color_discrete_sequence=["#7892B5","#FFC693","#97BDAC","#D98481"]

@callback(
    Output(component_id="graph",component_property="figure"),
    Input(component_id="region-radio",component_property="value")
)
def update_graph(selected_region):
    if(selected_region=='all'):
        fig=px.line(df,x='date',y='sales',line_group='region',color="region",color_discrete_sequence=color_discrete_sequence,title="Pink Morsel Sales")
    else:
        filtered_df=df[df['region']==selected_region]
        fig=px.line(filtered_df,x='date',y='sales',color_discrete_sequence=color_discrete_sequence,title="Pink Morsel Sales")
    return fig

if __name__=="__main__":
    app.run(debug=True)