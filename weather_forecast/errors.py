from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views import generic
#from django.conf.urls import handler404, handler500, handler403, handler400
from django.core.exceptions import BadRequest
import functools
from django.http import HttpResponseNotFound
def er(request,exception):
    return HttpResponseNotFound(request,'errors/four.html')