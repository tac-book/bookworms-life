from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
   path('', views.index, name='index'),
   path('rank2012/', views.rank2012, name='rank2012'),
]
