from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.admin_login,name='login'),
    path('logout/',views.admin_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
]
