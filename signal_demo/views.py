from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .signals import my_signal, transactional_operation

def trigger_signal(request):
    my_signal.send(sender=None)  # Trigger signal (for Q1 & Q2)
    return HttpResponse("Signal Triggered")

def trigger_transaction_signal(request):
    transactional_operation()  # Trigger signal inside a transaction (for Q3)
    return HttpResponse("Signal Triggered with Transaction")
