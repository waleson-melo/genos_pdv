from django.urls import path
from django.contrib.auth import views as auth_views

from .views import Cadastrar


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='autenticacao/form_login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar/', Cadastrar.as_view(), name='users-cadastrar'),
]
