from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plotly.offline import iplot
import plotly.figure_factory as ff

# Create your views here.
def hello_view(request):
    gender = ["gender0","gender1"]
    gender_df = pd.DataFrame()
    count =[]
    gender0 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count()
    gender1 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count()
    count.append(gender0)
    count.append(gender1)
    gender_df["gender"]=gender
    gender_df["count"]=count
    

    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
        'current_time': str(datetime.now()),
        'gender0': gender_df,
        # 'gender0': EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count(),
        # 'gender1': EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count(),
        # 'check_list': EDAData.objects.values_list('date', 'number', 'gender', 'age', 'edu', 'homeOwnership', 'job1', 'job2', 'job3', 'job4', 'industry1', 'industry2', 'industry3', 'industry4', 'industry5', 'CDLabel4Month').filter(date='2018/10/31'),
    })

def show(request):
    def scatter():
        # gender = []
        # gender0 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count()
        # gender1 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count()
        # gender.append(gender0)
        # gender.append(gender1)

        # gender = pd.DataFrame(gender)

        # x1 = [1,2,3,4]['性別', '數量']
        # y1 = [30, 35, 25, 45]

        # trace = go.Scatter(
        #     x=x1,
        #     y = y1
        # )
        # layout = dict(
        #     title='Simple Graph',
        #     xaxis=dict(range=[min(x1), max(x1)]),
        #     yaxis = dict(range=[min(y1), max(y1)])
        # )

        gender = ["gender0","gender1"]
        gender_df = pd.DataFrame()
        count =[]
        gender0 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='0').count()
        gender1 = EDAData.objects.values_list('gender').filter(date='2018/10/31', gender='1').count()
        count.append(gender0)
        count.append(gender1)
        gender_df["gender"]=gender
        gender_df["count"]=count

        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[0, 1]),
            yaxis = dict(range=[min(count), max(count)])
        )


        fig = px.bar(gender_df, x="gender", y="count")
        #return fig.show()
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'welcome.html', context)