from django.urls import path
from . import views

app_name = 'listing'


url_patterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
]


