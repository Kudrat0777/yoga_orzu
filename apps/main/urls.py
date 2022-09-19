from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('about/', views.AboutPageView.as_view(), name='about_page')
]
