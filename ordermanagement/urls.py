from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Login', views.Login,name='Login'),
    path('adminhomepage.html', views.admin,name='adminhomepage.html'),    
    path('userhomepage.html', views.upload_fetch, name = 'userhomepage.html'),
    path('addproduct.html', views.add_product, name = 'addproduct.html'),
    path('addcart.html', views.add_cart, name = 'addcart.html'),
    path('order.html', views.order, name = 'order.html'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# -*- coding: utf-8 -*-

