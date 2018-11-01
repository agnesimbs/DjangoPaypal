from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse

from paypal.standard.forms import PayPalPaymentsForm


# Create your views here.
class HomePageView(TemplateView):
	template_name='payment/index.html'

class PaymentPageView(TemplateView):
	template_name='payment/payment.html'



#def view_that_asks_for_money(request):

    # What you want the button to do.
    #