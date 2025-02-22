from django.urls import path
from . import views

app_name = 'santaku'
urlpatterns = [
    path('', views.index, name='index'),
]