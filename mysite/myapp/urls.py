from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:page>/', views.index),
    path('', views.index),
    path('suggestions/', views.suggestions_view),
    

]
