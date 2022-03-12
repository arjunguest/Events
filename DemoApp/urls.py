from django.urls import path, include
from DemoApp import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'DemoApp'
urlpatterns = [
        path('',views.Login,name='login'),
        path('dashboard/', csrf_exempt(views.Dashboard),name='dashboard'),
        path('logout/',views.Logout,name='logout'),
    ]