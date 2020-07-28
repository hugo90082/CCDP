from django.shortcuts import render
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from django.db import connection
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest
from EDA.models import EDAData

## 底下為錯誤代碼處理方式 可以導到特定頁面
def page_not_found(request, *args, **kwargs):
    return HttpResponseNotFound(render_to_string('interactivePlot.html', request=request))

def forbidden(request, *args, **kwargs):
    return HttpResponseForbidden(render_to_string('interactivePlot.html', request=request))

def server_error(request, *args, **kwargs):
    return HttpResponseServerError(render_to_string('interactivePlot.html', request=request))

def bad_request(request, *args, **kwargs):
    return HttpResponseBadRequest(render_to_string('interactivePlot.html', request=request))
## 以上為錯誤代碼處理方式

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

    def genderCD4():
        genderDataFrame = pd.DataFrame()

        gender = []
        count = []
        genderCD4 = []


        for j in range(6):
            gender.append("gender0")
            gender0 = EDAData.objects.values_list('gender').filter(gender='0', CDLabel4Month=j).count()
            count.append(gender0)
            genderCD4.append(j)

            gender.append("gender1")
            gender1 = EDAData.objects.values_list('gender').filter(gender='1', CDLabel4Month=j).count()
            count.append(gender1)
            genderCD4.append(j)

        genderDataFrame["gender"] = gender
        genderDataFrame["count"] = count
        genderDataFrame["genderCD4"] = genderCD4
        
        fig = px.bar(genderDataFrame, x="gender", y="count", color="genderCD4", barmode="group", title='CD4性別分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def jobCD4():
        jobDataFrame = pd.DataFrame()
        job = []
        count = []
        jobCD4 = []

        for j in range(6):
            job.append("job1")
            job1 = EDAData.objects.values_list('job1').filter(job1='1', CDLabel4Month=j).count()
            count.append(job1)
            jobCD4.append(j)

            job.append("job2")
            job2 = EDAData.objects.values_list('job2').filter(job2='1', CDLabel4Month=j).count()
            count.append(job2)
            jobCD4.append(j)

            job.append("job3")
            job3 = EDAData.objects.values_list('job3').filter(job3='1', CDLabel4Month=j).count()
            count.append(job3)
            jobCD4.append(j)

            job.append("job4")
            job4 = EDAData.objects.values_list('job4').filter(job4='1', CDLabel4Month=j).count()
            count.append(job4)
            jobCD4.append(j)

        jobDataFrame["job"] = job
        jobDataFrame["count"] = count
        jobDataFrame["jobCD4"] = jobCD4

        fig = px.bar(jobDataFrame, x="job", y="count", color="jobCD4", barmode="group", title='CD4職業分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def industryCD4():
        industryDataFrame = pd.DataFrame()
        industry = []
        count = []
        industryCD4 = []

        for j in range(6):
            industry.append("industry1")
            industry1 = EDAData.objects.values_list('industry1').filter(industry1='1', CDLabel4Month=j).count()
            count.append(industry1)
            industryCD4.append(j)

            industry.append("industry2")
            industry2 = EDAData.objects.values_list('industry2').filter(industry2='1', CDLabel4Month=j).count()
            count.append(industry2)
            industryCD4.append(j)

            industry.append("industry3")
            industry3 = EDAData.objects.values_list('industry3').filter(industry3='1', CDLabel4Month=j).count()
            count.append(industry3)
            industryCD4.append(j)

            industry.append("industry4")
            industry4 = EDAData.objects.values_list('industry4').filter(industry4='1', CDLabel4Month=j).count()
            count.append(industry4)
            industryCD4.append(j)

            industry.append("industry5")
            industry5 = EDAData.objects.values_list('industry5').filter(industry5='1', CDLabel4Month=j).count()
            count.append(industry5)
            industryCD4.append(j)

        industryDataFrame["industry"] = industry
        industryDataFrame["count"] = count
        industryDataFrame["industryCD4"] = industryCD4

        fig = px.bar(industryDataFrame, x="industry", y="count", color="industryCD4", barmode="group", title='CD4產業分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def eduCD4():
        eduDataFrame = pd.DataFrame()
        edu = []
        count = []
        eduCD4 = []

        for j in range(6):
            edu.append("edu0")
            edu1 = EDAData.objects.values_list('edu').filter(edu='0', CDLabel4Month=j).count()
            count.append(edu1)
            eduCD4.append(j)

            edu.append("edu2")
            edu2 = EDAData.objects.values_list('edu').filter(edu='2', CDLabel4Month=j).count()
            count.append(edu2)
            eduCD4.append(j)

            edu.append("edu2.5")
            edu3 = EDAData.objects.values_list('edu').filter(edu='2.5', CDLabel4Month=j).count()
            count.append(edu3)
            eduCD4.append(j)

            edu.append("edu3")
            edu4 = EDAData.objects.values_list('edu').filter(edu='3', CDLabel4Month=j).count()
            count.append(edu4)
            eduCD4.append(j)

            edu.append("edu4")
            edu5 = EDAData.objects.values_list('edu').filter(edu='4', CDLabel4Month=j).count()
            count.append(edu5)
            eduCD4.append(j)

        eduDataFrame["edu"] = edu
        eduDataFrame["count"] = count
        eduDataFrame["eduCD4"] = eduCD4

        fig = px.bar(eduDataFrame, x="edu", y="count", color="eduCD4", barmode="group", title='CD4教育程度分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def homeOwnershipCD4():
        homeOwnershipDataFrame = pd.DataFrame()

        homeOwnership = []
        count = []
        homeOwnershipCD4 = []

        for j in range(6):

            homeOwnership.append("homeOwnership1")
            homeOwnership1 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='1', CDLabel4Month=j).count()
            count.append(homeOwnership1)
            homeOwnershipCD4.append(j)

            homeOwnership.append("homeOwnership2")
            homeOwnership2 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='2', CDLabel4Month=j).count()
            count.append(homeOwnership2)
            homeOwnershipCD4.append(j)

            homeOwnership.append("homeOwnership6")
            homeOwnership3 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='6', CDLabel4Month=j).count()
            count.append(homeOwnership3)
            homeOwnershipCD4.append(j)

            homeOwnership.append("homeOwnership8")
            homeOwnership4 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='8', CDLabel4Month=j).count()
            count.append(homeOwnership4)
            homeOwnershipCD4.append(j)

            homeOwnership.append("homeOwnership9")
            homeOwnership5 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='9', CDLabel4Month=j).count()
            count.append(homeOwnership5)
            homeOwnershipCD4.append(j)

            homeOwnership.append("homeOwnership10")
            homeOwnership6 = EDAData.objects.values_list('homeOwnership').filter(homeOwnership='10', CDLabel4Month=j).count()
            count.append(homeOwnership6)
            homeOwnershipCD4.append(j)

        homeOwnershipDataFrame["homeOwnership"] = homeOwnership
        homeOwnershipDataFrame["count"] = count
        homeOwnershipDataFrame["homeOwnershipCD4"] = homeOwnershipCD4

        fig = px.bar(homeOwnershipDataFrame, x="homeOwnership", y="count", color="homeOwnershipCD4", barmode="group", title='CD4住房狀況分布圖')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'ageCD4': ageCD4(),
        'genderCD4': genderCD4(),
        'jobCD4': jobCD4(),
        'industryCD4': industryCD4(),
        'eduCD4': eduCD4(),
        'homeOwnershipCD4': homeOwnershipCD4(),
    }
    return render(request, 'basicStatistic.html', context)

def ourModel(request):
    def correlationHeatmap():

        df = pd.read_csv('correlation_matrix.csv')
        df=pd.DataFrame(df)
        feature=df["features"]
        fig = px.imshow(df,y=feature.values.tolist(), labels=dict(x="features", y="features", color="Person Correlation"), title='相關係數矩陣')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    def significantHistogram():

        df = pd.read_csv('significant_feature.csv')
        fig = px.histogram(df,x="Features", y="Significant", color="Date", marginal="rug",labels=dict(x="Features", y="Significant", color="Date"), title='顯著變數')
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'correlationHeatmap': correlationHeatmap(),
        'significantHistogram': significantHistogram(),
    }
    return render(request, 'ourModel.html', context)