from django.urls import path
from . import views

urlpatterns=[
    
	path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('shop/',views.shop),
    path('single/',views.single),
    # path('checkout/',views.checkout),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),


    path('addproduct/',views.addproduct),
    path('product_table/',views.product_table),
    path('prdelete/',views.prdelete),
    path('prdupdate/',views.prdupdate),
    path('addtocart/',views.addtocart),
    path('cart_update/',views.cart_update),
    path('payment/',views.payment),
    



]