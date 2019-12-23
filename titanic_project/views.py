from django.shortcuts import render
from . import test_model
from . import ML_model


def home(request):
    return render(request, 'index.html')

def result(request):
    pclass =  int(request.GET['pclass'])
    sex =  int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])

    prediction = ML_model.predict_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request, 'result.html', {'result': prediction})