from EDA.models import EDAData
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

genderDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()
date = []
gender = []
count = []
genderCD4 = []

for i in range(len(dataDate)):
    for j in range(6):
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        gender.append("gender0")
        gender0 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='0', CDLabel4Month=j).count()
        count.append(gender0)
        genderCD4.append(j)

        gender.append("gender1")
        gender1 = EDAData.objects.values_list('gender').filter(date=dataDate[i][0], gender='1', CDLabel4Month=j).count()
        
        count.append(gender1)
        genderCD4.append(j)

genderDataFrame["date"] = date
genderDataFrame["gender"] = gender
genderDataFrame["count"] = count
genderDataFrame["genderCD4"] = genderCD4

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('genderCD4', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='date-slider',
        min =0,
        max=len(dataDate)-1,
        marks={i: dataDate[i][0] for i in range(len(dataDate))},
        value=0,
        
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('date-slider', 'value')])

def update_figure(selected_date):
    newdate=dataDate[selected_date][0]
    filtered_df = genderDataFrame[genderDataFrame.date==newdate]

    fig = px.bar(filtered_df, x="gender", y="count", color="genderCD4", barmode="group", title=newdate+'：CD4性別分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig