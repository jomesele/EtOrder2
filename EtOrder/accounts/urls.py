from django.urls import path
from accounts import views


app_name='accounts'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('registerCustomer/',views.registerCustomer,name='registerCustomer'),
    path('registerStaff/',views.registerStaff,name='registerStaff'),
    path('login/',views.userLogin,name='userLogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    
   
]
