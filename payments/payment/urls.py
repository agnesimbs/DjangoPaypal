from django.urls import path
from  .views import *
urlpatterns=[
path('',HomePageView.as_view(),name='home'),
path('payment/',PaymentPageView.as_view(),name='payment'),
]