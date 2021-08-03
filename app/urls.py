from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("",views.home, name='homepage'),
    path('menu/<int:pk>',views.menu,name='menu'),
    path('signup/',views.Signup.as_view(),name='signup'),
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.logout),
    path('cart/<int:pk>',views.Cart.as_view()),
    

]