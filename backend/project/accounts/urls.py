from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.user_viewset),
    path('extension', views.user_contacts_viewset),
]