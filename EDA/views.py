from django.shortcuts import render

def show(request):    
    return render(request, 'welcome.html')

def showTable(request):    
    return render(request, 'tables.html')