from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name ='base.html'


class AboutPageView(TemplateView):
    template_name = 'about/index.html'


class ContactPageView(TemplateView):
    template_name = 'contact/index.html'


class TrainerPageView(TemplateView):
    template_name = 'trainers/index.html'