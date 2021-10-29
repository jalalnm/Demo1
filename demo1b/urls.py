from django.urls import path
from . import views
urlpatterns=[
    path('demo1ab',views.ntrends,name='demo1ab'),
    path('pag1',views.page1,name='pag1')

]