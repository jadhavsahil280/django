
from django.urls import path

from users.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_view

app_name = "users"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html", authentication_form=LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='profile')
]

