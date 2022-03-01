from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('fruit', views.fruit, name='fruit'),
    path('veg', views.vegetables, name='vegetables'),
    path('groc', views.daily, name='daily'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('log', views.log, name='log'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout')
]
