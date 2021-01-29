from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from main import forms

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactUsView(FormView):
    template_name = 'contact_form.html'
    form_class = forms.ContactForm
    success_url ="/"
    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


