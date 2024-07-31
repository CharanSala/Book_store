from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('book1_url/<str:name>/', views.book1, name='book1_url'),
    path('payment_success/<str:name>/', views.payment_success, name='payment_success'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('check_login/',views.check_login,name='check_login'),
    path('logout/',views.logout,name='logout'),
    path('history/',views.history,name='history'),
    path('submit/',views.submit,name='submit'),
    path('login_home/',views.login_home,name="login_home"),
]
