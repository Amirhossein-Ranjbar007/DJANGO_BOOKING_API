from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('create/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('list/', views.PaymentListView.as_view(), name='payment_list'),
    path('mockpay/<uuid:authority>/', views.MockPaySessionView.as_view(), name='mockpay-session'),
    path('mockpay-exe/<uuid:authority>/', views.MockpayExecuteView.as_view(), name='mockpay_exe'),
]



