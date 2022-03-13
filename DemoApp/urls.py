from django.urls import path, include
from DemoApp import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'DemoApp'
urlpatterns = [
        path('',views.Login,name='login'),
        path('dashboard/', csrf_exempt(views.Dashboard),name='dashboard'),
        path('dashboard/event_details/<int:pk>',views.EventDetails,name='eventdetails'),
        path('dashboard/event_category/<str:category>',views.EventCatagory,name='eventcatagory'),
        path('success/<int:id>',views.success,name='success'),
        path('cancel/', views.cancel,name='cancel'),
        path('dashboard/checkout/<int:id>',views.create_checkout_session,name='create_checkout_session'),
        path('logout/',views.Logout,name='logout'),
    ]