from EDA.models import EDAData
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

eduDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()
date = []
edu = []
count = []
eduCD4 = []

for i in range(len(dataDate)):
    for j in range(6):
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        edu.append("edu0")
        edu1 = EDAData.objects.values_list('edu').filter(date=dataDate[i][0], edu='0', CDLabel4Month=j).count()
        count.append(edu1)
        eduCD4.append(j)

        edu.append("edu2")
        edu2 = EDAData.objects.values_list('edu').filter(date=dataDate[i][0], edu='2', CDLabel4Month=j).count()
        count.append(edu2)
        eduCD4.append(j)

        edu.append("edu2.5")
        edu3 = EDAData.objects.values_list('edu').filter(date=dataDate[i][0], edu='2.5', CDLabel4Month=j).count()
        count.append(edu3)
        eduCD4.append(j)

        edu.append("edu3")
        edu4 = EDAData.objects.values_list('edu').filter(date=dataDate[i][0], edu='3', CDLabel4Month=j).count()
        count.append(edu4)
        eduCD4.append(j)

        edu.append("edu4")
        edu5 = EDAData.objects.values_list('edu').filter(date=dataDate[i][0], edu='4', CDLabel4Month=j).count()
        count.append(edu5)
        eduCD4.append(j)

eduDataFrame["date"] = date
eduDataFrame["edu"] = edu
eduDataFrame["count"] = count
eduDataFrame["eduCD4"] = eduCD4

# print(eduDataFrame)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('eduCD4', external_stylesheets=external_stylesheets)

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

    filtered_df = eduDataFrame[eduDataFrame.date==dataDate[selected_date][0]]

    fig = px.bar(filtered_df, x="edu", y="count", color="eduCD4", barmode="group", title=dataDate[selected_date][0]+'：CD4教育程度分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig