from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def i_topic(request):
    tn=input('enter topic ')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted')
def i_webpage(request):
    tn=input('enter topic ')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=WebPage.objects.get_or_create(Topic_name=TO,Name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage done')
def i_acr(request):
    tn=input('enter topic')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=WebPage.objects.get_or_create(Topic_name=TO,Name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    AC=AccessRecords.objects.get_or_create(Name=WO,date=d,author=a)[0]
    AC.save()
    return HttpResponse('RECORDS DONE:)')