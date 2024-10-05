from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.user_register,name='register'),
    path('profile/',views.update_profile,name='update_profile'),
    path('information/',views.update_user_info,name='update_user_info'),
    path('password/',views.change_password,name='changepassword'),
    
]

