from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views import generic
#from django.conf.urls import handler404, handler500, handler403, handler400


#def error_404(request, exception):
#   context = {}
#   return render(request,'errors/four.html', context)




def handler500(request):
   return render(request, 'errors/four.html', status=500)