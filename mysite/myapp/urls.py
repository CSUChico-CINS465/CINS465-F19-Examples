from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('<int:page>/', views.index),
    path('', views.index),
    path('suggestions/', views.suggestions_view),
    path('comment/<int:instance_id>/', views.comments_view),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', views.logout_view),
    path('register/', views.register),
]
