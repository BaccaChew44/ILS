from django.urls import path
from . import views

app_name = 'ILSA'
urlpatterns =[
    path('', views.HomepageView, name='home page'),
    path('lockers/', views.LockersView, name='lockers'),
    path('swipe', views.swipe, name='swipe')
]