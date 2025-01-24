from home import views
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('prediction', views.prediction, name='prediction'),

]