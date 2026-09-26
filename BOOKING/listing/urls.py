from django.urls import path
from . import views

app_name = 'listing'


urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
    path('list/', views.SpaceListView.as_view(), name='space_list'),
    path('detail/<int:id>/', views.SpacesDetailView.as_view(), name='space_detail'),
    path('create/', views.SpaceCreateView.as_view(), name='space_create'),
    path('update/<int:id>/', views.SpaceUpdateView.as_view(), name='space-update'),
    path('delete/<int:id>/',views.SpaceDeleteView.as_view(), name='space-delete'),
]


