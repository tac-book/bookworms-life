# Create your views here.
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'apps/index.html')

def rank2012(request):
   return render(request, 'apps/rank2012.html')
