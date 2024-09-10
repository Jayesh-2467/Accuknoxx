from django.urls import path
from . import views

urlpatterns = [
    path('trigger/', views.trigger_signal, name='trigger_signal'),
    path('trigger-transaction/', views.trigger_transaction_signal, name='trigger_transaction_signal'),
]
