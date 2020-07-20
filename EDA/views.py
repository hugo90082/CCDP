from django.shortcuts import render
from datetime import datetime
from EDA.models import EDAData

# Create your views here.
def hello_view(request):

    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
        'current_time': str(datetime.now()),
        'check': EDAData.objects.get(pk=10),
    })