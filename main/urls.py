from django.urls import path

from .views import HomeView, AboutView, ContactUsView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name ='about'),
    path('contact-us/', ContactUsView.as_view(), name = 'contact_us'),

]