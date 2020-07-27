from EDA.models import EDAData
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

industryDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()
date = []
industry = []
count = []
industryCD4 = []

for i in range(len(dataDate)):
    for j in range(6):
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        industry.append("industry1")
        industry1 = EDAData.objects.values_list('industry1').filter(date=dataDate[i][0], industry1='1', CDLabel4Month=j).count()
        count.append(industry1)
        industryCD4.append(j)

        industry.append("industry2")
        industry2 = EDAData.objects.values_list('industry2').filter(date=dataDate[i][0], industry2='1', CDLabel4Month=j).count()
        count.append(industry2)
        industryCD4.append(j)

        industry.append("industry3")
        industry3 = EDAData.objects.values_list('industry3').filter(date=dataDate[i][0], industry3='1', CDLabel4Month=j).count()
        count.append(industry3)
        industryCD4.append(j)

        industry.append("industry4")
        industry4 = EDAData.objects.values_list('industry4').filter(date=dataDate[i][0], industry4='1', CDLabel4Month=j).count()
        count.append(industry4)
        industryCD4.append(j)

        industry.append("industry5")
        industry5 = EDAData.objects.values_list('industry5').filter(date=dataDate[i][0], industry5='1', CDLabel4Month=j).count()
        count.append(industry5)
        industryCD4.append(j)

industryDataFrame["date"] = date
industryDataFrame["industry"] = industry
industryDataFrame["count"] = count
industryDataFrame["industryCD4"] = industryCD4

# print(industryDataFrame)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('industryCD4', external_stylesheets=external_stylesheets)

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

    filtered_df = industryDataFrame[industryDataFrame.date==dataDate[selected_date][0]]

    fig = px.bar(filtered_df, x="industry", y="count", color="industryCD4", barmode="group", title=dataDate[selected_date][0]+'：CD4產業分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig