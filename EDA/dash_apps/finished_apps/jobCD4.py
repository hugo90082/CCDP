from EDA.models import EDAData
import plotly.express as px
import pandas as pd
from django.db import connection
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

jobDataFrame = pd.DataFrame()
with connection.cursor() as cursor:
    cursor.execute('SELECT date FROM EDAData GROUP by date')
    dataDate = cursor.fetchall()
date = []
job = []
count = []
jobCD4 = []

for i in range(len(dataDate)):
    for j in range(6):
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        date.append(dataDate[i][0])
        job.append("job1")
        job1 = EDAData.objects.values_list('job1').filter(date=dataDate[i][0], job1='1', CDLabel4Month=j).count()
        count.append(job1)
        jobCD4.append(j)

        job.append("job2")
        job2 = EDAData.objects.values_list('job2').filter(date=dataDate[i][0], job2='1', CDLabel4Month=j).count()
        count.append(job2)
        jobCD4.append(j)

        job.append("job3")
        job3 = EDAData.objects.values_list('job3').filter(date=dataDate[i][0], job3='1', CDLabel4Month=j).count()
        count.append(job3)
        jobCD4.append(j)

        job.append("job4")
        job4 = EDAData.objects.values_list('job4').filter(date=dataDate[i][0], job4='1', CDLabel4Month=j).count()
        count.append(job4)
        jobCD4.append(j)

jobDataFrame["date"] = date
jobDataFrame["job"] = job
jobDataFrame["count"] = count
jobDataFrame["jobCD4"] = jobCD4

# print(jobDataFrame)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('jobCD4', external_stylesheets=external_stylesheets)

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

    filtered_df = jobDataFrame[jobDataFrame.date==dataDate[selected_date][0]]

    fig = px.bar(filtered_df, x="job", y="count", color="jobCD4", barmode="group", title=dataDate[selected_date][0]+'：CD4職業分布圖')

    fig.update_layout(transition_duration=100)
    

    return fig