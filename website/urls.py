from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='/'),
    path('courses/bfsi/',views.bfsi,name='bfsi'),
    path('courses/cpp/', views.cpp_view, name='cpp'),
    path('courses/java/', views.java, name='java'),
    path('courses/python/', views.python, name='python'),
    path('courses/web/', views.web, name='web'),
    path('courses/mern/', views.mern, name='mern'),
    path('courses/mobile/', views.mob, name='mob'),
    path('courses/react/', views.react, name='react'),
    path('courses/sql/', views.sql, name='sql'),
    path('courses/ecom/', views.ecom, name='ecom'),
    path('courses/dm/', views.dm, name='dm'),
    path('courses/report/', views.report, name='report'),
     path('courses/crm/', views.custom, name='custom'),
     path('courses/business/', views.business, name='business'),
path('courses/tax/', views.tax, name='tax'),
]
