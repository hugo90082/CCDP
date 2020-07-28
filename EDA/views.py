from django.shortcuts import render
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from django.db import connection

def interactivePlot(request):
    return render(request, 'interactivePlot.html')

def basicStatistic(request):
    def ageCD4():

        ageDataFrame = pd.DataFrame()
        with connection.cursor() as cursor:
            cursor.execute('SELECT date,age,CDLabel4Month FROM EDAData')
            dataDate = cursor.fetchall()
        
        date = []
        age = []
        CD4Label = []
        count = []

        for i in range(len(dataDate)):
            date.append(dataDate[i][0])
            age.append(dataDate[i][1])
            CD4Label.append(dataDate[i][2])
            count.append(1)

        ageDataFrame["date"] = date
        ageDataFrame["age"] = age
        ageDataFrame["CD4Label"] = CD4Label
        ageDataFrame["count"] = count

        fig = px.histogram(ageDataFrame, x="age", y="count", color="CD4Label", marginal="rug",
                   hover_data=ageDataFrame.columns, barmode="group", title='CD4年齡分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'ageCD4': ageCD4()
    }
    return render(request, 'basicStatistic.html', context)

def ourModel(request):    
    return render(request, 'ourModel.html')