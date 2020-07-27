import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from EDA.models import EDAData
from django.db import connection
import pandas as pd
import plotly.express as px
from plotly.offline import plot

with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1(dataDate[3][0], style={'margin-top': 10}),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: dataDate[i][0] for i in range(len(dataDate))},
        max=len(dataDate)-1,
        value=0,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):

    genderDataFrame = pd.DataFrame()
    with connection.cursor() as cursor:
        cursor.execute('SELECT date FROM EDAData GROUP by date')
        dataDate = cursor.fetchall()
    date = []
    gender = []
    count = []
    genderCD4 = []

    for j in range(6):
        date.append(dataDate[value][0])
        date.append(dataDate[value][0])
        gender.append("gender0")
        gender0 = EDAData.objects.values_list('gender').filter(date=dataDate[value][0], gender='0', CDLabel4Month=j).count()
        count.append(gender0)
        genderCD4.append(j)

        gender.append("gender1")
        gender1 = EDAData.objects.values_list('gender').filter(date=dataDate[value][0], gender='1', CDLabel4Month=j).count()
        count.append(gender1)
        genderCD4.append(j)


    genderDataFrame["date"] = date
    genderDataFrame["gender"] = gender
    genderDataFrame["count"] = count
    genderDataFrame["genderCD4"] = genderCD4

    fig = px.bar(genderDataFrame, x="gender", y="count", color="genderCD4", barmode="group", title=dataDate[value][0]+'CD4性別分布圖')

    return fig