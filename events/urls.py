from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/<slug:secret_url>/', views.CheckIn, name="checkin_form"),
    path('register/<int:pk>', views.EventRegistration, name="registration"),
]
