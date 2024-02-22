from django.urls import path
from . import views

urlpatterns = [
    path('create-staff', views.create_staff),
    path('list-staff', views.list_staff),
    path('create-attendance', views.create_attendance),
]