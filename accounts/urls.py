from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('edit_profile/<int:id>/',views.edit_profile,name='edit_profile'),


]