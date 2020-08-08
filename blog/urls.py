from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.BlogView.as_view(), name="blog"),
    path('form/', views.forms, name='form'),
    path('post/<int:pk>/', views.BlogDetailView, name='post'),
]
