from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from .views import signup_view






from  .  import views

app_name = 'users'

urlpatterns = [
        path('login/', LoginView.as_view(template_name = 'users/login.html'),
         name='login'),
        path('logout/' , LogoutView.as_view(template_name = 'learning_logs/index.html') ,
                                            name='logout'),
        path('signup/', signup_view, name="signup")
        
         
                                            
]