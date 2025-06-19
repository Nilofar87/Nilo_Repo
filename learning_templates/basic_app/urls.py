from django.urls import path
from . import views

#Template tagging
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('others/',views.others,name='others'),
]


