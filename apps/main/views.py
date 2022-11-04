from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from .forms import InstructorForm
from .models import Instructor

class HomePageView(TemplateView):
    template_name ='base.html'


class AboutPageView(TemplateView):
    template_name = 'about/index.html'


class ContactPageView(TemplateView):
    template_name = 'contact/index.html'


class TrainerPageView(TemplateView):
    template_name = 'trainers/index.html'


class LoginPage(TemplateView):
    template_name = 'auth/login.html'


class InstructorCreateView(CreateView):
    form_class = InstructorForm
    model = Instructor
    template_name = 'create/create_instructor.html'

    def get_success_url(self) -> str:
        return reverse('main:instructor_create')
