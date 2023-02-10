from django.urls import path
from . import views

urlpatterns = [
    path('user_login/',views.user_login,name="user_login"),
    path('register/',views.register,name="register"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('dashboard/',views.dashboard,name="dashboard") , 
]
