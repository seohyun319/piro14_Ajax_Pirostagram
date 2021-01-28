from django.urls import path
from . import views

urlpatterns = [
    path('ajax/', views.Ajaxview, name='ajax')
]