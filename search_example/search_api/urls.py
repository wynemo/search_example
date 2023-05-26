from django.urls import path

from . import views

urlpatterns = [
  path('', views.CandidateView.as_view()),
]