from django.urls import path
from candle import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('products/', views.products, name='products')

]