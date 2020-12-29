from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.sign_up, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/'), name="logout"),
    path("robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
