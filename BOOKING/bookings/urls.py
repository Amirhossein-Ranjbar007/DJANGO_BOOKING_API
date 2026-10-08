from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('book-create/', views.BookingCreateView.as_view(), name='book_create'),
    path('book-list/', views.BookingListView.as_view(), name='book_list'),
    path('book-detail/<int:id>/', views.BookingDetailView.as_view(), name='book_detail'),
    path('book-cancel/<int:id>/', views.BookingCancelView.as_view(), name='book_cancel'),
    path('hostbookingview/<int:id>/', views.HostBookingListView.as_view()),

]

