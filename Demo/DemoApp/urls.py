from django.urls import path, include
from DemoApp import views


app_name = 'DemoApp'
urlpatterns = [
        path('',views.Login,name='login'),
        path('dashboard/',views.Dashboard,name='dashboard'),
        path('logout/',views.Logout,name='logout'),
    ]