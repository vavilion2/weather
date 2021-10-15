from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views import generic
#from django.conf.urls import handler404, handler500, handler403, handler400


def er(request,exception):
    return render(request,'errors/four.html')