from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.SignUpPage,name='signup'),
    path('login',views.LoginPage,name='login'),
    path('',views.main,name='main'),
    path('Home',views.index,name='home'),
    path('logout',views.Logout,name='logout'),
    path('dashboard',views.index,name='dashboard'),
    path('predictions',views.predictions,name='predictions'),

]
