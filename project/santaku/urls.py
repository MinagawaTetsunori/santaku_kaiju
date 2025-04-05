from django.urls import path
from . import views

app_name = 'santaku'
urlpatterns = [
    path('', views.index, name='index'),
    path('sampleform/', views.SampleFormView.as_view(), name='sampleform'),
]