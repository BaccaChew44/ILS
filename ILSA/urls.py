from django.urls import path
from . import views

app_name = 'ILSA'
urlpatterns =[
    path('', views.HomepageView, name='home page'),
    path('lockers/', views.LockersView, name='lockers'),
    path('swipe/<str:card_uid>/', views.swipe, name='swipe'),
    path('lockers/check_in', views.check_in, name='check in'),
    path('lockers/arduino/<str:mac_address>/<int:battery_level>/', views.arduino, name='arduino'),
    path('lockers/success', views.success, name='success'),
    path('swipetest', views.swipetest, name='swipe test'),
]