from EDA.models import EDAData
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

homeOwnershipDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()
date = []
homeOwnership = []
count = []
homeOwnershipCD4 = []

for i in range(len(dataDate)):
    for j in range(6):
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])

        homeOwnership.append("homeOwnership1")
        homeOwnership1 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='1', CDLabel4Month=j).count()
        count.append(homeOwnership1)
        homeOwnershipCD4.append(j)

        homeOwnership.append("homeOwnership2")
        homeOwnership2 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='2', CDLabel4Month=j).count()
        count.append(homeOwnership2)
        homeOwnershipCD4.append(j)

        homeOwnership.append("homeOwnership6")
        homeOwnership3 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='6', CDLabel4Month=j).count()
        count.append(homeOwnership3)
        homeOwnershipCD4.append(j)

        homeOwnership.append("homeOwnership8")
        homeOwnership4 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='8', CDLabel4Month=j).count()
        count.append(homeOwnership4)
        homeOwnershipCD4.append(j)

        homeOwnership.append("homeOwnership9")
        homeOwnership5 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='9', CDLabel4Month=j).count()
        count.append(homeOwnership5)
        homeOwnershipCD4.append(j)

        homeOwnership.append("homeOwnership10")
        homeOwnership6 = EDAData.objects.values_list('homeOwnership').filter(date=dataDate[i][0], homeOwnership='10', CDLabel4Month=j).count()
        count.append(homeOwnership6)
        homeOwnershipCD4.append(j)

homeOwnershipDataFrame["date"] = date
homeOwnershipDataFrame["homeOwnership"] = homeOwnership
homeOwnershipDataFrame["count"] = count
homeOwnershipDataFrame["homeOwnershipCD4"] = homeOwnershipCD4

# print(homeOwnershipDataFrame)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('homeOwnershipCD4', external_stylesheets=external_stylesheets)

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

    filtered_df = homeOwnershipDataFrame[homeOwnershipDataFrame.date==dataDate[selected_date][0]]

    fig = px.bar(filtered_df, x="homeOwnership", y="count", color="homeOwnershipCD4", barmode="group", title=dataDate[selected_date][0]+'：CD4住房狀況分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig