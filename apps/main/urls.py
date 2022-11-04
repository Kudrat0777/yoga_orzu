from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('about/', views.AboutPageView.as_view(), name='about_page'),
    path('contact/', views.ContactPageView.as_view(), name='contact_page'),
    path('trainer/', views.TrainerPageView.as_view(), name='trainer_page'),

    path('login/', views.LoginPage.as_view(), name='login'),

    path('instructor/create/', views.InstructorCreateView.as_view(),
        name='instructor_create'),
]
